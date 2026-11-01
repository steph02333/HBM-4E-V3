# Feasibility research — Q3D Student 2025 R2, lossy Si TSVs

Date: 2026-11-01. **Research/design decision, not a completed V3 simulation.**

## Bottom line
Q3D's official C/G extractor supports lossy dielectric material physics and net-based multi-conductor extraction, so a meaningful *classical quasi-static lossy-substrate* TSV study is feasible in principle. Student Edition has hard 8000 surface / 64000 volume element caps; previously observed successful and failed meshes demonstrate that full HBM geometry may be too expensive. Q3D does **not** automatically solve MOS carrier accumulation/depletion/inversion vs bias; that belongs to Sentaurus or an independently justified MOS-equivalent treatment. Full independent cross-solver checks require another solver.

## Critical vendor documentation (original citations)
1. Ansys official Q3D C/G solution procedure: https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/Subsystems/Q3DExtractor/Content/Q3D/CapacitanceandConductionSolution.htm
2. Material conductivity thresholds govern whether an object is a conductor/net or dielectric: https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v251/en/Subsystems/Q3DExtractor/Content/Q3D/SettingtheMaterialThresholdinQ3DExtractor.htm
3. Lossy G matrices and admittance reduction Y=G+j omega C: https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/Subsystems/Q3DExtractor/Content/Q3D/TNMatrixReductionIntro.htm
4. Capacitance reference at infinity and float-at-infinity operation: https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/Subsystems/Q3DExtractor/Content/Q3D/TNMatrixReductionFloatingAtInfinity.htm
5. CG surface-charge-density field `SmoothQ` and E fields: https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v251/en/Subsystems/Q3DExtractor/Content/ReportsandPostProc/FieldquantitiesinQ3DExtractor.htm
6. Student limits: https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v251/en/Subsystems/Q3DExtractor/Content/GettingStarted/Q3DStudentLimitations.htm
7. Q3D quasistatic assumptions: https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v261/en/Subsystems/Q3DExtractor/Content/Q3D/TheSolutionProcess.htm
8. Published Wang et al 2014 MOS TSV Q3D comparison: https://www.sciencedirect.com/science/article/pii/S0026269213002553
9. Published Ramadan et al ISCAS 2016 lossy TSV coupling: https://ieeexplore.ieee.org/document/7538951/

## What must be established experimentally before a V3 reference model
**Material-threshold pilot:** set Si epsilon_r=11.7 and conductivity 10 S/m (rho=10 ohm-cm) and explicitly inspect Q3D material thresholds, detected conductors, automatically identified nets, exported C and G matrices. Treat as hypothesis until Q3D logs prove lossy Si contributes as intended. Two further material cases: sigma=1 and 100 S/m. Do not silently manipulate thresholds to force desired interpretation; if no physically credible classification exists, document incompatibility and consider Maxwell or a calibrated external technique.

**Reference/ground pilot:** GSSG with distinct Cu signal/ground nets; evaluate substrate as finite physical material with separately defined backside ohmic contact if defensible. Reference-to-infinity vs local reference is a mathematical boundary choice, not interchangeable. In lossy media use Y matrix for floating reference operations; record original C and G matrices and any reductions.

**Frequency/target pilot:** Y(omega)=G(omega)+j omega C(omega); define the frequency and physical regime. Physical conductivity-to-displacement crossover f_c=sigma/(2 pi epsilon0 11.7) approximately 1.54,15.4,154 GHz for sigma=1,10,100 S/m, respectively (assuming constant epsilon and conductivity; not circuit bandwidth). Do not assert Q3D's extraction frequency is physically meaningful without checking specific Q3D solver implementation.

**Charge audit:** CG field SmoothQ (C/m^2) is available per official Q3D help; investigate integrating signed surface charge over *all* Cu signal/ground/substrate-contact nets and accounting for potential reference at infinity; compare to matrix-predicted conductor charges under 1-V excitations. Reduced-matrix inferred ground charge by definition does not independently prove conservation. Practical field calculator API and Student support need testing.

**Numerical tests:** re-run V2.5/2.7 mesh procedure on V3 finite-conductivity model; test across 3 layout classes x 3 resistivities and severe geometric corners, plus domain/contact sensitivity. Explicitly separate physical die dimensions from artificial exterior boundary reference. Keep untrusted solver outputs quarantined.

## Important limitations
- **Q3D cannot alone validate MOS bias response**; do not imply ordinary conductivity models are semiconductor space-charge solvers. Sentaurus pilot remains necessary under Prof Lim's instructions.
- **Independent solver comparison** needs Maxwell/COMSOL or a second independently formulated solver (not another Q3D run).
- Hard Student mesh cap may prevent full 3x3/high-fidelity package models; smaller physically defensible multiport patterns, matched cross-solver subsets or an unrestricted university license may be necessary.
- Floating conductors and substrate references must not be swapped without admittance-aware reduction and documentation.
- The finite-Si GSSG test should produce useful classical electrostatic/conductive coupling labels if properly verified; exact student build behaviour remains untested.
