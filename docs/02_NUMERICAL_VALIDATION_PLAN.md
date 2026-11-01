# G02 — Numerical Convergence and Physical Consistency (Plan v1)

**Status:** OPEN / NOT YET RUN. **Date:** 2026-11-01. Follows G01 PASS (ideal coax only).

## Purpose

Prof Lim requires numerical reliability of the **multi-conductor reference EM model**, not just a single analytical coax cylinder. Before any DOE or ML, verify Cself and Cmutual under additional adaptive refinement, capacitance matrix symmetry/passivity/charge bookkeeping, geometry trends, and outer-domain sensitivity. No legacy CA2 solver labels are reused.

## Step 0 — freeze a genuinely multi-conductor test fixture

Draft selection for review: central signal victim (V), at least one independent signal aggressor (A), and a separate ground/reference conductor in a small Cu TSV / SiO2 liner / finite silicon substrate structure. The final target is a defensible 3x3 local array with published signal/ground topology, not necessarily one arbitrary array. Prof Lim later requests explicit GSG, GSSG, GSGSG studies. They are different **net layouts**, not labels to assign without confirming the actual conductor arrangement.

**Key conditions to document BEFORE code execution:** D, P, H, tox, pad presence/absence, silicon conductivity/permittivity, material frequency dependence, silicon body reference/return path, whether substrate is a conductive net or finite-conductivity material, dielectric domain boundaries, ground net placement, solver extraction convention. Suggested nominal engineering starting point from Prof Lim: D=4 µm, P=15 µm, H=35 µm, tox=0.3 µm, silicon resistivity 10 ohm-cm (conductivity 10 S/m). These are **proposed nominal choices**, not published exact HBM4E specifications.

A simplistic Cu/SiO2/outer Cu coax shield would suppress TSV-to-TSV coupling; do **not** reuse the G01 fixture for G02 mutual tests.

## Step 1 — single frozen nominal geometry and mesh pass history

- Export full original Maxwell C matrix in fF with net names; record ground/reference conventions.
- Export each adaptive pass / convergence report and mesh statistics.
- Track positive diagonal C(V,V), signed off-diagonal C(V,A), and magnitude |C(V,A)|; do **not** conflate mutual magnitude with signed Maxwell coefficients.
- Change solver mesh/refinement settings deliberately and independently (normal vs stricter), not just stop at the first below-target adaptive pass.
- Compare successive stricter solutions of self/mutual using absolute relative change, target <1% for both. If mutual is very close to zero, use a declared absolute fF tolerance as well to avoid unstable relative percentages.
- Repeat on corner structures after nominal passes, especially thin oxide, close pitch, tall TSV.

## Step 2 — matrix QA

- Validate numerical symmetry: norm(C-C^T), with stated denominator and threshold.
- Maxwell convention check: diagonal >=0; signal-signal off-diagonals generally <=0 for ideal electrostatics (check actual solver convention).
- Energy/passivity: symmetrized matrix positive semidefinite within a numerical tolerance appropriate to its scale; record eigenvalues.
- Reference/ground: row sums need **not** be zero for a reduced matrix when ground is eliminated. Determine charge balance by applying V vector and accounting for grounded terminal and exterior/reference flux; do not assert row-sum=0 without stating all boundary/reference conductors.
- Archive raw matrix unchanged alongside derived QA results.

## Step 3 — trend checks (controlled one-factor comparisons)

Use valid dimensions within Lim's ranges:
- P increasing at fixed D,H,tox: expect nearest-neighbor |Cmutual| generally to decrease, not unconditional monotonicity in every multiport arrangement.
- D increasing at fixed P,H,tox: examine Cself and |Cmutual| with fixed reference.
- tox increasing at fixed D,P,H: examine cap changes, recognizing different response of substrate and mutual terms.
Always record deviations instead of forcing expected trends.

## Step 4 — domain sensitivity

Hold all conductor dimensions/ground conditions fixed; enlarge finite silicon lateral margins and outer dielectric boundaries (proposed x1, x1.5, x2). Record Cself and Cmutual. Define tolerance before running (initial target 1% for both, with near-zero safeguard). Beware that changing a *physical* silicon body or grounded electrode size is not the same as moving an artificial open boundary.

## Evidence + pass gate

Store experiments under `C:\CA2 result V2\02_numerical_convergence\` with unique case IDs, configuration JSON, solver/pass logs, raw C/G matrix, screenshots of geometry and net assignments, QA CSV and summary figures. Commit small scripts, configs, reviewed tables and report to this repo.

**G02 PASS only if:** the intended electrical reference/geometry is documented, numerical meshes are stable for relevant self and mutual C, physical/mathematical sanity checks pass or discrepancies are physically explained, and domain effects are bounded. If the final physical topology/materials change later, affected G02 tests must be rerun.

**Immediate action:** produce/inspect a frozen multi-TSV geometry-and-net specification (G02-MODEL-01), then generate a new parametrized Q3D script. No full DOE or ML.

## 2026-11-01 — Student-edition mesh-budget protocol (confirmed with official Ansys documentation)

Researcher's installed solver: **Ansys Electronics Desktop Student 2025 R2, Q3D**, Python 3.13, PyAEDT 1.9.0.

Official Student limits (Ansys Electronics Desktop Student product restrictions): **64,000 3D volume elements, 8,000 3D surface elements, 2,000 2D triangles; maximum 4 HPC cores**. Source: https://ansys.synopsys.com/academic/students/ansys-electronics-desktop-student . These are product limits, **not** convergence results.

### Staged protocol (adaptive coverage rather than arbitrary case count)

1. **Feasibility pilot:** start with a minimal 2-signal + ground reference fixture and modest mesh settings. This is a resource/capability test only, not a substitute for representative multi-TSV validation.
2. **Freeze target topology:** validate the actual relevant multi-TSV topology once a feasible geometry and reference path have been demonstrated; state where topology simplification changes physics.
3. **Progressive refinement:** progressively tighten Q3D capacitance error and/or adaptive pass budget. Archive each separate solved state, its matrix, surface and volume mesh statistics, pass history and AEDT message log. Early runs should target a buffer below the official caps (e.g. 70–80% is a **planning heuristic**, not a vendor threshold).
4. **Stop rules:** stop further refinement at validated <1% self and mutual change; alternatively stop at verified license element cap or solver resource failure. Distinguish `LICENSE_MESH_LIMIT`, `FAILED_OTHER`, `CONVERGED`, `NOT_CONVERGED_WITHIN_AVAILABLE_BUDGET`.
5. **Numerical error:** track changes under at least two progressively stricter reproducible solutions; Q3D internal adaptive delta alone is not independent mesh validation. A relative test on near-zero mutual terms requires a preregistered absolute-fF threshold.
6. **Consistency:** complete symmetry, energy/passivity, physically consistent terminal charge accounting, one-factor trend checks and outer-domain size sensitivity even if the mesh limit blocks <1% refinement.
7. **Corner coverage:** repeat tighter mesh checks on geometrically stressful cases (small pitch, thin liner, tall TSV) to avoid extrapolating nominal convergence to every geometry.
8. **Report** both achieved discretization stability and unresolved uncertainty. If <1% cannot be demonstrated, describe the Student edition's cap as a **documented limitation**; do not report an unpassed numerical criterion as validated or call it an error estimate without an appropriate convergence study.
9. **Impact on ML:** final reference model cannot be treated as quantitatively high fidelity beyond demonstrated convergence. If needed, simplify the physical domain with justification, license academic full AEDT, or narrow claims and propagate estimated label uncertainty.

**No experimental results from this protocol have yet been collected; G02 remains OPEN.**

## 2026-11-01 — Corrective runner V2 after 18-case audit
A new local script artifact `G02_validation_v2.py` was prepared for download in the associated ChatGPT conversation. Its Python syntax and dry-run plan have been checked; **actual AEDT execution is not yet verified**. The code is not yet committed to GitHub, so do not mistake this note for a repository script update.

Design: explicit Q3D `assign_length_mesh(assignment=[Cu and liner objects], inside_selection=False, maximum_length=...)` with decreasing length; distinct fresh projects per case, mesh-statistics evidence; separate 3-TSV G-S-S nominal pilot and broader mesh, pitch, diameter, liner, domain and stressed-corner cases. Each failure is recorded per case without terminating the overall campaign. For ordered mesh/domain escalations, after three consecutive solver failures, more aggressive levels are skipped; independent test groups continue. The 1% requirement is checked only after authentic differences in actual mesh counts are confirmed. Domain sensitivity distinguishes finite physical silicon geometry and artificial truncation; reference charge closure computed from a reduced Maxwell matrix is algebraic bookkeeping, **not** an independent physical charge-conservation proof. A physical silicon-resistivity model and independent charge/flux verification remain required before G02 closes.

Suggested run commands on user's Windows system:
- `py -3.13 "C:\暂时下载\G02_validation_v2.py" --mode pilot --student --aedt-version 2025.2`
- After reviewing pilot: `py -3.13 "C:\暂时下载\G02_validation_v2.py" --mode full --student --aedt-version 2025.2`

All results: `C:\CA2 result V2\02_numerical_convergence\runs\<run_id>\G02_results_bundle.zip`.

Reference: PyAEDT length-mesh API https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_length_mesh.html
