# G02 V3.7: uniform Higher-order solver, reference/contact and frequency diagnostics
Date: 2026-11-02. **Experiment design, NOT AEDT results. G02 OPEN.**

## Downloaded runner
`G02_V37_higher_contact_frequency.py` SHA256 `daa4a015367a9b660cd741f0d68d09e335cf668bcbc389518599d26fd5311e89`.
Python syntax and 42-case `--dry-run` ZIP tested locally; not yet tested in Ansys Student 2025 R2. Preserve full executable and script hash in the user's experiment archive.

## Core decision
Use one **Higher solution order** for all silicon conductivities (1,10,100 S/m), with a common error target. Cross-check Direct versus Iterative on overlapping cases. Mesh counts need not be identical; actual independent mesh solution stability must be documented for C and meaningful G entries, with near-zero G assessed in absolute units. No automatic pass from small adaptive delta, successful solve, or nominal total mesh count.

## 42-case pilot
- 18 nominal material × mesh: 1/10/100 S/m; PerRefine 5,7,10,12,14 and Cu-SIG_A seed16; `Cap.SolutionOrder='Higher'`.
- 6 overlap Direct solver cases at two refinements for each conductivity, keeping Higher order.
- 9 independent reference/contact models for 10 S/m: no contact, far-edge grounded metal strip, corner grounded metal patch × three mesh settings. All contact electrodes are outside TSV metal and oxide. They are **boundary/reference hypotheses, NOT proof of semiconductor ohmic contact**.
- 9 frequency-dependent independent solves: 1,100,1000 MHz × 3 conductivities, all Higher order and up to 20 CG adaptive passes. Frequency convergence at low frequency must be checked, not inferred.
- Optional `--mode deep` adds 15 additional mesh/solver cases.

## Frequency export
Source uses PyAEDT 1.9-compatible `export_matrix_data` experimental selections: default adaptive, `sweep='LastAdaptive'`, `freq='<MHz>MHz'`, `freq='<number>', freq_unit='MHz'`, `freq='<Hz>',freq_unit='Hz'`. Matrix headers and full matrices are preserved for every attempt. **A header frequency mismatch is not repaired or dismissed as display-only without independent agreement.** The primary export uses default adaptive because previous forced exports often failed.

Vendor docs: https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.q3d.Q2d.export_matrix_data.html

## Net and reference audit
For each case the script records Cu/Ground net-object map, Q3D's `GetAssignment` and legacy fallback on Q3D BoundarySetup, all exported signal matrix net names, contact lateral clearance, material classifications and solver messages. It does not fake charge conservation: **independent signed SmoothQ field surface integration is not yet implemented** and remains a required technical gate. Reference contact electric current/ohmic physics cannot be certified by C/G sign changes alone.

Vendor docs: https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v261/en/Subsystems/Q3DExtractor/Subsystems/Q3DExtractor%20Scripting/Content/GetBoundaryAssignment.htm and https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/Subsystems/Q3DExtractor/Content/ReportsandPostProc/FieldquantitiesinQ3DExtractor.htm

## QA fixes inherited from V3.6
- Avoid erroneous all-true CG-warning flag by scanning per-case `AEDT_after_solve_design.txt` only, preserving matched message lines and raw convergence files. This remains to be verified with live AEDT.
- Stratified mesh comparisons separate *all* geometry, frequency, conductivity, solution order, solver algorithm, grounded contact **and contact variant**.
- Preserve [CASE 01/42] START and [DONE/FAILED 01/42] messages, remaining count, complete transcript, raw C/G, profile, mesh stats and source SHA in ZIP.
- Student licence limit applies to its own surface mesh counter, not the reported sum of mesh objects.

## Command
```bat
py -3.13 "C:\暂时下载\G02_V37_higher_contact_frequency.py" --mode pilot --student --aedt-version 2025.2
```
Upload `G02_V37_results_bundle.zip` from `C:\CA2 result V2\02_numerical_convergence\V3_conductive_silicon\run_<id>\`.

## Remaining G02 gates
Full 1/10/100 S/m consistency and independent mesh convergence, physically justified substrate and return contact, independent terminal/field-charge flux, separate physical silicon extent versus computational boundary, representative topology/geometry corners. Final ML DOE remains blocked.
