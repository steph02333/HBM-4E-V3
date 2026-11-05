# G02 Section 12B — Executed preflight results (2026-11-05)

## STATUS
**PRE-Q3D SCREEN COMPLETED. NO NEW Q3D SIMULATIONS. NO CANDIDATES REMOVED, REPLACED, OR RETUNED.** This document records the actual user-executed output of Section 12B, shared in-chat and bound to the pre-registered [verification protocol](G02_SECTION12B_VERIFICATION_PROTOCOL_20261105.md).

## Full pre-registered candidate table
| ID | Purpose | Topology | rho ohm-cm | D um | P um | H um | tox um | gap um | predicted CAA fF | predicted CBB fF | predicted CAB fF | objective fF | P² um² | closest same topology/rho TRAIN DOE | normalized geometry distance | checked local matrices | status |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| OPT03671 | compact GSG | GSG | 10 | 3.665956 | 10.181201 | 25.271726 | 0.474021 | 5.567203 | 16.281986 | NA | NA | 16.281986 | 103.656855 | DOE0113 | 0.487287 | 0/9 invalid | BASIC_SCREEN_PASS_PENDING_Q3D_BUILDER_REVIEW |
| OPT01697 | compact GSSG | GSSG | 10 | 3.254574 | 10.358027 | 26.883445 | 0.459217 | 6.185019 | 14.726529 | 14.814701 | -5.909626 | 5.909626 | 107.288732 | DOE0265 | 0.413240 | 0/9 invalid | BASIC_SCREEN_PASS_PENDING_Q3D_BUILDER_REVIEW |
| OPT02901 | low-coupling GSGSG | GSGSG | 10 | 4.525267 | 19.934391 | 26.079064 | 0.440812 | 14.527499 | 19.070661 | 18.571125 | -2.979704 | 2.979704 | 397.379931 | DOE0231 | 0.395788 | 0/8 in-domain invalid (1 outside envelope) | BASIC_SCREEN_PASS_PENDING_Q3D_BUILDER_REVIEW |
| **OPT00662** | deliberately suspected surrogate failure | **GSGSG** | **100** | **3.899532** | **12.477734** | **25.288979** | **0.111516** | **8.355170** | **8.277696** | **8.641673** | **-0.003095** | **0.003095** | **155.693854** | **DOE0371** | **0.436801** | **4/9 invalid** | **FLAGGED_REQUIRES_REVIEW** |

All candidates passed the simplified original design-envelope, positive dimensions, outer-oxide nonoverlap and provisional gap>=3.5µm checks, and **no exact same topology/rho DOE geometry duplicate** was detected in the 450-design data. These screens are not full Q3D-builder approval, manufacturing validation, or physical accuracy evidence.

## LOCAL FAILURE EVIDENCE — NEVER DELETE
For OPT00662, local 1%-of-bound-width one-dimensional perturbations at fixed other inputs remain inside preliminary domain yet predict *positive* CAB under the Maxwell convention. They were correctly counted **invalid**:

| Case | D um | P um | H um | tox um | predicted CAB fF | Why invalid |
|---|---:|---:|---:|---:|---:|---|
| Centre | 3.899532 | 12.477734 | 25.288979 | 0.111516 | -0.003095 | Centre passes tested reduced matrix checks, but near-zero coupling is **unverified and suspicious** |
| D - 0.03 | 3.869532 | 12.477734 | 25.288979 | 0.111516 | +0.005718 | positive Maxwell mutual sign |
| P - 0.10 | 3.899532 | 12.377734 | 25.288979 | 0.111516 | +0.001604 | positive Maxwell mutual sign |
| H - 0.25 | 3.899532 | 12.477734 | 25.038979 | 0.111516 | +0.011462 | positive Maxwell mutual sign |
| tox - 0.004 | 3.899532 | 12.477734 | 25.288979 | 0.107516 | +0.005319 | positive Maxwell mutual sign |

LOCAL OBJECTIVE RANGES (in-domain): OPT00662 [0.001604,0.017688] fF; OPT01697 [5.861347,5.957881] fF; OPT02901 [2.912806,3.046527] fF; OPT03671 [16.139456,16.425088] fF. Small absolute variation near zero DOES NOT make OPT00662 physically robust, since sign is violated and zero-crossing can attract optimizer artificially.

## SAME-GROUP TRAINING COVERAGE
Each nearest neighbor is from matching topology AND ρ (50 training rows per group, except actual training topology × rho distribution is 35 each). Exact nearest matches: OPT03671 DOE0113 distance .487287, source CAA 23.912083; OPT01697 DOE0265 .413240, source [CAA,CBB,CAB]=[28.130907,28.135395,-9.198126] fF; OPT02901 DOE0231 .395788, source [29.923409,29.920919,-5.596219] fF; OPT00662 DOE0371 .436801, source [7.412958,7.414535,-0.585844] fF. Distance is Euclidean in full-range-scaled four geometry inputs only; it is **not calibrated uncertainty**. Very different neighboring labels indicate a risk that the surrogate optimum is not locally supported; differences cannot establish a precise error estimate.

## Preflight audit and digest
- Total 4 pre-registered cases; **36** local checks; in-domain counts 9,9,8,9 (35 total).
- OPT00662 4 matrix-sign violations; no other local matrix violations.
- Q3D runs completed in this stage: **0**. Re-training: **0**. Changes to frozen candidate shortlist: **0**.
- `SECTION12B_FROZEN_Q3D_VERIFICATION_MANIFEST.csv` SHA-256 supplied by run: `af7ec78d526ab976c665754475ad22f9c7d6ee3877946afd81212a3c40b44891`. This hash is of the **local manifest CSV bytes**; the exact CSV itself is not embedded in this document or committed by this text write, so it cannot yet be independently verified from GitHub.
- The current preflight code checks simplified bounds, not complete AEDT mesh solver material/geometry feasibility. Confirm all generated entities and configuration against original validated G02 scripts, choose adaptive convergence criteria, log both last adaptive pass matrices; do not assert physical adequacy without Q3D.

## SCIENTIFIC ASSESSMENT
The current held-out random test supports interpolative prediction on the sampled DOE; it does **not** establish high-confidence surrogate-guided optimization near minima. The sign-crossing for OPT00662 is evidence of model-exploiting optimization, not confirmed near-zero Q3D capacitance. Report all four verification attempts and any failures or surprises without post-hoc exclusion. The three basic-screen-pass designs are **eligible for full Q3D-builder checking**, not certified validated optima. OPT00662 must be retained as an intentional stress test unless it is impossible to simulate; if impossible report geometry/solver failure explicitly.

## Next gate
1. Obtain exactly four full-precision manifest entries (not rounded display table). Verify original G02 PyAEDT building-script dimensional/material/electrode assumptions and conductivity conversion `sigma_Spm=100/rho_ohm_cm` when rho in Ω·cm.
2. Generate four new independent project runs using same reference solver configuration and appropriate mesh adaptive passes. Preserve failures too.
3. Extract native Maxwell matrices and compare all available components [CAA,CBB,CAB] in fF; include per-component absolute errors, sign consistency, numerical convergence (<1% last-pass criterion or explicitly flagged exceptions), objective improvement relative to matching-topology/rho Q3D baseline, and full provenance.
4. Do not use verification results to retune the *same* claimed final model.

Previous evidence: [12A audit](G02_SECTION12A_PARETO_AUDIT_20261105.md); [full ML record](../ml/G02_ML_FINAL_450DOE_20261105.md); [11B sensitivity](../ml/G02_ML_SECTION11B_PHYSICAL_SENSITIVITY_20261105.md).
