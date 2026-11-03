# Production DOE — Open Mesh Verification Ledger (Chunk 1–5)

**Last updated:** 2026-11-04 · **Authoritative living GitHub backlog**. Append new Chunk 2/3/4/5 issues to THIS SAME FILE, do not create separate disconnected to-do lists. Frozen 450-point V6.2/V6.3 manifest; never replace an original DOE coordinate because of mesh difficulty.

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


## Chunk 3/4/5 — awaiting results

Status: NOT YET RUN / RECEIVED.

## Follow-up execution plan (do this AFTER main DOE acquisition, per researcher's preference)

1. Accumulate and audit each 100-point Chunk; append P1/P2 lists without rerunning prior successful solves.
2. Generate deduplicated **targeted follow-up manifest** preserving original DOE IDs and all six original inputs. **P1 first**: try a third genuinely different adaptive level, compare all relevant C coefficients to both historical levels, check Student surface license constraints. If R7 is infeasible or ineffective, use controlled alternate mesh allocation and compare independently. No universal blind R7 assumption.
3. For P2, audit a **representative random / risk-stratified sample**, not necessarily all 63 solely because of arbitrary 10% mesh-growth cutoff. Examine actual mesh distribution and adaptive history; further levels only where needed.
4. Maintain follow-up result statuses `OPEN`, `ATTEMPTED`, `CONFIRMED_WITHIN_POLICY`, `UNRESOLVED`, `BLOCKED_STUDENT_LIMIT`; never call `SOLVED` automatically `PHYSICALLY_VALIDATED`.
5. Before training/reporting as truth: resolve Q3D native 1 GHz vs exported matrix frequency-header mismatch (present in all 400 Chunk 1 + Chunk 2 solves); address remaining simplified H0 physical-model and independent solver caveats separately.
6. Record exact follow-up command, runner/script checksum, run folder, numerical comparisons and evidence ZIP; commit updated ledger alongside per-point QA CSV.

**This ledger is a living audit backlog, not a declaration that 90/100 labels are unusable.**
