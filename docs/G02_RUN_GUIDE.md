# G02 execution guide — pilot first

Created 2026-11-01. Status: **G02 OPEN / NOT VALIDATED**.

## Technical scope
- A *fresh*, simplified **G-S-S** 3 TSV row: Cu cores, 0.3 µm nominal SiO2 liners, finite homogeneous silicon-permittivity block.
- **Silicon is assigned epsilon_r=11.7 and conductivity=0 for this initial resource/solver test.** This is deliberately **NOT** a realistic finite-resistivity doped Si substrate and must be revisited before results can support an HBM-relevant claim.
- Ground TSV is a Q3D grounded net; the two independent signals `SIG_A` and `SIG_B` give a 2x2 Maxwell coefficient matrix.
- Model has no pads/hybrid bonding/active semiconductor regions. A domain sensitivity sweep of silicon block margin alters the *physical finite material block*, so interpret changes accordingly.
- Before claiming charge conservation, validate reference charge and exterior flux; reduced Maxwell matrix row sums alone are **not** zero-conservation test.

## Student Edition precautions
AEDT Student 2025 R2 has mesh-element licensing restrictions. The campaign halts on the first exception and preserves a diagnostic ZIP. Mesh pass budgets do not guarantee element limits will be respected. The pilot checks basic geometric/API capability only. Any limit claim must be backed by actual license error or output mesh counts.

## Run on Windows
Save `scripts/G02_validation.py` from GitHub into `C:\暂时下载\G02_validation.py`. Open Windows CMD and execute:

```bat
py -3.13 "C:\暂时下载\G02_validation.py" --mode pilot --student --aedt-version 2025.2
```

Use `--dry-run` first if desired to inspect the planned case and output folder. Use the explicit `-3.13` Python selector; the script launcher previously selected an unintended Python for G01.

Outputs are automatically saved under:

`C:\CA2 result V2\02_numerical_convergence\runs\<run_id>\`

Upload that run folder's `G02_results_bundle.zip` regardless of success/failure. The bundle excludes large saved AEDT projects.

**After we inspect the pilot only**, we can launch the wider resource-adaptive assessment:

```bat
py -3.13 "C:\暂时下载\G02_validation.py" --mode campaign --student --aedt-version 2025.2
```

The current initial campaign contains 4 mesh settings, 4 pitch perturbations, 3 diameter perturbations, 2 liner changes, 3 silicon-margin changes, and 2 corner studies (18 total configurations). This is a **starting coverage plan**, not a fixed maximum or a claim of sufficiency; we may add corner/mesh tests based on quantitative evidence.

## G02 PASS criteria
Must document <1% stability of self and mutual C under additional mesh refinement where feasible, matrix symmetry/passivity, correct reference/charge accounting, trends, and finite-domain sensitivity. In particular, this initial zero-conductivity Si feasibility fixture does **not** satisfy Prof Lim's realistic 10 ohm-cm silicon recommendation. Expect model updates and revalidation before G02 formally passes.
