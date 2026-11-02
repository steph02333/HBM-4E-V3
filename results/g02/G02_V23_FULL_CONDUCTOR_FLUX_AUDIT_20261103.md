# G02 v23 Full Conductor Complex E-Flux Audit — 2026-11-03

Evidence: user-supplied `G02_Q3D_EN_ALL23_diagnostic.zip` containing 16 `.reg` scalar exports and `status.json`. Frequency 1 GHz; saved `V3_Setup : LastAdaptive`; no new Analyze and no Save. Original AEDT SHA-256 before/after identical: `b52a00eb189d37356b8ae960f42a879ca4aa1dc282e49a2cf66df336ef4f3b81`.

## Execution
- A1 source edit PASS, B1 source edit PASS; A/B field response not identical.
- 16/16 real/imag normal E surface integrations succeeded across `CU_GROUND_L`, `CU_SIG_A`, `CU_SIG_B`, `CU_GROUND_R` for both source configurations.
- Candidate charge conversion is `eps0 * 3.9 * integral(E.normal)`, conditionally valid where metal faces adjoin oxide. It is **not** globally established charge on mixed-material conductor surfaces.

## Candidate flux (fC)
| Excitation | Conductor | Real | Imag |
|---|---|---:|---:|
| A1 | CU_GROUND_L | -13.7626334862 | 1.2504128893 |
| A1 | CU_SIG_A | 35.4068169191 | -9.7480777056 |
| A1 | CU_SIG_B | -11.5898601268 | 2.5971653731 |
| A1 | CU_GROUND_R | -9.0416646242 | 5.1294047768 |
| B1 | CU_GROUND_L | -9.0452786290 | 5.1319553551 |
| B1 | CU_SIG_A | -11.5906153603 | 2.5982967260 |
| B1 | CU_SIG_B | 35.4078303285 | -9.7482459348 |
| B1 | CU_GROUND_R | -13.7584995420 | 1.2497444483 |

## Matrix comparison and reciprocity
- Against previously recorded nominal native Q=C-jG/omega, A1 SIG_A real/imag errors 0.2111%, 0.5571%; A1 SIG_B 0.2444%, 0.6076%; B1 SIG_A 0.2379%, 0.5643%; B1 SIG_B 0.2159%, 0.5665%. All 8/8 under 1%; maximum 0.6076%.
- Cross terms: A1→SIG_B vs B1→SIG_A candidate real -11.5898601268 vs -11.5906153603 fC, symmetric relative difference 0.00652%; imag +2.5971653731 vs +2.5982967260 fC, symmetric relative difference 0.04355%. This is a field-response reciprocity diagnostic subject to common epsilon assumption, not an independent physical validation.
- Ground A1 L/R real -13.76263/-9.04166; B1 L/R -9.04528/-13.75850, showing expected swap pattern.

## Full four-conductor candidate sums (NOT conservation residual)
- A1: 1.0126586818 - j0.7710946663 fC.
- B1: 1.0134367972 - j0.7682494054 fC.
- Nonzero sums are not evidence of charge conservation failure or success. Cu surfaces may adjoin media with differing permittivity; field side/normal and infinity reference have not been independently checked; the latter is OPEN.

**Decision:** PASS v23 dual-excitation 16-register extraction, signal/matrix internal agreement, and reciprocal cross-field response. **OPEN:** globally valid displacement-flux surface audit, external infinity-reference closure, independent solver check. Stop repeating identical calculator probes; prioritize identifying material-interface surface coverage and a defensible independent Gauss surface, without re-solving unless necessary.
