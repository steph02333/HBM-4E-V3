# G02 V5.1 — Multilevel representative mesh qualification (2026-11-03)

## Why 3–5 levels
Researcher requested more than a single R12/R18 comparison per high-risk representative. For each new geometry sentinel V5.1 requests PerRefine=8%,12%,18% and records **actual** reported mesh elements, CG convergence and signed C matrix. PerRefine is NOT monotonic in actual mesh density. Audit sorts by actual mesh total and computes each successive relative delta, with <1% pairwise differences across the last TWO adjacent intervals needed to mark `THREE_LEVEL_PAIR_CONSISTENCY_PASS`. This is an empirical reproducibility screen, NOT a rigorous continuum error proof. Identical mesh counts are not independent. A 4th/5th **targeted** level should be requested only for flagged samples with headroom under Student 8,000-surface-element license; not by blindly increasing global mesh.

## Implemented runnable file
`G02_V51_H0_multilevel_mesh_qualification.py`, SHA256 `d61bb37a8caac62c6d80845407d90400b03b95b022417fd75e8b59dbd5ab17e9`. Built from researcher-tested V4.9 Q3D geometry/export. Python compile, CLI and configuration count checked; **NO actual AEDT runs performed by assistant**. 66 planned new solves across:
- 4 anomaly local oxide probes: GSGSG sigma100 and GSSG sigma1, two OX_1 local seed lengths each. Analyze jointly with saved V4.1/V4.9 historic baseline; V5.1 marks these as diagnostic, NOT auto-PASS.
- 48 new Q3D solves: strong and weak extreme geometry, 3 PerRefine requests each, for 8 of 9 topology×sigma strata. sigma10/GSSG old V4.7 paired R12/R18 is reused.
- 2 new R8 solves to make the existing sigma10/GSSG strong+weak R12/R18 evidence three-level in postprocessing (not auto-approved by V5.1 alone).
- 12 new solves: 4 mixed extreme shapes × 3 mesh requests (not just strong/weak diagonal).
Includes all nine stratum topology/rho combinations. Shapes STRONG D6/P10/H50/tox0.1, WEAK D3/P20/H25/tox0.5, two mixed D6/P20/H25/tox0.1 and D3/P10/H50/tox0.5. H0, Si margin25µm, requested1GHz, Higher, rho1/10/100 ohm-cm, no explicit substrate contact.

### Execution
- Place Python at `C:\暂时下载\G02_V51_H0_multilevel_mesh_qualification.py`
- Run `py -3.13 "C:\暂时下载\G02_V51_H0_multilevel_mesh_qualification.py" --mode full --student --aedt-version 2025.2`.
- Optional staging: `--mode anomalies` (4), `--mode sentinels` (60), `--mode historic2` (2), `--mode mixed` (12; subset of sentinels). Separate modes create separate result roots, so prefer `full` for one coherent 66-case manifest and use `--resume <run_folder>` if interrupted.
- Existing session connection failure can be mitigated with `--new-desktop`; close any busy AEDT sessions first.
- Upon completion upload `G02_V51_H0_multilevel_mesh_results_bundle.zip` from latest `C:\CA2 result V2\02_numerical_convergence\V3_conductive_silicon\run_<timestamp>_<id>\`.
- The ZIP contains solver raw C/G, mesh stats/profile, full case results, manifest, `MULTILEVEL_MESH_SCREEN.json`, diagnostic; binary .aedt projects intentionally excluded, retained on user's PC. Script best-effort closes each AEDT project after saving to reduce desktop memory use.
- Run supports `--resume <exact run folder>`, skips successful and prior FAILED cases by default; `--force-failed` can retry failed cases on resume.
- Automatic multilevel screen needs human verification of matrix passivity, surface triangle cap, consistency across different mesh strategies and per-case warnings. It is not an automated full physics qualification.

## ML DOE principle
Keep final DOE design independent and space-filling across full professor-suggested D/P/H/tox ranges and rho/topology strata. Representative mesh points are a *numerical validation panel*, NOT a rule to bias DOE samples closer to them. For novel DOE geometry, per-point adaptive QA and risk-based independent mesh audits remain necessary; no finite representative set proves all 4D interiors converged.

## Current unresolved risk
V4.9 nominal GSGSG sigma100: R12 vs R18 |CAB| 5.893%, R18 7828 last CG triangles. V4.1 GSSG sigma1 local oxide difference ~1.5%. Never claim G02 all mesh PASS from this run before inspecting actual results and resource limits.