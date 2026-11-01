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
