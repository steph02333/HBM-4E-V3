# 76 original DOE points — batched, decouplable mesh-remediation experiment plan (2026-11-04)

## Fixed cohort, no dropped data
Use original frozen V6.3 physical coordinates and labels without resampling or altering original solved outputs. Original 450-row unified audit: **75 paired DOE points with worst R3/R5 relevant-C relative disagreement ≥2%**, and **one separate Student license-failed point, DOE0447** (8030/8340 actual 3D surface elements, greater than 8000 Student cap). Goal is to recover as many of all 76 as feasible, not delete hard ML labels.

**Operational target**: <2% consistency across truly distinct adequately resolved mesh solutions for every relevant coefficient (GSG CAA, GSSG/GSGSG CAA/CBB/|CAB|). This is not proof of absolute error <2%, and professor's stronger ~1% mesh refinement demonstration remains separate.

## One batch, multiple independent policy arms: 23+52+1 design

**Batch A: 23-case stratified method comparison**. Include **all 11 current ≥5% discrepancy points** plus **12 2–5% points** sampled deterministically to cover every represented topology × resistivity problem stratum (7), additional high exported-mesh and low exported-mesh stress cases. Frozen selected case IDs:

DOE0240, DOE0380, DOE0407, DOE0365, DOE0184, DOE0319, DOE0361, DOE0421, DOE0050, DOE0422, DOE0406, DOE0047, DOE0121, DOE0062, DOE0272, DOE0084, DOE0057, DOE0373, DOE0104, DOE0402, DOE0019, DOE0159, DOE0038.

For each, run **two additional independent meshes**, each once, reusing original R3 and R5 as historical anchors: nominal **46 new Q3D solves**. Methods to implement and verify in PyAEDT before execution:

- **M_A — globally different adaptive policy**: change controlled percent-refinement / target mesh policy to produce a genuinely different realized surface-element distribution without blindly increasing MaxPass or assuming R7 is finer. Preserve physical geometry, boundary nets, materials, frequency setup and Student surface budget.
- **M_B — oxide/interface-targeted policy**: change ONLY targeted oxide/TSV sidewall mesh allocation / surface seed family, retaining physics and other mesh controls. Verify actual realized element differentiation and oxide-interface convergence, so comparison can isolate the mesh-allocation effect.
- Both arms MUST emit actual Student license-checked 3D surface counts where available, exported total-element counts separately, adaptive history, net definitions, all signed C terms, solver outcome, native vs export-frequency provenance, original DOE ID, exact policy hash and project path. A changed parameter without a changed realized mesh is NOT independent validation.
- Do not assume all 46 solve attempts feasible under Student limit. Reserve a short smoke test for first two contrasting cases to stop policy-level session/licensing faults early, then continue the whole batch automatically on success. This is one planned multi-case campaign with fail-fast checkpoints, not hand-running one DOE at a time.

**Separate CAP_A lane: DOE0447**: one modified license-safe mesh method producing **two distinct solved meshes** (R3/R5 analogues) = **2 attempts** initially. Coarser/redistributed surface seeding with same frozen physical coordinate. Never run raw R7 on this proven cap failure.

**Batch B: remaining 52 ≥2% points**: after diagnosing Batch A, select arm **per risk stratum** (not one universal policy) using worst coefficient reduction, cross-mesh agreement, realized mesh budget and solver success. Budget **52 new first-attempt solves**, one independent third mesh per original DOE point; cases failing confirmation get a further run only where warranted. Exactly 52 original IDs remain after selected 23, no overlap.

## Budget and interpretation
- Baseline scheduled **46 + 2 + 52 = 100 new Q3D solve attempts**, on **76 original DOE points**. This is a *planning minimum*, not a promised pass rate or a cap on additional validation.
- Outcomes per DOE: `SOLVER_FAILURE`, `LICENSE_BLOCKED`, `NUMERICALLY_UNRESOLVED`, `THIRD_MESH_INCONSISTENT`, `PROVISIONAL_C_LT_2PCT`, `STRONG_1PCT_DEMO` (only with appropriate evidence). Keep all evidence regardless of outcome.
- Compare M_A vs M_B fairly **within the same 23 DOE points**; compute per-arm median/max C disagreements, % resolving each component, actual surface and total mesh, runtime, failed solves, topology/material subgroup effects. Decouple by coefficient, rho, topology, mesh budget, and physical geometry *after* the batch; no Simpson's-paradox shortcuts.
- Prefer two genuinely different adequately resolved meshes agreeing and third mesh being consistent; if R3/R5 and M_A/M_B don't exhibit stable refinement trend, do not choose whichever output happens to be <2% by arbitrary reference pairing or average discordant labels.
- Pilot arm definitions, exact policy parameters and batch-safe runner **are not implemented by merely writing this research plan**. Must modify/validate existing PyAEDT runner and checkpoint/resume logic before giving user a runnable command.

## Follow-through
Working manifest: `G02_V63_76POINT_BATCH_EXPERIMENT_MANIFEST_20261104.csv` (76 rows, all original geometric inputs, error stats, and assignment to Batch A, Batch B, CAP_A), generated locally. After batch A, record exact signed C comparisons, adaptive history, surface-license failures and policy-effect attribution, then update the same 76-point ledger and choose Batch B policies. Preserve professor-oriented previous 1%-P1 audits.
