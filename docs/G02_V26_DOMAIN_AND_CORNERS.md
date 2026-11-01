# G02 V2.6 — domain and corner mesh follow-up (2026-11-01)

**G02 status: OPEN**. Script artifact: `G02_validation_v2_6.py` shared in the project chat; this is based on `G02_validation_v2_5.py` with the same per-case Q3D logging/ZIP handling. Python syntax and `--dry-run` bundle were verified locally; **not yet tested inside Ansys**. The complete code is not yet committed to GitHub, so do not mistake this documentation update for a source commit.

## Motivation

The nominal simplified dielectric TSV fixture achieved measured cross-mesh changes below 1% between independent meshes of 4,780 and 7,152 elements. However, earlier finite-Si domain growth did NOT meet the 1% criterion. Charge balance remains an independent, unresolved concern. The final ML reference model must be revalidated after actual silicon conductivity and physical return path are fixed.

## V2.6 experiment scope

- Seven **finite silicon block margin** values: 25, 40, 60, 90, 130, 180, 250 micrometres, while D=4, P=15, H=35, tox=.3 micrometres stay fixed. A preliminary stability indicator requires *two consecutive domain increments* each produce <1% change in Cself_A, Cself_B and |Cmutual_AB|. This is a physical-body-size sensitivity check; it is **not** an independent open-boundary test.
- Two stressed corner geometries: close (D=6, P=10, H=50, tox=.1 micrometres) and far (D=3, P=20, H=25, tox=.5 micrometres), at silicon margin 40 micrometres. Each has default mesh and Cu-A-only surface constraints of 35 and 16 micrometres. Only actual distinct successful mesh-element counts count as independent meshes.
- Failures do not abort other groups; student limit messages, mesh files and AEDT diagnostics are bundled.

## User command

Save `G02_validation_v2_6.py` into `C:\暂时下载`:

```bat
py -3.13 "C:\暂时下载\G02_validation_v2_6.py" --mode domain-check --student --aedt-version 2025.2
```

All outputs are timestamped at `C:\CA2 result V2\02_numerical_convergence\runs\<id>\G02_results_bundle.zip`. Upload only the ZIP.

## Required interpretation

- Domain sensitivity and nominal/corner mesh stability are numerical requirements for the chosen *simplified* material model.
- Current silicon is `epsilon_r=11.7, conductivity=0` (not Prof Lim's `rho=10 Ω·cm`, corresponding to conductivity 10 S/m).
- Maxwell reduced-matrix row sums are not a physical charge conservation test. The existing inferred-reference-charge bookkeeping identity is **not an independent validation**. G02 charge closure must be addressed via explicitly defined complete conductors/return/reference surfaces or field-charge evidence.
- Before final ML DOE: freeze semiconductor model, topology and nets; redo nominated mesh/domain/charge checks on that *actual* model. Otherwise the G02 evidence is only preliminary.

**Do not mark G02 PASS until these remaining tests are independently reviewed.**
