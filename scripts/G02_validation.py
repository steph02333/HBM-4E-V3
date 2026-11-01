#!/usr/bin/env python3
"""CA2 V3 G02 resource-aware Q3D multi-TSV numerical-validation runner.

Windows AEDT Student 2025 R2 / PyAEDT 1.9.0, Python 3.13.
First: py -3.13 G02_validation.py --dry-run
Then:  py -3.13 G02_validation.py --mode pilot --student --aedt-version 2025.2
After checking pilot: same command with --mode campaign.

This script tests a SIMPLIFIED 3-TSV G-S-S structure, not an HBM4E final
stack. Its Si is a homogeneous material. The physical return path and
frequency-dependent silicon conduction MUST be reviewed before final DOE.
"""
from __future__ import annotations
import argparse, csv, datetime as dt, hashlib, json, math, re, sys, traceback, uuid, zipfile
from pathlib import Path

ROOT=Path(r"C:\CA2 result V2")
FIELDS=("id","category","d","p","h","tox","margin","per_error","max_pass")
# All dimensions in micrometres. 3 TSVs at x = -P, 0, +P;
# left is ground, center=SIG_A, right=SIG_B.
NOM=dict(d=4.0,p=15.0,h=35.0,tox=0.3,margin=18.0)
MESH=[("mesh_lo",2.0,5),("mesh_mid",1.0,9),("mesh_hi",0.5,13),("mesh_tight",0.25,17)]
# Series is modest but nontrivial; no ML/DOE sampling.
# Larger plan is gated by resource checks and scientific interpretation.
def campaign():
    out=[]
    def add(name, category, edits=None, per_error=1.0, max_pass=10):
        v=dict(NOM);v.update(edits or {})
        out.append(dict(id=name,category=category,**v,per_error=per_error,max_pass=max_pass))
    for name,err,passes in MESH: add(name,"mesh",per_error=err,max_pass=passes)
    for p in (10.,12.5,17.5,20.):add(f"pitch_{str(p).replace('.','p')}","pitch",dict(p=p))
    for d in (3.,5.,6.):add(f"diam_{str(d).replace('.','p')}","diameter",dict(d=d))
    for t in (0.1,0.5):add(f"liner_{str(t).replace('.','p')}","liner",dict(tox=t))
    for m in (12.,27.,40.):add(f"domain_{str(m).replace('.','p')}","domain",dict(margin=m))
    for name,edits in [("corner_close",dict(d=6.,p=10.,tox=.1,h=50.)),
                        ("corner_far",dict(d=3.,p=20.,tox=.5,h=25.))]:
        add(name,"corner",edits,per_error=.5,max_pass=13)
    return out

def timestamp():return dt.datetime.now().isoformat(timespec="seconds")
def save_json(path,obj):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(obj,indent=2,default=str,ensure_ascii=False)+"\n",encoding="utf-8")
def um(x):return f"{x:.8g}um"
def check(x,msg):
    if x is None or x is False:raise RuntimeError(msg)
    return x

def parse_c_matrix(path):
    """Read the named Maxwell capacitance block from the Q3D text export."""
    lines=path.read_text(encoding="utf-8-sig",errors="replace").splitlines()
    marker=next((i for i,s in enumerate(lines) if s.strip()=="Capacitance Matrix"),None)
    if marker is None:raise ValueError("No Capacitance Matrix block")
    tokens=[s.split() for s in lines[marker+1:] if s.strip()]
    if not tokens:raise ValueError("Empty capacitance matrix")
    names=tokens[0]
    n=len(names)
    rows=[]
    for row in tokens[1:1+n]:
        if len(row)!=n+1:raise ValueError(f"Wrong C matrix row {row}")
        if row[0]!=names[len(rows)]:raise ValueError("Row names differ from headings")
        rows.append([float(x.replace("D","E")) for x in row[1:]])
    if len(rows)!=n:raise ValueError("Incomplete matrix")
    return names,rows

def matrix_qa(names,C):
    n=len(C)
    norm=max(max(abs(x) for row in C for x in row),1e-20)
    symmetry=max(abs(C[i][j]-C[j][i]) for i in range(n) for j in range(n))/norm
    diagonal_min=min(C[i][i] for i in range(n))
    offdiag_max=max([C[i][j] for i in range(n) for j in range(n) if i!=j],default=0.)
    # Strict diagonal dominance is a sufficient passivity check, NOT universal;
    # use independently computed eigenvalues when numpy is available.
    eigen=None
    try:
        import numpy as np
        eigen=np.linalg.eigvalsh(np.asarray(C,dtype=float)).tolist()
    except ImportError:pass
    return dict(names=names,symmetry_norm=symmetry,min_diagonal_fF=diagonal_min,
        max_off_diagonal_fF=offdiag_max,min_eigenvalue_fF=min(eigen) if eigen else None,
        eigenvalues_fF=eigen,row_sums_fF=[sum(r) for r in C],
        comment="Rows need not sum to zero when ground/exterior reference is eliminated; no charge-conservation PASS is claimed.")

def get_observables(names,C):
    if "SIG_A" not in names or "SIG_B" not in names:
        raise ValueError(f"Missing required signal nets; got {names}")
    a=names.index("SIG_A");b=names.index("SIG_B")
    return dict(Cself_A_fF=C[a][a],Cself_B_fF=C[b][b],
                Cmutual_AB_signed_fF=C[a][b],
                Cmutual_AB_magnitude_fF=abs(C[a][b]))

def build_one(conf, dirs, args, log):
    from ansys.aedt.core import Q3d
    cid=conf["id"];d,p,h,t,m=(conf[k] for k in ("d","p","h","tox","margin"))
    assert all(x>0 for x in (d,p,h,t,m))
    if p<=d+2*t:raise ValueError("Oxide regions overlap; choose larger pitch")
    case_dir=dirs["cases"]/cid;case_dir.mkdir(parents=True,exist_ok=True)
    app=None; info=dict(**conf,status="STARTED",start=timestamp())
    try:
        kw=dict(project=f"V3G02_{cid}_{uuid.uuid4().hex[:6]}",design=f"G02_{cid}",
            new_desktop=False,non_graphical=args.non_graphical,
            student_version=args.student,close_on_exit=False)
        if args.aedt_version:kw["version"]=args.aedt_version
        app=Q3d(**kw)
        app.modeler.model_units="um"
        oxide=check(app.materials.add_material(f"SiO2_G02_{cid}"),"oxide material failed")
        oxide.permittivity=3.9;oxide.conductivity="0";check(oxide.update(),"oxide property update failed")
        silicon=check(app.materials.add_material(f"Silicon_G02_{cid}"),"silicon material failed")
        silicon.permittivity=11.7
        # Homogeneous dielectric pilot. A finite-conductivity semiconductor has
        # frequency/reference complications in Q3D, so it is NOT silently assumed
        # that eps=11.7 reproduces the rho=10 Ohm-cm MOS TSV case.
        silicon.conductivity="0"
        check(silicon.update(),"silicon update failed")
        # Finite silicon rectangular block; increasing 'margin' changes this
        # physical block size, not only a mathematical open boundary.
        r=d/2; centers=[(-p,"GROUND"),(0.,"SIG_A"),(p,"SIG_B")]
        left=-p-r-t-m;right=p+r+t+m; yext=r+t+m
        si=check(app.modeler.create_box([um(left),um(-yext),"0um"],
                [um(right-left),um(2*yext),um(h)],name="SILICON",
                material=silicon.name),"silicon box creation failed")
        # Cut holes first, before placing coaxial liners and Cu pillars.
        for i,(x,_) in enumerate(centers):
            tool=check(app.modeler.create_cylinder("Z",[um(x),"0um","0um"],
                um(r+t),um(h),name=f"SiHoleTool_{i}",material="vacuum"),
                "Si bore tool failed")
            check(app.modeler.subtract("SILICON",tool.name,keep_originals=False),
                  "Si hole subtraction failed")
        for i,(x,net) in enumerate(centers):
            oxide_outer=check(app.modeler.create_cylinder("Z",[um(x),"0um","0um"],
                     um(r+t),um(h),name=f"OX_{i}",material=oxide.name),"oxide outer failed")
            tool=check(app.modeler.create_cylinder("Z",[um(x),"0um","0um"],
                     um(r),um(h),name=f"OXTOOL_{i}",material="vacuum"),"liner tool failed")
            check(app.modeler.subtract(oxide_outer.name,tool.name,keep_originals=False),
                 "Liner hollowing failed")
            core=check(app.modeler.create_cylinder("Z",[um(x),"0um","0um"],
                     um(r),um(h),name=f"CU_{net}",material="copper"),"Cu cylinder failed")
            check(app.assign_net(core.name,net_name=net,
                      net_type="Ground" if net=="GROUND" else "Signal"),
                  "Net assign failed")
        # Confirm core object names, no leftover subtraction tools.
        objects=set(app.modeler.object_names)
        expected={"SILICON"}|{f"OX_{i}" for i in range(3)}|{f"CU_{n}" for _,n in centers}
        if objects!=expected:raise RuntimeError(f"Geometry object audit: {objects} != {expected}")
        setup=check(app.create_setup(name="G02_Setup"),"create setup failed")
        setup.capacitance_enabled=True;setup.ac_rl_enabled=False;setup.dc_enabled=False
        setup.props["Cap"]["MaxPass"]=int(conf["max_pass"])
        setup.props["Cap"]["MinPass"]=3
        setup.props["Cap"]["MinConvPass"]=2
        setup.props["Cap"]["PerError"]=float(conf["per_error"])
        check(setup.update(),"setup update failed")
        project_dir=dirs["projects"];project_dir.mkdir(parents=True,exist_ok=True)
        project=project_dir/f"{cid}_G02.aedt"
        check(app.save_project(str(project)),"project save failed")
        info["project_file"]=str(project)
        log(f"{cid}: SOLVING d={d},p={p},h={h},tox={t},margin={m},"
            f" target={conf['per_error']}%,maxpass={conf['max_pass']}")
        ok=app.analyze_setup("G02_Setup",cores=args.cores)
        if ok is False or not setup.is_solved:raise RuntimeError("Q3D did not solve")
        matrix_path=case_dir/"C_Maxwell_fF.txt"
        exported=app.export_matrix_data(file_name=str(matrix_path),problem_type="C",
               setup="G02_Setup",reduce_matrix="Original",c_unit="fF",
               matrix_type="Maxwell",precision=15)
        if not exported or not matrix_path.exists():raise RuntimeError("Matrix export missing")
        names,C=parse_c_matrix(matrix_path)
        info.update(get_observables(names,C));info["matrix_QA"]=matrix_qa(names,C)
        info["matrix_fF"]=C
        for name,fn in [
            ("convergence",lambda:app.export_convergence(setup="G02_Setup",
                          output_file=str(case_dir/"convergence.txt"))),
            ("mesh",lambda:app.export_mesh_stats(setup="G02_Setup",
                          output_file=str(case_dir/"mesh_stats.txt"))),
            ("profile",lambda:app.export_profile(setup="G02_Setup",
                          output_file=str(case_dir/"profile.prof")))]:
            try:fn()
            except Exception as e:info[f"{name}_warning"]=str(e)
        check(app.save_project(str(project)),"saving solved project failed")
        info["status"]="SOLVED_PENDING_REVIEW"
        log(f"{cid}: Cself_A={info['Cself_A_fF']:.8g}fF, "
            f"|Cmutual_AB|={info['Cmutual_AB_magnitude_fF']:.8g}fF")
    finally:
        info["end"]=timestamp();save_json(case_dir/"case_result.json",info)
        if app:
            try:app.save_project()
            except Exception:pass
    return info

def zip_bundle(run_dir):
    out=run_dir/"G02_results_bundle.zip"
    with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as z:
        for p in run_dir.rglob("*"):
            if not p.is_file() or p==out:continue
            if "ansys_projects" in p.parts or p.suffix.lower() in (".aedt",".lock"):continue
            z.write(p,p.relative_to(run_dir))
    return out

def relchange(a,b):
    return 100*abs(a-b)/max(abs(a),abs(b),1e-12)

def summarize(results,dest):
    path=dest/"G02_case_summary.csv"
    cols=["id","category","d","p","h","tox","margin","per_error","max_pass","status",
          "Cself_A_fF","Cself_B_fF","Cmutual_AB_signed_fF",
          "Cmutual_AB_magnitude_fF"]
    with path.open("w",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=cols);w.writeheader()
        for row in results:w.writerow({k:row.get(k,"") for k in cols})
    mesh=[x for x in results if x.get("category")=="mesh" and x.get("status")=="SOLVED_PENDING_REVIEW"]
    comparisons=[]
    for a,b in zip(mesh,mesh[1:]):
        comparisons.append(dict(coarse=a["id"],fine=b["id"],
              delta_Cself_percent=relchange(a["Cself_A_fF"],b["Cself_A_fF"]),
              delta_Cmutual_percent=relchange(a["Cmutual_AB_magnitude_fF"],
                                                b["Cmutual_AB_magnitude_fF"])))
    save_json(dest/"mesh_cross_solution_changes.json",comparisons)
    return path

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--mode",choices=("pilot","campaign"),default="pilot")
    p.add_argument("--root",type=Path,default=ROOT)
    p.add_argument("--student",action="store_true")
    p.add_argument("--aedt-version",default="2025.2")
    p.add_argument("--cores",type=int,default=2)
    p.add_argument("--dry-run",action="store_true")
    p.add_argument("--non-graphical",action="store_true")
    args=p.parse_args()
    if args.cores<1 or args.cores>4:p.error("Use 1–4 cores for Student edition")
    cases=[dict(id="pilot",category="pilot",**NOM,per_error=2.,max_pass=5)] if args.mode=="pilot" else campaign()
    sid=dt.datetime.now().strftime("%Y%m%d_%H%M%S")+"_"+uuid.uuid4().hex[:6]
    root=args.root/"02_numerical_convergence"/"runs"/sid
    dirs=dict(cases=root/"cases",projects=root/"ansys_projects")
    dirs["cases"].mkdir(parents=True,exist_ok=True)
    (root/"reports").mkdir(exist_ok=True)
    log_file=root/"reports"/"runner.log"
    def log(s):
        s=f"{timestamp()} {s}";print(s,flush=True)
        with log_file.open("a",encoding="utf-8") as f:f.write(s+"\n")
    meta=dict(run_id=sid,mode=args.mode,source_sha256=hashlib.sha256(
        Path(__file__).read_bytes()).hexdigest(),cases=cases,
        model_warning="Homogeneous Si epsilon=11.7 and conductivity=0; NOT realistic doped Si.",
        pass_status="G02_NOT_PASSED")
    save_json(root/"manifest.json",meta)
    log(f"G02 {args.mode}: {len(cases)} new configurations. Output: {root}")
    results=[]
    for conf in cases:
        if args.dry_run:
            results.append(dict(**conf,status="DRY_RUN"))
            continue
        try:results.append(build_one(conf,dirs,args,log))
        except Exception:
            err=traceback.format_exc();log(f"STOP on {conf['id']}:\n{err}")
            save_json(root/"reports"/"failure.json",dict(case=conf,error=err))
            results.append(dict(**conf,status="FAILED",error=err))
            break
    summarize(results,root)
    out=zip_bundle(root)
    log(f"Upload this file: {out}")
    log("Do not claim G02 pass before reviewing physical reference, matrix and mesh.")
    return int(any(x["status"]=="FAILED" for x in results))

if __name__=="__main__":sys.exit(main())
