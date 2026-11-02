# G02 pre-DOE acceptance gates — 2026-11-02

Decision: **G02 OPEN, do not freeze final DOE labels.** GO for targeted closure experiments and parallel DOE planning.

Supervisor's checks: self/mutual C adaptive mesh sensitivity ~<1%; reciprocity Cij=Cji; positive/passive C matrix; independent charge conservation; expected diameter/pitch/liner trends; sufficiently remote simulation domain boundaries.

Current evidence and gaps:
- Q3D V3.9 sigma1/10/100 S/m nominal R16/R18 max C differences 0.027%/0.261%/0.064%. At sigma10 independent local Cu/oxide mesh C <0.37%, G <0.93%. Nominal **conditional** qualification only.
- Sigma1 S/m oxide mesh L12 versus L8 mutual C differs 1.129%; L8 and L6 have identical numbers and mesh, not independent further refinement. OPEN.
- Sigma100 G local mesh variants differ up to 12.62%. OPEN if G is an output target.
- V3.9 65 successful reduced 2x2 matrices passed symmetry and positive eigenvalue checks; final DOE batch still needs guardrails.
- Independent current/charge flux conservation **NOT DONE**; cannot define ground balance by construction.
- V4.0 Si margin 25/50/100um changes actual silicon size. Self C 25->100um changes 1.929%, G_AB ~13%: **physical extent sensitivity**, not pure numerical far-boundary independence. OPEN.
- V4.0 D3->6, pitch10->20, tox0.1->0.5 show expected C directions for sigma10 H35 GSSG. Height H25/H50 NOT TESTED; GSG and GSGSG topologies NOT QUALIFIED; few multivariate stress corners tested. OPEN.
- Model physics H0 finite no-explicit-contact lossy Si, not genuine guaranteed floating active HBM silicon. Position/connectivity of HBM real substrate tie unsupported; do not claim device-biased inversion/depletion included. Must freeze explicitly sourced or conditional fixture before final DOE.
- Maxwell cross-check: same GSSG D4 P15 H35 tox0.3 sigma10 margin25 1GHz; 8-pass Maxwell 51308 tets, pass6->8 C_AA .027%, abs(C_AB) .033%, G_AA .099%, abs(G_AB) .155%; native loss error 2.0011% ABOVE 1% target. Maxwell versus Q3D nominal: C discrepancies 2.80%/4.86%, G 12.75%/21.90%. Fresh top-face/whole-Cu object voltage test does not reduce mismatch; underlying Q3D infinity reference versus Maxwell default Neumann exterior not proven equivalent. Q3D native saved solution 1GHz confirmed; exported header 1Hz/1kHz remains provenance caveat.

Priority:
P0 document model H0 and seek Prof agreement on C-only vs C+G target and true HBM substrate-return assumptions.
P1 one independent charge/flux audit from saved nominal Q3D; sigma1 oxide distinct mesh; controlled physical Si extent vs computational outer boundary; height endpoints and GSG/GSGSG representative tests; 2-4 high-risk legal corners. Preserve Higher solver, all metadata, Student limits.
P2 if retaining G targets address sigma100 local G mesh; no more untargeted Maxwell mesh/terminal experiments. Investigate true boundary-reference BVP before claiming solver cross-validation.
P3 batch invariants and provenance for each final DOE case: geometry, sigma, topology, physical model, frequencies, solver mesh, raw signed matrices and flags.

Important inference: Prof ~1% refers to changes under credible refinement, not necessarily absolute solver error. Cross-solver discrepancies need not be <1%; cannot infer physical validation solely from C being close.

Detailed report delivered in chat: G02_PRE_DOE_GATE_REVIEW_20261102.md. Local evidence includes G02_V39_results_bundle.zip, G02_V40_targeted_results_bundle.zip, G02_M01_ADAPT8_17_diagnostic.zip, DOM10_M25_R18.aedt + .aedtresults.zip.

Likely original Q3D Windows path:
C:\CA2 result V2\02_numerical_convergence\V3_conductive_silicon\run_20261102_164954_6a5874\ansys_projects\DOM10_M25_R18.aedt
