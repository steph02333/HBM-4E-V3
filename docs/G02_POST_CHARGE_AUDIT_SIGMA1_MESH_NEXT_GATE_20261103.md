# G02 post-charge-audit roadmap and sigma1 mesh next gate — 2026-11-03

## Decision: close charge audit as bounded limitation
G02 v21–v23 native E flux demonstrated internal signal matrix agreement (maximum 0.6076%) and cross-excitation reciprocity (<0.05%), not independent Gauss closure. v24 mapped conductor sidewall/endcaps, and v25 showed that supplying a numeric face ID string to FieldsReporter.EnterSurf failed. The researcher explicitly elects to stop this branch. **Charge conservation is NOT INDEPENDENTLY VERIFIED, not measured FAIL or PASS.** No further v26 flux work without an independent, documented method and a compelling new need.

## Next highest-value gap: sigma=1 S/m local oxide mesh convergence
Nominal V3.9 at sigma 1/10/100 S/m R16/R18 C differences were 0.027%/0.261%/0.064%, respectively. Yet sigma=1 S/m local oxide L12 vs L8 showed 1.129% difference in mutual C; L8 vs L6 used identical mesh and cannot be accepted as independent. We must distinguish local mesh under-resolution from physical change before qualifying sigma=1 for DOE.

### Controlled qualification protocol (not a claim of a completed solve)
- Baseline: the exact prior V3.9 **GSSG** fixture at D=4 um, P=15 um, H=35 um, tox=0.3 um, silicon margin=25 um, Si epsilon_r=11.7, sigma=1 S/m (=100 ohm-cm), 1GHz, no explicit substrate contact, Higher-order solver; preserve project/net/source and substrate reference exactly. Use project copies, not original; log source SHA and AEDT/solver versions.
- Recover the original V3.9 sigma1 local Cu/OX mesh configuration and outputs. Do not guess local mesh assignment details from the label L12/L8.
- Compare at least two genuinely distinct converged solutions at progressively refined **oxide-sidewall** surface meshes with the same physical model; preferably three. Record *actual* surface triangles, total elements, passes, convergence errors, Solver Student limit and any warnings. A different requested refinement value with identical mesh is not independent.
- Predeclare target: C_AA, C_BB and |C_AB| differences <1% between final two genuinely distinct mesh configurations, after checking the third level / trend. Absolute fF difference should be recorded alongside relative %.
- Evaluate C and G separately. If the intended ML label is C-only, sigma100 conductance discrepancies are a separate open gate, not justification to label C as converged automatically.
- Save full signed matrices and provenance for each mesh. On Student mesh exhaustion keep failed logs and do not relabel as PASS. Avoid modifying geometry/material/topology or physical silicon margin during this experiment.
- If no distinct feasible refinement fits the Student limit, mark sigma1 local-mesh uncertainty as unresolved and either restrict DOE domain or raise the modelling/solver resource issue explicitly.

### Remaining tasks after sigma1
1. Physical silicon extent sensitivity versus artificial solver exterior boundary (do not conflate them).
2. Height endpoint checks H25/H50, qualified meshes.
3. GSG/GSGSG topology family representative tests, with GSG mutual C undefined (one signal).
4. Legal coupled geometry corners.
5. Sigma100 local G mesh only if G is a required ML target.
6. Cross-solver matching BVP before declaring Maxwell validation (prior C differences 2.80/4.86%, G differences 12.75/21.90%).
7. Freeze H0 reference/substrate interpretation and C-only vs C+G output choice with supervisor before full new DOE.

### Current handoff
Prior run references: G02_V39_results_bundle.zip; G02_V40_targeted_results_bundle.zip; existing V3.9 mesh campaign script if available. Not stored in repository presently. A reproducible new AEDT runner should be created only after inspecting previous script and exact mesh/solution metadata, rather than inventing a new mesh setup.
