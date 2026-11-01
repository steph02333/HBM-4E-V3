# G02 final reference-model qualification — DOE readiness gate

Date: 2026-11-01. **PLAN, NOT SIMULATION RESULTS. G02 OPEN.**

## Governing decision
Changing silicon conductivity, TSV signal/ground geometry, backside/substrate reference, physical die extent, or terminal definitions invalidates extrapolating V2.5/V2.7 numerical convergence to the final reference model. Preserve V2.5/V2.7 as automation/method verification, not final ML labels. G01 ideal Cu/SiO2 analytic benchmark remains passed.

## Authoritative user-provided specification
Prof Lim, Sep 26, 2026: D=3–6 um, pitch 10–20 um, height 25–50 um, liner 0.1–0.5 um, Si resistivity 1/10/100 ohm-cm (10 nominal); topology GSG/GSSG/GSGSG. Mesh stability self+mutual <~1%, symmetry, physical trends, conservation/passivity, adequate boundaries, independent solver check later, Sentaurus voltage pilot after physical Q3D model.

## Mandatory model-freeze gates before validation solves
- Explicit geometry/units: copper radius, SiO2 liner, TSV termination/end faces, pad and bond omission rationale, silicon thickness and lateral extent.
- Define Q3D nets: GSG has only one signal (no signal-signal mutual label); GSSG and GSGSG have two signals; physically specify which conductors are ground.
- Specify substrate contact/return/reference. Ground TSV does not by itself ground semiconductor bulk. State whether substrate is a lossy dielectric and how charge returns. Separate actual die boundary from artificial solver boundary.
- Check Q3D lossy silicon physics: epsilon_r approximately 11.7 with conductivity = 100/10/1 S/m for rho 1/10/100 ohm-cm; review C/G matrix definitions, frequency/dependency and whether the chosen target is well-defined. An ideal-dielectric simulation does not validate lossy silicon.
- Fix all observation definitions: Cii signed Maxwell diagonal, -Cij coupling magnitude for i!=j, separate grounded and substrate terminal quantities, optional G/frequency.
- Freeze script SHA, AEDT release, PyAEDT release, mesh policy, exception handling, output schema and project identity.

## Validation coverage (initial adaptive allocation, no upper bound)
1. 9 nominal physical cases (3 topologies × 3 resistivities), each with independent cross-mesh evidence.
2. 18–27 strategically selected coupled geometry extremes across physical topology families; cover largest D/smallest P/thinnest liner/tallest H and weak-coupling opposite corner, plus mixed extrema.
3. 12–24 controlled one-factor D/P/H/tox trends, with mesh-qualified values.
4. 6–12 substrate-contact/reference alternatives and domain tests; isolate moving artificial exterior boundaries versus changing the actual silicon body/contact.
5. Additional cases triggered by unexpectedly large mesh variation, topology/material regime changes, weak mutual signal, failed trend, passivity issue, or Student mesh ceiling.
Cases can serve multiple categories; do not double count duplicated physical simulations. An exhaustive 3^4 × 3 × 3 = 729-grid is neither required nor an appropriate starting mesh-validation program.

## Each mesh-qualified geometry
- At least two *genuinely distinct successful mesh resolutions*; preferably 3 where mesh count increases and small deltas could be accidental. Record mesh statistics, *surface* count relative to Student 8000 limit, total elements, pass profiles, capacitance and conductance matrices. Internal adaptive delta alone not independent proof.
- Relative cross-solution change <1% on each relevant Cii and coupling |Cij|; predeclare absolute-fF rule for near-zero coupling. Re-run after relevant physical model change.
- Check symmetry, symmetric-part eigenvalues/energy positivity, sign convention, matrix units, setup convergence and other solver warnings.
- For charge: provide independent terminal/ground/exterior field charge or flux check where supported; simply infer Qground from minus signal sum is algebraic, not independent conservation validation.
- Domain: test physically justified finite body size separately from artificial boundary distance; require stabilized observables or explicitly state unresolved systematic domain uncertainty.
- On confirmed Student resource failures, retain case-specific AEDT messages and upper feasible mesh. Never relabel an unconverged case PASS.

## Final ML qualification
- Freeze material/topology/reference model and target observables.
- Show representative corner mesh/domain validation **within every materially distinct structure family**.
- Define physical admissibility + resource feasibility region; exclude or flag conditions outside Student resource envelope.
- Per dataset run: validate geometry, net labels, solve status, pass convergence, unit/matrix consistency, symmetry, passivity, mesh/resource stats, provenance and export completeness; quarantine failures.
- Audit additional DOE cases through independent mesh reruns at high-risk corners and anomalies. Sample until observed failure rate and learning-curve behaviour justify adequacy, not a predetermined sample count.
- Build train-only adaptive designs after fixing a holdout strategy; never use previous CA2 labels as V3 references.

## Non-substitutability
No finite number of modeled corners can guarantee an arbitrary future DOE outside validated range. Every substantial physical-model change must trigger impact assessment and affected revalidation. Independent solver cross-check (Prof Lim Level 3) and semiconductor-bias Sentaurus pilot remain separate gates.
