# Maxwell M01 five-level decision, 2026-11-02

Four solved mesh-setting levels at 1GHz, one Student mesh cap failure. Levels 1-4 have actual matrices but **no element counts/adaptive-pass histories**; do not call strict convergence PASS.

| Level | C_AA fF | C_AB fF | G_AA mS | G_AB mS | Outcome |
|---|---:|---:|---:|---:|---|
| L1 | 37.611 | -12.577 | .074947 | -.021589 | Solved |
| L2 | 36.889 | -12.326 | .071372 | -.020580 | Solved |
| L3 | 36.763 | -12.285 | .070776 | -.020391 | Solved |
| L4 | 36.484 | -12.187 | .069375 | -.019982 | Solved |
| L5 | NA | NA | NA | NA | 80,988 elements > Student 64,000 limit |

Adjacent L2->L3 changes C_AA .342%, abs(C_AB) .333%, G_AA .835%, abs(G_AB) .918%. Adjacent L3->L4 changes .759%, .798%, 1.980%, 2.006%, respectively. G is not demonstrably stable. Setting slider progression does not independently prove mesh refinement ordering.

Matched nominal Q3D V4.0 DOM10_M25_R18: C_AA 35.481712 fF, C_AB -11.618261 fF, G_AA .061592086 mS, G_AB -.016418221 mS. Maxwell L4 deviations +2.82%, +4.90%, +12.64%, +21.71%. **These are preliminary**, because exact Q3D case header says 1kHz despite requested 1GHz and outer reference/boundary equivalence not demonstrated.

Maxwell L4 2x2 reduced C and G are symmetric and positive definite, a sanity check only. Does not prove total current conservation or real HBM substrate tie physics.

## Next steps (no new broad sweep)
1. Preserve solved .aedt and .aedtresults L1-L4; recover actual volume elements and adaptive pass histories **without re-solving** via AEDT UI or carefully tested narrow API.
2. Check exact Q3D DOM10_M25_R18 native matrix frequency at 1GHz; resolve exporter 1kHz header.
3. Compare silicon extent, two-ground reference, outer boundary, and Y=G+jwC definitions in both solvers. If G mismatch remains, one targeted reference/boundary pilot instead of many arbitrary meshes.
4. Only then run representative tox=.5 um and sigma=1 S/m checks. G02 remains OPEN; other Q3D orthogonal oxide/domain/contact gaps remain.

Detailed reproducible local report is `G02_M01_FIVE_LEVEL_DECISION_20261102.md`, CSV `G02_M01_mesh_level_comparison.csv`, both delivered through conversation. Sources are user ZIPs MESH14/MESH15 and Q3D raw V4.0 reference, with L2/L3 from previous user-returned ZIP review.
