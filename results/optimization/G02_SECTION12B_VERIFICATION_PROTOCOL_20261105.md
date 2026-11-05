# G02 Section 12B — Pre-registered Q3D verification protocol and failure registry
Date: 2026-11-05. **Status: PLANNED / no new Q3D measurements.** Final models and Section 12A prediction values are frozen. This is a verification proposal, not an optimization success claim.

## Why this gate is required
1. 450 original DOE physical-matrix checks passed but **83/36,828** new Sobol scenario predictions violated the 2x2 matrix-validity filter (82 GSGSG rho=100; 1 GSSG rho=100). This discrepancy is a negative observation and remains in the final report.
2. Section 11B GSGSG at rho=100 shows a counterintuitive oxide-thickness response; Section 12A predicts near-zero mutual capacitance at GSGSG/rho100 OPT00662 **|CAB|≈0.00310 fF** and balanced OPT02705 ≈0.08708 fF. These are possible surrogate artefacts; no physical result has yet confirmed them.
3. The sampled 94-point Pareto set came from 4096 Sobol geometries filtered only by a provisional 3.5 µm gap and a reduced-matrix check. **It is not a proven global Pareto front or validated manufacturing feasibility.**
4. Previous Section 12A `nearest_DOE_ID` is nearest in normalized four-dimensional geometry **across all topologies/resistivities**, possibly the wrong operating condition. Section 12B must recompute proximity only against matching topology and resistivity, using the 315 training rows.
5. The original Q3D production geometry builder places parallel cylindrical TSVs at pitch P, core radius D/2 and outer oxide radius D/2+tox; verify P>D+2tox, positive dimensions, non-overlap, materials/sigma settings and identical solver/mesh strategy. These checks are necessary, **not proof of full solver geometry/simulation validity**.

## Frozen preliminary four-case shortlist (from the 18 saved Section 12A rows)
The following are *candidates for screening*, not launched simulations. Intentional mixed coverage rather than selecting only a predicted perfect result:
| Role | Topology | rho (Ωcm) | Candidate | D µm | P µm | H µm | tox µm | Predicted target |
|---|---|---:|---|---:|---:|---:|---:|---|
| Single-signal practical compact | GSG | 10 | OPT03671 (Balanced) | 3.66596 | 10.18120 | 25.27173 | 0.47402 | CAA 16.28199 fF |
| Dual-signal compact | GSSG | 10 | OPT01697 (Balanced) | 3.25457 | 10.35803 | 26.88344 | 0.45922 | CAB -5.90963 fF |
| Dual-signal low coupling, larger footprint | GSGSG | 10 | OPT02901 (MinCap) | 4.52527 | 19.93439 | 26.07906 | 0.44081 | CAB -2.97970 fF |
| **Deliberate possible failure** | **GSGSG** | **100** | **OPT00662 (MinCap)** | **3.89953** | **12.47773** | **25.28898** | **0.11152** | **CAB -0.00310 fF (UNVERIFIED / SUSPICIOUS)** |

**Preserve full-precision geometry from Section 12A selected CSV or the in-memory `selected12`; table above rounds for readability.** Use full predicted vector [CAA,CBB,CAB] on every relevant two-signal candidate, not CAB alone. Each Q3D verification run must be independent, on previously unsolved exact geometry/topology/rho combinations. Existing campaign data cannot be re-labelled as fresh verification. Four-case budget is provisional, not a statistically representative validation set.

## Required preflight outputs before Q3D
- Exact candidate parameter manifest, run tag, objective, solver version, native matrix frequency (1 GHz), sigma=100/rho S/m (check units: ρ in Ω·cm gives sigma_Spm=100/rho), and selected-R mesh scheme.
- Geometry checks: original DOE envelopes; P-D-2tox; source builder's pitch/net layout/core/oxide overlap, silicon domain and margin; distinct new geometry check against **all original DOE with matching topology and rho**.
- A nearest-neighbour table with normalized distance to **same-topology/same-rho TRAINING rows**, also disclose distance to existing validation/test rows **only after freeze** if needed for provenance, not for candidate selection. Nearest-distance is a heuristic, not calibrated uncertainty.
- A local prediction check around each candidate (perturb geometry while staying within DOE domain) and explicit number of invalid matrix predictions. **Keep every invalid prediction in the audit output**, not just passing records.
- Full-precision pre-Q3D surrogate prediction per coefficient; SHA-256 of manifest. Frozen model parameters and fit source (315 train) unmodified.

## Pass/fail reporting (do not move goalposts after seeing Q3D results)
For each run log: launched/succeeded/failed and reason; solver Q3D matrix provenance; last two native adaptive-pass matrices with per-component ΔC and chosen mesh setting; all Q3D and surrogate coefficients (fF); absolute and relative error (relative error marked unstable near tiny target CAB); sign / positive-definiteness checks; optimization objective vs a **proper comparable Q3D baseline** (same topology and rho; same objective). **Do not claim successful optimization merely because prediction agrees with Q3D**, and do not claim accurate coupling when prediction is near 0 unless absolute solver-noise/mesh criteria support it.

Report every result including failures, inconvenient signs, unsuccessful convergence, or mismatched predictions; no data erasure or post-hoc exclusion. If OPT00662 Q3D CAB is materially nonzero, record as explicit **surrogate exploitation/failure under optimizer search**, not 'unexpected outlier' to remove. If OPT00662 is close to zero, independently corroborate mesh convergence before claiming engineering meaning. No retuning the model after looking at verification results for the present evaluation.

## Evidence links
- [Section 12A anomaly + Pareto audit](G02_SECTION12A_PARETO_AUDIT_20261105.md)
- [Full 18 selected candidates](G02_SECTION12A_SELECTED_CANDIDATES_20261105.csv)
- [Section 11B counterintuitive sensitivity](../ml/G02_ML_SECTION11B_PHYSICAL_SENSITIVITY_20261105.md)
- [Original frozen ML study](../ml/G02_ML_FINAL_450DOE_20261105.md)

## Outcome as of protocol creation
No Section 12B numeric preflight or independent Q3D confirmation has yet been executed. The proposed code must be run against the exact final notebook state; record its actual output in a follow-up audit before requesting new simulations.
