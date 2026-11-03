# G02 V6.3 — Production DOE Chunk 2 audit (2026-11-04)

Uploaded real archive: `G02_V63_H0_PRODUCTION_DOE_results_bundle.zip`. SHA256 `47d27ce553030ff08e69c62fc72daa251563d6d7c8f4a6434073645f9e4c23df`. The original raw ZIP remains with the researcher, not in this GitHub repository.

**Results:** Chunk 2 DOE IDs verified against frozen V6.3 chunk map. Exactly 100 distinct sampled DOE geometries, each with R3/R5, **200/200 Q3D successful solves**. 66/100 DOE points show all applicable CAA/CBB/|CAB| differences below 1%; **34/100 need priority additional mesh verification** because at least one C difference is >=1%. Median worst coefficient difference 0.4974%; 90th percentile 2.6716%; maximum 4.9242% (DOE0092, mutual). Median total-mesh growth 5.30%.

**Mesh diversity diagnostic, not a professor criterion:** Of the 66 C-under-1% DOE points, 57 have total mesh growth under 10% and 9 reach 10% growth or more. The arbitrary 10% heuristic is not a mandatory gate for ML label usefulness and does not establish physical accuracy. All 100 raw points are retained in the frozen DOE.

The 34 high-delta IDs, worst coefficient, exact deviation and mesh growth, as well as 57 lower-priority audit candidate IDs and 9 extra-screen-clear IDs, are now appended to the **same** [living mesh follow-up ledger](G02_PRODUCTION_DOE_OPEN_MESH_FOLLOWUP_LEDGER.md); no separate backlog.

**Cumulative Chunk 1+2:** 200/450 DOE points acquired, 400/400 solves, 139/200 pairs show <1% all relevant C coefficients, 61/200 do not. The 10%-mesh diagnostic categories total 120 P2 plus 19 additional-screen-clear among the 139 C-under-1% points.

All 200 new result JSON records report no CG adaptive nonconvergence warning, matching expected signal nets and positive C eigenvalues. All 200 text exports again have a frequency header inconsistent with the requested native 1000MHz setup; this unresolved **frequency provenance** must be audited separately. This reduced H0 conductive-silicon model is not a complete biased HBM4 physical model.

Paired case-level local artifacts created: `G02_V63_chunk2_100points_mesh_audit.csv` (100 rows, including original geometry, signed C, mesh and numerical QA) and `G02_V63_chunk2_200solve_signed_matrices.csv` (200 rows); the full artifacts are retained locally and are not claimed committed. See [stratum summary CSV](G02_V63_CHUNK2_summary_by_stratum_20261104.csv) for all nine topology x resistivity groups.

**Next action:** Continue production chunks 3–5 without changing the 450-point manifest. After acquisition, generate a deduplicated targeted follow-up run plan, prioritizing all P1; P2 sampled or risk-triggered rather than rejected. Keep solver completion, professor's ~1% C refinement screen, and physical validation as different evidence categories.
