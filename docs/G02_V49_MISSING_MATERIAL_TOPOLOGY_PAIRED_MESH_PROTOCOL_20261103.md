# G02 V4.9 — Complete missing material × topology nominal cells (2026-11-03)

**Purpose.** Bridge the four never-tested cells in the 3×3 grid of Professor Lim's resistivity rho={1,10,100} Ω·cm and topology={GSG,GSSG,GSGSG}, before starting a full six-input Q3D C-only pilot DOE.

**Source and runnable file:** `G02_V49_H0_missing_material_topology.py`, produced by adapting researcher-tested `G02_V48_H0_topology_mesh_qualification.py`. Downloadable from the associated FYP project chat, SHA256: `12c1d4c64bca0a4d0dd7ba65018740d4be9417e6f6cdaee02928e1cd704daa2f`. Python compilation PASS, CLI --help PASS, 8/8 dry-run manifest and output ZIP PASS. **Actual Windows AEDT runtime PENDING; don't claim solved or mesh PASS.**

| Topology | Silicon sigma S/m | Resistivity ohm-cm | Refinements |
|---|---:|---:|---|
| GSG | 1 | 100 | 12,18 |
| GSG | 100 | 1 | 12,18 |
| GSGSG | 1 | 100 | 12,18 |
| GSGSG | 100 | 1 | 12,18 |

**Previously tested, deliberately not rerun:** GSSG at sigma1/10/100; GSG at sigma10; GSGSG at sigma10. This new runner uses 8 new Q3D solves, not a full DOE.

Fixed: D4um, adjacent pitch P15um, H35um, SiO2 liner0.3um, epsilonSi11.7, epsilonOx3.9, finite Si margin25um, H0 no explicit Si ohmic contact, no MOS bias, requested 1GHz, Q3D Higher/Iterative with Cap.PerError0.5, MaxPass22. PerRefine requests 12 and18; **different parameter requests do not establish distinct actual mesh resolution**. Verify mesh counts, matrix self/mutual pair differences, 8000 surface limit, warnings. GSG only outputs valid SIG_A scalar C_AA; no C_AB is defined. GSGSG outputs C_AA, C_BB, signed C_AB. Existing Q3D matrix export can contain stale frequency headers; source setup and native 1GHz readback caveat persists.

**Windows command:**
`py -3.13 "C:\暂时下载\G02_V49_H0_missing_material_topology.py" --student --aedt-version 2025.2`

**Upload after run:** `G02_V49_H0_material_topology_results_bundle.zip` from the newest `C:\CA2 result V2\02_numerical_convergence\V3_conductive_silicon\run_<timestamp>_<id>\`. Contains case result.json, raw matrix exports, adaptive mesh logs, full stdout and strata audit. Heavy AEDT projects remain local.

**Decision after evaluation:** If all 4 cells solve and two actual meshes differ per stratum with relevant C changes under 1%, call nominal material×topology paired-mesh coverage COMPLETE **for these four cells only**. If some fail, keep failed/limit statuses and restrict initial six-input DOE accordingly. Do not infer 1% physical error, cross-strategy oxide convergence, true HBM substrate tie, apples-to-apples Maxwell, domain-independence or independent charge conservation. Remaining Phase 1 goal: topology-aware C-only space-filling pilot 5–10 unique points per nine strata, exact schema/QC and holdout design.