# G02 M01 v1.7 — controlled L4 adaptive-pass extension (2026-11-02)

## Why
L1–L4 1GHz Maxwell 3D AC Conduction meshes have native counts 7,340 / 14,910 / 18,551 / 30,356 tetrahedra; all ran the 6-pass maximum. L4 reported AC Conduction Loss Error=2.5478% vs configured 1%, Delta Loss=0.018825% (not the same metric). L5 mesh exceeded Student 64,000 elements. Q3D V4.0 matched nominal C is within 2.82–4.90% of Maxwell L4; G differs 12.64–21.71%; exact Q3D frequency and solver ground/reference equivalence remain open.

## User runner
`G02_M01_L4_adaptive8_v17.py` delivered as downloadable Python file in chat. Python compilation and `--help` passed in assistant container; AEDT Student runtime NOT validated.

## Procedure
- Auto-discover newest solved `Maxwell_M01_MESH15_*/L4/M01_L4.aedt` and sibling `.aedtresults`; optional `--source` accepts explicit L4 file. Close any AEDT GUI using it before copying.
- Validate baseline native saved setup `MaximumPasses=6`, `PercentError=1`, `PercentRefinement=30`; SHA256 original.
- Copy `.aedt` plus `.aedtresults` into a dedicated timestamped folder. Exclude live `.semaphore`/`.lock` files from results copy. Keep existing source files untouched.
- Native verify AC Conduction, M01_Setup, Matrix presence, 72/116/160/204 faces and 0/1/1/0 V.
- Apply documented Maxwell `AnalysisSetup.EditSetup('M01_Setup',['NAME:M01_Setup','MaximumPasses:=',8])` to COPY ONLY, Save, reparse copy's setup and ensure `PercentError`, `PercentRefinement`, `Frequency`, and `MinimumPasses` unchanged.
- Analyze one copy at 1GHz. Best-effort native `ExportMeshStats`, `ExportConvergence` and PyAEDT `export_matrix`, record success/failure separately. ZIP diagnostics only, not `.aedtresults` or locked files; source SHA verified after.
- **Caveat:** solver may rebuild the mesh rather than resume prior six passes; classify from actual saved `.conv` and `.ms` rather than assuming reuse. Two extra passes could still exceed Student limit; do not claim numerical convergence without actual native error and C/G stabilization.

Run `py -3.13 "C:\暂时下载\G02_M01_L4_adaptive8_v17.py" --student --aedt-version 2025.2`.

## Follow-up evidence
Upload `G02_M01_ADAPT8_17_diagnostic.zip`; preserve copied `.aedt` and `.aedtresults`. Analyze native error target and tetrahedra, matrix, exact original frequency and outer return-path definitions. G02 stays OPEN until these checks.

Ansys 2025R2 native official `EditSetup` AC Conduction syntax: https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/Subsystems/Maxwell/Subsystems/Maxwell%20Scripting/Content/EditSetupMaxwell.htm
