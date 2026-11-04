# Production DOE — Open Mesh Verification Ledger (Chunk 1–5)

**Last updated:** 2026-11-04 (combined 450-point <2% provisional ML triage, license-cap evidence added)

## New combined-dataset operational ML triage (2026-11-04; do not overwrite original professor QA)

The researcher now elects a **<2% worst-coefficient R3/R5 difference** as an **operational provisional ML-label screen**, treating all five chunks as ONE database: **374/450 provisional retain (312 <1%, 62 1–<2%)**, **75/450 at ≥2% requiring numerical follow-up (64 at 2–<5%, 11 at ≥5%)**, and **1/450 solver failure (DOE0447)**. The original **137 ≥1% P1** cases remain in this audit log for stricter professor-oriented mesh-refinement reporting: **62 are now 1–<2% and provisionally retainable by the weaker ML rule**, 75 remain >=2%; this is **not** retroactive physical validation.

**Confirmed license cause for DOE0447:** original AEDT raw error identifies **8030 Student 3D surface elements R3** and **8340 R5**, both exceeding 8000. This is a real cap violation. By contrast, successful mesh-export **total elements** ≥8000 (144 of 449 successful DOE pairs) are NOT the same license counter and **must not** be called license violations. **75-case exact geometry + per-mesh data** and **144-case total-mesh diagnostic list** are in the new local unified datasets; [global analysis and repair plan](G02_V63_ALL450_GLOBAL_2PCT_MESH_REMEDIATION_20261104.md) is committed on GitHub.

Target **DOE0447 separately first**, then small third-mesh pilot at extreme >=5% cases, then remaining 2–<5% using independent mesh allocations under Student surface cap. Never blindly blanket-R7; require genuine mesh distinction and cross-solution C stability before relabeling. Preserve every frozen DOE coordinate, original values, and both <1% and <2% QA flags.

## Meaning of statuses — professor-aligned

- **P1_C_DELTA_GE_1PCT**: all requested mesh solves succeeded, but at least one of CAA/CBB/|CAB| changed ≥1% between R3 and R5. **Run targeted additional adaptive refinement / alternative qualified mesh policy** and examine signed matrices. These 27 Chunk 1 cases are highest priority.
- **P2_C_STABLE_MESH_CLOSE**: all C changes <1%, but total-element change <10%. **This is NOT a failure of the professor's 1% criterion**. It is only an investigator-added mesh-diversity diagnostic and a selective audit queue; retain labels, consider sampling for R7 or independent policy. The 10% cutoff is not mandated by the professor or Ansys.
- **TWO_LEVEL_SCREEN_CLEAR**: all C changes <1%, and extra total-element change ≥10%. Still **not proven mesh-independent**, but lower follow-up priority; random audit some for selection-bias control.
- **QUALIFIED**: assign only after explicit separate multi-mesh and physical-provenance assessment with traceable evidence; none in this ledger is automatically labeled qualified.

Source file: researcher's `G02_V63_H0_PRODUCTION_DOE_results_bundle.zip`, 200 solved case results; detailed 100-row per-point audit `G02_V63_chunk1_100points_mesh_audit.csv` kept by researcher. Summary: [Chunk 1 numerical audit](G02_V63_CHUNK1_100POINT_PRODUCTION_AUDIT_20261103.md).

## Chunk 1 — 100 original DOE points, 200/200 Q3D solves

**27 P1 (all required C deltas not <1%)**. Percentages are worst individual coefficient R3-versus-R5 changes; mesh change is percentage increase in *total* elements; these are different from Student license's 8000 *surface*-element cap.

| DOE ID | Topology | rho (Ω·cm) | Worst C | ΔC (%) | Δ total elements (%) | Queue status |
|---|---|---:|---|---:|---:|---|
| DOE0002 | GSGSG | 1 | AB | 1.4665 | 2.67 | P1 OPEN |
| DOE0003 | GSGSG | 1 | AB | 4.1252 | 16.95 | P1 OPEN |
| DOE0009 | GSGSG | 10 | AB | 1.0232 | 2.97 | P1 OPEN |
| DOE0014 | GSGSG | 100 | AB | 1.0994 | 3.29 | P1 OPEN |
| DOE0017 | GSG | 1 | AA | 3.2090 | 72.94 | P1 OPEN |
| DOE0019 | GSG | 1 | AA | 2.4782 | 25.49 | P1 OPEN |
| DOE0020 | GSG | 1 | AA | 1.3959 | 56.04 | P1 OPEN |
| DOE0037 | GSSG | 10 | BB | 3.2760 | 24.02 | P1 OPEN |
| DOE0038 | GSSG | 10 | AB | 2.3551 | 24.01 | P1 OPEN |
| DOE0044 | GSSG | 100 | BB | 1.0468 | 17.25 | P1 OPEN |
| DOE0047 | GSGSG | 1 | AB | 4.9936 | 46.74 | P1 OPEN |
| DOE0049 | GSGSG | 1 | AB | 1.1231 | 9.35 | P1 OPEN |
| DOE0050 | GSGSG | 1 | AB | 5.1177 | 49.83 | P1 OPEN |
| DOE0051 | GSGSG | 10 | AB | 1.0266 | 2.51 | P1 OPEN |
| DOE0054 | GSGSG | 10 | AB | 1.1812 | 2.62 | P1 OPEN |
| DOE0055 | GSGSG | 10 | AB | 1.0926 | 3.15 | P1 OPEN |
| DOE0057 | GSGSG | 100 | AB | 3.5916 | 33.47 | P1 OPEN |
| DOE0062 | GSG | 1 | AA | 4.8162 | 37.91 | P1 OPEN |
| DOE0080 | GSSG | 1 | AB | 2.3428 | 14.51 | P1 OPEN |
| DOE0081 | GSSG | 10 | AB | 1.2316 | 24.10 | P1 OPEN |
| DOE0084 | GSSG | 10 | BB | 4.0175 | 24.35 | P1 OPEN |
| DOE0090 | GSSG | 100 | AB | 2.5269 | 30.48 | P1 OPEN |
| DOE0091 | GSGSG | 1 | AB | 3.5591 | 16.72 | P1 OPEN |
| DOE0096 | GSGSG | 10 | AB | 1.2979 | 2.72 | P1 OPEN |
| DOE0107 | GSG | 1 | AA | 3.6736 | 71.40 | P1 OPEN |
| DOE0121 | GSSG | 1 | AB | 4.8292 | 22.44 | P1 OPEN |
| DOE0131 | GSSG | 100 | AB | 1.8594 | 18.96 | P1 OPEN |

**63 P2 (C <1% but total mesh growth <10%; do not call these failed)**:

DOE0001, DOE0004, DOE0006, DOE0007, DOE0008, DOE0010, DOE0011, DOE0012, DOE0013, DOE0015, DOE0018, DOE0021, DOE0022, DOE0023, DOE0024, DOE0025, DOE0026, DOE0027, DOE0029, DOE0030, DOE0031, DOE0032, DOE0033, DOE0034, DOE0035, DOE0036, DOE0040, DOE0041, DOE0042, DOE0046, DOE0052, DOE0053, DOE0056, DOE0058, DOE0059, DOE0060, DOE0061, DOE0063, DOE0064, DOE0065, DOE0066, DOE0067, DOE0068, DOE0069, DOE0070, DOE0071, DOE0072, DOE0073, DOE0074, DOE0075, DOE0077, DOE0078, DOE0079, DOE0082, DOE0086, DOE0087, DOE0088, DOE0089, DOE0101, DOE0106, DOE0111, DOE0116, DOE0126.

**10 TWO_LEVEL_SCREEN_CLEAR** (also select some for independent QA; NOT fully qualified automatically):

DOE0005, DOE0016, DOE0028, DOE0039, DOE0043, DOE0045, DOE0048, DOE0076, DOE0083, DOE0085.

**Chunk 1 partitions:** 27 + 63 + 10 = 100; 27 high-delta, 73 C-under-1 including 63+10. All cases remain saved raw DOE data. No point deleted.

## Chunk 2 — VERIFIED complete, 2026-11-04

Uploaded archive `G02_V63_H0_PRODUCTION_DOE_results_bundle.zip`; SHA-256 `47d27ce553030ff08e69c62fc72daa251563d6d7c8f4a6434073645f9e4c23df`. Checked 200 unique `result.json`: **100/100 matching frozen Chunk-2 manifest DOE IDs; 200/200 solved**. R3/R5 signed capacitance all relevant coefficients <1% for **66/100**; ≥1% for **34/100**. 57 additional under-1% cases have <10% total-mesh separation (diagnostic ONLY), 9 under-1% cases have ≥10% separation (additional diagnostic, NOT professor requirement). 34+57+9=100. No native CG-adaptive-nonconvergence warning in 200. Exported frequency header doesn't match requested native 1GHz in **200/200**, still unverified. Median maximum C delta 0.4974%, p90 2.6716%, max 4.9242% (DOE0092 |CAB|). Median total-mesh increase 5.30%. **Original coordinates / IDs intact, none replaced.**

### P1: all 34 Chunk-2 priority mesh follow-ups (worst C coefficient ≥1%)

| DOE ID | Topology | rho (Ω·cm) | Worst C | R3/R5 ΔC (%) | Δ total mesh elements (%) | Status |
|---|---|---:|---|---:|---:|---|
| DOE0092 | GSGSG | 1 | CAB | 4.9242 | 47.39 | OPEN |
| DOE0093 | GSGSG | 1 | CAB | 3.8052 | 19.20 | OPEN |
| DOE0094 | GSGSG | 1 | CAB | 3.7321 | 16.62 | OPEN |
| DOE0098 | GSGSG | 10 | CAB | 1.2669 | 2.56 | OPEN |
| DOE0099 | GSGSG | 10 | CAB | 1.0121 | 2.62 | OPEN |
| DOE0100 | GSGSG | 10 | CAB | 1.5389 | 2.56 | OPEN |
| DOE0103 | GSGSG | 100 | CAB | 1.1467 | 2.44 | OPEN |
| DOE0104 | GSGSG | 100 | CAA | 3.0213 | 51.88 | OPEN |
| DOE0105 | GSGSG | 100 | CAB | 1.2447 | 5.88 | OPEN |
| DOE0108 | GSG | 1 | CAA | 3.3385 | 53.43 | OPEN |
| DOE0109 | GSG | 1 | CAA | 2.6716 | 22.89 | OPEN |
| DOE0124 | GSSG | 1 | CAB | 2.3032 | 48.61 | OPEN |
| DOE0128 | GSSG | 10 | CBB | 2.5218 | 24.45 | OPEN |
| DOE0133 | GSSG | 100 | CAB | 2.1839 | 20.67 | OPEN |
| DOE0136 | GSGSG | 1 | CAB | 1.2570 | 2.82 | OPEN |
| DOE0137 | GSGSG | 1 | CAB | 3.9335 | 16.63 | OPEN |
| DOE0138 | GSGSG | 1 | CAB | 4.2381 | 16.92 | OPEN |
| DOE0139 | GSGSG | 1 | CAB | 1.4289 | 2.50 | OPEN |
| DOE0142 | GSGSG | 10 | CAB | 1.5057 | 2.72 | OPEN |
| DOE0146 | GSGSG | 100 | CAB | 2.3590 | 2.83 | OPEN |
| DOE0147 | GSGSG | 100 | CAB | 2.7626 | 16.44 | OPEN |
| DOE0149 | GSGSG | 100 | CAB | 1.3251 | 3.45 | OPEN |
| DOE0151 | GSG | 1 | CAA | 4.4739 | 35.91 | OPEN |
| DOE0152 | GSG | 1 | CAA | 2.0182 | 83.28 | OPEN |
| DOE0153 | GSG | 1 | CAA | 1.9126 | 24.64 | OPEN |
| DOE0154 | GSG | 1 | CAA | 1.0226 | 14.57 | OPEN |
| DOE0159 | GSG | 10 | CAA | 2.4781 | 38.95 | OPEN |
| DOE0168 | GSSG | 1 | CAB | 2.8036 | 50.03 | OPEN |
| DOE0170 | GSSG | 1 | CAB | 1.2169 | 5.93 | OPEN |
| DOE0174 | GSSG | 10 | CAB | 2.5251 | 17.53 | OPEN |
| DOE0179 | GSSG | 100 | CAB | 2.1129 | 28.12 | OPEN |
| DOE0186 | GSGSG | 10 | CAB | 1.0125 | 2.56 | OPEN |
| DOE0187 | GSGSG | 10 | CAB | 1.3407 | 2.67 | OPEN |
| DOE0197 | GSG | 1 | CAA | 2.2611 | 62.61 | OPEN |

### P2: 57 Chunk-2 selective QA candidates, C stable <1% (additional total-mesh separation heuristic <10%)

DOE0095, DOE0097, DOE0102, DOE0110, DOE0112, DOE0113, DOE0114, DOE0115, DOE0117, DOE0118, DOE0119, DOE0120, DOE0122, DOE0125, DOE0127, DOE0129, DOE0130, DOE0134, DOE0135, DOE0140, DOE0141, DOE0143, DOE0144, DOE0145, DOE0148, DOE0150, DOE0155, DOE0156, DOE0157, DOE0158, DOE0160, DOE0161, DOE0162, DOE0164, DOE0165, DOE0166, DOE0167, DOE0169, DOE0171, DOE0172, DOE0173, DOE0176, DOE0178, DOE0180, DOE0181, DOE0182, DOE0191, DOE0192, DOE0196, DOE0198, DOE0201, DOE0202, DOE0203, DOE0211, DOE0216, DOE0217, DOE0221.

**P2 cases are NOT failed professor criterion.** Only sampled third-level checks / mesh allocation diagnostics are contemplated.

### TWO_LEVEL_SCREEN_CLEAR: 9 Chunk-2 cases (under-1% C and extra total-mesh separation ≥10%)

DOE0123, DOE0132, DOE0163, DOE0175, DOE0177, DOE0206, DOE0207, DOE0212, DOE0222.

### Cumulative after Chunk 1 + 2

| Metric | Chunk 1 | Chunk 2 | Total |
|---|---:|---:|---:|
| Original DOE points / two-mesh pairs | 100 | 100 | **200** |
| Solved Q3D cases | 200 | 200 | **400** |
| P1: C difference ≥1% | 27 | 34 | **61** |
| P2: C difference <1%, mesh-growth heuristic <10% | 63 | 57 | **120** |
| Additional two-level screen clear (not fully validated) | 10 | 9 | **19** |
| All relevant C differences <1% | 73 | 66 | **139** |

After the full 450-point acquisition, prioritize the 61 P1 to date for controlled adaptive follow-up. Save the complete per-point matrix/mesh CSV and source result ZIPs; no training-label "truth" certification can be inferred from the above alone.


## Chunk 3 — independently audited real archive, 2026-11-04

Original uploaded `G02_V63_H0_PRODUCTION_DOE_results_bundle.zip` SHA256 `6fe9493b46571b6e5fcfc16735010844bbb8e1c27b940b30c9c5510a3590e19b`; native `manifest.json` explicitly says `chunk=3`. **100 unique DOE IDs / 200 of 200 successful saved R3/R5 solves.** Worst relevant capacitance difference is `max(ΔCAA,ΔCBB,Δ|CAB|)` across each real pair; for GSG only CAA. **73/100 below professor's ~1% two-level C consistency screen; 27/100 at or above 1%**. Supplemental only: 64 below 1% with under-10% total mesh growth; 9 below 1% with 10%+ growth. The 10% heuristic is *not* mandated by professor or Ansys.

**Chunk 3 error buckets**: <1%=73; 1–2%=15; 2–5%=10; ≥5%=2. Median max coefficient difference 0.4093%, P90 3.1036%, max **7.8223%**. Median total mesh growth 5.1422%. All 200 native exports again have frequency header mismatch with requested 1000MHz; this remains an unresolved provenance caveat.

### High-risk ≥5% watchlist (retain permanently for concentrated follow-up)

| Chunk | DOE ID | Topology | rho (Ω·cm) | Worst coefficient | ΔC (%) | D/P/H/tox (µm) |
|---|---|---|---:|---|---:|---|
| 1 | DOE0050 | GSGSG | 1 | AB | 5.1177 | 3.52713 / 19.15600 / 41.97181 / 0.19028 |
| 3 | DOE0184 | GSGSG | 1 | AB | 5.4688 | 4.83921 / 12.23673 / 25.54518 / 0.30285 |
| 3 | DOE0240 | GSGSG | 100 | AB | **7.8223** | 4.30498 / 14.09166 / 26.05169 / 0.37574 |

Chunk 2 has zero ≥5% cases. Keep these P1; all 1–5% P1 cases remain equally in main queue.

### P1: 27 new Chunk 3 priority follow-ups

| DOE ID | Topology | rho (Ω·cm) | Worst coefficient | R3/R5 ΔC (%) | Δ total mesh (%) | Status |
|---|---|---:|---|---:|---:|---|
| DOE0183 | GSGSG | 1 | AB | 1.232918 | 7.534598 | OPEN |
| DOE0184 | GSGSG | 1 | AB | 5.468813 | 19.982159 | OPEN |
| DOE0193 | GSGSG | 100 | AB | 3.566586 | 30.327869 | OPEN |
| DOE0214 | GSSG | 1 | AB | 3.152298 | 23.392461 | OPEN |
| DOE0215 | GSSG | 1 | AB | 1.360188 | 8.930426 | OPEN |
| DOE0224 | GSSG | 100 | AA | 1.111789 | 18.797164 | OPEN |
| DOE0226 | GSGSG | 1 | AB | 4.318705 | 24.621014 | OPEN |
| DOE0228 | GSGSG | 1 | AB | 3.106298 | 16.849817 | OPEN |
| DOE0232 | GSGSG | 10 | AB | 1.438295 | 2.667364 | OPEN |
| DOE0234 | GSGSG | 10 | AB | 1.282138 | 2.615063 | OPEN |
| DOE0238 | GSGSG | 100 | AB | 1.696310 | 2.770518 | OPEN |
| DOE0240 | GSGSG | 100 | AB | 7.822347 | 36.165176 | OPEN |
| DOE0241 | GSG | 1 | AA | 4.650763 | 72.691162 | OPEN |
| DOE0242 | GSG | 1 | AA | 3.931186 | 72.249752 | OPEN |
| DOE0245 | GSG | 1 | AA | 1.073186 | 35.881842 | OPEN |
| DOE0257 | GSSG | 1 | AB | 2.798561 | 25.235718 | OPEN |
| DOE0266 | GSSG | 100 | AB | 1.436286 | 27.428999 | OPEN |
| DOE0269 | GSSG | 100 | AA | 1.406627 | 31.395082 | OPEN |
| DOE0271 | GSGSG | 1 | AB | 1.764267 | 8.133087 | OPEN |
| DOE0272 | GSGSG | 1 | AB | 4.698227 | 65.577627 | OPEN |
| DOE0273 | GSGSG | 1 | AB | 3.236429 | 29.144385 | OPEN |
| DOE0277 | GSGSG | 10 | AB | 1.276051 | 2.564103 | OPEN |
| DOE0282 | GSGSG | 100 | AB | 1.734545 | 20.877316 | OPEN |
| DOE0286 | GSG | 1 | AA | 3.103249 | 66.253575 | OPEN |
| DOE0288 | GSG | 1 | AA | 1.096690 | 17.931689 | OPEN |
| DOE0303 | GSSG | 1 | AB | 1.298873 | 6.772009 | OPEN |
| DOE0307 | GSSG | 10 | BB | 1.010822 | 17.498613 | OPEN |

### P2: 64 under-1%-C points, extra mesh-growth heuristic below 10% (selectively audit, NOT failed)

DOE0185, DOE0188, DOE0189, DOE0190, DOE0194, DOE0195, DOE0199, DOE0200, DOE0204, DOE0205, DOE0208, DOE0209, DOE0210, DOE0213, DOE0219, DOE0220, DOE0227, DOE0229, DOE0230, DOE0231, DOE0233, DOE0235, DOE0236, DOE0237, DOE0239, DOE0243, DOE0244, DOE0246, DOE0247, DOE0248, DOE0249, DOE0250, DOE0251, DOE0252, DOE0253, DOE0254, DOE0255, DOE0256, DOE0258, DOE0259, DOE0260, DOE0261, DOE0263, DOE0264, DOE0265, DOE0267, DOE0268, DOE0276, DOE0278, DOE0281, DOE0283, DOE0289, DOE0291, DOE0292, DOE0293, DOE0294, DOE0296, DOE0297, DOE0298, DOE0299, DOE0301, DOE0302, DOE0311, DOE0312.

### TWO_LEVEL_SCREEN_CLEAR: 9 under-1%-C points with extra >=10% mesh-growth heuristic

DOE0218, DOE0223, DOE0225, DOE0262, DOE0270, DOE0287, DOE0306, DOE0308, DOE0313.

### Cumulative Chunk 1 + 2 + 3

| Metric | Chunk 1 | Chunk 2 | Chunk 3 | Total |
|---|---:|---:|---:|---:|
| DOE points sampled | 100 | 100 | 100 | **300** |
| Successful solves | 200 | 200 | 200 | **600** |
| C coefficients all <1% | 73 | 66 | 73 | **212** |
| P1 C ≥1% | 27 | 34 | 27 | **88** |
| P2 C <1%, small mesh growth (extra diagnostic) | 63 | 57 | 64 | **184** |
| Under-1% + >=10% growth (extra diagnostic) | 10 | 9 | 9 | **28** |

New local evidence files: `G02_V63_chunk3_100points_mesh_audit.csv` (100 real pairs and full inputs), `G02_V63_chunk3_200solve_signed_matrices.csv` (200 signed matrices), original raw archive retained by researcher. **These companion files are local artifacts, not yet in repository.** [Chunk 3 detailed audit](G02_V63_CHUNK3_100POINT_PRODUCTION_AUDIT_20261104.md).

## Chunk 4 — fully recovered and audited, 2026-11-04

Real recovered `G02_V63_H0_PRODUCTION_DOE_results_bundle.zip` SHA256 `25f01cd3a86e81234a09ac59173bea9893fc64bb7a9d1dcb64b2d22474494303`. ZIP `manifest.json` says `chunk=4`, and `progress.json` lists 200 cases. **All 200 unique R3/R5 solves saved `SOLVED_UNVERIFIED_PHYSICS`**, representing **100 original frozen DOE points**. Previously interrupted local run had 155 solved/14 failed/31 unsaved; successful safe resume filled all 45 without discarding the 155 solved cases. Final output has no failed result.json.

**Professor-relevant R3→R5 numerical C screen:** **68/100** have all applicable CAA/CBB/|CAB| coefficient differences <1%; **32/100** have at least one ≥1% and are P1. Adjacent bucket counts **<1%=68, 1–2%=15, 2–5%=13, ≥5%=4**. Median worst per-point C delta **0.4637%**, p90 ~**3.2905%**, maximum **6.2131%** (DOE0380 CAA). Median actual total mesh growth **5.0879%**. The supplemental 10% mesh-growth heuristic is NOT the professor's criterion; it labels 59 C-under-1% points for selective verification, while 9 meet that extra diagnostic.

### ≥5% special watchlist — Chunk 4 only

| DOE ID | Topology | rho (Ω·cm) | Worst coefficient | ΔC (%) | D/P/H/tox (µm) |
|---|---|---:|---|---:|---|
| DOE0319 | GSGSG | 1 | AB | 5.4031 | 4.05424 / 14.67569 / 34.46872 / 0.32166 |
| DOE0361 | GSGSG | 1 | AB | 5.4009 | 3.41919 / 18.93650 / 37.20655 / 0.20478 |
| DOE0365 | GSGSG | 1 | AB | 5.7074 | 4.94650 / 16.59706 / 36.66756 / 0.27781 |
| DOE0380 | GSG | 1 | AA | **6.2131** | 3.34749 / 13.39294 / 29.90007 / 0.19222 |

The combined four-chunk >=5% watchlist now has **7 distinct points**: Chunk 1 DOE0050; Chunk 3 DOE0184, DOE0240; Chunk 4 DOE0319, DOE0361, DOE0365, DOE0380; Chunk 2 none. The living [special-watchlist CSV](G02_V63_CHUNKS1TO4_GE5_SPECIAL_WATCHLIST_20261104.csv) has all original parameter coordinates.

### P1: all 32 Chunk-4 high-priority DOE points, worst coefficient ≥1%

| DOE ID | Topology | rho Ω·cm | Worst coefficient | R3/R5 ΔC (%) | Δ total mesh elements (%) | Status |
|---|---|---:|---|---:|---:|---|
| DOE0279 | GSGSG | 10 | AB | 1.538751 | 2.615063 | OPEN |
| DOE0300 | GSG | 100 | AA | 1.035704 | 17.318982 | OPEN |
| DOE0314 | GSSG | 100 | AB | 1.555528 | 17.830009 | OPEN |
| DOE0317 | GSGSG | 1 | AB | 4.491268 | 29.211470 | OPEN |
| DOE0319 | GSGSG | 1 | AB | 5.403076 | 24.110879 | OPEN |
| DOE0320 | GSGSG | 1 | AB | 1.030632 | 40.019714 | OPEN |
| DOE0321 | GSGSG | 10 | AB | 1.347436 | 2.615063 | OPEN |
| DOE0324 | GSGSG | 10 | AB | 1.298121 | 2.722513 | OPEN |
| DOE0327 | GSGSG | 100 | AB | 1.068542 | 3.092243 | OPEN |
| DOE0330 | GSGSG | 100 | AB | 2.096997 | 19.139105 | OPEN |
| DOE0331 | GSG | 1 | AA | 4.351269 | 71.853320 | OPEN |
| DOE0332 | GSG | 1 | AA | 3.290394 | 49.513619 | OPEN |
| DOE0335 | GSG | 1 | AA | 3.758090 | 29.224652 | OPEN |
| DOE0346 | GSSG | 1 | AB | 4.427775 | 22.936288 | OPEN |
| DOE0349 | GSSG | 1 | AB | 1.536955 | 65.051715 | OPEN |
| DOE0352 | GSSG | 10 | AB | 2.002961 | 17.461197 | OPEN |
| DOE0355 | GSSG | 10 | BB | 1.501988 | 24.181919 | OPEN |
| DOE0357 | GSSG | 100 | AB | 2.022561 | 27.632874 | OPEN |
| DOE0359 | GSSG | 100 | AB | 1.005922 | 21.190765 | OPEN |
| DOE0361 | GSGSG | 1 | AB | 5.400901 | 48.144276 | OPEN |
| DOE0364 | GSGSG | 1 | AB | 1.311286 | 2.772809 | OPEN |
| DOE0365 | GSGSG | 1 | AB | 5.707363 | 16.718913 | OPEN |
| DOE0371 | GSGSG | 100 | BB | 1.188688 | 22.799181 | OPEN |
| DOE0372 | GSGSG | 100 | AB | 2.019250 | 18.734793 | OPEN |
| DOE0373 | GSGSG | 100 | AB | 3.291440 | 43.682733 | OPEN |
| DOE0376 | GSG | 1 | AA | 1.699867 | 22.656250 | OPEN |
| DOE0380 | GSG | 1 | AA | 6.213086 | 61.374795 | OPEN |
| DOE0391 | GSSG | 1 | AB | 4.159713 | 25.124792 | OPEN |
| DOE0392 | GSSG | 1 | AB | 2.754280 | 17.474186 | OPEN |
| DOE0393 | GSSG | 1 | AB | 1.049908 | -10.815047 | OPEN |
| DOE0402 | GSSG | 100 | BB | 2.708468 | 19.410745 | OPEN |
| DOE0403 | GSSG | 100 | AA | 1.070785 | 20.921409 | OPEN |

### P2: 59 Chunk-4 selective-audit candidates (all C<1%, additional total-mesh-growth heuristic <10%)

DOE0274, DOE0275, DOE0280, DOE0284, DOE0285, DOE0290, DOE0295, DOE0304, DOE0309, DOE0310, DOE0316, DOE0322, DOE0323, DOE0325, DOE0326, DOE0328, DOE0329, DOE0333, DOE0334, DOE0336, DOE0337, DOE0338, DOE0339, DOE0340, DOE0341, DOE0342, DOE0343, DOE0344, DOE0347, DOE0348, DOE0350, DOE0351, DOE0353, DOE0354, DOE0358, DOE0360, DOE0362, DOE0363, DOE0366, DOE0367, DOE0368, DOE0369, DOE0374, DOE0377, DOE0379, DOE0381, DOE0382, DOE0383, DOE0384, DOE0385, DOE0386, DOE0387, DOE0388, DOE0389, DOE0390, DOE0394, DOE0397, DOE0398, DOE0399.

### TWO_LEVEL_SCREEN_CLEAR: 9 Chunk-4 cases (C<1% with additional ≥10% mesh-growth diagnostic)

DOE0305, DOE0315, DOE0318, DOE0345, DOE0356, DOE0378, DOE0396, DOE0401, DOE0404.

### Cumulative after Chunk 4

| Metric | Chunk1 | Chunk2 | Chunk3 | Chunk4 | Total |
|---|---:|---:|---:|---:|---:|
| Frozen original DOE points acquired | 100 | 100 | 100 | 100 | **400/450** |
| Successful saved Q3D solves | 200 | 200 | 200 | 200 | **800** |
| All relevant C deltas <1% | 73 | 66 | 73 | 68 | **280** |
| P1 (≥1% in ≥1 C term) | 27 | 34 | 27 | 32 | **120** |
| P2 (C<1%, under10% mesh-growth diagnostic) | 63 | 57 | 64 | 59 | **243** |
| C<1% with extra ≥10% mesh-growth diagnostic | 10 | 9 | 9 | 9 | **37** |
| C difference ≥5% | 1 | 0 | 2 | 4 | **7** |

Original Chunk-4 per-point/matrix audits: `G02_V63_chunk4_100points_mesh_audit.csv` and `G02_V63_chunk4_200solve_signed_matrices.csv`, both generated from actual uploaded ZIP, currently retained locally, not claimed committed to GitHub. **All 200 solves have no CG adaptive nonconvergence warning recorded**, and native exported header mismatch with requested 1GHz persists. This does not automatically prove accurate HBM4 physical simulation. Do not alter DOE IDs or replace hard points.

## Chunk 5 — recovered partial result audit, 2026-11-04

The submitted `G02_V63_H0_PRODUCTION_DOE_results_bundle.zip` SHA256 `7d6759a3faa9672418df4ae0807f2e2a2778f167d14bbc41572e9f309792cf3e` contains a native `manifest.json` declaring `chunk=5`; all 100 planned original R3/R5 IDs have `result.json` (50 frozen DOE points). **98/100 solved; 2/100 FAILED**, both belonging to **DOE0447, GSSG, rho=100 Ω·cm, R3 and R5**. Solver failure is a distinct quality class, not a C-error category. It is **NOT yet correct** to call all 450 original DOE points successfully acquired.

For the **49 successfully paired DOE points**, professor-aligned worst relevant R3/R5 C relative differences: <1% **32**, 1–2% **6**, 2–5% **7**, ≥5% **4**. Median 0.4732%, P90 4.3252%, worst 6.1822% (DOE0407 |CAB|). **17/49 P1 C discrepancy ≥1%; 32/49 under1%**, of which 28 under-10%-mesh-growth diagnostic P2 candidates and 4 >=10%-growth additional-screen-clear. The 10% separation is an investigator auxiliary heuristic, **not professor-mandated**. All 49 C matrices have positive eigenvalues and matching signal nets in the recorded checks. Exported matrix frequency header still mismatches requested 1 GHz across solved cases.

### Chunk-5 ≥5% special watchlist

| DOE ID | Topology | rho Ω·cm | Worst coefficient | ΔC % | D/P/H/tox (µm) |
|---|---|---:|---|---:|---|
| DOE0406 | GSGSG | 1 | CAB | 5.0820 | 5.29121 / 12.93521 / 26.31592 / 0.36866 |
| DOE0407 | GSGSG | 1 | CAB | **6.1822** | 3.26199 / 19.64152 / 42.14727 / 0.33561 |
| DOE0421 | GSG | 1 | CAA | 5.3004 | 3.43947 / 12.26979 / 49.50157 / 0.35947 |
| DOE0422 | GSG | 1 | CAA | 5.0903 | 3.90312 / 10.55119 / 26.81056 / 0.17715 |

Five-chunk ≥5% special watchlist now contains **11** points (1 Chunk1 + 0 Chunk2 + 2 Chunk3 + 4 Chunk4 + 4 Chunk5). These are included in the normal P1 queue, not separate replacement samples.

### P1: all 17 Chunk-5 ≥1% C-delta DOE IDs (OPEN)

| DOE ID | Topology | rho Ω·cm | Worst C | R3/R5 ΔC % | Total mesh growth % | Status |
|---|---|---:|---|---:|---:|---|
| DOE0395 | GSSG | 1 | CAB | 3.032357 | 24.598338 | OPEN |
| DOE0405 | GSSG | 100 | CAB | 1.769312 | 36.262866 | OPEN |
| DOE0406 | GSGSG | 1 | CAB | 5.082031 | 20.232766 | OPEN |
| DOE0407 | GSGSG | 1 | CAB | 6.182178 | 39.378914 | OPEN |
| DOE0408 | GSGSG | 1 | CAB | 4.317604 | 19.392315 | OPEN |
| DOE0410 | GSGSG | 1 | CAB | 3.428453 | 16.544694 | OPEN |
| DOE0411 | GSGSG | 10 | CAB | 1.319865 | 2.615063 | OPEN |
| DOE0412 | GSGSG | 10 | CAB | 1.227960 | 2.667364 | OPEN |
| DOE0421 | GSG | 1 | CAA | 5.300429 | 51.892430 | OPEN |
| DOE0422 | GSG | 1 | CAA | 5.090286 | 34.206219 | OPEN |
| DOE0424 | GSG | 1 | CAA | 4.355676 | 74.280040 | OPEN |
| DOE0425 | GSG | 1 | CAA | 4.291699 | 51.391650 | OPEN |
| DOE0433 | GSG | 100 | CAA | 1.161961 | 17.073171 | OPEN |
| DOE0435 | GSG | 100 | CAA | 1.186759 | 26.803119 | OPEN |
| DOE0437 | GSSG | 1 | CAB | 1.272572 | 14.147910 | OPEN |
| DOE0438 | GSSG | 1 | CAB | 2.710329 | 24.736550 | OPEN |
| DOE0443 | GSSG | 10 | CBB | 3.537656 | 24.902940 | OPEN |

### P2: 28 under-1% C cases with extra <10% total-mesh-growth diagnostic (selective audit only)

DOE0370, DOE0375, DOE0400, DOE0409, DOE0413, DOE0414, DOE0415, DOE0416, DOE0417, DOE0418, DOE0419, DOE0420, DOE0423, DOE0426, DOE0427, DOE0428, DOE0429, DOE0430, DOE0431, DOE0432, DOE0434, DOE0436, DOE0439, DOE0440, DOE0442, DOE0444, DOE0445, DOE0446.

### Extra-screen-clear: 4 C-under1% points with ≥10% mesh-growth diagnostic

DOE0441, DOE0448, DOE0449, DOE0450.

### Separate solver-failure queue — rerun before claiming completed 450-point production acquisition

**DOE0447**, GSSG, rho **100 Ω·cm**: `V62_DOE0447_GSSG_S1_BOTH_OX_L6p0_R3` and `..._R5` both `FAILED` with "AEDT did not solve; inspect case AEDT messages". The case ID `S1` refers to conductivity sigma=1 S/m, corresponding to rho=100 Ω·cm. Do not confuse sigma S1 with rho1. Retry only this original frozen DOE coordinate after verifying AEDT health; keep every previously solved Chunk5 case intact. If this persists, preserve profile and AEDT error messages.

### Cumulative production DOE acquisition at this checkpoint

| Metric | Chunk 1–4 | Chunk 5 | Combined |
|---|---:|---:|---:|
| Original DOE points attempted | 400 | 50 | **450/450** |
| Planned simulations | 800 | 100 | **900** |
| Saved successful simulations | 800 | 98 | **898/900** |
| Fully successful R3/R5 DOE pairs | 400 | 49 | **449/450** |
| R3/R5 relevant C delta <1% | 280 | 32 | **312** |
| P1 R3/R5 C delta ≥1% | 120 | 17 | **137** |
| P2 under1%-C and <10% mesh growth (extra diagnostic) | 243 | 28 | **271** |
| Under1%-C and ≥10% mesh growth (extra diagnostic) | 37 | 4 | **41** |
| ΔC ≥5% special cases | 7 | 4 | **11** |
| Unpaired due to failure | 0 | 1 | **1 (DOE0447)** |

This is a robust **first-pass acquisition coverage** record, **not validated physical truth**. Dataset freeze is retained and no DOE cases were resampled. The local files `G02_V63_chunk5_50points_mesh_audit.csv` and `G02_V63_chunk5_100solve_signed_matrices.csv` were exported from the real ZIP but are not committed by this ledger update.



## Follow-up execution plan (do this AFTER main DOE acquisition, per researcher's preference)

1. Accumulate and audit each 100-point Chunk; append P1/P2 lists without rerunning prior successful solves.
2. Generate deduplicated **targeted follow-up manifest** preserving original DOE IDs and all six original inputs. **P1 first**: try a third genuinely different adaptive level, compare all relevant C coefficients to both historical levels, check Student surface license constraints. If R7 is infeasible or ineffective, use controlled alternate mesh allocation and compare independently. No universal blind R7 assumption.
3. For P2, audit a **representative random / risk-stratified sample**, not necessarily all 63 solely because of arbitrary 10% mesh-growth cutoff. Examine actual mesh distribution and adaptive history; further levels only where needed.
4. Maintain follow-up result statuses `OPEN`, `ATTEMPTED`, `CONFIRMED_WITHIN_POLICY`, `UNRESOLVED`, `BLOCKED_STUDENT_LIMIT`; never call `SOLVED` automatically `PHYSICALLY_VALIDATED`.
5. Before training/reporting as truth: resolve Q3D native 1 GHz vs exported matrix frequency-header mismatch (present in all 898 successful Chunk 1–5 solves; two DOE0447 cases failed before valid C exports); address remaining simplified H0 physical-model and independent solver caveats separately.
6. Record exact follow-up command, runner/script checksum, run folder, numerical comparisons and evidence ZIP; commit updated ledger alongside per-point QA CSV.

**This ledger is a living audit backlog, not a declaration that 90/100 labels are unusable.**
