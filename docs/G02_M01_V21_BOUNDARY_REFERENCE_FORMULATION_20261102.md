# G02 M01 v2.1 boundary/reference audit (2026-11-02)

**Status: CROSS-SOLVER PHYSICS VALIDATION OPEN.**

Direct native file evidence: Q3D DOM10_M25_R18.aedt has V3_Setup Matrix, AdaptiveFreq=1000MHz, ReduceMatrix/Original; SignalNet IDs 1/2 (SIG_A/SIG_B), GroundNet 0/3 (GROUND_L/R), ConductorThreshold=10000. Maxwell M01_GSSG_Maxwell.aedt has AC Conduction with signal IDs1/2 and ground IDs0/3. Both Si volume x=-49.8..49.8um y=-27.3..27.3um z=0..35um, epsilon=11.7 sigma=10S/m, no explicit substrate ohmic contact. Native Q3D saved solution is 1GHz; Maxwell pass8 is 1GHz.

**Important external-boundary formulation difference from official Ansys documentation:**
- Q3D capacitance/conductance surface-integral formulation assumes potential goes to zero at infinity unless its Floating at Infinity reduction modifies the setup. https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/Subsystems/Q3DExtractor/Content/Q3D/FormulationoftheCapacitanceConductanceSolution.htm
- Maxwell 3D AC Conduction's default external boundaries are Neumann (zero normal current/flux; tangential E,J) while interior interfaces are natural (continuous). https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v261/en/Subsystems/Maxwell/Content/Maxwell/ACConductionBoundaries.htm
These formulations are not automatically equivalent merely because Si geometries match. Zero potential at infinity is **not the same as grounding all Si box faces**; artificially assigning Si=0V would be a NEW physical model, not an apples-to-apples correction.

Q3D at nominal: CAA35.481712fF, CAB-11.618261fF, GAA0.061592086mS, GAB-0.016418221mS. Maxwell pass8 CAA36.474fF CAB-12.183fF GAA0.069444mS GAB-0.020013mS. Differences +2.80/+4.86/+12.75/+21.90% magnitude. Maxwell C/G pass6->8 changed <=0.16%, but native loss-error=2.0011% > target1%. Fresh whole-object vs top-face voltage experiment did not materially change C/G. Default boundary formulation is now a leading **untested** hypothesis for differences; it is NOT a proven quantitative root cause. Matrix conversion and units already audited.

**Decision:** NO more blind surface sliders or terminal-scope sweeps. Do not apply 0V on external Si to force agreement. Before one targeted numerical experiment, determine Q3D open-space dielectric exterior versus Maxwell modeled outer surfaces and inspect potential/current return path, full-port matrix conventions; if needed design one controlled lateral margin sensitivity in a copy, explicitly noting it also changes finite Si body physics. An actually identical physical closed BVP across solvers may require independently specified boundary/reference model and could require redesign on both sides, not just Maxwell.

Stage3 tox=.5/sigma1 deferred until apples-to-apples assumptions are explicit. C-focused DOE planning permitted provisionally with remaining Q3D numerical and physical gaps declared. Technical report artifact in conversation: G02_M01_V21_BOUNDARY_REFERENCE_DECISION.md.

Likely Windows: C:\CA2 result V2\02_numerical_convergence\V3_conductive_silicon\run_20261102_164954_6a5874\ansys_projects\DOM10_M25_R18.aedt and sibling .aedtresults. Maxwell C:\CA2 result V2\02_numerical_convergence\V3_conductive_silicon\Maxwell_M01_BUILD06_20261102_175348\M01_GSSG_Maxwell.aedt.