# Decision and evidence log

## 2026-11-01 — CA2 V3 restart
- New GitHub repository: `steph02333/HBM-4E-V3`.
- Local Windows results root: `C:\CA2 result V2` (not directly accessible by connector).
- Previous datasets, previous mesh outputs, previous optimizer predictions and ML training are retired as experimental evidence. No old datapoints will be carried into V3.
- Stage-gated workflow adopted. Prof Lim's first requirement (single-TSV analytical benchmark) is current task.
- Q3D termed **reference EM solver** rather than ground truth.
- Physical model changes trigger revalidation of impacted numerical results.
- This log documents decisions, not a record of an Ansys solver execution.
- Next action: implement and run the fresh G01 benchmark on the user's Ansys machine; return raw outputs, then evaluate against the gate.

## Evidence ledger
| Gate | Evidence | Status |
|---|---|---|
| G01 | Prof Lim email + CA1 Wang 2014 formula + benchmark design | SPECIFIED, NOT RUN |
| G02–G07 | Not yet generated | NOT STARTED |

## 2026-11-01 17:57 (SGT) — G01 B01 first-run failure (environment)
- Command: `py "C:\暂时下载\G01_coax_benchmark.py" --case B01 --student --aedt-version 2025.2`
- Run ID: `20261101_175731_2c15db`.
- Script SHA-256 reported: `18e2fc8c7c5982e54e524f2fcb0518343ae24dcb18459312629ac16dc5de4cbf`.
- Analytical B01 value calculated: `84.045449519 fF`.
- Failure during `from ansys.aedt.core import Q3d`: `ModuleNotFoundError: No module named 'ansys'`.
- No Q3D simulation was performed; G01 remains OPEN / NOT PASSED.
- User-side next step: install PyAEDT into same `py` interpreter with `py -m pip install -U pyaedt`, verify import, then retry B01.
- Local log/bundle folder: `C:\CA2 result V2\01_analytical_benchmark\runs\20261101_175731_2c15db` (not available to connector; results based on pasted console log).

## 2026-11-01 17:58 (SGT) — G01 B01 second import failure despite successful command-line import
- Successful command: `py -c "from ansys.aedt.core import Q3d; print('PyAEDT import OK')"` printed `PyAEDT import OK`.
- Failed script invocation: `py "C:\暂时下载\G01_coax_benchmark.py" --case B01 --student --aedt-version 2025.2`.
- New run ID: `20261101_175846_8e90b4`; same reported source SHA-256 `18e2fc8c7c5982e54e524f2fcb0518343ae24dcb18459312629ac16dc5de4cbf`.
- Script still failed on `from ansys.aedt.core import Q3d` with `ModuleNotFoundError: No module named 'ansys'`, **before** creating/solving Q3D geometry.
- Diagnosis **not yet confirmed**: Windows Python launcher may honor script's `#!/usr/bin/env python3` shebang and select a different interpreter from `py -c`. A conflicting module in the script folder is an alternative possibility.
- Next diagnostic: confirm `py -3.13 -c "import sys; from ansys.aedt.core import Q3d; print(sys.executable)"`, then rerun B01 using explicit `py -3.13 "C:\暂时下载\G01_coax_benchmark.py" --case B01 --student --aedt-version 2025.2`. If it fails again, inspect import with `sys.path.insert(0, r'C:\暂时下载')`.
- G01 remains OPEN; no numerical Q3D result exists from either failed run.

## 2026-11-01 17:59–18:00 (SGT) — G01 B01 fresh AEDT solve completed; numerical validation pending

- User launched with explicit interpreter: `py -3.13 "C:\暂时下载\G01_coax_benchmark.py" --case B01 --student --aedt-version 2025.2`.
- Run ID: `20261101_175942_4a2c83`. Source SHA-256 reported: `18e2fc8c7c5982e54e524f2fcb0518343ae24dcb18459312629ac16dc5de4cbf`.
- Runtime: Python 3.13.5, PyAEDT 1.9.0, AEDT 2025.2SV Student, Q3D Extractor.
- AEDT installation path from log: `C:\ANSYS Inc\ANSYS Student\v252\AnsysEM`.
- Fresh project `CA2V3_B01_af470450`, design `Coax_B01`; three reported final objects: `Cu_SIGNAL`, `SiO2_LINER`, `Cu_GROUND_SHELL`; signal and ground nets created.
- `G01_Setup` reported solved correctly in 18 seconds; script reported `SOLVED_EXPORT_READY_FOR_REVIEW` and C-Maxwell matrix export success.
- Analytical value: **84.045449519 fF**. **Actual Q3D value and relative error not yet available** in pasted console log.
- User's evidence bundle path: `C:\CA2 result V2\01_analytical_benchmark\runs\20261101_175942_4a2c83\G01_results_bundle.zip`.
- **G01 remains OPEN / NOT PASSED** pending upload and inspection of exported matrix, unit conventions and solver convergence, plus eventual completion of B01–B09 and formal gate review. Do not run additional cases until B01 review.

## 2026-11-01 — G01 B01 ZIP independently inspected (preliminary numeric success)
- User provided `G01_results_bundle.zip` (SHA256: `1ae6b6a5d228773b0c209ed7110729d47a63e958b9f497cc688f6adca4d08680`).
- Original Maxwell C matrix has one non-reference signal coefficient: `C(SIGNAL,SIGNAL) = 84.87557931367954 fF`. Ground is the reference net.
- Analytical Eq. (5) prediction: `84.04544951915052 fF`; difference +0.83012979452902 fF; absolute relative error **0.9877153365%** (<5% initial target).
- CG adaptive mesh: **6 passes**, final **0.18624%**, configured target **0.5%**; normal solver completion.
- The error's cause (possibly finite-end fringing) has NOT been demonstrated. Single-coax test cannot validate semiconductor effects or mutual TSV coupling.
- Detailed traceable report: [B01 independent review](../results/g01/B01_20261101_175942_4a2c83_review.md).
- **Gate G01 remains OPEN**. Next: run B02–B09 with the same frozen version of `G01_coax_benchmark.py` (the existing `--all` command also repeats B01 in a new run); inspect complete new evidence before moving to G02.

## 2026-11-01 G02 pilot evidence
Run 20261101_182327_f0dcfa: new three-TSV G-S-S extraction solved. Maxwell C matrix (fF): [[7.73364348, -3.46365160], [-3.46365160, 5.80995368]]. Symmetry exact to exported digits. Eigenvalues positive (approximately 3.1771 and 10.3665 fF). Q3D CG adaptive 4 passes, final delta 0.18863% against 2% setting; 4358 total reported mesh elements. Source material is epsilon-r 11.7 and silicon conductivity 0 S/m, so this is a software/geometry feasibility pilot, not validation of 10 ohm-cm silicon. Charge/reference balance, cross-run mesh independence, physical trend, and domain checks remain open. No mesh license failure observed. G02 NOT PASSED.

## 2026-11-01 21:09 G02 revised pilot failure
Uploaded ZIP: run dated 2026-11-01 21:09, containing pilot_base and pilot_refine, both FAILED at Q3D solve. The requested explicit surface-length mesh seeds were 1.5 um and 1.2 um. Neither produced a C matrix. Reported exception: RuntimeError Q3D solve unsuccessful. The bundle omitted AEDT messages, saved solver profile and mesh-failure diagnostics, so no evidence currently proves Student mesh ceiling or its cause. A downloadable diagnostic v2.1 script was prepared with default no-mesh-operation baseline, gentler 6.0 um and 4.32 um length seeds, and best-effort AEDT GetMessages / failure mesh and profile exports. The diagnostic script has been syntax checked and dry-run tested but not yet tested in AEDT. G02 remains OPEN; do not run full campaign until diagnostic pilot reviewed.

## 2026-11-01 21:18–21:20 — G02 V2.2 student surface-mesh limit confirmed
User-uploaded G02 diagnostic bundle already includes full_console_transcript.txt and multiple cases/*/AEDT_messages_*.txt. pilot_base SOLVED. AEDT diagnostics from pilot_refine explicitly state mesh size 9956 surface elements greater than Student simulation limit; pilot_refine2 states 9516 surface elements greater than Student limit. These are observed solver failures, not inferred limitations. These failed finer-mesh cases do not establish <1% convergence. V2.2 also prints a shutdown-only logging ValueError because PyAEDT atexit still writes to a Tee whose file is closed; the ZIP itself was created beforehand. V2.3 Python artifact has been locally syntax/dry-run tested: safeguards closed streams, rebinds lingering logging handlers, includes final console transcript and logging status in rebuilt ZIP, labels verified mesh limit errors, starts with gentler mesh seeds (12 um then 9.6 um). Actual AEDT verification remains pending. G02 OPEN.
