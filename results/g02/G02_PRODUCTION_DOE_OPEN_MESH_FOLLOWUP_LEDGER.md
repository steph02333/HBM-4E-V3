# Production DOE — Open Mesh Verification Ledger (Chunk 1–5)

**Last updated:** 2026-11-03 · **Authoritative living GitHub backlog**. Append new Chunk 2/3/4/5 issues to THIS SAME FILE, do not create separate disconnected to-do lists. Frozen 450-point V6.2/V6.3 manifest; never replace an original DOE coordinate because of mesh difficulty.

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

## Chunk 2 — awaiting researcher result archive

Status: **NOT YET RECEIVED**. Append new rows to the same P1/P2/CLEAR categories; preserve original IDs, topology, rho, D/P/H/tox, R3/R5 C coefficients and actual mesh statistics in case-level CSV when available. Avoid overwriting Chunk 1 status.

## Chunk 3/4/5 — awaiting results

Status: NOT YET RUN / RECEIVED.

## Follow-up execution plan (do this AFTER main DOE acquisition, per researcher's preference)

1. Accumulate and audit each 100-point Chunk; append P1/P2 lists without rerunning prior successful solves.
2. Generate deduplicated **targeted follow-up manifest** preserving original DOE IDs and all six original inputs. **P1 first**: try a third genuinely different adaptive level, compare all relevant C coefficients to both historical levels, check Student surface license constraints. If R7 is infeasible or ineffective, use controlled alternate mesh allocation and compare independently. No universal blind R7 assumption.
3. For P2, audit a **representative random / risk-stratified sample**, not necessarily all 63 solely because of arbitrary 10% mesh-growth cutoff. Examine actual mesh distribution and adaptive history; further levels only where needed.
4. Maintain follow-up result statuses `OPEN`, `ATTEMPTED`, `CONFIRMED_WITHIN_POLICY`, `UNRESOLVED`, `BLOCKED_STUDENT_LIMIT`; never call `SOLVED` automatically `PHYSICALLY_VALIDATED`.
5. Before training/reporting as truth: resolve Q3D native 1 GHz vs exported matrix frequency-header mismatch (present in all Chunk 1 solves); address remaining simplified H0 physical-model and independent solver caveats separately.
6. Record exact follow-up command, runner/script checksum, run folder, numerical comparisons and evidence ZIP; commit updated ledger alongside per-point QA CSV.

**This ledger is a living audit backlog, not a declaration that 90/100 labels are unusable.**
