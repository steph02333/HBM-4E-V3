# G02 V6.3 — Production DOE Chunk 4 recovered, 100-point actual audit (2026-11-04)

**Real uploaded ZIP** `G02_V63_H0_PRODUCTION_DOE_results_bundle.zip` checksum SHA256 `25f01cd3a86e81234a09ac59173bea9893fc64bb7a9d1dcb64b2d22474494303`. Native manifest explicitly identifies Chunk 4. All 200 planned R3/R5 case result.json files exist and carry `SOLVED_UNVERIFIED_PHYSICS`, and progress.json records 200 cases / 100 distinct DOE IDs. This is the fully recovered run following previous AEDT crash (155 saved successful, 14 failed and 31 missing before recovery). Data are **numerically solved, not claimed physically verified**.

## Professor-aligned Cscreen
Compare each originally frozen DOE point's R3/R5 matrices. Worst coefficient deviation = max of CAA, CBB and absolute CAB where applicable (GSG: CAA only), normalized to R5 coefficient magnitude. This is a **two-level adaptive consistency screen**, not absolute convergence proof.

| C error bucket | Chunk 1 | Chunk 2 | Chunk 3 | **Chunk 4** | Cumulative |
|---|---:|---:|---:|---:|---:|
| <1% | 73 | 66 | 73 | **68** | **280** |
| 1–2% | 12 | 14 | 15 | **15** | **56** |
| 2–5% | 14 | 20 | 10 | **13** | **57** |
| >=5% | 1 | 0 | 2 | **4** | **7** |
| Total points | 100 | 100 | 100 | 100 | **400/450** |

Chunk4 **68/100** C under 1%, **32/100** >=1% placed in same living [DOE mesh follow-up ledger](G02_PRODUCTION_DOE_OPEN_MESH_FOLLOWUP_LEDGER.md). Chunk4 median max C delta 0.46372%, p90 3.29050%, maximum 6.21309%; median total-element growth 5.08789%. Of 68 C-under1 points, 59 <10% growth and 9 >=10% growth. This optional total mesh difference is **not a professor requirement** and not a standalone accuracy test.

## Chunk4 >=5% follow-up priority
| DOE ID | Topology | rho Ωcm | coefficient | max R3/R5 delta | D (µm) | P (µm) | H (µm) | tox (µm) |
|---|---|---:|---|---:|---:|---:|---:|---:|
| DOE0319 | GSGSG | 1 | |CAB| | 5.40308% | 4.05424 | 14.67569 | 34.46872 | .32166 |
| DOE0361 | GSGSG | 1 | |CAB| | 5.40090% | 3.41919 | 18.93650 | 37.20655 | .20478 |
| DOE0365 | GSGSG | 1 | |CAB| | 5.70736% | 4.94650 | 16.59706 | 36.66756 | .27781 |
| DOE0380 | GSG | 1 | CAA | **6.21309%** | 3.34749 | 13.39294 | 29.90007 | .19222 |

All four are high conductivity silicon rho=1 Ωcm, but topology differs; do not infer mechanism from category alone. Complete cumulative 7-point >=5% watchlist in sibling CSV. Only one of the original 450 is sampled at each preselected geometry; don't replace difficult samples.

## Checks / limitations
- 200/200 successful solves; no native CG adaptive nonconvergence warnings recorded.
- Signed matrices and input geometry were preserved in extracted local `G02_V63_chunk4_100points_mesh_audit.csv` and `G02_V63_chunk4_200solve_signed_matrices.csv`; full raw ZIP remains outside this GitHub repo. No explicit verification of all points' mesh independence from just two levels.
- All 200 returned exported frequency headers disagree with requested native 1GHz setup. Provenance remains unresolved. Q3D reduced H0 conductive Si finite-domain model is not a full physically validated HBM4 die.
- One recovered example DOE0393 has **R5 total mesh count below R3** (the PerRefine setting does not guarantee monotonic actual mesh size). Compute delta by corresponding R labels, not sorted mesh count.
- Ready to acquire final Chunk5 50 points (100 R3/R5 solves), while separately planning targeted follow-up for 120/400 currently >=1% C. Selectively validate C-under1% points with a genuinely different mesh and resolve frequency provenance before final training claims.

## Related
- [Living P1/P2 DOE follow-up ledger](G02_PRODUCTION_DOE_OPEN_MESH_FOLLOWUP_LEDGER.md)
- [>=5% all-four-chunk watchlist](G02_V63_CHUNKS1TO4_GE5_SPECIAL_WATCHLIST_20261104.csv)
