# G02 V6.7 Phase C — 7-solve native adaptive-pass C audit (2026-11-05)

## Scope and data

**Two original user-uploaded native packages**: `G02_V67_FINAL_RESULTS.zip` and `G02_V67_FINAL_MCAP_ASOL.zip`. Seven completed Ansys Q3D Student 2025.2 solutions (`SOLVED_UNVERIFIED_PHYSICS`): DOE0099, DOE0100, DOE0233, DOE0321 with `PerRefine=1`, `mesh_seed_um=8.0`; DOE0447 with `PerRefine=1`, `mesh_seed_um=6.0,8.0,10.0` while keeping the original frozen geometry/materials/nets.

All **7/7** runs have saved adaptive-pass full Maxwell C matrices: 3 passes each for the four GSGSG outliers, 4 passes each for DOE0447. Native files `DV*_SOL*_MCAP{pass}_V0.sd` contain `Frequency=1000000000` Hz. Final-pass matrices agree with the corresponding `CG_Maxwell_fF_mS.txt` exports to a **max absolute difference of 2.84e-14 fF** in all seven cases. As previously observed, the exported text reports `Frequency: 1kHz` despite 1 GHz native SD frequency and requested 1000 MHz; this header discrepancy remains unresolved.

Per-run coefficient criterion: last two consecutive adaptive passes, `100*abs(Cij[p]-Cij[p-1])/abs(Cij[p-1])`, require **every applicable CAA,CBB,CAB <1%**. Not a physics model validation or strict continuum-error bound.

| DOE | Phase C configuration | ΔCAA % | ΔCBB % | ΔCAB % | Worst % | Screen |
|---|---|---:|---:|---:|---:|---|
| DOE0099 | R1, 8um | 0.089233 | 0.086186 | 1.156310 | **1.156310** | FAIL (CAB) |
| DOE0100 | R1, 8um | 0.033808 | 0.031303 | 0.537153 | **0.537153** | PASS |
| DOE0233 | R1, 8um | 0.097006 | 0.090006 | 1.321183 | **1.321183** | FAIL (CAB) |
| DOE0321 | R1, 8um | 0.090623 | 0.087453 | 1.249977 | **1.249977** | FAIL (CAB) |
| DOE0447 | R1, 6um | 0.066891 | 0.066539 | 0.093075 | **0.093075** | PASS |
| DOE0447 | R1, 8um | 0.020791 | 0.022070 | 0.015313 | **0.022070** | PASS |
| DOE0447 | R1, 10um | 0.020791 | 0.022070 | 0.015313 | **0.022070** | PASS |

**DOE0447 Student license recovery:** all three new R1/seed cases solved; choose **R1, seed=8um** as the representative from tied 8/10um results, since it also matches the original 8um seed rather than needlessly changing a second mesh control. Recovered DOE0447 final Maxwell C matrix in fF:

```
[[ 16.618041..., -6.565857... ],
 [ -6.565857..., 16.618623... ]]
```

**Note:** 6um and 8/10um are independent mesh policies. Their close final matrices and internal pass stability do not independently establish continuum error bounds. The actual Student cap is 8,000 3D surface elements, not archived total volume elements.

## Updated best-available selected-run, final-C-matrix ML-label *candidates*

**Critical data provenance invariant:** `selected_R`, `selected_case_id`, and `selected_CAA/selected_CBB/selected_CAB` must all refer to the **same successfully solved run's final capacitance matrix**. Never choose an R based on its last-pass stability but use another R's matrix values, average different R outputs, or treat failed solver partial SD files as training labels.

Relative to V6.5 best-available 450-row candidate table:
- **DOE0099:** old R4 worst 1.269489%; new R1 worst **1.156310%**. Select R1 as best available provisional record, **FAIL/EXCLUDE strict-ML**, not 1%-verified.
- **DOE0100:** old R2 worst 1.024578%; new R1 worst **0.537153%**, **PASS**, selected final C: CAA=86.205011 fF, CBB=86.248074 fF, CAB=-8.802016 fF.
- **DOE0233:** old R4 worst **1.243862%** better than new R1 1.321183%; retain R4, **FAIL/EXCLUDE strict-ML**.
- **DOE0321:** old R3 worst 1.665203%; new R1 worst **1.249977%**, select R1 provisional record, **FAIL/EXCLUDE strict-ML**.
- **DOE0447:** previous R3/R5 solver failure and invalid partial matrices; select newly successful **R1, 8um**, last-pass worst **0.022070%** (CBB), **PASS**, final CAA=16.618041 fF, CBB=16.618623 fF, CAB=-6.565857 fF.

**Updated aggregate 450 DOE:** **447/450** have at least one successful run with strict last-pass coefficient-change <1%. Remaining **3 numerical CAB outliers**: **DOE0099, DOE0233, DOE0321**. No DOE remains without a successful native capacitance matrix. DOE0447's earlier FAILED_LICENSE and partial matrix labels must be superseded by its successful R1 native C result; do not backfill the old invalid R3/R5 result.

## Interpretation / next work

R1 does not guarantee monotone refinement with R2–R6: each policy generates a different adaptive mesh trajectory, and a smaller *last-pass coefficient difference* does not prove a more accurate physical C. The numerical last-pass screen is one axis; final R-policy sensitivity and representative independent mesh/domain/physical checks remain required. G02 remains **OPEN**, especially for simplified homogeneous Si assumptions and Q3D 1GHz native/1kHz export header provenance.

Current final user-deliverable candidate files: `G02_V67_ALL450_SELECTED_R_ML_LABEL_CANDIDATES.csv`, `G02_V67_7_RUNS_VERIFIED_CONVERGENCE.csv`, `G02_V67_ALL_NATIVE_ADAPTIVE_PASS_C.csv`, `G02_V67_QA_NATIVE_VS_EXPORTED_FINAL_MATRIX.csv`. Saved in the chat's Phase C final audit ZIP.

**Do not assert that 447 labels have been physically validated or are automatically approved for training.**
