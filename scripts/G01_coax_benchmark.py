#!/usr/bin/env python3
"""G01 (CA2 V3): fresh Ansys Q3D coaxial Cu/SiO2 analytical benchmark.

Single case first (recommended):
    py -m pip install -U pyaedt
    py G01_coax_benchmark.py --case B01

Without AEDT (tests case geometry, math, and file paths only):
    py G01_coax_benchmark.py --dry-run

After reviewing B01 with the research team:
    py G01_coax_benchmark.py --all

No previous CA2 project/data is read. Local result root: C:\\CA2 result V2.
A completed solver run is NOT a validation PASS. Raw matrices require review.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import importlib.metadata
import json
import math
import os
from pathlib import Path
import sys
import traceback
import uuid
import zipfile

EPS0_F_PER_M = 8.8541878128e-12
EPSR_OX = 3.9
SHIELD_THICKNESS_UM = 0.2
DEFAULT_ROOT = Path(r"C:\CA2 result V2")
CASES = (
    ("B01", 1.50, 25.0, 0.10),
    ("B02", 1.50, 37.5, 0.30),
    ("B03", 1.50, 50.0, 0.50),
    ("B04", 2.25, 25.0, 0.30),
    ("B05", 2.25, 37.5, 0.50),
    ("B06", 2.25, 50.0, 0.10),
    ("B07", 3.00, 25.0, 0.50),
    ("B08", 3.00, 37.5, 0.10),
    ("B09", 3.00, 50.0, 0.30),
)


def analytical_fF(r_um: float, h_um: float, tox_um: float) -> float:
    if min(r_um, h_um, tox_um) <= 0:
        raise ValueError("Nonpositive geometry parameter")
    r, h, t = [v * 1e-6 for v in (r_um, h_um, tox_um)]
    return 1e15 * (2 * math.pi * EPS0_F_PER_M * EPSR_OX * h / math.log1p(t / r))


def must(value, message: str):
    if value is False or value is None:
        raise RuntimeError(message)
    return value


def um(x: float) -> str:
    return f"{x:.9g}um"


def safe_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False, default=str) + "\n", encoding="utf-8")


def zip_evidence(stage_dir: Path, zip_path: Path) -> None:
    """Bundle light-weight evidence, never huge AEDT project/.aedtresults files."""
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for child in sorted(stage_dir.rglob("*")):
            if not child.is_file() or child == zip_path:
                continue
            rel = child.relative_to(stage_dir)
            if any(x in ("ansys_projects", ".aedtresults", "*.aedtresults") for x in rel.parts):
                continue
            if child.suffix.lower() in (".aedt", ".lock", ".aedtresults"):
                continue
            z.write(child, arcname=str(rel))


def run_case(case, dirs, args, logger):
    cid, r_um, h_um, tox_um = case
    result = {
        "case_id": cid,
        "r_um": r_um,
        "D_um": 2 * r_um,
        "h_um": h_um,
        "tox_um": tox_um,
        "outer_shield_thickness_um": SHIELD_THICKNESS_UM,
        "epsr_ox": EPSR_OX,
        "C_analytical_fF": analytical_fF(r_um, h_um, tox_um),
        "C_Q3D_fF": None,  # deliberate: needs unambiguous C-matrix review
        "error_percent": None,
        "status": "NOT_STARTED",
        "reference": "Wang et al. (2014) Eq. (5); ideal coaxial approximation",
        "geometry": "Cu center cylinder + annular SiO2 + annular Cu ground shield",
        "reference_net": "GROUND",
        "signal_net": "SIGNAL",
        "end_conditions": "Both cylinders and SiO2 end at z=0 and z=h; finite-length fringe fields possible",
        "solver_version_requested": args.aedt_version,
        "student_version": args.student,
        "non_graphical": args.non_graphical,
        "setup": "G01_Setup",
        "setup_cap_max_pass": 12,
        "setup_cap_min_pass": 3,
        "setup_cap_min_conv_pass": 2,
        "setup_cap_error_percent": 0.5,
    }
    safe_json(dirs["configs"] / f"{cid}.json", result)
    logger(f"{cid}: r={r_um}um, h={h_um}um, tox={tox_um}um, C_analytical={result['C_analytical_fF']:.9f} fF")

    if args.dry_run:
        result["status"] = "DRY_RUN_NO_SOLVER"
        safe_json(dirs["configs"] / f"{cid}.json", result)
        return result

    try:
        from ansys.aedt.core import Q3d
    except ImportError as ex:
        raise RuntimeError("PyAEDT is not installed in this Python. Run: py -m pip install -U pyaedt") from ex

    try:
        result["pyaedt_version"] = importlib.metadata.version("pyaedt")
    except importlib.metadata.PackageNotFoundError:
        result["pyaedt_version"] = "UNKNOWN"

    # New project/case. NO reuse of legacy geometry or simulation results.
    unique_project_name = f"CA2V3_{cid}_{uuid.uuid4().hex[:8]}"
    app = None
    try:
        # AEDT version can be omitted to select the latest installed version.
        kwargs = dict(
            project=unique_project_name,
            design=f"Coax_{cid}",
            new_desktop=False,
            non_graphical=args.non_graphical,
            student_version=args.student,
            close_on_exit=False,
        )
        if args.aedt_version:
            kwargs["version"] = args.aedt_version
        logger(f"{cid}: connecting to AEDT and creating new Q3D project {unique_project_name}")
        app = Q3d(**kwargs)
        app.modeler.model_units = "um"
        logger(f"{cid}: building Cu / SiO2 / Cu coaxial test fixture")

        material = must(app.materials.add_material(f"G01_oxide_er39_{cid}"), "Could not create oxide material")
        material.permittivity = EPSR_OX
        material.conductivity = "0"
        must(material.update(), "Could not update SiO2 material properties")
        oxide_material = material.name

        origin = ["0um", "0um", "0um"]
        h = um(h_um)
        # Central Cu conductor: r, z=0..h.
        core = must(app.modeler.create_cylinder("Z", origin, um(r_um), h,
                         name="Cu_SIGNAL", material="copper"), "Failed to create center Cu cylinder")

        # Oxide annulus: hollow shell (r, r+tox); subtraction tool is sacrificial.
        oxide = must(app.modeler.create_cylinder("Z", origin, um(r_um + tox_um), h,
                         name="SiO2_LINER", material=oxide_material), "Failed to create oxide blank")
        oxide_tool = must(app.modeler.create_cylinder("Z", origin, um(r_um), h,
                         name="TOOL_oxide_inner", material="vacuum"), "Failed oxide cutter")
        must(app.modeler.subtract(oxide.name, oxide_tool.name, keep_originals=False),
             "Oxide subtraction failed")

        # Ground copper shield annulus: (r+tox, r+tox+0.2um).
        outer_r = r_um + tox_um + SHIELD_THICKNESS_UM
        ground = must(app.modeler.create_cylinder("Z", origin, um(outer_r), h,
                         name="Cu_GROUND_SHELL", material="copper"), "Failed to create ground blank")
        shield_tool = must(app.modeler.create_cylinder("Z", origin, um(r_um + tox_um), h,
                         name="TOOL_shield_inner", material="vacuum"), "Failed shield cutter")
        must(app.modeler.subtract(ground.name, shield_tool.name, keep_originals=False),
             "Ground-shell subtraction failed")

        # This is a capacitance-only test; a net alone is sufficient for C.
        must(app.assign_net(core.name, net_name="SIGNAL", net_type="Signal"),
             "Failed to assign SIGNAL net")
        must(app.assign_net(ground.name, net_name="GROUND", net_type="Ground"),
             "Failed to assign GROUND net")

        objs = list(app.modeler.object_names)
        logger(f"{cid}: final objects: {objs}")
        expected = {"Cu_SIGNAL", "SiO2_LINER", "Cu_GROUND_SHELL"}
        if set(objs) != expected:
            raise RuntimeError(f"Geometry object audit failed: expected {expected}, got {set(objs)}")
        result["geometry_object_names"] = objs

        setup = must(app.create_setup(name="G01_Setup"), "Failed to create Q3D setup")
        setup.capacitance_enabled = True
        setup.ac_rl_enabled = False
        setup.dc_enabled = False
        cap_props = setup.props["Cap"]
        cap_props["MaxPass"] = 12
        cap_props["MinPass"] = 3
        cap_props["MinConvPass"] = 2
        cap_props["PerError"] = 0.5
        must(setup.update(), "Failed to apply Q3D capacitance setup")
        result["cap_setup_properties"] = {k: str(v) for k, v in cap_props.items()}

        project_path = dirs["ansys_projects"] / f"{cid}_G01.aedt"
        must(app.save_project(str(project_path)), "Failed to save AEDT project before solving")
        result["project_file"] = str(project_path)
        logger(f"{cid}: AEDT project saved: {project_path}")
        logger(f"{cid}: solving capacitance ...")
        solved = app.analyze_setup("G01_Setup", cores=args.cores)
        if solved is False:
            raise RuntimeError("Q3D analysis returned False")
        if not setup.is_solved:
            raise RuntimeError("Q3D did not report solved setup")
        logger(f"{cid}: solver completed; exporting C matrix (MAXWELL convention)")
        matrix_path = dirs["raw_exports"] / f"{cid}_C_Maxwell_fF.txt"
        exported = app.export_matrix_data(
            file_name=str(matrix_path),
            problem_type="C",
            setup="G01_Setup",
            reduce_matrix="Original",
            c_unit="fF",
            matrix_type="Maxwell",
            precision=15,
        )
        if not exported or not matrix_path.exists() or matrix_path.stat().st_size < 30:
            raise RuntimeError("Q3D C matrix export failed or output is empty")
        result["C_matrix_file"] = str(matrix_path)

        # Best-effort extra evidence, do not turn solved C data into failure if
        # convergence/profile format differs between AEDT versions.
        for kind, function, path in (
            ("convergence", lambda: app.export_convergence(
                setup="G01_Setup", output_file=str(dirs["raw_exports"] / f"{cid}_convergence.txt")),
                dirs["raw_exports"] / f"{cid}_convergence.txt"),
            ("mesh", lambda: app.export_mesh_stats(
                setup="G01_Setup", output_file=str(dirs["raw_exports"] / f"{cid}_mesh_stats.txt")),
                dirs["raw_exports"] / f"{cid}_mesh_stats.txt"),
            ("profile", lambda: app.export_profile(
                setup="G01_Setup", output_file=str(dirs["raw_exports"] / f"{cid}_profile.prof")),
                dirs["raw_exports"] / f"{cid}_profile.prof"),
        ):
            try:
                function()
                result[f"{kind}_file"] = str(path) if path.exists() else "NOT_GENERATED"
            except Exception as exc:
                result[f"{kind}_export_warning"] = str(exc)
                logger(f"{cid}: WARNING: {kind} export failed: {exc}")

        must(app.save_project(str(project_path)), "Could not save solved AEDT project")
        result["status"] = "SOLVED_EXPORT_READY_FOR_REVIEW"
        logger(f"{cid}: SOLVED and matrix exported. Validation still NOT PASSED.")
    finally:
        # Keep user's already-running AEDT session intact, and retain saved project.
        # PyAEDT may keep project open, which is fine for inspection.
        if app is not None:
            try:
                app.save_project()
            except Exception:
                pass
        safe_json(dirs["configs"] / f"{cid}.json", result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="CA2 V3 G01: single TSV analytical benchmark")
    grp = parser.add_mutually_exclusive_group()
    grp.add_argument("--case", choices=[c[0] for c in CASES], default="B01")
    grp.add_argument("--all", action="store_true", help="Run all 9 cases (only after B01 review)")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT, help=r"Default: C:\CA2 result V2")
    parser.add_argument("--aedt-version", default=None, help="e.g. 2025.2 or 2026.1 (default: installed latest)")
    parser.add_argument("--student", action="store_true", help="Use AEDT Student version")
    parser.add_argument("--non-graphical", action="store_true", help="Launch AEDT without GUI")
    parser.add_argument("--cores", type=int, default=2)
    parser.add_argument("--dry-run", action="store_true", help="Compute analytic values and paths without AEDT")
    args = parser.parse_args()
    if args.cores < 1:
        parser.error("--cores must be >= 1")
    if os.name != "nt" and not args.dry_run and args.root == DEFAULT_ROOT:
        parser.error("Run real Q3D on Windows, or specify --root and an installed AEDT instance")
    source_sha256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    run_id = dt.datetime.now().strftime("%Y%m%d_%H%M%S") + "_" + uuid.uuid4().hex[:6]
    stage_dir = args.root / "01_analytical_benchmark" / "runs" / run_id
    dirs = {name: stage_dir / name for name in
            ("configs", "ansys_projects", "raw_exports", "analysis", "reports")}
    for folder in dirs.values():
        folder.mkdir(parents=True, exist_ok=True)
    log_path = dirs["reports"] / "runner.log"

    def logger(msg):
        line = f"{dt.datetime.now().isoformat(timespec='seconds')} {msg}"
        print(line, flush=True)
        with log_path.open("a", encoding="utf-8") as stream:
            stream.write(line + "\n")

    cases = CASES if args.all else [c for c in CASES if c[0] == args.case]
    meta = {
        "run_id": run_id, "date": dt.datetime.now().isoformat(),
        "python_version": sys.version, "platform": sys.platform,
        "script_sha256": source_sha256, "script_name": Path(__file__).name,
        "root": str(args.root), "case_ids": [c[0] for c in cases],
        "dry_run": args.dry_run, "aedt_version_requested": args.aedt_version,
        "student": args.student, "cores": args.cores,
        "gate": "G01_NOT_PASSED",
    }
    safe_json(dirs["configs"] / "run_manifest.json", meta)
    logger(f"G01 CA2 V3 run_id={run_id}; script_sha256={source_sha256}")
    logger(f"Root: {stage_dir}")
    results = []
    for case in cases:
        try:
            results.append(run_case(case, dirs, args, logger))
        except Exception:
            error_text = traceback.format_exc()
            logger(f"{case[0]}: FAILED\n{error_text}")
            failure = {
                "case_id": case[0], "r_um": case[1], "h_um": case[2],
                "tox_um": case[3], "C_analytical_fF": analytical_fF(*case[1:]),
                "C_Q3D_fF": None, "error_percent": None,
                "status": "FAILED", "error": error_text,
            }
            safe_json(dirs["configs"] / f"{case[0]}_failure.json", failure)
            results.append(failure)
            break  # Stop on first failure: do not fabricate later results.

    summary = dirs["analysis"] / "G01_summary.csv"
    columns = ["case_id", "r_um", "D_um", "h_um", "tox_um", "epsr_ox",
               "C_analytical_fF", "C_Q3D_fF", "error_percent", "status", "C_matrix_file"]
    with summary.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for row in results:
            writer.writerow({k: row.get(k, "") for k in columns})
    zip_path = stage_dir / "G01_results_bundle.zip"
    zip_evidence(stage_dir, zip_path)
    logger(f"Evidence bundle (send this back): {zip_path}")
    logger(f"Note: solved simulations are not a G01 PASS; the C-matrix must be inspected before comparison.")
    return 1 if any(row["status"] == "FAILED" for row in results) else 0


if __name__ == "__main__":
    sys.exit(main())
