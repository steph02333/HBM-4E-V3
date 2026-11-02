# Native Q3D exact-case frequency and reference audit — 2026-11-02

User supplied `DOM10_M25_R18.aedt` (ASCII AEDT project) plus `DOM10_M25_R18.aedtresults.zip` from local `run_20261102_164954_6a5874/ansys_projects`. These are the previously missing original project and solution files.

## Native evidence
- Project native `AnalysisSetup/SolveSetups/V3_Setup` is Q3D `SetupType='Matrix'`, `AdaptiveFreq='1000MHz'`, Cap higher accuracy, target error 0.5%.
- Results zip contains `Design_a5e3f73.asol`; inside the **saved LastAdaptive solution definition**, `SolutionName='LastAdaptive'`, `SolutionID=32`, `Frequencies(1000000000)`; inside `AdaptivePass` solution definition, `SolutionID=33`, `Frequencies(1000000000)` also. These are native saved-solution metadata, stronger than setup readback.
- Results ZIP includes native C/G data `DV73_SOL32_MCAP0_V0.sd` and `DV73_SOL32_MCOND0_V0.sd`, plus six adaptive-pass MCAP and MCOND data files each. Matrix export output previously carried incorrect 1Hz/1kHz headers for apparently identical numeric matrices. **Actual solved Q3D solution at 1GHz CONFIRMED**. Still verify an export/readout mapped to the saved solution if strict end-to-end matrix trace is needed; we have not decoded binary .sd matrices.
- `asol` CapConv: six passes, final `delta=0.117615` (%) versus target `0.5` (%), 2662 triangles.
- Native boundaries: Cu `GROUND_L` object 108 GroundNet ID0, `SIG_A` object139 SignalNet ID1, `SIG_B` object170 SignalNet ID2, `GROUND_R` object201 GroundNet ID3. `ConductorThreshold=10000` (Si10S/m remains lossy dielectric, not reclassified as a conductor).
- Native material `V3_SI_fa29d58` relative eps 11.7 and conductivity 10 (S/m); native oxide eps 3.9, sigma 0. Core geometry reference 4um diameter, 15um pitch, H35um, tox0.3um, finite silicon margin25um.
- Q3D exported CG Fields shows 1V on SIG_A and 0V on SIG_B for *field visualization*, not proof that SIG_B is permanently GroundNet: Boundaries show both are SignalNet.

## Current GO/NO GO
Q3D saved solution frequency gate: **PASS**. Geometry/material/SignalNet/GroundNet nominal matching: **strong evidence**. Remaining: end-to-end exact saved result matrix readback if needed; compare silicon extent and *effective outer boundary and current return* between Q3D GroundNet and Maxwell voltage electrode Matrix; ensure same reduction/reference and G=Re(Y) interpretation. Only then claim apples-to-apples cross-solver validation. Maxwell 8-pass pass8 has 51308 tets and stable matrix entries but native loss-error 2.0011% >1% target; remain transparent.
