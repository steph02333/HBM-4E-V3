# G02 V2.5 — Mesh-search evidence audit (2026-11-01)

**Status:** nominal dielectric-fixture mesh refinement is within the target; full G02 remains OPEN.

Run: `20261101_213418_7fcbd5`. Source: user-uploaded `G02_results_bundle.zip`. Script source SHA-256 reported in manifest: `c87a16de88259f0bad9d7d67baaaf8f6f1591c33fdcba9b4a7249274109e4a67`.

## Observed mesh levels, not merely requested settings

| Mesh-seed settings (um) | Distinct total elements | CG adaptive passes | Last delta (%) |
|---|---:|---:|---:|
| default, 80, 60, 45 | 4388 | 4 | 0.30931 |
| 35, 27, 21 | 4780 | 4 | 0.32095 |
| 16, 12, 9 | 7152 | 6 | 0.34847 |

Small numerical differences exist within nominally identical mesh-count groups (e.g., 60 vs default), but the number of mesh elements is identical. The truly different mesh resolutions are 4388, 4780 and 7152.

## Independent finer-mesh comparison

**4388 -> 4780** (search_02 -> search_03):
- Cself_A change 0.187297%.
- Cself_B change 0.047883%.
- |Cmutual| change 0.191603%.

**4780 -> 7152** (search_05 -> search_06):
- Cself_A 7.7903435296 -> 7.7858897967 fF: **0.057170%**.
- Cself_B 6.0765986521 -> 6.0638151240 fF: **0.210373%**.
- |Cmutual| 3.4368927166 -> 3.4429981376 fF: **0.177329%**.

All last-two-distinct-mesh differences are below 1%. Q3D was solved independently in separate fresh projects. Final mesh pass history: 6 adaptive passes, convergence delta 0.34847% against configured target 0.5%. Matrix is symmetric with positive eigenvalues at the finest mesh.

## Limitations requiring explicit disclosure

1. No resource boundary was hit in V2.5. The finest successful resolution **observed** is 7152 reported elements. This is NOT the proven maximum Student mesh capacity. Prior explicit seed experiments exceeded the Student surface limit, but their mesh operations were not directly equivalent to this one-Cu-surface-seed protocol.
2. The 9/12/16 um settings produced identical meshes. Additional smaller seed values and independently verified mesh counts are needed to bracket a limit *if resource maximization remains a goal*.
3. The model is a **homogeneous nonconducting** silicon dielectric and a simplified G-S-S array. It is not the final doped-Si/grounding/bonded HBM model.
4. Charge conservation with the reference and external boundary is not independently demonstrated by the algebraically inferred reference charge. Domain independence previously failed. Neither is repaired by this mesh result.
5. The observed 0.2104% is a **last-two-mesh change**, not a rigorous upper bound on the discretization error. Use cautious language in any thesis claim.

## Decision

**Mesh subcriterion: PASS for this nominal simplified fixture only. G02 overall: OPEN.**

Next tests: demonstrate domain stabilization (or model limitations) and independent charge/ground bookkeeping; revalidate the mesh protocol at final realistic silicon physics and corner geometries before producing ML labels.
