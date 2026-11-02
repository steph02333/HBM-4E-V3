# G02 M01 v1.6 native postsolve audit — 2026-11-02

User ZIP G02_M01_POSTSOLVE16_diagnostic.zip provided native Maxwell ExportMeshStats (.ms), ExportConvergence (.conv), and audit.json for L1-L4. All four files exported successfully without resimulation or altering source hashes.

| Level | Final tetrahedra | Passes | Last loss error % | Last delta loss % | C_AA fF | C_AB fF | G_AA mS | G_AB mS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| L1 | 7340 | 6/6 | 8.7390 | 0.076691 | 37.611 | -12.577 | .074947 | -.021589 |
| L2 | 14910 | 6/6 | 4.7956 | 0.040084 | 36.889 | -12.326 | .071372 | -.020580 |
| L3 | 18551 | 6/6 | 4.1223 | 0.029732 | 36.763 | -12.285 | .070776 | -.020391 |
| L4 | 30356 | 6/6 | 2.5478 | 0.018825 | 36.484 | -12.187 | .069375 | -.019982 |

L5 blocked at 80,988 vs Student 64,000 element cap. L4 native adaptive mesh sequence: 8167, 10620, 13810, 17956, 23347, 30356.

**Important correction:** All four reached the configured max six passes WITHOUT meeting loss-error target 1%. L4 loss error 2.5478% despite delta loss 0.018825%. Native .conv includes another Current error 2.1252%; distinguish fields rather than silently treating one as final. AC Conduction loss convergence is not a guarantee of C/G matrix-entry convergence. Increasing tetrahedra across L1-L4 establishes true mesh density progression, not necessarily nested meshes. Adjacent L3-L4 C changes <1% while G changes about 2%.

Existing Q3D V4 reference DOM10_M25_R18 nominal 1GHz-requested: C_AA 35.481712fF, C_AB -11.618261fF, G_AA .061592086mS, G_AB -.016418221mS. Maxwell L4 vs Q3D magnitude discrepancy +2.825%, +4.895%, +12.636%, +21.706%. **Not yet fully apples-to-apples**: Q3D exact case exporter says 1kHz or 1Hz; native frequency readback unresolved. Q3D vs Maxwell substrate return and outer boundaries unverified. G02 OPEN.

**Next gate**: Pilot a *copy* of solved L4 with max adaptive passes e.g. 8 (not altering 1% threshold or model), export actual .conv and CG matrix; inspect whether solver error crosses 1%, and avoid Student cap. Do not promise success: two more 30%-growth passes project ~51k but this is extrapolation, not actual. Independently verify exact Q3D frequency and solver reference. Representative tox=.5, sigma1 remain conditional.

Raw native exports and analysis CSV are delivered to user in current turn, not stored in repo by this commit.