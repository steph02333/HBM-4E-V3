# G02 V6.3 — complete 450-DOE adaptive-pass Cself/Cmutual audit

**Date:** 2026-11-04. **CURRENT NUMERICAL RESULT.** The 2% R3/R5 final-matrix screen, the old P1/P2 classifications, and 76-point remediation plan are historical independent-run diagnostics, **NOT** the criterion for within-run adaptive mesh convergence.

## Reproducibility / inputs

Source: five researcher-uploaded ZIPs named `G02_Chunk{1..5}_Adaptive_C_MCAP_asol.zip` and `G02_Adaptive_Matrix_Collection_Manifest.csv`; 450 unique frozen DOE IDs (DOE0001 through DOE0450) and 900 distinct R3/R5 results folders. Each pass capacitance matrix was recovered from `Design_*.results/DV*_SOL*_MCAP{pass}_V0.sd`, using the `AdaptivePass` solution block and MCAP ID/file mapping in `Design_*.asol`. `LastAdaptive` MCAP0 must **not** be confused with pass number 0. Matrices are SI farads converted to fF by ×10^15.

Joined 4,225 MCAP matrices from the 898 successful runs, **pass-by-pass 1:1** to the independently extracted `convergenceCG.txt` adaptive-pass histories by `(DOE_ID, run, pass)`. The two failed DOE0447 runs had 11 additional *partial* MCAP pass files; these are retained but excluded from success/convergence denominators. Total recovered 4,236 pass-matrix files, all 900 run folders accounted for; parser issues: 0. For chunks 2–5, the last-pass matrices were independently checked against final `CG_Maxwell_fF_mS.txt`: **698/698 successful runs matched all applicable coefficients** to numeric tolerance. The original chunk-1 final-export ZIP was not separately available for this particular 698-case cross-check; its MCAP files were parsed and matched to convergence history.

**Actual matrix-frequency metadata:** All 900 parsed `.sd` solution matrices declare `Frequency=1000000000` Hz, supporting 1 GHz *native matrix* provenance. Historical textual final-matrix exports display `1kHz`; that export-header discrepancy remains to be explained; do not misstate it as proven 1 kHz native solving.

## Metric (professor-aligned)

For one run's last two adjacent adaptive passes p−1 and p, calculate each individual Maxwell matrix coefficient:
`delta_Cij_pct = 100 * abs(Cij[p] - Cij[p-1]) / abs(Cij[p-1])`.

For GSG, check CAA (1×1). For GSSG/GSGSG, check CAA, CBB and signed CAB (2×2). Compare Cmutual as signed coefficient, retaining the sign (absolute difference makes the percent mathematically equivalent to comparing its magnitude where the sign is stable). A run **PASS_LT1** only if **all applicable individual coefficients** change strictly <1% in the last two passes. This is an **operational final-pass stability test**; it is not an absolute discretization error bound, proof of physics accuracy or proof that additional passes would never change the result.

R3 and R5 are **separate adaptive solutions** (`PerRefine=3` versus `PerRefine=5` per pass), so final R3/R5 element counts and capacitance differences are not the requested within-run adjacent-pass measurement. The professor did not require ≥5% or ≥10% final total-element growth.

## Full 900-run numerical results

| Run status | Count |
|---|---:|
| SOLVED; last two passes: **all individual C <1%** | **817** |
| SOLVED; last two passes: **at least one C ≥1%** | **80** |
| SOLVED; only one stored adaptive pass, no adjacent-pass comparison (DOE0402 R3) | **1** |
| FAILED Student surface-element license cap (DOE0447 R3 and R5), partial MCAP files do not certify success | **2** |
| **Total** | **900** |

**All 80 individual-coefficient failures are Cmutual/CAB**, not CAA or CBB. Every evaluable self-capacitance coefficient was <1% from penultimate to last pass. For the 897 evaluable successful runs, the median of the *maximum per-coefficient last-pass delta* is **0.280482%**, p90 **0.945925%**, maximum **2.052226%** (DOE0100 R5, CAB). Actual last two passes' *triangle-count increase* median **3.264925%**, observed range **1.779661%–6.186613%**. These within-solution triangle-growth figures must not be confused with the separate R3-final vs R5-final **total** element-growth figure.

## Full 450-DOE interpretation (strict BOTH-run confirmation, not professor-mandated requirement to run twice)

| Point status | Count |
|---|---:|
| **Both R3 and R5 last-pass coefficients all <1%** | **380** |
| Exactly one of R3/R5 meets <1% | **56** |
| Neither R3 nor R5 meets <1% | **12** |
| DOE0402: R3 only one pass; R5 passes; cannot assess both | **1** |
| DOE0447: both runs failed Student license | **1** |
| **Total** | **450** |

By chunk (BOTH_PASS / ONLY_ONE / BOTH_FAIL / NO_HISTORY / LICENSE_FAILURE):
- Chunk 1 (100): **84 / 15 / 1 / 0 / 0**
- Chunk 2 (100): **78 / 17 / 5 / 0 / 0**
- Chunk 3 (100): **93 / 5 / 2 / 0 / 0**
- Chunk 4 (100): **83 / 14 / 2 / 1 / 0**
- Chunk 5 (50): **42 / 5 / 2 / 0 / 1**

The 380-point both-run category is an **additional conservative cross-run reproducibility screen**, *not* a statement that the other 68 numerically evaluable DOE points need to rerun automatically. For a single simulation, the professor's further-adaptive-pass requirement is more directly assessed by its **own** last two passes. In particular, a DOE with one pass-level failure but one stable run may still support a limited, well-described result, pending robustness and physics validation. Do not automatically use any subset as ML ground truth.

## Why Ansys Delta C is insufficient

Previously collected `convergenceCG.txt` data contained final overall matrix Delta C <0.5% in **897/897** successful runs with a reported value. Direct MCAP extraction proves **80** of those successful runs nonetheless had **CAB last-pass relative change ≥1%**. Therefore a small solver matrix Delta C cannot be substituted for professor-requested individual Cself / Cmutual percentage changes. The large disparity is particularly relevant to smaller off-diagonal coupling terms.

## QA, remaining limitations, action

1. Preserve exact DOE ID / R3 / R5 / adaptive pass provenance and signed Maxwell matrices. Audit data are **not** R3-vs-R5 final differences.
2. Investigate the 80 runs with CAB ≥1%, prioritizing **12 DOE where both R3 and R5 fail**. Confirm whether additional Student-budget-compatible adaptive passes are required, or whether 1% is only a suggested representative demonstration rather than per-DOE acceptance rule.
3. Diagnose DOE0402 R3 one-pass history and license-failed DOE0447 separately; **do not** treat its residual SD files as solved labels.
4. Q3D's last two passes are not necessarily a strict continuum error bound. More stringent selected-case higher-resolution/independent solver checks and domain, matrix symmetry/passivity/physical consistency gates remain open.
5. The extraction demonstrates native C matrices at 1 GHz, but `CG_Maxwell_fF_mS.txt` export header's 1 kHz needs a documented explanation.
6. **Retire** the old 374/75 2%-pair-eligibility and 76-point broad mesh-remediation plan; do **not** launch 450 new simulations without reviewing the new numerical evidence.

**GitHub-committed per-point/per-run result tables:** [all 450 DOE point statuses and worst R3/R5 final-pass coefficient changes](G02_V63_ALL450_DOE_FINAL_PASS_WORST_COEFFICIENTS_20261104.csv), [all 900 R3/R5 runs with individual CAA/CBB/CAB last-pass changes and pass counts](G02_V63_ALL900_RUNS_LASTPASS_INDIVIDUAL_COEFFICIENTS_20261104.csv), and [exact 80 CAB >=1% run IDs and values](G02_V63_ALL80_MUTUAL_C_LASTPASS_GE1_RUNS_20261104.csv). All were audited for row counts and status totals.\n\n**Local researcher-delivered detailed CSV artifacts**: `G02_V63_ALL450_POINTS_VERIFIED_PASSWISE_C_CONVERGENCE.csv` (450 rows; final C and coefficient deltas), `G02_V63_ALL900_RUNS_VERIFIED_LAST_PASS_C_CONVERGENCE.csv` (900 rows), `G02_V63_ALL_ADAPTIVE_PASS_C_MATRICES_WITH_MESH.csv` (4236 rows; includes flagged failed-run partial SDs). They are generated from the five input ZIPs, not fabricated or inferred from R3/R5 pair differences. The entire 450-point and 900-run final-pass coefficient summary is now committed above; the full **4,236-row per-pass raw matrix history** is in the downloadable local audit package, **not yet uploaded as a GitHub table**. Do not misrepresent its storage location.
