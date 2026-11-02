# G02 Maxwell M01 v1.6 — post-solve evidence & Q3D frequency gate
Date: 2026-11-02. G02 remains OPEN.

Maxwell 1 GHz L1–L4 matrices available; L5 exceeds Student 64,000-volume cap (80,988). L4 C_AA=36.484fF, C_AB=-12.187fF, G_AA=0.069375mS, G_AB=-0.019982mS. Versus matched Q3D V4.0 `DOM10_M25_R18`: C_AA=35.481712fF, C_AB=-11.618261fF, G_AA=0.061592086mS, G_AB=-0.016418221mS. L4 percentage magnitude deviations: +2.82%, +4.90%, +12.64%, +21.71%. Cross-solver agreement remains conditional on physical/reference equivalence and frequency readback.

## Newly verified offline Q3D evidence
From original `G02_V40_targeted_results_bundle.zip`, case `cases/DOM10_M25_R18/convergenceCG.txt`: 6 adaptive passes, Q3D target Delta 0.5%, final Delta 0.11761%, pass-6 2,662 triangles. Separate `mesh_stats.txt`: total 4,512 mesh elements (do NOT compare to Maxwell volume elements). Alternate Q3D exports `CG_export_default.txt`, `CG_export_freq_Hz_unit.txt`, `CG_export_freq_number_unit.txt`, `CG_export_sweep_last_adaptive.txt` contain **identical matrices** but frequency headers vary 1kHz versus 1Hz. Thus exact-case frequency still unverified by native GUI. Do not assume header alone proves 1GHz.

## v1.6 collector handed to user
`G02_M01_postsolve_evidence_v16.py`, syntax and CLI verified offline, AEDT runtime NOT yet run. This is a **read-only/no-Analyze/no-Save** script operating on previously saved solved L1–L4 .aedt and .aedtresults. Uses documented native `de.ExportMeshStats('M01_Setup','',filename.ms,True)` and `de.ExportConvergence('M01_Setup','',filename.conv)` to correct earlier failing PyAEDT wrapper. Exports new ZIP with `.ms`, `.conv`, JSON, preserves source hash. Failure of one native export must be reported, not interpreted as failed solution.

Windows command:
`py -3.13 "C:\暂时下载\G02_M01_postsolve_evidence_v16.py" --base "C:\CA2 result V2\02_numerical_convergence\V3_conductive_silicon\Maxwell_M01_BUILD06_20261102_175348" --student --aedt-version 2025.2`

Await user `G02_M01_POSTSOLVE16_diagnostic.zip` (we don't have local access to saved solved projects). User must preserve original .aedtresults. Read-only script may create AEDT lock files but makes no intentional modifications.

## Additional 2 gates
1. Exact Q3D nominal `DOM10_M25_R18.aedt` and saved results: AEDT GUI setup-frequency screenshot and native CG Matrix at 1 GHz screenshot or exported evidence. Q3D raw ZIP does not contain native .aedt. No metadata relabel shortcut.
2. Q3D vs Maxwell Si box including z, 2 ground TSVs, zero substrate contacts, outer boundary and returned-current interpretation. Different solver G values might reflect actual material/reference differences, so do not claim physical confirmation simply because C is close.

Ansys references: `ExportMeshStats` https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v251/en/Subsystems/Maxwell/Subsystems/Maxwell%20Scripting/Content/ExportMeshStats.htm ; `ExportConvergence` in Maxwell 2025R2 scripting guide https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/PDFs/MaxwellScriptingGuide.pdf ; `Viewing Convergence Data` https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v261/en/Subsystems/Maxwell/Content/ReportsandPostProc/ViewingConvergenceData.htm (AC Conduction convergence's loss criterion is apparent power magnitude).
