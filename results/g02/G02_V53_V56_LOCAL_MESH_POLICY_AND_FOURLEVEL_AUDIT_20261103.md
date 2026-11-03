# G02 V5.3–V5.6: Local mesh mechanisms, four-level C convergence and next transfer gate

Date: 2026-11-03. **Independently re-audited from real user-uploaded V53, V54, V55, V56 raw ZIPs.** All reports refer to simplified finite homogeneous conductive Si H0/no explicit silicon ohmic contact, Si margin 25µm, requested 1GHz, Q3D AEDT 2025.2 Student, Higher/Iterative, Cap.PerError0.5%, maxPass22, nominal D4/P15/H35/tox0.3µm.

## Bottom line
**V5.6 GSSG at rho=100Ω·cm (sigma=1 S/m), both signal oxides length seed L6µm: 4 distinct successful adaptive mesh results; all CAA/CBB/|CAB| neighboring pair differences <1%. The highest pairwise component changes (mesh ascending) are 0.44942%, 0.22664%, 0.20557%. PASS for four-level *within-policy paired-mesh consistency at this exact nominal structure*.**
**V5.6 GSGSG rho=1Ω·cm (sigma=100 S/m): 4 distinct meshes, but middle pair violates <1% (CAA 1.10122%, |CAB| 1.33876%). Last finer pair has max 0.65328% and shows promising late stability, NOT four-level PASS.**
No proof of strict nested h-refinement, absolute continuum error, orthogonal strategy consistency, geometry-wide transfer, or full professor physical gate. Adaptive PerRefine labels are not mesh element levels and can be nonmonotonic.

## Evidence / checksums of uploaded raw bundles (researcher's locally retained artifacts; **ZIPs are not committed into repository**)
- V5.3 `G02_V53_H0_local_mesh_diagnostics_bundle.zip` SHA256 `76a1ac7dbf098f5c8a8c3f1fb06743cb5b8dd45fed4a21cf6aaaf70f41cb019f`
- V5.4 oxide `G02_V54_H0_mesh_budget_results_bundle.zip` SHA256 `093f6f92924bb3726d81ced81dee7c0f3d90366be60142ca172a2b554e8accf2`. Note: this is the **later oxide-mode archive**, not the earlier Cu-mode archive that used the same filename.
- V5.5 `G02_V55_H0_mesh_policy_results_bundle.zip` SHA256 `aed15f2e58250682872e84431fbf6135ea22b18d51abf96ba4588db302c8eae2`
- V5.6 `G02_V56_H0_fourlevel_mesh_results_bundle.zip` SHA256 `e0223723a43e8e47d2f8f6ff8cf5ba8d03f52696c6a8214465e80bc77874ceb0`
Each archive contains result.json, raw signed C/G matrix exports (when solved), mesh_stats and CG convergence/profile, run log / AEDT messages. Versioned runner files `G02_V53_H0_targeted_local_mesh_diagnostics.py`, `G02_V54_H0_mesh_budget_calibration.py`, `G02_V55_H0_mesh_policy_diagnostics.py`, `G02_V56_H0_fourlevel_oxide_mesh.py`, plus merge audit script, are in researcher project chat/local storage, NOT claimed to be in repository. GitHub sibling CSV below includes all actual V53–V56 case-level C values; raw ZIPs needed for full third-party reproduction.

## V5.2 starting evidence
V5.2 primary: 54 attempts, 52 solved, 2 official Student 8000-surface-element-limit failures, 20 reporting groups: 7 three-level pass, 7 fail, 2 two-level only, 4 lacking independent mesh levels / historical merge. See `results/g02/G02_V52_MULTILEVEL_REPRESENTATIVE_MESH_AUDIT_20261103.md`.
Existing anomalies: GSGSG sigma100 nominal V49 R12/R18 |CAB| 5.893%; GSSG sigma1 nominal V41 cross-strategy oxide |CAB| ≈1.5%. V52 oxide L10/L12 made identical meshes: ineffective independent test. Keep these historical discrepancies as context; don't erase them with current within-policy pass.

## V5.3 diagnostics
6/6 FAILED under Student surface mesh cap from aggressive oxide surface length L0.75/L1.5 and Cu L2; these did materially alter meshing demand, but yield no extracted converged C for quality comparison. E.g. Cu L2 GSGSG sigma100 8092 official surface elements and GSSG sigma1 8738; oxide L1.5 ~13376/13068. The native 8000 surface-element cap is NOT total mesh elements.

## V5.4 Cu and oxide budget calibration
Cu mode (separate earlier archive, only summary preserved here): six local Cu L2.5/L3/L4 tests all hit 8000 limit; GSGSG sigma100 official surface count 8754/8726/8676 and GSSG sigma1 8006/9040/9034. Cu-local surface contributions were nearly unchanged while oxide/silicon allocation changed, thus Cu length alone is not a controllable monotonic mesh knob.
Oxide mode (SHA above): six tests, two solved (GSGSG sigma100 L6/L8). L6 and L8 same actual 13684 total mesh, 7362 final CG triangles, same CAA=42.50046, CBB=42.45811, |CAB|=9.40690 fF. **One distinct mesh, not two independent levels.** GSSG sigma1 L4/L6/L8 all over cap; GSGSG sigma100 L4 over cap. The GSGSG oxide L6 versus historical R18 differed by about CAA 0.327%, CBB 0.278%, |CAB| 1.157%; historical cross-strategy issue was not resolved.

## V5.5: mesh assignment scope × adaptive growth, SIX succeeded
Both structures D4/P15/H35/tox.3, local oxide length L6:
- GSGSG sigma100 (rho1): SIG_A-only R8 = 12368 total mesh elements /6704 final CG triangles, CAA42.60366945, CBB42.48496243, CAB−9.34570009 fF. BOTH-signal oxide R5=9432/5220, CAA42.131874, CBB42.493412, CAB−9.467827; BOTH R8=12416/6728, CAA42.601003, CBB42.521506, CAB−9.342749.
- GSSG sigma1 (rho100): SIG_A-only R8=5268/3044, CAA10.805921, CBB10.806457, CAB−4.065628; BOTH R5=9272/5126, CAA10.603034, CBB10.624455, CAB−3.986847; BOTH R8=12102/6602, CAA10.557955, CBB10.566006, CAB−3.966988.
- At identical R8, SIG_A-only versus BOTH-signal oxide C differs ~2.35% self and ~2.49% mutual for GSSG sigma1, so the cheap single-oxide assignment is NOT generally equivalent. GSGSG sigma100 difference is much smaller (~0.006% CAA, 0.086% CBB, 0.032% |CAB|), underscoring stratum specificity. It is **not** a validation pass from the two different assignments.
- BOTH R5→R8 maximum C change: GSGSG sigma100 1.33876% (NOT PASS); GSSG sigma1 0.55276% (paired PASS only).
**Inference/hypothesis:** jointly changing scope and adaptive growth can shift mesh allocation into license-feasible regime; physically identifying why requires actual local surface mesh diagnostics, not just global counts.

## V5.6: merge new R6/R10 with V5.5 BOTH R5/R8 — exact raw matrix audit
Units: fF. Max C % computed separately for `CAA`, `CBB`, and `|CAB|` as `abs(C_earlier-C_later)/abs(C_later)*100` and report maximum. Sorting is by ACTUAL total mesh elements, not PerRefine.

### GSSG, rho 100Ω·cm, sigma1 S/m — **within-policy four-level consistency PASS**
| Requested PerRefine | Actual total elements | CG final triangles | CAA | CBB | |CAB| |
|---|---:|---:|---:|---:|---:|
| R5 | 9272 | 5126 | 10.603034 | 10.624455 | 3.986847 |
| R6 | 10644 | 5848 | 10.574318 | 10.576921 | 3.975979 |
| R8 | 12102 | 6602 | 10.557955 | 10.566006 | 3.966988 |
| R10 | 13792 | 7476 | 10.558733 | 10.544329 | 3.968967 |

Pairwise per-coefficient (%) in ascending actual total elements:
- R5→R6: CAA 0.27156, CBB 0.44942, |CAB| 0.27334; worst **0.44942%**
- R6→R8: CAA 0.15499, CBB 0.10331, |CAB| 0.22664; worst **0.22664%**
- R8→R10: CAA 0.00737, CBB 0.20557, |CAB| 0.04986; worst **0.20557%**
All cases solver-solved with distinct actual meshes and no recorded CG adaptive nonconvergence in previous review. Internal adaptive criterion is separately 0.5%. Last triangles=7476 is not a certified license counter, but suggests limited headroom. Do NOT chase unnecessary fifth nominal mesh. Historical V41 cross-strategy ~1.5% is not disproven; report scope truthfully.

### GSGSG, rho 1Ω·cm, sigma100 S/m — **four-level full interval gate NOT PASS**
| Requested PerRefine | Actual total elements | CG final triangles | CAA | CBB | |CAB| |
|---|---:|---:|---:|---:|---:|
| R6 | 9300 | 5154 | 42.169329 | 42.536855 | 9.428021 |
| R5 | 9432 | 5220 | 42.131874 | 42.493412 | 9.467827 |
| R8 | 12416 | 6728 | 42.601003 | 42.521506 | 9.342749 |
| R10 | 13752 | 7396 | 42.496474 | 42.464029 | 9.404185 |

Pairwise per-coefficient (%) ascending actual total elements:
- R6→R5: CAA 0.08890, CBB 0.10223, |CAB| 0.42043; worst **0.42043%**
- R5→R8: CAA 1.10122, CBB 0.06607, |CAB| 1.33876; worst **1.33876% FAIL**
- R8→R10: CAA 0.24597, CBB 0.13535, |CAB| 0.65328; worst **0.65328%**
R8/R10 late-stage stability is encouraging but fails all-interval criterion and does not overcome V49 5.893% cross-strategy discrepancy. High-sigma five-TSV nominal remains **MESH_UNRESOLVED**, not categorically physically invalid. Signal symmetry diagnostic: R5/R6 |CAA−CBB|/mean ≈0.86% and R10 ≈0.076%; supplementary diagnostic, not convergence proof. Additional global refinement risks Student limit (7396 final CG triangles at R10).

## Scientific acceptance and transfer
- Evaluate all relevant `CAA,CBB,|CAB|` independently; GSG has one signal (CAB undefined, not zero). Max component drives combined gate; numerical objective is BELOW ~1%, not to target exactly 0.99%.
- Mesh policies can depend on topology, silicon resistivity and geometry risk. Any new policy must be confirmed by truly distinct solved meshes; PerRefine R5/R6/R8/R10 are requested growth fractions, not guaranteed monotone h levels.
- Near-term priority **(a)** GSSG rho100: try transferring BOTH signal oxide L6 policy to selected V52 strong/weak geometries and measure 3+ distinct meshes with all C terms, not more nominal; **(b)** GSGSG rho1: one bounded local mesh allocation / alternative strategy diagnostic, using prior R8/R10 reference, without blindly expanding global triangle count; **(c)** use observations to refine reusable risk-aware mesh policies before V52 reserve or final DOE.
- Every DOE label still requires per-point solver adaptive convergence, original full matrix QA/passivity/symmetry, provenance/uncertainty and selective independent mesh audit. **DO NOT bias ML DOE sampling toward mesh representatives.** DOE remains independently space filling in D3–6/P10–20/H25–50/tox.1–.5, rho1/10/100 and GSG/GSSG/GSGSG.
- Other limitations unchanged: no demonstrated global independent charge closure, silicon external domain independence, Maxwell identical BVP independent validation, MOS bias/true HBM die substrate reference, and export frequency header remains at odds with requested native setup.

## Next action
Plan focused V5.7 policy transfer & single difficult-regime diagnostic; do not yet commit unexecuted experiment as accomplished. After new results, update evidence and select further geometry sentinels adaptively. **V52 reserve 54 and final production DOE remain on hold.**
