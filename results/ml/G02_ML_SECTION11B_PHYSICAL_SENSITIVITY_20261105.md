# G02 Section 11B — Frozen Pooled-SVR Physical Sensitivity (2026-11-05)

## Evidence and experiment status
Source: user-executed `ML (13).ipynb`, **code cell 16**, execution count 17, run following frozen 450-DOE Sections 1–11A. Section 11B executed successfully and printed **2,196 feasible sensitivity evaluations**. No retraining or tuning in 11B; predictions from the previously fitted 3-target-wise pooled SVRs in 11A (315 CAA train labels, 210 CBB, 210 CAB). The full executed notebook was supplied in chat; the notebook binary is not implied to be committed to GitHub by this text record.

### Reproducible setup
- Training-median reference geometry: D=**4.55362 µm**, P=**15.14774 µm**, H=**37.677 µm**, tox=**0.29933 µm**.
- Bounds used by Section 11B, derived from 315 training cases (NOT a demonstrated full fabrication constraint specification):
  - D: [3.01077,5.98829] µm
  - P: [10.04155,19.96818] µm
  - H: [25.01427,49.86637] µm
  - tox: [0.10127,0.49972] µm
- Topologies: GSG, GSSG, GSGSG. Resistivity scenarios: 1,10,100 Ω·cm. Four one-at-a-time sweeps: D,P,H,tox, **61 grid points per sweep**.
- 3 × 3 × 4 × 61 = **2196** = actual completed count, indicating **no points were filtered out** under the reference-geometry and current simplified `gap = P-D-2tox >= 3.5µm` feasibility check.
- Inputs to model: `log10_rho,D_um,P_um,H_um,tox_um` plus one-hot topology, where ρ handled in three scenarios. Prediction targets exist as CAA for GSG and CAA/CBB/CAB for GSSG/GSGSG.
- Curves are *conditional one-factor-at-a-time sweeps at a common reference geometry*, **not population-averaged PDPs**. Endpoint differences **do not prove monotonicity over every intermediate point**.
- The code generated 12-subplot CAA curves and 8-subplot |CAB| curves. It wrote local `SECTION11B_SENSITIVITY_CURVES.csv` and `SECTION11B_SENSITIVITY_SUMMARY.csv` but these CSVs are not automatically stored on GitHub.

## Verified numeric evidence — CAA endpoints, all topologies and ρ levels
Each row: topology, ρ, D increase (ΔCAA), H increase (ΔCAA), P increase (ΔCAA), tox increase (ΔCAA), in fF. All CAA changes have D,H positive and P,tox negative.
| Topology | ρ Ωcm | ΔD | ΔH | ΔP | Δtox |
| --- | ---: | ---: | ---: | ---: | ---: |
| GSG | 1 | +32.0107 | +28.3822 | -2.9946 | -71.9752 |
| GSG | 10 | +22.3666 | +26.5391 | -4.0226 | -50.7909 |
| GSG | 100 | +4.0486 | +7.5376 | -5.8039 | -2.7657 |
| GSSG | 1 | +32.9519 | +32.6150 | -1.6217 | -78.6857 |
| GSSG | 10 | +23.2901 | +28.5574 | -3.7552 | -49.1850 |
| GSSG | 100 | +5.7930 | +6.2809 | -5.3532 | -1.4643 |
| GSGSG | 1 | +33.7248 | +33.1440 | -5.1971 | -84.2964 |
| GSGSG | 10 | +22.9016 | +29.2161 | -4.9288 | -48.0233 |
| GSGSG | 100 | +5.3947 | +7.0940 | -5.1504 | -2.9151 |

## Verified numeric evidence — signed CAB endpoints (fF)
Reported ΔCAB is signed (last minus first). Since CAB is conventionally negative, more-negative CAB means **more** mutual-coupling magnitude, less-negative means **less** magnitude.
| Topology | ρ Ωcm | ΔCAB on ↑D | ↑H | ↑P | ↑tox |
| --- | ---: | ---: | ---: | ---: | ---: |
| GSSG | 1 | -11.0117 | -11.2919 | +0.1637 | +27.3819 |
| GSSG | 10 | -8.4681 | -9.7708 | +1.4727 | +17.7346 |
| GSSG | 100 | -2.6604 | -2.9326 | +2.2891 | +1.3479 |
| GSGSG | 1 | -7.4289 | -9.1938 | +1.7219 | +19.7323 |
| GSGSG | 10 | -1.5079 | -5.6156 | +2.6489 | +3.8531 |
| **GSGSG** | **100** | **-0.0991** | **-0.3993** | **+0.6574** | **-0.4220 (ANOMALOUS DIRECTION)** |

### Main anomaly — must preserve, do not silently sanitize
For **GSGSG, ρ=100 Ω·cm, tox sweep**, Section 11B prediction changes from **CAB=-0.2268 fF at low tox** to **CAB=-0.6488 fF at high tox**. Thus **|CAB| increases by ≈0.4220 fF as oxide becomes thicker**, contrary to the other 5 topology×ρ scenarios and usual capacitive-decoupling intuition. Furthermore this low-tox endpoint magnitude (0.2268 fF) is smaller than the lowest |CAB| seen in the original GSGSG labels (≈0.5858 fF), though this alone does not invalidate it because it is a newly constructed input geometry.
- This is **a surrogate prediction**, not a verified Q3D result.
- Do **not** retrain or change the frozen surrogate merely to force the expected trend.
- During optimization, prevent extrapolation and target this region for new high-quality Q3D checks if selected as an apparently favorable optimum.
- Check actual intermediate curves, multiple references, and local coverage before interpreting an endpoint trend as global monotonic physics.

## Findings / limits
- In all 9 topology×ρ scenarios CAA endpoint increases for D and H, decreases for P and tox.
- For all 6 two-signal topology×ρ scenarios, |CAB| grows with increasing D and H (signed CAB decreases) and generally shrinks with larger P.
- tox direction for |CAB| reduces in **5/6**, but **increases in 1/6** (GSGSG, ρ=100).
- This is a conditional sweep near training medians; physical-domain representativeness depends on local DOE coverage. The fixed 3.5 µm gap check is an **ad hoc diagnostic filter, not a validated geometry/fabrication constraint**; no pass/fail definitive safety gate is established.
- No quantitative monotonicity violation count, true held-out boundary challenge, or independent Q3D verification is demonstrated in Section 11B. These remain for later stages.
- Section 11A, separately, audited 450 DOE: no sign/diagonal/positive-definiteness or reported diagonal-dominance violations for pooled predictions at sampled points; this does **not** guarantee physical consistency throughout the continuous optimization domain.

## Decision / next step
**Section 11B accepted as descriptive physics-sensitivity evidence; anomaly explicitly flagged. Freeze surrogate.** Proceed to constrained optimization only after implementing actual G02 geometric bounds/constraints and transparent objective definitions (e.g. |CAB| / self-capacitance plus TSV footprint proxy P²), separately optimize resistivity scenario and topology, and schedule new independent Q3D checks on selected not-previously-simulated candidates. Do not claim real optimization results or fresh Q3D verification until those experiments run.

Related ML record: [G02 final ML study](G02_ML_FINAL_450DOE_20261105.md), [Decision log](../../docs/DECISION_LOG.md).
