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
