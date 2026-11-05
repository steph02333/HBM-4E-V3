# G02 Section 12A — Sampled Pareto optimization audit (2026-11-05)

**Evidence:** Executed `ML (14).ipynb`, Section 12A (code cell 17, execution 18). Frozen pooled target-wise SVR, no retraining. No fresh Q3D runs yet.

## Exact method
The experiment generated 4096 scrambled Sobol geometries in four variables (seed 2026). Training-only bounds (µm): D 3.01077–5.98829, P 10.04155–19.96818, H 25.01427–49.86637, tox 0.10127–0.49972. A provisional geometric screen `P-D-2*tox >= 3.5 µm` retained 4092 geometries. Three topologies and discrete resistivities 1,10,100 Ω·cm produced **36,828 predictions**. The 3.5 µm gap is NOT a verified fabrication or complete Q3D geometry criterion.

The two minimized quantities are **GSG CAA** or **GSSG/GSGSG |CAB|**, and **P²** as a footprint proxy. CAA and CBB for two-signal topologies were recorded but not optimized as objectives. Predictions with invalid reduced capacitance matrices were excluded. The Pareto front is the nondominated set *among the generated candidates*, not a proof of global optimum. `Balanced` selects a 50/50 normalized-objective compromise (illustrative weights only). `MinCap` selects lowest predicted capacitance among valid Pareto points.

## Actual observed results
- **4096** Sobol inputs; **4092** passed provisional gap; **36,828** model evaluations.
- **83 matrix-invalid** predictions on previously unsampled geometries: **82** in GSGSG at rho=100, **1** in GSSG at rho=100, **0** in other seven scenarios. The output alone does not establish which particular positivity/sign/determinant predicate failed.
- Matrix-valid counts 4092 for seven scenarios, 4091 for GSSG/rho100, 4010 for GSGSG/rho100.
- **94** Pareto points across nine scenarios; **18 selection rows**, some sharing geometry across scenarios.

### Minimum sampled predicted capacitance (fF)
| Topology | rho=1 | rho=10 | rho=100 |
|---|---:|---:|---:|
| GSG CAA | 15.93698 | 13.60279 | 4.44237 |
| GSSG |CAB| | 5.84016 | 5.10520 | 0.85201 |
| GSGSG |CAB| | 3.04223 | 2.97970 | **0.00310** |

**High-priority anomaly:** GSGSG, rho=100, **OPT00662**: D=3.89953, P=12.47773, H=25.28898, tox=0.11152 µm; predicted CAA=8.27770, CBB=8.64167, CAB=-0.00310 fF. The balanced alternative **OPT02705** is also near-zero (CAB=-0.08708 fF). These are **surrogate predictions only, not independently simulated Q3D physics**, and align with the concerning anomalous oxide-thickness sensitivity reported in Section 11B.

The original 450 DOE Section 11A physical audit found zero detected invalid matrices; the new Sobol audit finds violations. The surrogate therefore cannot be assumed matrix-valid throughout the continuous design space solely from its original held-out scores.

## Interpretation and verification gate
**Accept 12A as an exploratory Pareto analysis, not a verified optimized design.** Before new Q3D runs, confirm the selected geometry in the actual G02 build script, check nearest *same-topology and same-resistivity* training neighbors (the current nearest DOE is based on 4D geometry alone), and choose a deliberately small confirmation shortlist including both ordinary cases and the suspicious GSGSG/rho100 regime. A low predicted |CAB| can arise from extrapolative or poor surrogate behavior. Do not report 0.00310 fF as a validated HBM improvement.

Final source numeric files in this folder:
- [Nine scenario summary](G02_SECTION12A_PARETO_SUMMARY_20261105.csv)
- [All 18 selected rows](G02_SECTION12A_SELECTED_CANDIDATES_20261105.csv)

**Reproducibility:** The supplied executed notebook is about 5.7 MB and is not committed here; the full 36,828-row candidate CSV and 94-row Pareto CSV also remain local execution outputs. These Markdown/CSV artifacts preserve the report-relevant verified printed tables, not the entire executable state. See [final ML research record](../ml/G02_ML_FINAL_450DOE_20261105.md).
