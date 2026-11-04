# G02 V6.5 Phase B — direct MCAP/ASOL audit of 36 new R2/R4/R6 solves

**Audited 2026-11-05. G02 remains OPEN; no assertion of physics validation.**

## Evidence and provenance

Uploaded native archives: `G02_V65_PhaseB_RESULTS.zip` and `G02_V65_PhaseB_MCAP_ASOL.zip`. The frozen geometry and V6.3 physics/solver setup were reused; targeted independent adaptive runs vary only `Cap.PerRefine` = **2, 4, 6**. The 12 target DOE IDs were those with neither earlier R3 nor R5 passing the per-coefficient last-two-pass <1% check.

**36/36 cases have `SOLVED_UNVERIFIED_PHYSICS` solver status**, and **36/36 have ≥2 stored `DV*_SOL*_MCAP{pass}_V0.sd` files**. Each was parsed as a capacitance matrix in F then converted to fF. 36/36 complete final pass matrices agree with the separately exported `CG_Maxwell_fF_mS.txt` to max absolute difference < 1.5e-14 fF, and all stored pass counts match `convergenceCG.txt`. Native SD declares **Frequency=1000000000 Hz (1 GHz)** for all cases, while Ansys export headers still say `Frequency: 1kHz`; export-header explanation remains open.

Criterion: for each R run's final two adjacent adaptive passes, take the **maximum absolute relative percentage change in CAA, CBB and CAB**, using `100*abs(Cij_last - Cij_previous)/abs(Cij_previous)`. **Strictly <1%** is a pass. This is per-run stability, not a global discretization error bound. R2/R3/R4/R5/R6 represent separate adaptive solutions, not a monotonic mesh sequence.

## New 36-run success and pass statistics

| Newly run PerRefine | Solved | Pass individual-C <1% | Did not pass |
|---|---:|---:|---:|
| R2 | 12 | **7** | 5 |
| R4 | 12 | **2** | 10 |
| R6 | 12 | **3** | 9 |
| **Total** | **36** | **12** | **24** |

The new runs do **not** indicate that a higher `PerRefine` systematically improves last-pass coefficient stability. Observed pass histories span 3 to 9 adaptive passes; 26 of 36 cases stop after 3 passes. Median last-two-pass triangle growth = **2.4871%** (range **1.2048%–7.2319%**).

## Best-of-R2/R3/R4/R5/R6, compared to previous best-of-R3/R5

| DOE | Previous best worst delta (%) | Selected R | New best worst delta (%) | Numerical screen |
|---|---:|---|---:|---|
| DOE0052 | 1.189127 | R2 | 0.814131 | PASS |
| DOE0093 | 1.363676 | R4 | 0.191413 | PASS |
| DOE0099 | 1.316096 | R4 | **1.269489** | FAIL |
| DOE0100 | 1.195412 | R2 | **1.024578** | FAIL |
| DOE0170 | 1.078488 | R6 | 0.115252 | PASS |
| DOE0187 | 1.108209 | R6 | 0.481124 | PASS |
| DOE0233 | 1.329949 | R4 | **1.243862** | FAIL |
| DOE0277 | 1.172778 | R6 | 0.458203 | PASS |
| DOE0279 | 1.117097 | R2 | 0.848035 | PASS |
| DOE0321 | 1.665203 | R3 | **1.665203** | FAIL |
| DOE0406 | 1.188164 | R4 | 0.941327 | PASS |
| DOE0411 | 1.116374 | R2 | 0.756617 | PASS |

Of the 12 previously not-pass DOE, **8 now have at least one run with all individual C changes <1%; 4 still do not.** Four remaining: DOE0099 (best R4, 1.269489%), DOE0100 (best R2, 1.024578%), DOE0233 (best R4, 1.243862%), DOE0321 (best old R3, 1.665203%). Each is limited by relative CAB rather than CAA/CBB.

Selected R distribution: R2 = 4 DOE; R4 = 4; R6 = 3; R3 = 1; R5 = 0. Note an optimal *last-pass delta* may not be the most physically accurate final capacitance; preserve all original R3/R5 and new R2/R4/R6 native results.

## Updated global 450-DOE status

Original dataset: 436 points with ≥1 successful per-coefficient last-pass PASS plus DOE0402 with R5 PASS = **437**; originally 12 both-not-pass, 1 failed license (DOE0447). V6.5 recovers **8** of those 12, yielding **445 / 450** with ≥1 eligible *numerical last-pass stability* run. Remaining **four** coefficient-stability outliers and **one** Student-license DOE0447. DOE0402 R3 remains insufficient (single pass), though its R5 passed. This is NOT 445 fully physically validated points or 445 globally mesh-independent solutions.

## Recommended next actions

1. Do **not** initiate bulk 450-point reruns. Prioritize four CAB stability outliers, especially DOE0100 (1.024578%, narrowly >1%) and DOE0321 (1.665203%). Review the 3-pass stopping conditions and consider additional adaptive passes, alternate mesh policies or selected independent mesh refinements subject to the Student 8000-surface-element cap.
2. Inspect cross-run final C disagreement separately; picking the minimum last-pass delta can hide substantial final-matrix disagreement.
3. Handle DOE0447 separately via a license-compliant mesh strategy, retaining frozen physical geometry.
4. Continue domain independence, matrix symmetry/passivity, and H0 physical validation. The 1 GHz native-vs-1kHz export-header ambiguity needs documenting.

**Analysis deliverables kept with project chat:** `G02_V65_PhaseB_36_R246_Convergence.csv`, `G02_V65_PhaseB_12DOE_All_R23456_Convergence.csv`, `G02_V65_PhaseB_12DOE_Best_of_R23456.csv`, `G02_V65_PhaseB_All_Adaptive_Pass_C_Matrices.csv`, `G02_V65_PhaseB_36_Run_QA.csv`, and two plots. The complete detailed artifact bundle must be retained separately until added to GitHub.
