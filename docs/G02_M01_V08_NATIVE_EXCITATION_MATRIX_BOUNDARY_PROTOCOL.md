# G02 M01 v0.8: Native excitation/matrix/boundary audit

Status: script compiled, AEDT user run pending. **Do not authorize solve yet.**

## Inputs
Existing user saved project `C:\CA2 result V2\02_numerical_convergence\V3_conductive_silicon\Maxwell_M01_BUILD06_20261102_175348\M01_GSSG_Maxwell.aedt`. M01 v0.7 native check validated four face IDs: GROUND_L=72, SIG_A=116, SIG_B=160, GROUND_R=204, all correct Cu top faces.

## Read-only v0.8 audit
The file `G02_M01_excitation_matrix_boundary_audit_v08.py` delivered separately uses a new isolated AEDT Student 2025.2 session and opens, but does not save, modify, or analyze the existing model. It tries `BoundarySetup.GetAssignment(name)` for excitation face IDs (Ansys documentation notes this replaces former GetBoundaryAssignment); `GetExcitations`, `GetExcitationNames`, and object-tree property readbacks where available, plus Matrix/Parameters module discovery and `GetBoundaries`. Unavailable API methods are recorded, not treated as false physical FAIL. Generates `G02_M01_VERIFY08_bundle.zip` with `verification_v08.json`, console and native messages.

Run:
`py -3.13 "C:\暂时下载\G02_M01_excitation_matrix_boundary_audit_v08.py" "C:\CA2 result V2\02_numerical_convergence\V3_conductive_silicon\Maxwell_M01_BUILD06_20261102_175348\M01_GSSG_Maxwell.aedt" --student --aedt-version 2025.2`

## Gate definitions
- `native_assignment_ids_verified` requires four returned `GetAssignment` face IDs to match 72/116/160/204. Any unavailable readback stays null, not PASS.
- Voltage magnitudes 0/1/1/0 V and Matrix signal IDs 1/2, ground 0/3 were independently extracted statically from saved `.aedt` in previous audit, but runtime native property verification is pending.
- `GetBoundaries()` returning `[]` does **not** imply absent voltage excitations. No grounded substrate boundary is modeled. Maxwell and Q3D outer-boundary conditions/reference are **not yet proven equivalent**; current continuity not checked, no solve performed.
- G02 remains OPEN even if M01 v0.8 verifies voltage/matrix because true HBM substrate ties not sourced and DOE geometry/topology qualification is pending.

## Source references
Ansys AEDT: https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v261/en/Subsystems/Maxwell/Subsystems/Maxwell%20Scripting/Content/GetBoundaryAssignment.htm , https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v261/en/Subsystems/Maxwell/Subsystems/Maxwell%20Scripting/Content/ObjectOrientedPropertyScripting.htm .
