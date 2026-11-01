# Validation gates — Prof Lim instruction tracker

**Status: G01 OPEN; all later gates BLOCKED.** Date initiated: 2026-11-01.

| Gate | Required evidence | Exit test | Status |
|---|---|---|---|
| G01 Analytical benchmark | New multi-geometry single cylindrical Cu/SiO2 simulations, analytical calculations, matched boundary conditions and error report | Numerical agreement evaluated against a predeclared target (initial target ≤5% for suitable ideal benchmark geometry); any outlier explained, raw outputs archived, review documented | OPEN |
| G02 Mesh + physical consistency | Multiple TSV geometries; pass-by-pass Cself and Cmutual, symmetry, sign, passivity, charge/terminal balance, trend checks | Additional refinement changes selected key C values <1%; failed checks resolved or characterized | BLOCKED |
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
