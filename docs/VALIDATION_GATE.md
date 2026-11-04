# Validation gates — Prof Lim instruction tracker

**Status: G01 PASS (2026-11-01); G02 OPEN; later gates BLOCKED.** Date initiated: 2026-11-01.

| Gate | Required evidence | Exit test | Status |
|---|---|---|---|
| G01 Analytical benchmark | Nine ideal Cu/SiO2/Cu reference-coax cases, raw Q3D matrices, convergence histories | All 9 absolute errors 0.776–1.668%, below 5% preliminary target; each final CG delta <0.5%. Ideal-coax-only scope explicitly stated. | PASS (2026-11-01) |
| G02 Mesh + physical consistency | Multi-TSV C matrix plus mesh-pass history, symmetry, physical trends, passivity/charge bookkeeping, domain-size sensitivity | Converged self and mutual capacitance to <1% under further refinement, remaining checks documented | OPEN |
| G03 Domain sensitivity | Increase simulation domain with identical physical test geometry | Boundary influence quantified, acceptable tolerance documented | BLOCKED |
| G04 Independent solver | 10–20 representative matched geometries in Maxwell/COMSOL or other independent field solver | ~2–5% agreement as target; define exact metrics/limitations before execution | BLOCKED |
| G05 Physical model revision | Evidence-backed dimensions D=3–6, P=10–20, H=25–50, tox=0.1–0.5 µm; Si resistivity 1/10/100 Ω·cm (10 nominal); GSG/GSSG/GSGSG arrangements | Geometry/material/net/return-path conventions justified; silicon conductivity conversion checked; sensitivity study complete | BLOCKED |
| G06 Sentaurus pilot | Selected representative cases with matched physics, voltage-dependent Cself and Cmutual | Quantify bias effect relative to solver uncertainty; decide whether voltage is necessary as ML input | BLOCKED |
| G07 Final simulation + ML | Only after preceding gates and documented scope approval: new versioned DOE, labels, QA, splits, models and independent Q3D optimum checks | Approved reference model, reproducible experiments and verified predictions | BLOCKED |

**Notes on ordering:** G05 is required *before* trusting final reference model or starting Sentaurus. G02–G04 should be run on a properly specified geometry; revisions may require repeating numerical validation and cross-solver checks. This tracker represents validation obligations, not a claim that all gates can be completed in a single linear pass.

### Exit protocol (all gates)
1. Freeze and version geometry, material, boundary conditions, sources and scripts.
2. Reproduce from a clean project with unique run identifiers.
3. Save raw exports + numerical pass histories + machine/software settings under the local results root.
4. Publish small result tables, figures, residual plots and a written failure analysis in Git.
5. Mark **PASS** only after checking criteria; record the reviewer, date and evidence links.
6. If a physical model changes after a gate passes, mark affected downstream gates **REVALIDATION REQUIRED**.

No previous CA2 dataset is admissible as a V3 gate result.

## G01 subcase progress (2026-11-01)

| Subcase | Numerical outcome | Decision |
|---|---|---|
| B01 | Analytic 84.045449519 fF; Q3D 84.875579314 fF; error 0.987715%; 6 CG passes; final delta 0.18624% (<0.5% solver target) | Numeric agreement favorable; evidence inspected; **G01 still OPEN** |
| B02–B09 | No new V3 evidence reviewed | NOT STARTED |

Traceability: [B01 evidence review](../results/g01/B01_20261101_175942_4a2c83_review.md) and [B01 numeric CSV](../results/g01/B01_review_metrics.csv).

A single reference-grounded coax capacitor is not evidence for 3x3 mutual coupling. It cannot establish the validity of the final TSV substrate model. Complete B02–B09 within G01 first.

## G01 closure decision — 2026-11-01
The new V3 bundle `20261101_180629_c27de8` was inspected directly: nine raw Q3D C matrices agree with the analytical coaxial Cu/SiO2/ground result, largest relative error 1.66823%. All nine CG convergence histories report final delta <0.5%. **G01 passes only as an ideal coaxial benchmark.** It does not independently validate doped Si, coupling, bias, or end-effect causality. The systematic positive offset may include end fringing; it remains an interpretation, not a proven cause.

**G02 OPEN:** first establish a representative multi-conductor geometry/net/reference specification. Do not interpret matrix row sums as unconditional zero where reference conductors are eliminated; the energy criterion requires the correct Maxwell coefficient convention.

## G02 V2.5 mesh-subcriterion result (2026-11-01)
New run 20261101_213418_7fcbd5: 10/10 solved; independently distinct mesh sizes 4388, 4780 and 7152 elements. Comparison 4780->7152: Cself_A 0.05717%, Cself_B 0.21037%, |Cmutual_AB| 0.17733%. Internal adaptive convergence final delta 0.34847% after six passes. Thus **nominal simplified dielectric-fixture mesh stability <1% is demonstrated**. These changes do not rigorously bound continuum discretization error; the 7152-element result is the *finest observed* mesh, not a proven maximum Student capability. G02 remains OPEN because physical charge balance and domain independence have not passed, and a realistic finite-resistivity Si final model requires fresh mesh/corner revalidation. See [detailed V2.5 audit](../results/g02/G02_V25_mesh_search_audit_20261101.md).

## 2026-11-04 — G02 V6.3: recovered per-pass Cself/Cmutual validation (new evidence)

**Direct original MCAP evidence now available.** Researcher supplied all five `G02_Chunk{1..5}_Adaptive_C_MCAP_asol.zip` archives plus the 900-run collection manifest. Extracted 4,225 individually mapped adaptive-pass Maxwell capacitance matrices from 898 successful R3/R5 solutions, plus 11 partial matrices from two license-failed DOE0447 runs. All 4,225 successful-run pass matrices match the prior `convergenceCG.txt` pass history by DOE/run/pass; 698 original final-matrix text exports from Chunks 2–5 match corresponding recovered last-pass values. Every native SD declares `Frequency=1000000000` Hz, although old exported text headers say `1kHz` (header mismatch still needs explanation).

For each successful run with >=2 adaptive passes, compute the last-pass relative change in each applicable Maxwell coefficient (GSG: CAA; GSSG and GSGSG: CAA,CBB,CAB). **817 of 897 evaluable runs** satisfy <1% for every entry, while **80 runs** exceed 1% for **CAB only**. DOE0402 R3 has one pass only; DOE0447 R3/R5 failed surface-license limits. Among 450 original DOE points: **380** have R3 and R5 both <1%, **56** have exactly one of R3/R5 <1%, **12** have neither <1%, **1** has missing adjacent-pass evidence, **1** has license failure. Actual median last-pass triangle growth ~3.264925% (897 evaluable runs).

**Decision correction:** Previous 374/75/1 grouping used two independently computed *final* matrices (R3 versus R5) and was not the professor's direct "further adaptive mesh refinement" check. Retire the 2% provisional ML-eligibility and 76-point follow-up plan; preserve historical R3/R5 differences as a separate sensitivity measure. Q3D matrix Delta C <0.5% does NOT imply small mutual coefficient relative changes (80 counterexamples). Despite new numerical evidence, **G02 remains OPEN** until representative coefficient-specific convergence, domain, symmetry/passivity, boundary conditions and physical model gate criteria are adjudicated; no blanket ML-label qualification.

Links: [full 450-point MCAP audit](../results/g02/G02_V63_450POINT_PASSWISE_CSELF_CMUTUAL_AUDIT_20261104.md); [all 450 DOE worst per-run final-pass coefficient percentages](../results/g02/G02_V63_ALL450_DOE_FINAL_PASS_WORST_COEFFICIENTS_20261104.csv).
