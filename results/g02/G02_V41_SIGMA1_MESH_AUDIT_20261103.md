# G02 V4.1 σ=1 S/m targeted local oxide mesh audit — 2026-11-03

Source: researcher-uploaded G02_V41_sigma1_mesh_results_bundle.zip, including 7 cases, result.json, full C/G, mesh_stats and convergence files.

## Execution
All 7/7 cases marked SOLVED_UNVERIFIED_PHYSICS, no CG adaptive nonconvergence warnings recorded. GSSG, D4 P15 H35 tox0.3 µm, Si margin25µm, sigma1 S/m, Higher, 1GHz, no explicit substrate contact. Physical return remains assumption-limited. Total mesh element counts below are NOT verified Student surface-element license counts.

| Case | Total reported elements | abs(C_AB) fF |
|---|---:|---:|
| BASE_s1_r18 | 2800 | 4.073954714273 |
| LOCAL_s1_OX_1_L12 | 3768 | 4.061243934034 |
| LOCAL_s1_OX_1_L8 | 7680 | 4.013281211168 |
| LOCAL_s1_OX_1_L5 | 7680 | 4.013281211168 |
| LOCAL_s1_OX_2_L12 | 3768 | 4.061261675638 |
| LOCAL_s1_OX_2_L8 | 7652 | 4.013258715300 |
| LOCAL_s1_OX_2_L5 | 7652 | 4.013258715300 |

OX_1 L12→L8 relative difference (denominator L8) = 1.19510%, BASE R18→OX_1 L8 relative difference (denominator L8) = 1.51182%. L8 and L5 **identical actual meshes and output matrices** within each oxide target, so they are NOT independent convergence evidence. OX_1 and OX_2 symmetry-swapped fine refinements agree closely, which suggests repeatability, but does not remove coarse-to-fine drift. C matrices symmetric and positive; zero nonconvergence warnings do not prove cross-mesh convergence.

Decision: **V4.1 solve PASS, σ1 targeted local oxide mesh convergence OPEN, not <1% qualified.** Do not use this sigma1 fixture as a fully mesh-qualified final DOE label. Next step should not repeat L5 with same method. Investigate student budget / mesh-seeding saturation and choose an actually distinct feasible mesh strategy (or a rigorously bounded resource-limited uncertainty); compare both self and mutual C and capture true surface triangles. Explicit physical model/contact and frequency reference are separate outstanding issues. Charge conservation investigation closed as NOT INDEPENDENTLY VERIFIED by user choice.
