# Unified 450-point V6.3 DOE: 2% numerical C screening and mesh-cap investigation

**Date:** 2026-11-04. Analyze all five frozen original DOE chunks as **one 450-row database**, not five separate quality pools. Independently derived from the five 100/50-point mesh-audit CSVs; all 450 original IDs unique.

## New operational selection rule versus professor's mesh study

For each successfully paired DOE point, use the worst R3/R5 relative difference across relevant CAA, CBB and |CAB| (GSG: CAA). Under the **researcher's requested, operational 2% threshold**, 374 original points are provisionally retainable: 312 <1%, 62 from 1% to <2%. **75** require targeted follow-up: 64 in 2–<5%, **11 ≥5%**. **One failed** original DOE point, DOE0447, lacks any paired C label. Combined: **449/450 paired, 898/900 successful solves**.

**Do not confuse operational <2% screening with <2% absolute mesh error.** The professor's original indicative **<1% further-refinement demonstration** remains a separate, stronger evidence requirement. No arbitrary ≥10% total mesh growth condition is mandated.

| Topology | rho (Ωcm) | <1% | 1–<2% | 2–<5% | ≥5% | Failed |
|---|---:|---:|---:|---:|---:|---:|
| GSG | 1 | 24 | 6 | 17 | 3 | 0 |
| GSG | 10 | 49 | 0 | 1 | 0 | 0 |
| GSG | 100 | 47 | 3 | 0 | 0 | 0 |
| GSGSG | 1 | 20 | 8 | 15 | 7 | 0 |
| GSGSG | 10 | 31 | 19 | 0 | 0 | 0 |
| GSGSG | 100 | 33 | 8 | 8 | 1 | 0 |
| GSSG | 1 | 33 | 6 | 11 | 0 | 0 |
| GSSG | 10 | 40 | 3 | 7 | 0 | 0 |
| GSSG | 100 | 35 | 9 | 5 | 0 | 1 |
| **Total** | | **312** | **62** | **64** | **11** | **1** |

Among the **75 ≥2%**, 53 are rho1, 8 rho10, 14 rho100; GSG 21, GSSG 23, GSGSG 31. Worst coefficient: 48 mutual AB, 22 self AA, 5 self BB. These are prioritization signals, NOT proven causal mechanisms.

## Distinguish Student license surface counter from CSV total-mesh elements

Ansys Student Q3D official limit: **8,000 3D surface elements**, **64,000 3D volume elements**. The CSV's `elements_R3/R5` are **exported total mesh-statistics elements**, **NOT the internal license-checked surface count**. Among 449 solved pairs, **144** have at least one exported total ≥8,000 (R3 >8000: 54; R5 >8000: 143). Largest exported total **15,076**, DOE0041 (successfully solved with C-delta 0.627%). **45 of 75** ≥2% cases have exported max total ≥8,000, 30 have <8,000. **None of these 144 may be called a license violation from total counts alone.** Every ID and R3/R5 total is in local researcher-delivered `G02_V63_ALL450_TOTAL_MESH_GE8000_POINTS.csv`.

**Confirmed actual 3D surface LICENSE EXCEEDANCE** from original raw Chunk5 `AEDT_after_solve_design.txt`: **DOE0447, GSSG, rho=100 Ωcm (sigma 1 S/m)**, physical D/P/H/tox 5.35525/16.12131/48.12573/0.21186 µm. R3 exceeds with **8030 surface elements** and R5 with **8340 surface elements**; both failed. Do **not** rerun blindly with a finer R7. Instead hold geometry and materials fixed, use controlled coarser initial surface seed or redistribute object-based mesh, and get two distinct successful, mutually stable meshes under the license cap. The four earlier chunks' original per-case AEDT messages are not in the five aggregate CSVs, so exact license surface counts for each historical point **cannot** be inferred from these CSVs.

**Increasing MaxPass alone is not the solution:** DOE0407 R5 native convergence has **8 completed passes vs allowed 22**, internal adaptive Delta=0.12092% against 0.5% criterion, but R3/R5 mutual C differs **6.182%**. Native solver's internal convergence metric differs from cross-mesh coefficient robustness; merely running more passes with same stop policy may do nothing. Among 449 paired points, 12 have *lower total exported mesh count in R5 than R3*, hence **R5 is not automatically the finer reference**.

## Recommended practical decision tree

1. **Preserve original 450 DOE coordinates and complete raw R3/R5 provenance.** No silent resampling, dropping, replacing or relabeling as validated physics. For ML provisional data use 374 points under the new <2% screen, with 312/62 substatus and separate holdout-stratification documentation.
2. **Repair DOE0447 license failure separately** before claiming 450/450 fully acquired. If a mesh refinement algorithm hits 8000 surface triangles, alter nonphysical mesh controls with proof, not silicon conductivity or geometry.
3. **Pilot controlled THIRD-MESH validation on 3–4 cases first** spanning extreme GSG AA, GSGSG AB and GSSG AB; expand to **all 11 ≥5%** only if viable under Student license. One genuinely different mesh (changed oxide-surface length/target allocation or percent refinement and verified achieved surface counts) is more informative than blanket R7.
4. **Then work through 64 remaining 2–<5% cases**, ranked by discrepancy, rho, topology and *actual* accessible mesh budget. For each, compare **R3, R5, M3** relevant signed C terms; look for agreement of two genuinely distinct sufficiently resolved solutions and trend toward stable C. If stable at <2%, retain the better justified mesh label; otherwise tag `NUMERICALLY_UNRESOLVED`. No averaging contradictory R3 and R5 outputs just to force pass.
5. **Keep the professor's <1% numerical-convergence demonstration separate**, with suitable independent finer mesh evidence on representative cases; continue to investigate all five chunks' 1GHz exported frequency-header mismatch and homogeneous-silicon H0 physical model limitations before claiming reliable ML ground truth.

## Working data delivered to researcher

- `G02_V63_ALL450_UNIFIED_MESH_2PCT_AUDIT.csv`: all **450 DOE points**.
- `G02_V63_ALL450_GE2PCT_POINT_BY_POINT_TARGETS.csv`: all **75 ≥2%** DOE IDs, exact geometry, R3/R5 total mesh and per-component errors.
- `G02_V63_ALL450_TOTAL_MESH_GE8000_POINTS.csv`: all **144** exported-total-mesh ≥8k DOE IDs, **not license violations**.
- `G02_V63_ALL450_UNIFIED_BY_STRATUM_2PCT.csv`: nine 50-point strata.
- `G02_V63_ALL450_GLOBAL_2PCT_MESH_REMEDIATION_REPORT.md`: fuller locally generated analysis.

**Current status:** 374 provisionally eligible under changed 2% ML screen; 75 targeted mesh-quality follow-up cases; 1 confirmed Student 3D-surface license failure. Full improvement to <2% for all is **not guaranteed** by current evidence or student limits.
