# G02 V4.3 results and V4.4 topology guard repair — 2026-11-03

V4.3 user diagnostic ZIP: 3/7 solved, 4/7 FAILED **before solving**. GSSG H25/H35/H50 ran successfully at sigma10 S/m, 1GHz Higher, D4/P15/tox0.3 and no explicit semiconductor contact. GSG_H35 and GSGSG_H25/H35/H50 geometry objects were correctly generated (3 or 5 Cu plus corresponding oxide), but V4.3 code hard-coded four oxide names in its object-set assertion: `{f'OX_{i}' for i in range(4)}`. All four failures thus are **script assertion bugs**, not AEDT solver/physics failures.

| H um | GSSG C_AA fF | abs(C_AB) fF | G_AA mS | reported total elements |
|--:|--:|--:|--:|--:|
|25|25.126111|8.211700|0.042743|3164|
|35|35.485989|11.648644|0.061884|3872|
|50|51.089978|16.812051|0.091107|3800|

Trend increases with H. Not independently mesh-qualified per H; no cross-mesh claims. GSG has one signal, no AB mutual. GSGSG A/B spacing 30um vs GSSG 15um, so cannot attribute all differences to shielding.

**V4.4 corrected runner:** `G02_V44_topology_geometry_guard_fix.py` supplied in chat (not committed as script). Changes: `range(len(centers))` in geometry guard, oxide mesh stats parser `OX_[0-9]+`, four-case configs only, revised diagnostic ZIP name `G02_V44_topology_repair_results_bundle.zip`, version 4.4.0. Python compile, CLI help, 4/4 dry-run passed. Windows AEDT runtime **pending**. Run `py -3.13 "C:\暂时下载\G02_V44_topology_geometry_guard_fix.py" --student --aedt-version 2025.2`; upload named ZIP from newest V3_conductive_silicon/run_* folder.

Global charge conservation archived NOT independently verified. Sigma1 local oxide refinement approximately 1.5% remains provisional with explicit limitation. Remaining model/reference/domain gates OPEN.
