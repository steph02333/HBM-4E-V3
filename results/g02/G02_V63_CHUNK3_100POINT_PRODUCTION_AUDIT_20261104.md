# G02 V6.3 — Chunk 3 real 100-point audit, with three-chunk comparison (2026-11-04)

## Source and reproducibility
Original uploaded `G02_V63_H0_PRODUCTION_DOE_results_bundle.zip`, SHA256 `6fe9493b46571b6e5fcfc16735010844bbb8e1c27b940b30c9c5510a3590e19b`. ZIP contains `manifest.json` with `chunk:3`, 200 successful `cases/.../result.json` for 100 unique originally frozen geometry IDs, each R3 and R5. **No simulated data were invented; no Chunk 4 data are included here.** Full `G02_V63_chunk3_100points_mesh_audit.csv` and `G02_V63_chunk3_200solve_signed_matrices.csv` generated from the ZIP and retained locally, not committed to GitHub in this write.

The professor-relevant pair metric is worst percentage change across CAA, CBB, and |CAB| (only CAA for GSG), from R3 to R5. This is **two-level numerical stability**, NOT verified continuum solution or physical accuracy. Additional >=10% total mesh growth heuristic is *not* a professor requirement.

## Comparison across batches
| Metric | Chunk1 | Chunk2 | Chunk3 | Combined |
|---|---:|---:|---:|---:|
| Distinct DOE input points | 100 | 100 | 100 | 300 |
| Successful Q3D solves | 200 | 200 | 200 | 600 |
| Worst-C-delta <1% | 73 | 66 | 73 | **212** |
| Worst-C-delta 1–2% | 12 | 14 | 15 | **41** |
| Worst-C-delta 2–5% | 14 | 20 | 10 | **44** |
| Worst-C-delta ≥5% | 1 | 0 | 2 | **3** |
| Worst-C-delta ≥1% requiring P1 follow-up | 27 | 34 | 27 | **88** |
| Supplemental P2 low mesh-growth review | 63 | 57 | 64 | **184** |
| Extra ≥10%-mesh + C<1% screen | 10 | 9 | 9 | **28** |

Chunk3 median worst-C-delta **0.40927%**, p90 **3.10355%**, max **7.82235%**, median actual total mesh-growth 5.14216%. **200/200 solved**, no recorded CG adaptive nonconvergence warning. All 200 export-frequency header readbacks remain mismatched with requested 1000MHz; native frequency provenance remains unresolved.

## ≥5% high-risk special watchlist (all three completed chunks)
| Chunk | DOE ID | Topology | rho (Ωcm) | Coefficient | Worst ΔC | D µm | P µm | H µm | tox µm |
|---|---|---|---:|---|---:|---:|---:|---:|---:|
| 1 | DOE0050 | GSGSG | 1 | |CAB| | 5.11768% | 3.52713 | 19.15600 | 41.97181 | .19028 |
| 3 | DOE0184 | GSGSG | 1 | |CAB| | 5.46881% | 4.83921 | 12.23673 | 25.54518 | .30285 |
| 3 | DOE0240 | GSGSG | 100 | |CAB| | **7.82235%** | 4.30498 | 14.09166 | 26.05169 | .37574 |

Chunk2 currently has **zero ≥5%**. Each remains P1; the persistent GSGSG mutual-C pattern warrants investigation, but no causation claimed. Main P1 list includes **all 27 Chunk3 >=1% cases**, not only the two >=5%. See [single living follow-up ledger](G02_PRODUCTION_DOE_OPEN_MESH_FOLLOWUP_LEDGER.md).

## Chunk3 9 material/topology strata
| Topology | rho Ωcm | n | under-1% | Max % |
|---|---:|---:|---:|---:|
| GSG | 1 | 11 | 6 | 4.651 |
| GSG | 10 | 11 | 11 | .222 |
| GSG | 100 | 12 | 12 | .380 |
| GSSG | 1 | 11 | 7 | 3.152 |
| GSSG | 10 | 11 | 10 | 1.011 |
| GSSG | 100 | 11 | 8 | 1.436 |
| GSGSG | 1 | 11 | 4 | 5.469 |
| GSGSG | 10 | 11 | 8 | 1.438 |
| GSGSG | 100 | 11 | 7 | 7.822 |

The higher relative mutual-C discrepancies in GSGSG occur repeatedly, especially rho1. A low C delta alone does not demonstrate mesh independence if realized meshes are very similar; however the arbitrary 10% element difference must not be promoted to a professor-mandated reject criterion.

## Next steps
- Keep frozen 450-point DOE manifest intact. Chunk4 previously stopped with AEDT project/session errors; local preliminary check: 155 saved successes, 14 failed, 31 missing; **no claim of Chunk4 completion**.
- When Chunk4 recovered, audit and append to original living ledger; do not delete any successful prior case on reruns.
- After acquiring all 450, prioritize 88+ P1 to date, especially three ≥5%; perform controlled additional mesh levels or independent mesh allocation as Student cap permits; track original signed capacitance and solver provenance for ML label QA.
