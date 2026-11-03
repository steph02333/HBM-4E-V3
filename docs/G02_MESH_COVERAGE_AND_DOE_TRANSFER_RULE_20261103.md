# G02 Mesh Evidence Coverage and DOE Transfer Rule — 2026-11-03

Reviewed directly: uploaded V39, V41, V43–V49 result ZIPs and existing GitHub audits. This document separates a **tested representative point** from a **qualified continuous design-space region**. All are simplified H0/no-explicit-substrate-contact finite conductive Si, requested 1 GHz, C-only objective. Actual DOE label QA and representative independent mesh audits are different.

## Coverage by material × topology
Resistivity rho 1/10/100 ohm-cm corresponds to sigma 100/10/1 S/m.

| Topology | rho 1 (sigma100) | rho 10 (sigma10) | rho 100 (sigma1) |
|---|---|---|---|
| GSG | V49 nominal paired adaptive PASS 0.079% CAA | V48 nominal paired PASS 0.026% CAA | V49 nominal paired PASS 0.070% CAA |
| GSSG | V39 nominal adaptive C stable; cross-strategy C up to ~0.8%; no sigma100 geometric corners | V39 nominal local strategy C <0.37%, V47 four high-risk corners paired C max 0.412% | V41 nominal local oxide L8 vs baseline R18 |CAB| drift ~1.51% (L12 vs L8 ~1.20%); OPEN for cross-strategy criterion |
| GSGSG | V49 nominal paired R12/R18 **FAIL** CAA 1.71%, CBB 1.57%, |CAB| 5.893%; R18 CG last triangles 7828 of ~8000 Student cap | V48 nominal pair PASS max |CAB|0.547%; no corners | V49 nominal paired PASS max |CAB|0.159%; no corners |

ALL nine nominal cells have been **simulated** but not all **mesh-qualified**. The sigma10 GSSG V47 corners do not verify sigma1/sigma100 or GSG/GSGSG corners. The sigma1 GSSG nominal adaptive R16/R18 delta 0.027% does not settle local-oxide discrepancy; identical L8/L5 meshes cannot support further convergence.

## Scientific answer to extrapolation question
A representative geometry is useful only insofar as a proposed DOE point is **inside a defined and sampled topology × conductivity × geometric envelope** and the dominant mesh-risk variables are comparable. There is no theorem that nominal mesh settings converge across P=10..20, tox=0.1..0.5, H=25..50, D=3..6. High-risk indicators include thin oxide, high aspect ratio H/tox, small liner-to-liner clearance P-D-2tox, increased number of conductors, lossy-Si material regime, and near-zero coupling terms. Use the actual C errors and Student surface resource indicators to calibrate, not a fixed universal threshold of normalized distance.

**Proposed bounded next campaign (not yet executed):**
- Priority A: re-evaluate two anomalous nominal cells with an actually distinct mesh approach (GSGSG sigma100 and GSSG sigma1 local oxide). Cap 2 additional attempts per anomaly, do not blindly demand global R20 near Student cap. On resource/unchanged-mesh failures archive limitation, quarantine.
- Priority B: representative **geometric sentinel** audits, at least one strong/weak coupling extreme per physically distinct topology/material group not already covered; start 4 strategically chosen cases: GSGSG sigma10 strong corner, GSGSG sigma1 weak or strong corner, GSG sigma100 strong corner, GSSG sigma100 strong corner (the two sigma extremes across topology are more informative than repeating sigma10 GSSG). Each 2 distinct meshes, so ~8 additional solves; after inspecting flags expand selectively. Include GSGSG sigma100 extreme only if nominal mesh issue resolved. Remaining groups are not globally qualified without further coverage.
- Each sentinel must compare same geometry/material/reference using genuinely different mesh statistics and full signed C, report both self and mutual errors, convergence pass logs, Student surface cap. <1% pair changes is empirical consistency, not proof of continuum discretization accuracy; choose additional orthogonal local oxide refinement where feasible.

## DOE candidate-to-evidence distance/gating
For each candidate x=(D,P,H,tox,rho,topology):
- exact match topology & rho stratum mandatory for nearest evidence; do not interpolate topology as an ordinal dimension or rho as if a mesh-refinement proof were transferable.
- normalize geometry as u=((D-3)/3,(P-10)/10,(H-25)/25,(tox-.1)/.4).
- compare to verified representatives from SAME stratum using max absolute normalized-coordinate distance, optionally Euclidean. This is a **triage score** only; no 0.25 radius can rigorously certify convergence.
- require that high-risk feature descriptors (liner gap g=P-D-2tox, aspect ratio H/tox, TSV count, expected coupling) be **bracketed** by mesh-checked representatives; a single nominal point cannot bracket the 4D space.
- candidate with nearby evidence gets standard Q3D single solve + per-point adaptive and matrix QA, with periodic independent audits; distant, novel, high risk or suspicious C jump gets targeted paired mesh **before being called a validated label**. If stratum nominal FAIL, quarantine until mesh policy changes or limit the DOE domain and explicitly document exclusion.
- every data point must pass adaptive convergence, solve status, geometry/net/matrix, frequency provenance, no serious warnings, resource guard; repeated mesh runs of same x are ONE ML sample and must stay in same train/test group.

Suggested QA statuses: INVALID_GEOMETRY, SOLVE_FAILED, SOLVER_PASS, MESH_AUDITED_PASS, MESH_UNRESOLVED, QUARANTINED. Do not reclassify SOLVER_PASS as MESH_AUDITED_PASS. Select fixed heldout geometry points before adaptive sampling and avoid moving strata-specific exclusions without documenting them.

## Confidence limitations
Even all nominal + several extreme samples under <1% does not prove every interior point converges. Use feedback-loop sentinel expansion based on observed error, resource ceiling and anomalies. No claim that Maxwell identical-BVP/charge closure/domain physical fidelity has been verified. Prof suggested ranges are research ranges not manufacturing guarantees. Need separate model-to-reality qualifications for real HBM4 DRAM / substrate bias.
