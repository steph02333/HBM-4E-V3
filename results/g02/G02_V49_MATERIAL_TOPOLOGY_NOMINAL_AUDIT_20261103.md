# G02 V4.9 material-topology nominal mesh audit — 2026-11-03

Evidence: researcher-uploaded `G02_V49_H0_material_topology_results_bundle.zip`, including 8 result.json, CG exports, CG convergence/profile, mesh_stats and runner.log. This ZIP originates from a **subsequent successful rerun** (runner log starts 11:36:41), after an earlier user console line at 11:35 reported a PyAEDT `'NoneType' object is not iterable` error while connecting to an active desktop session. No such error appears in this finished rerun's runner.log. Do not confuse first session-connect failure with successful Q3D solving.

## Results
All 8/8 status `SOLVED_UNVERIFIED_PHYSICS`; all original matrix net lists agree with topology; matrices symmetric and positive C/G eigenvalues; no CG adaptive nonconvergence warnings recorded. Frequency setup requested 1000MHz, but text exporter still labels 1kHz and `export_frequency_matches_request=false`—historical unresolved provenance issue.

| Topology | sigma S/m | rho ohm-cm | total elements R12/R18 | CG last triangles R12/R18 | Max paired C difference |
|---|---:|---:|---|---|---:|
| GSG |1|100|3212 / 3648|2102 / 2320|0.06957% CAA |
| GSG |100|1|3132 / 3628|2056 / 2304|0.07905% CAA |
| GSGSG |1|100|2388 / 2664|1698 / 1836|0.15895% abs CAB |
| GSGSG |100|1|3492 / 14616|2242 / 7828|5.89327% abs CAB |

Comparisons use denominator R18; GSG C_AB is undefined (one signal).

For GSGSG sigma100, signed C R12: [[41.63627457,-10.07782443],[-10.07782443,41.67416219]] fF; R18 [[42.36184313,-9.51696367],[-9.51696367,42.34039882]] fF. CAA pair deviation1.71279%, CBB1.57352%, |CAB|5.89327%, **FAIL predeclared 1% paired-mesh gate**. G_AB also changes sign from -0.0069370mS (R12) to +0.00326094mS (R18), and G matrix approaches singularity for R12. The R18 converged in 11 adaptive passes with final internal delta0.45516% under 0.5% target, versus R12 5 passes final0.05029%, illustrating that internal convergence does not ensure cross-strategy consistency. R18 final CG triangles 7828 near Student 8000 surface-triangle cap (although this count is from CG convergence report and not a certified license counter); further global refinement may fail.

**Decision:** Missing four material×topology nominal cells now ALL SIMULATED. Three of four paired-mesh C consistency PASS; GSGSG sigma100 (rho1) INCONCLUSIVE/FAIL <1% gate. Do not label it mesh-qualified, do not call all nine strata qualified, and do not silently include this high-risk region in final ML training without QA flag. Resistivity sigma100 (rho1) and topology GSGSG interaction merits a targeted re-check only if aiming to include this stratum. Avoid blindly trying R20 higher global refinement near Student limit. Potential workarounds: a bounded one-case mesh strategy with local refinement or license-compatible iteration, plus read-only native geometry/material/mesh checks; if no independent stable pair, restrict that stratum from initial C-only pilot, preserving the professor-suggested full-six-variable scope as a phase-II goal. Other three cells should not be rerun.

## Implications
Complete 3×3 resistivity/topology nominal *coverage* (existing V39 GSSG sigma1/10/100 and V4.8 GSG/GSGSG sigma10 + V4.9 above), but not global qualification. Q3D H0 homogeneous lossy silicon remains model-specific, with Maxwell Neumann-vs-infinity BVP mismatch, global independent charge closure and true boundary independence unverified and documented; no new Maxwell campaign justified. For DOE start with stratified C-only pilot, R12/R18 repeat-geometry considered ONE sample, GSG 1x1 target separate from GSSG/GSGSG 2x2; quarantine high-risk GSGSG sigma100 regime until resolved.

## Windows runner and files
Source `G02_V49_H0_missing_material_topology.py` supplied in user project conversation. Output archived by user as `G02_V49_H0_material_topology_results_bundle.zip`. Original root `C:\CA2 result V2\02_numerical_convergence\V3_conductive_silicon\run_<timestamp>_<id>\` with corresponding local AEDT projects. Do not claim raw binary projects are in GitHub.
