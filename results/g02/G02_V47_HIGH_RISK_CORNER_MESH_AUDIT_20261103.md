# G02 V4.7 high-risk corners: paired adaptive-mesh audit (2026-11-03)

Source: researcher-uploaded `G02_V47_H0_corner_mesh_results_bundle.zip` (eight case result.json, mesh_stats, CG profile and logs); audited after V4.6. GSSG, H0 no explicit Si ohmic contact, homogeneous Si sigma10 S/m, margin25um, 1GHz requested, Higher iterative, PerError0.5, maxpass22. Four geometry corners, each two adaptive `PerRefine` settings 12% and 18%.

| Corner D/P/tox/H um | R12 total elements | R18 total elements | R12 triangles last CG | R18 triangles last CG | Max self C pair delta % | abs CAB pair delta % |
|---|---:|---:|---:|---:|---:|---:|
| A 6/10/0.1/50 | 2284 | 2816 | 1532 | 1798 | 0.13372 | 0.09759 |
| B 3/20/0.5/25 | 2720 | 3436 | 1770 | 2132 | 0.06857 | 0.39136 |
| C 6/10/0.5/50 | 1920 | 2260 | 1350 | 1522 | 0.11376 | 0.41176 |
| D 3/10/0.1/50 | 1908 | 2980 | 1344 | 1880 | 0.28141 | 0.05582 |

Relative pair delta: abs(R12-R18)/abs(R18) * 100. All 8/8 marked SOLVED_UNVERIFIED_PHYSICS; different mesh counts in every paired case; all 12 signed CAA/CBB/CAB relative pair comparisons <1%; maximum 0.41176%. C and G symmetry/passivity checks passed; no CG adaptive nonconvergence warnings recorded. These counts do NOT by themselves certify independent surface-triangle license metrics.

**Decision:** four high-risk sigma10 GSSG corners PASS paired adaptive-mesh consistency for capacitance. This is **not** proof of absolute <1% error or independent orthogonal local-oxide mesh convergence; cannot transfer pass automatically to sigma1/sigma100, other topology, arbitrary unsampled combinations. Historical sigma1 oxide cross-strategy ~1.5% and sigma100 G cross-strategy up to ~12.62% remain explicit limitations.

**DO NOT restart Maxwell M01**: numerical comparison already run, geometry matched but exterior BVP mismatch between Q3D infinity and Maxwell default Neumann remains unresolved. Existing nominal C crosssolver differences +2.80% self and +4.86% mutual, not strictly independently validated identical boundary. Independent charge closure also not verified.

**Next:** begin constructing **provisional C-only DOE workflow** with frozen H0 and sigma10 default plus transparent conditional extensions to other sigma/topology. Every case must log topology, D/P/H/tox, rho/sigma, Si extent, actual frequency setup, full signed C matrix and labels, solver pass/profile, mesh counts, warnings, matrix symmetry/PSD; geometry filter P>D+2tox, protect GSG missing CAB, quarantine anomalies; perform selective additional mesh reruns for novel topology/material and high-risk corners. Reserve holdout by geometry before sampling. C-only does not make contact, bias, domain or solver formulation limitations disappear.

C evidence robust enough to proceed with DOE *engineering design and limited pilot*, not scientifically certify arbitrary final production labels.
