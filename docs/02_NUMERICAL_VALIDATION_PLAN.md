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
