# Representative validation coverage for final ML (design decision, 2026-11-01)

**This is a prospective protocol, not a claim that simulations have been run or G02 has passed.**

## Scientific rule
Numerical validation follows the **physical model being trained on**. A mesh verified for a simplified G-S-S row with nonconducting silicon cannot certify finite-resistivity GSG/GSSG/GSGSG HBM TSVs. Keep existing G02 V2.5 results as a method demonstration; repeat representative checks after final topology, silicon conductivity, references and outputs are frozen. No previous CA2 labels reused.

## Domain suggested by Prof Lim
D: 3–6 µm; pitch P: 10–20 µm; H: 25–50 µm; SiO2 liner: 0.1–0.5 µm; silicon resistivity 1, 10, 100 ohm-cm (nominal 10); GSG, GSSG, GSGSG. Converting to SI: conductivity 100, 10, 1 S/m respectively. These are research ranges, not fabrication specifications.

## Representative validation strata (adaptive, not a fixed count)
1. Nominal for **each** physically valid topology and silicon condition (3 layouts x 3 resistivities); define each layout's own signal/ground nets and meaningful observables.
2. Stress corners: D maximum; pitch minimum; tall H; thin liner; opposing weak-coupling/far-pitch/small-D/thick-liner corner. Cover combinations that maximize mesh requirements as well as those that make mutual capacitance small.
3. One-factor trend sequences for D, P, tox (hold other features fixed), plus H checks. Record any unexpected trend with physical interpretation; do not assume every multiport coefficient is globally monotonic.
4. Sensitivity to silicon conductivity and to physical reference/substrate grounding, with frequency/return-path conventions made explicit.
5. Full-matrix checks, charge-reference bookkeeping, domain checks and independent cross-mesh checks at nominal and corners in **every materially distinct physical-model family**.
6. For any geometry family with convergence failure, increase audit density, refine local mesh or limit claimed accuracy. Never claim that sample count alone establishes convergence.

## ML label quality gates
Per run: solver solved, internal adaptive convergence, geometry validity, net IDs and reference, material settings, units, symmetry, passivity tolerance, mesh stats, license warnings, source script/solver version, unique run ID, full matrix and extraction target. Failures quarantined.
Across selected audits: at least two genuinely distinct solved mesh resolutions, <1% changes in relevant self and mutual, domain stability, charge-accounting review. Re-audit if physical model changes.

## ML dataset sizing
**Do not commit to 200 or 2,000 labels up front.** Begin with space-filling design in each eligible topology/material regime; hold out an independent corner/topology-aware final test set before adaptive sampling. Track learning curves for MAE/RMSE and relative error, with physically useful absolute-fF metrics on near-zero mutual terms. Add new Q3D points where uncertainty, high residuals or inadequate coverage warrant it. Keep the frozen test set untouched until final evaluation. When comparing layout generalization, explicitly choose holdout protocol (interpolation within topology vs transfer to unseen topology).
The final label budget and optimal ML architecture will be determined by evidence, software limits and target error requirements.

## Current statuses
- G01 ideal analytical coax benchmark: PASS.
- G02 nominal simplified dielectric fixture: mesh subcriterion demonstrated (4,780 -> 7,152 elements, worst observed change 0.2104%); domain and charge/reference tests still unresolved.
- G02 V2.7 proposed: mesh-verified domain/corner screening for current fixture; outcomes not yet reviewed.
- Final finite-resistivity and signal/ground reference model: not validated; must not be treated as ML-ready.
