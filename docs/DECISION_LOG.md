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
