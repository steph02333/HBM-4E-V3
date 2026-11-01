# G02 Physical Reference Model V3 — proposed specification

Date: 2026-11-01. **Design specification only; no V3 solves have been performed. G02 remains OPEN.**

## Decision

Stop expanding the nonconductive-silicon V2.7 model to ever-larger physical silicon dimensions. Rebuild a physically meaningful finite-resistivity TSV reference model before formally closing G02. Keep G01 PASS and V2.5/V2.7 cross-mesh findings as *method development evidence*, never as labels for the final reference model.

## Source provenance

1. Prof Yeow Kheng Lim, email 2026-09-26 (in researcher-provided `Mail - Fang Tianchi - Outlook.pdf`): D=3–6 um, P=10–20 um, H=25–50 um, tox=0.1–0.5 um, silicon rho=1/10/100 ohm cm, 10 nominal, compare GSG / GSSG / GSGSG; validate analytical, mesh/consistency and independent solver; only later Sentaurus voltage pilot.
2. Wang et al., *Microelectronics Journal* 45 (2014) 205–210 (in supplied CA2 literature collection): cylindrical/tapered Cu/oxide/Si MOS capacitor; oxide capacitance and depletion physics.
3. Ramadan et al., 2016 paper in supplied CA2 literature: multi-TSV/3x3 coupling; lossy silicon and frequency dependence affect extraction and interpretation.
4. Supplied floating-silicon-interposer paper: substrate reference can radically affect TSV capacitance, but an interposer floating condition is **not** automatically a DRAM/HBM substrate condition.

## Model hierarchy (do not add every possible feature simultaneously)

**V3-A, first physically upgraded Q3D reference**
- Finite-length vertical copper TSVs, concentric SiO2 liner, homogeneous **finite-conductivity silicon** epsilon_r nominal 11.7 (verify adopted dispersive response/frequency).
- D=4 um, P=15 um, H=35 um, tox=0.3 um nominal. Study prescribed parameter envelope later.
- Si rho nominal 10 ohm cm = 10 S/m, compare 1 -> 100 S/m and 100 -> 1 S/m conversions for rho 1 and 100 ohm cm respectively.
- **Explicit substrate boundary/reference**: propose an ohmic backside substrate contact electrode/net as a modelling hypothesis, not a verified HBM4E contact fact. Document how the contact is made, whether Si is conductive volume, where signal return current and charge go, and whether the extracted C is frequency dependent. Compare alternative substrate contact assumptions before locking.
- Distinguish copper TSV ground nets from substrate grounding/contact; merely declaring one TSV `Ground` does not automatically ground all silicon.
- Export full original Maxwell C and G matrices (and AC/frequency response if supported by chosen Q3D setup). Do not interpret `Cii` as oxide-only capacitance nor `-Cij` as frequency-independent mutual in lossy silicon without checking the extraction formulation.
- Frequency and quasi-static validity must be explicit; compare selected frequencies if Q3D models silicon as conductive versus dielectric and discuss how C/G are defined. Avoid simply changing silicon conductivity and assuming the electrostatic C matrix captures semiconductor space charge.

**V3-B, topology families**
- GSG = Ground-Signal-Ground: ONE signal conductor => self/reference capacitance, **no signal-to-signal mutual target**.
- GSSG = Ground-Signal A-Signal B-Ground: TWO signal conductors => mutual A/B is defined.
- GSGSG = Ground-Signal A-Ground-Signal B-Ground: TWO signal conductors; different signal separation and shielding; compare meaningful physical observables, not unnormalized raw entry indexes.
- Start with minimal GSSG and GSGSG after the V3-A net/reference test, then extend to a compact multi-row/3x3 neighborhood if Student Edition resource limits permit. Record which layout and where each conductor is grounded.
- A 3x3 array is optional for the reference model until grounded in literature and mesh feasibility. A 3x3 test may be necessary for surrounding-neighbor impacts, but the new 1D patterns must be spatially mapped consistently first.

**V3-C, controlled complexity (only if quantitative sensitivity warrants)**
- TSV end-cap, pads, hybrid bond/interconnect dielectric, sidewall/taper and silicon depth beyond conductor; study one at a time. Do not introduce unexplained pad dimensions.
- MOS accumulation/depletion/inversion and voltage **belong to later Sentaurus pilot**, not an unverified ad hoc Q3D dielectric modification.

## Numerical verification required on frozen V3 model

1. **Geometry/net audit** via manifests/screenshots, no conductor overlap, explicit reference/charge convention.
2. **Real mesh refinement**, using V2.5/V2.7 successful method as starting point. At least two demonstrably distinct solved meshes; track Cself and Cmutual <1% change at nominal/corners **of every materially distinct layout/material regime**. If Student limit blocks result, archive error, best change and limitations. Q3D per-pass delta alone insufficient.
3. **Symmetry** signed Maxwell Cij approximately Cji, suitable tolerance and units; store full matrices.
4. **Passive matrix** check symmetric-part eigenvalues >= negative numerical tolerance; C/G interpretation and reference treatment documented.
5. **Charge conservation** independent field/terminal check with complete signal/ground/substrate/exterior charges if AEDT exposes them, otherwise show what can be verified and mark full charge check not demonstrated. `Qref=-sum(Qsignals)` inferred algebraically is NOT independent validation; reduced-matrix row sums need not vanish.
6. **Trends** at controlled D, P, tox, H; compare equivalent observable across topologies; qualify exceptions in shielding/grounding.
7. **Domain** vary artificial exterior boundary separately from physical silicon die/contact size. If growing silicon size changes physics, fix a physically justified finite silicon extent or use an effective/infinite substrate treatment. Mesh-check each domain size against distinct meshes and quantify residual impact.
8. **Student resources** retain official surface/volume element limit errors and use feasible mesh policy; do not declare no-convergence = success.

## Proposed immediate execution order

- Check the Q3D treatment of finite-conductivity silicon and C/G extraction; formalize the intended frequency, reference and substrate contact geometry.
- Implement V3-A minimum two-signal, at-least-one-ground physical pilot (e.g. GSSG) under Student budget with nominal rho=10 ohm cm; inspect full matrix and AEDT warnings.
- Validate two distinct meshes on nominal upgraded pilot; then verify GSG and GSGSG.
- Run representative material/layout/corner/physics and exterior-boundary checks with per-geometry cross-mesh verification.
- Complete independent charge/ground evidence or explicitly document that Q3D export cannot support the claimed check.
- **Only after G02 and the later independent-solver level are defensible:** start final DOE/ML labels.

## ML policy
Freeze physical model, net/reference conventions, frequency/observable definition and mesh protocol. All future labels get automatic matrix/solve/quality checks; independent mesh/domain checks on representative corners and suspicious cases. Label rows contain topology and silicon regime. Do not silently merge one-signal GSG with two-signal mutual targets; missing mutual is **not a zero**.
