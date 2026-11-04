# G02 V6.3 — Final Chunk 5 original ZIP audit (2026-11-04)

**Real archive** `G02_V63_H0_PRODUCTION_DOE_results_bundle.zip` SHA-256 `7d6759a3faa9672418df4ae0807f2e2a2778f167d14bbc41572e9f309792cf3e`. `manifest.json` identifies Chunk 5 with 50 original DOE points, 100 distinct original R3/R5 configurations. All 100 result.json are present, but **98 are SOLVED_UNVERIFIED_PHYSICS, 2 are FAILED**. Do NOT state 450/450 fully solved until DOE0447 is recovered.

## Outcome and C numerical screen

| Worst applicable R3/R5 C coefficient delta | Chunk 1 | Chunk 2 | Chunk 3 | Chunk 4 | Chunk 5 (paired) | Cumulative |
|---|---:|---:|---:|---:|---:|---:|
| <1% | 73 | 66 | 73 | 68 | **32** | **312** |
| 1–2% | 12 | 14 | 15 | 15 | **6** | **62** |
| 2–5% | 14 | 20 | 10 | 13 | **7** | **64** |
| ≥5% | 1 | 0 | 2 | 4 | **4** | **11** |
| Unpaired because solve FAILED | 0 | 0 | 0 | 0 | **1** | **1** |
| Fully paired DOE points | 100 | 100 | 100 | 100 | **49** | **449/450** |

Chunk 5 49 successful paired points: median worst coefficient delta **0.4732%**, 90th percentile **4.3252%**, maximum **6.1822%** (DOE0407 mutual C). **32/49 below 1%, 17/49 at or above 1%.** Professor's C refinement comparison is a *two-level numerical consistency screen*, not physical accuracy validation or absolute mesh convergence proof. An additional ≥10% mesh growth check is a **non-mandatory researcher diagnostic**, not a professor requirement.

### Chunk 5 four ≥5% points

| DOE | Topology | rho Ωcm | Worst coefficient | Delta (%) | D µm | P µm | H µm | tox µm |
|---|---|---:|---|---:|---:|---:|---:|---:|
| DOE0406 | GSGSG | 1 | mutual AB | 5.0820 | 5.29121 | 12.93521 | 26.31592 | .36866 |
| DOE0407 | GSGSG | 1 | mutual AB | **6.1822** | 3.26199 | 19.64152 | 42.14727 | .33561 |
| DOE0421 | GSG | 1 | self AA | 5.3004 | 3.43947 | 12.26979 | 49.50157 | .35947 |
| DOE0422 | GSG | 1 | self AA | 5.0903 | 3.90312 | 10.55119 | 26.81056 | .17715 |

Full five-batch [11-case high-discrepancy special watchlist](G02_V63_CHUNKS1TO5_GE5_SPECIAL_WATCHLIST_20261104.csv).

### DOE0447 solver-failure blocker

`DOE0447` (GSSG, **rho=100 Ωcm**, sigma=1 S/m) is the only missing **paired numerical label**. Original fixed geometry needs two valid R3 and R5 results; both current results say `FAILED: AEDT did not solve`. The case ID string `S1` is conductivity, NOT resistivity, to avoid mislabeling. Root cause is not proven by `result.json` alone; inspect exported AEDT messages and actual failure profiles before altering meshing or claiming physical nonconvergence. Rerun only failed cases via prior verified safe-resume and preserve source archive + per-case QA. New results must supersede FAILED only with provenance.

### Combined five-batch current status
- 450 distinct frozen design coordinates attempted; 449 have complete R3/R5 results. **898/900 successful** Q3D solves; 2 FAILED.
- **312** paired DOE points with worst relevant C difference under 1%, **137** with ≥1% requiring P1 targeted mesh verification; **1** unpaired solver failure.
- **11** paired DOE points with worst difference ≥5%, all retained in original P1.
- Across C-under1% points, **271** have <10% optional mesh separation diagnostic (P2 selective review), and 41 have ≥10% extra separation diagnostic. Neither subset is automatically physically validated.
- No recorded CG adaptive nonconvergence on the 98 successful Chunk5 cases. All 98 corresponding exported matrix headers currently mismatch the requested 1GHz frequency as recorded; native frequency provenance still unresolved.
- Local export artifacts: `G02_V63_chunk5_50points_mesh_audit.csv` (50 rows, including DOE0447 failure status) and `G02_V63_chunk5_100solve_signed_matrices.csv` (100 rows, two failures carry missing C). Full ZIP remains held by researcher, not in GitHub.
- The original DOE input coordinates are frozen. Do not replace difficult points. Follow-up requires targeted additional refinement, independent mesh diversification or mesh policy where Student capacity permits, frequency provenance investigation, and separate physical-model validation.

See [living backlog](G02_PRODUCTION_DOE_OPEN_MESH_FOLLOWUP_LEDGER.md) for all 137 P1 IDs, all 271 P2 candidate IDs and DOE0447 solver failure.
