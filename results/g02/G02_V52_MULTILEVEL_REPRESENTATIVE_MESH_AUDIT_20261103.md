# G02 V5.2 — Representative multilevel C-mesh audit and V5.3 decision (2026-11-03)

**Status: AUDITED, PARTIAL MESH QUALIFICATION; G02 PHYSICS GATE STILL OPEN.** User explicitly requested committing this evidence and direction to GitHub. This is the measured result of a real Ansys Student run, not an unexecuted protocol.

## 0. Evidence provenance and reproducibility
- Uploaded archive: `G02_V52_H0_multilevel_mesh_results_bundle.zip`, SHA256 `f36196c3c6e210dab224542162caa79cff4e69c56c07b4dfdc5d55a2fd5d770c`. **Large 685KB binary ZIP lives with researcher, not presently committed to GitHub.**
- Includes 54 case folders, `case_summary.csv`, `MULTILEVEL_MESH_SCREEN.json`, `runner.log`, `AUDIT_REQUIRED.json`, C/G raw export, actual CG profile/convergence, mesh_stats and AEDT warning text for each case.
- Independent derived table `G02_V52_independent_audit_summary.csv`, SHA256 `44e4e8ea5e0c7e9e0653c05636bef4e6541732014b4b1f481608ea944576ac89`; summary published to this repository in sibling CSV.
- Context: version 5.2.0, H0 simplified homogeneous conductive-Si TSV array, no explicit Si ohmic contact, 25um Si margin, epsilonSi=11.7/epsilonOx=3.9, requested CG 1GHz, Q3D Higher Iterative, PerError=0.5%, MaxPass22. Si conductivity sigma=1,10,100 S/m corresponds to resistivity rho=100,10,1 ohm-cm, **reverse numeric ordering**.
- **Geometries:** STRONG D6/P10/H50/tox0.1um, WEAK D3/P20/H25/tox0.5um, nominal D4/P15/H35/tox0.3um. R8/R12/R18 are Cap.PerRefine requests, NOT guaranteed ordered element counts or rigorously nested h refinement.
- V5.2 primary attempted 54 cases, **52 solved / 2 AEDT Student 8000-surface-element limit failures**. Cases marked `SOLVED_UNVERIFIED_PHYSICS` are validly solved but not necessarily mesh-qualified or physically verified.
- The provisional 45-point representative panel was designed as 9 material×topology strata with nominal+strong+weak+2 mixed maximin points. **Only primary strong/weak + anomaly tasks were run. Reserve/mixed cases NOT yet run**. Preserve the candidate panel but don't run Reserve blindly.

## 1. Automatic multilevel screen: 20 reporting groups
Counts: **7 `THREE_LEVEL_PAIR_CONSISTENCY_PASS`, 7 `THREE_LEVEL_PAIR_CONSISTENCY_FAIL`, 2 `TWO_LEVEL_ONLY_NEEDS_THIRD_DISTINCT_LEVEL`, 4 `INSUFFICIENT_DISTINCT_MESH_LEVELS`**. These 20 include two nominal local-oxide experiments and two sigma10/GSSG R8-only groups that must be merged with prior V47 raw results. No failed group is deemed physically invalid solely from its numerical difference.

| Topology | rho Ω·cm | Geometry | Actual mesh total elements sorted ascending | Worst adjacent C % | Screen |
|---|---:|---|---|---:|---|
| GSG | 100 | Strong | 5038/5534/6270 | 0.011 | PASS |
| GSG | 100 | Weak | 2696/2780/3356 | 0.106 | PASS |
| GSG | 10 | Strong | 5088/5540/6276 | 0.155 | PASS |
| GSG | 10 | Weak | 2624/2974/3380 | 0.102 | PASS |
| GSG | 1 | Strong | 7036/7676/8008 | 0.177 | PASS |
| GSG | 1 | Weak | 4456/FAILED/11552 | 2.143 | TWO LEVELS; Student limit |
| GSSG | 100 | Strong | 1796/1940/2168 | 0.121 | PASS |
| GSSG | 100 | Weak | 2600/3816/7250 | 1.791 | FAIL |
| GSSG | 10 | Strong | 1804 this run | — | V47 R12/R18 MERGE NEEDED |
| GSSG | 10 | Weak | 1944 this run | — | V47 R12/R18 MERGE NEEDED |
| GSSG | 1 | Strong | 2460/4712/8656 | 5.221 | FAIL; last adjacent 0.496 |
| GSSG | 1 | Weak | 2716/6192/13128 | 3.963 | FAIL |
| GSGSG | 100 | Strong | 2280/2412/2696 | 0.260 | PASS |
| GSGSG | 100 | Weak | 3258/3774/8812 | 3.309 | FAIL |
| GSGSG | 10 | Strong | 2264/2408/2624 | 3.463 | FAIL |
| GSGSG | 10 | Weak | 2284/3372/3604 | 1.031 | FAIL; last adjacent 0.829 |
| GSGSG | 1 | Strong | 3596/5980/6572 | 5.296 | FAIL; last adjacent 0.528 |
| GSGSG | 1 | Weak | 3570/3714/FAILED | 3.866 | TWO LEVELS; Student limit |
| GSGSG | 1 | Nominal oxide L12/L10 | 5808/5808 | — | IDENTICAL mesh, NOT an independent audit |
| GSSG | 100 | Nominal oxide L12/L10 | 6192/6192 | — | IDENTICAL mesh, NOT an independent audit |

All percentages are *worst relevant Cself or signed-mutual magnitude differences between neighboring actually distinct meshes*: `abs(C_lower-C_higher)/abs(C_higher)*100`. **Original signed C_AB is negative; relative test uses magnitude differences.** GSG has one signal and therefore C_AB is undefined, not 0.

## 2. Important individual self/mutual behavior, not just one aggregated %
The actual pass criterion must check each independently: `CAA`, `CBB` (two-signal layouts), and `abs(CAB)`; use max of these for overall gate, but keep the per-coefficient columns.

- GSGSG rho=1, **STRONG** (sigma100): mesh 3596→5980: self A 1.521%, self B 1.669%, mutual 5.296%; mesh 5980→6572: self A 0.113%, self B 0.023%, mutual **0.528%**. *Promising late stabilization*, but the three-level rule fails because the earlier interval exceeds 1%; one further genuinely independent mesh is informative, provided license headroom and mesh controls allow.
- GSSG rho=1, **STRONG** (sigma100): 2460→4712: self A 1.999%, self B 2.208%, mutual 5.221%; 4712→8656: self A 0.424%, self B 0.398%, mutual **0.496%**. Same promising-but-not-yet-qualified trajectory.
- GSGSG rho=10, **STRONG** (sigma10): 2264→2408: mutual 2.282% with both self deviations <0.08%; 2408→2624: mutual **3.463%** with both self deviations <0.28%. **Self C stability does NOT imply mutual C stability.**
- GSGSG rho=10, **WEAK**: 2284→3372 mutual 1.031%; 3372→3604 mutual 0.829%; self A/B remain <0.38%. One failed early interval needs interpretation; late interval alone is not multi-step proof.
- GSSG rho=100, **WEAK** (sigma1): 2600→3816 mutual 1.791%; 3816→7250 self A 1.483%, self B 1.394%, mutual 1.029%. Both observables remain relevant.
- GSSG rho=1, **WEAK** (sigma100): 2716→6192 mutual 1.220%; 6192→13128 mutual **3.963%**; Cself relatively steadier. Do not assume adding total mesh always improves mutual.
- GSGSG rho=100, **WEAK** (sigma1): 3258→3774 max 0.098%; 3774→8812 self A/B ~2.338% and mutual 3.309%, an *increase in disagreement on larger adaptive mesh* (not mathematical proof that finer grid is worse).
- GSG rho=1, **WEAK**: only 4456 and 11552 elements solved, `CAA` pair difference 2.143%, and the middle attempt failed license; not qualified.
- GSGSG rho=1, **WEAK**: only 3570 and 3714 elements solved, mutual 3.866%; last attempt exceeded license. Not qualified.

**Avoid targeting exactly 1% as a numerical 'sweet spot':** smaller stable changes are better, subject to cost. The requirement is every relevant coefficient **below** ~1% over effective independent refinement; targeting 0.99% is not an optimization goal.

## 3. Two historical mesh anomalies remain unresolved, and attempted local seeds did NOT add levels
- V49 nominal GSGSG rho=1 (sigma100) R12/R18: `|CAB|` disagreement **5.893%**; R18 last CG triangles 7828 near Student limit; self 1.6–1.7%. V52 requested `OX_1_L12` versus `OX_1_L10` but both actually had **5808 total mesh elements and identical 3408 last CG triangles**, so these are not independent mesh tests and cannot close this gap.
- V41 nominal GSSG rho=100 (sigma1) local oxide cross-strategy `|CAB|` disagreement ~**1.5%**; V52 `OX_1_L12`/`L10` produced identical **6192 elements and 3548 last triangles**, also cannot close this gap.
- **Candidate technical cause to inspect, not proven:** applying a 'length mesh' seed to an oxide body/surface whose geometry is much smaller than 10–12um may produce ineffective mesh constraints; verify actual AEDT mesh operation target/assignment, operation type, size relative to oxide and its mesh, and per-object/surface breakdown. Don't assert a causal fix until a controlled geometry-specific comparison actually changes effective mesh topology.
- Next experiment must first establish a *genuinely changed local oxide mesh* via saved AEDT mesh-operation readback and local/surface indicators; avoid repeated L10/L12-type identical attempts.

## 4. Student licensing and interpretation
Official solver errors:
- `H0_GSG_S100_WEAK_R12`: **8488 surface elements** exceeding Student 8000 limit.
- `H0_GSGSG_S100_WEAK_R18`: **9016 surface elements** exceeding Student 8000 limit.

These values come from license errors, while table `total elements` and `last CG triangles` are distinct mesh measures, **not interchangeable with the official license counter**. A globally 'finer' R18 may cause radically different adaptive meshes, need more passes, or hit limit.

## 5. Research decision and action plan (not claiming work completed)
**Do not launch V5.2 Reserve 54 or production DOE yet.** Next: a bounded V5.3 *mesh operation efficacy / local refinement* diagnostic campaign before more broad space-filling structures.

1. Read-only inspect exact V52/V49 scripts, AEDT operation logs and per-object mesh breakdown to confirm that specific Cu/oxide interface surfaces actually got an applied local mesh operation, and the local size is meaningful vs `tox=0.1–0.5um`; capture assignment API/operation readback before/after. No blind copy/paste of L12/L10.
2. Single-case preflight on anomalous nominal GSGSG sigma100 and GSSG sigma1: two materially different but Student-viable *effective* mesh policies (e.g., localized face/oxide sizing or alternate targeted seeds with verified resulting local mesh diagnostics); compare actual mesh and **all** C coefficients, not just C_AB.
3. For converging-tail cases (GSGSG rho1 STRONG, GSSG rho1 STRONG; optionally GSGSG rho10 WEAK) attempt 4th distinct, targeted mesh if license headroom; record the last two adjacent paired Cself/Cmutual deltas.
4. For persistent oscillators (GSGSG rho10 STRONG, GSSG rho1 WEAK, GSGSG rho100 WEAK), test local vs global meshing strategy instead of extending globally on autopilot.
5. For the two license failures, avoid repeats of known-overlimit settings; consider alternate mesh allocation or a second distinct feasible level. Stop and mark resource boundary if not feasible.
6. Once effective policy families exist, rerun focused qualification at the 7 failed/2 incomplete groups first; only then use maximin sample expansion for untested interior/mixed geometry. Reuse V47 paired points when comparing sigma10 GSSG R8; never claim that V52 standalone R8 is 3 levels.
7. Final ML DOE remains independently *space-filling* across D3–6, P10–20, H25–50, tox0.1–0.5, rho1/10/100, topology GSG/GSSG/GSGSG; NEVER pull DOE samples toward verified representatives just to make QA easier. Different mesh policy families by topology/rho/geometry risk are acceptable if predeclared and transparently QA-checked.

**Acceptance:** same geometry/material/source/reference; at least 3 genuinely distinct successful mesh resolutions or justified exception; two consecutive final intervals with all CAA/CBB/CAB pair deltas <1%, no serious convergence warnings; record surface license limit. Total-element ordering is *descriptive*, not proof of nested refinements. Every final DOE point must pass internal adaptive convergence and matrix/metadata QA; selective independent mesh repeats required for unfamiliar or high-risk cells.

## 6. Open physics limitations that are NOT solved by meshing
H0 no verified physical silicon backside ohmic contact; Si-body extent vs exterior domain not independently converged; global field charge closure unverified despite extensive V07–V25 work; Q3D infinity vs Maxwell M01 Neumann boundary not identical-BVP verified; MOS bias/Sentaurus not run; exporter frequency header conflicts despite 1000MHz requested setup. Do not represent this simplified HBM-relevant TSV structure as complete physical HBM4 die validation.

## 7. Sibling evidence
- `results/g02/G02_V52_independent_audit_summary_20261103.csv`: 20-group view of mesh counts, surface triangles, status and anomalies; sourced from uploaded V52, not merely a design proposal.
- Prior baseline: `results/g02/G02_V47_HIGH_RISK_CORNER_MESH_AUDIT_20261103.md`, `results/g02/G02_V49_MATERIAL_TOPOLOGY_NOMINAL_AUDIT_20261103.md`.
- Historical research policy: `docs/G02_MESH_COVERAGE_AND_DOE_TRANSFER_RULE_20261103.md`, V51 prospective protocol.
