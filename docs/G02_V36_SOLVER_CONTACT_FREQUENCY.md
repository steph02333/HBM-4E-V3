# G02 V3.6 software-limit and physics experiment — research note
Date: 2026-11-02. Script delivered in chat: G02_V36_solver_contact_frequency.py (SHA256 270d76946fea83f88a4cc989210f39214849ebd03a7b848ed159a8b255e476f4). **Syntax and dry-run ZIP verified; not tested against AEDT. G02 OPEN.**

## Why V3.6, not another PerRefine sweep
V3.5 completed 37/37 projects but 12 cases had CG adaptive nonconvergence warnings, including 10 of the sigma=100 S/m cases and 1/100 MHz runs. At sigma100, C variation and G variations remain substantial; completing a solve is not equivalent to convergence. Do not interpret G at sigma100 as accurate ML labels. Evidence in uploaded V3.5 bundle/audit.

Ansys says the iterative solver employs FMM compression and can have slow GMRES convergence for poorly conditioned systems; the direct solver uses LU factorization and can be useful for poor conditioning. Solve order and CG adaptive target/pass count are independent controls. **We must test these instead of repeatedly selecting an apparently agreeing mesh pair.**

Official Ansys: https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/Subsystems/Q3DExtractor/Content/Q3D/SettingCapacitanceConductanceAnalysisParametersinQ3DExtractor.htm
PyAEDT setup schema: https://aedt.docs.pyansys.com/version/stable/API/SetupTemplatesQ3D.html
Export API: https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.q3d.Q2d.export_matrix_data.html
Q3D field charge SmoothQ: https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/Subsystems/Q3DExtractor/Content/ReportsandPostProc/FieldquantitiesinQ3DExtractor.htm

## V3.6 planned 34 trials
- sigma100, PerRefine 10/12/14/16, iterative-vs-direct = 8.
- sigma100, solution order Normal/High/Higher and iterative/direct = 6.
- sigma100, max adaptive passes 16/20 and target error 0.5/1.0% = 4 (looser target is diagnostic, never proof of sub-1% accuracy).
- sigma1/10, iterative/direct numerical controls = 4.
- sigma10, localized reference contact yes/no with PerRefine 7/10/12 = 6.
- sigma10, independently solved 1MHz/100MHz/1GHz with iterative/direct = 6.

**Total 34**. Deep mode adds 10 more. Every run includes [CASE i/N] START and [DONE|FAILED i/N], remaining count; solver messages, original signed C/G, matrix/export headers, mesh object counts, raw convergence files and full console log in one ZIP.

The *same* Cu/SiO2/Si GSSG fixture and original D=4, P=15, H=35, tox=.3 um dimensions remain unchanged. The contact variant is explicitly a reference hypothesis, **not validated ohmic silicon physics**. There is still no independent charge conservation or fully justified HBM substrate contact. Script intentionally does not assert G02 PASS.

The exporter now passes a single unit-bearing freq string, e.g. "1000MHz", rather than passing separate numeric/unit fields that produced a 1e-9 conversion anomaly. **This is a candidate fix, not verified on user's PyAEDT 1.9.0; verify the actual header and GUI.** Independent frequency setups continue to be required to claim dispersion.

## Run
py -3.13 "C:\暂时下载\G02_V36_solver_contact_frequency.py" --mode pilot --student --aedt-version 2025.2
Upload G02_V36_results_bundle.zip.

## Decision rule
To accept a numerical regime, require no CG nonconvergence warning, independent genuinely distinct meshes, stable relevant signed C and G (1% aspiration; absolute tolerance for near-zero), correct net geometry and reference interpretation. If sigma100 cannot achieve this under Student limits with direct/Higher and targeted refinement, report the limitation; do not force G predictions into ML.
