# G02 V4.4 completed topology repair and combined V4.3 height sensitivity — 2026-11-03

Evidence: uploaded G02_V44_topology_repair_results_bundle.zip: 4/4 `SOLVED_UNVERIFIED_PHYSICS`, no CG adaptive nonconvergence warnings, C/G symmetric with positive eigenvalues. These are **single-mesh physics pilot results**, not per-geometry independent mesh convergence or a proven physically faithful HBM substrate reference.

Fixed D4µm, adjacent pitch15µm, tox0.3µm, sigma10 S/m, 1GHz Higher; finite Si margin25µm, no explicit semiconductor contact. GSG 3 TSV; GSSG 4 TSV; GSGSG 5 TSV.

| Topology | H um | Self C_AA fF | abs C_AB fF | G_AA mS | G_AB mS | reported mesh total |
|---|---:|---:|---:|---:|---:|---:|
| GSG |35|33.363571|N/A|0.0526183|N/A|3500|
| GSSG |25|25.126111|8.211700|0.042743|not consolidated here|3164|
| GSSG |35|35.485989|11.648644|0.061884|not consolidated here|3872|
| GSSG |50|51.089978|16.812051|0.091107|not consolidated here|3800|
| GSGSG |25|25.662195|4.614627|0.0471942|-0.0187672|3488|
| GSGSG |35|36.238176|6.446437|0.0686223|-0.0279007|3488|
| GSGSG |50|52.120359|9.202295|0.1013296|-0.0415309|3504|

At H35 the GSGSG vs GSSG |C_AB| difference is -44.659%. This **cannot** be interpreted as pure ground shielding because SIG A/B separation doubles from 15 to 30µm and a ground is inserted. Need a separation-matched control to isolate shielding.

Height 25→50µm |C_AB| increases GSSG 104.7%, GSGSG 99.4%; expected direction at all sampled points.

**Decision:** geometry/topology pilot PASS; 7/7 combined cases solved; per-topology mesh, substrate model/contact and domain qualification OPEN. Recommended next high-value gate: controlled finite silicon physical extent vs computational exterior boundary, while maintaining identical reference assumption and geometry; explicit H0 reference decision with supervisor before DOE. Preserve user-agreed sigma1 mesh provisional 1.5% uncertainty and charge conservation NOT INDEPENDENTLY VERIFIED.
