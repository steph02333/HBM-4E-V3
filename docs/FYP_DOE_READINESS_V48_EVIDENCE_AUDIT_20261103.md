# FYP DOE readiness audit after G02 V4.8 — 2026-11-03

**Scientific decision: GO for DOE design and a bounded feasibility pilot; CONDITIONAL for scaling to a final six-input data-generating campaign.** Do not restart extensive Maxwell M01, charge conservation or finite-domain sweeps. This document supersedes stale historical "not tested" claims; it does not declare all professor validation requirements PASS.

## Grounding
Professor Yeow Kheng email, Sep 26, 2026: D=3–6um, adjacent pitch P=10–20um, height H=25–50um, oxide liner 0.1–0.5um, resistivity rho=1/10/100 ohm-cm (nominal 10), GSG/GSSG/GSGSG. Corresponding Q3D conductivity sigma=100/10/1 S/m. 3 validation levels: analytical coax, Q3D mesh/reciprocity/passivity/charge/domain/trends, independent solver ~10–20 representative structures; Sentaurus bias pilot to decide whether voltage should enter ML. This email sets parameter ranges and research guidance, not a mandatory exhaustive 729-point factorial.

## Existing results and corrections
- G01: nine ideal coax benchmarks: corrected direct original audit finds **0.776–1.668%** error (max 1.668%); old chat statements claiming 3.14–4.02% should not supersede original audited G01 evidence. This is not a finite-Si TSV analytic validation.
- Maxwell M01 already extensively attempted: nominal Q3D–Maxwell C differences 2.80% self and 4.86% mutual, G 12.75/21.90%, with Maxwell external Neumann versus Q3D infinity-reference BVP unresolved and Maxwell loss-error ~2%. Independent identical-BVP validation NOT established, previously intentionally deferred.
- Charge flux was extensively attempted V07–V25, signal field-integral checks good, full independent global closure absent; archived as LIMITATION by researcher.
- Domain tested extensively V2.7, V4.0/V4.5; finite Si body, exterior boundary and mesh effects confounded. V4.5 M25->M100 CAA +1.74%, |CAB| ~0.04%, |GAB| -16.45%. Not a proved artificial-boundary convergence.
- V39 GSSG nominal rho=100,10,1 ohm-cm, i.e. sigma=1,10,100 S/m, CAA at sigma1/10/100 ~10.8215/35.4817/40.2253 fF; |CAB| ~4.0739/11.6183/12.0194 fF. Material response is **large, nonlinear across levels**. Sigma1 oxide mesh variation ~1.5% C, sigma100 G local variation up to 12.62%; no blanket sigma10 numerical pass transfer to other materials/topologies.
- V4.3–V4.4: height and topology physical trend pilot at sigma10; GSGSG vs GSSG at H35 shows |CAB| 6.446 vs 11.649 fF, but signal spacing is 30 vs 15 um and central G added; therefore 44.7% cannot be attributed solely to shielding.
- V4.6: D/P/tox single-factor trends in expected directions, seven successful solver points.
- V4.7: four high-risk geometry corners × two distinct adaptive mesh settings at sigma10 GSSG, max C pair difference 0.412%.
- **NEW V4.8 raw uploaded ZIP:** four out of four Q3D cases solved, no recorded adaptive nonconvergence. GSG nominal H35 sigma10 R12 vs R18 total mesh 3132 vs 3708, CAA=33.356406 vs33.365005 fF, pair difference 0.02577%. GSGSG sigma10 mesh 3032 vs3600, CAA 36.209600 vs36.225974 fF (0.04520%), CBB 36.283111 vs36.290410 fF (0.02011%), |CAB| 6.440745 vs6.476171 fF (0.54702%). All relevant C pair differences <1%; actual mesh sizes differ. V4.8 topology nominal paired-mesh consistency PASS (not absolute accuracy).
- **Deduplication audit across eight uploaded ZIPs V39,V41,V43,V44,V45,V46,V47,V48:** 101 successful Q3D solves. Of these, 82 are H0/no-contact, physical Si margin25um, 1GHz requested; they comprise only **19 distinct six-input nominal/corner coordinates** (topology,D,P,H,tox,sigma). Repeated meshes are validation, not independent training labels. Ignore failed cases and contact/frequency/margin perturbations for final H0 dataset.

## Why a useful DOE is possible
Validated geometry/material responsiveness, meaningful output magnitudes, reliable output serialization (full signed matrices and metadata), Student solver feasibility on sampled corners, and some representative independent mesh support. Q3D should be called **reference EM solver**, not experimental ground truth. Strong possible thesis: uncertainty-aware, topology-conditioned, multi-parameter surrogate of **simplified homogeneous conductive-Si H0 TSV model**, with held-out Q3D validation and optimization confirmation.

## Remaining DOE-significant holes
1. **Four missing nominal material × topology strata:** (GSG, sigma1), (GSG, sigma100), (GSGSG, sigma1), (GSGSG, sigma100). Existing nominal 5/9 cells are GSSG × three sigma plus GSG/GSGSG at sigma10. Prioritize 4 new nominal solves, optionally add second distinct mesh per cell (total 8 solves) if Student allows; avoid unbounded retries. This tests regime feasibility, multi-net and material coupling.
2. Only sigma10 GSSG high-risk corners are two-mesh checked. Use selective extra corner/sigma/topology probes if new stratum shows instability, not full nine-stratum exhaustive mesh.
3. Main observed topology contrast confounds central ground shielding with signal separation. If claiming shielding effectiveness, use a separation-matched control (same 30um A/B spacing, with and without central G), keeping surrounding ground geometry and Si footprint controlled. Otherwise report topology-conditioned result and not causal shielding.
4. Freeze outputs by topology: GSG 1x1 C_AA only (CAB not zero, undefined); GSSG/GSGSG 2x2 signed CAA,CBB,CAB. Separate regression heads or compatible masked labels. Do not mix independent validation mesh repeats in ML train/test split.
5. DOE runs must capture setup frequency via independent native readback because exporter headers often say 1kHz although setup is 1000MHz. Track uncertainty in label provenance.
6. Model validity remains conditional: no verified real HBM substrate ohmic contact, MOS bias, true infinity/domain independence, independent charge balance, or apples-to-apples Maxwell. Literature and HBM standard documents are not direct proof the linear TSV array is exact HBM4 die structure.
7. The professor's rectangular geometric constraints already satisfy P>D+2tox at all endpoints (minimum gap 10-(6+2*0.5)=3um), but keep geometry checks as an implementation safeguard. Distinguish adjacent pitch (15um) from actual signal-signal distance in GSGSG (30um).

## Recommended DOE design
**Phase 0:** missing 4 nominal cells, 4 quick solver pilot cases; if feasible do pairwise distinct meshes (8 attempts total). Capture fail/resource status and actual C.
**Phase 1:** small space-filling Q3D DOE over six input variables: four continuous geometry axes D/P/H/tox, discrete log-rho levels 1/10/100 ohm-cm and three categorical topologies. Nominal initial pilot around 5–10 new unique points per stratum *subject to demonstrated feasibility* (45–90 candidate geometry/material/topology combinations). Do not fix 180 points before examining failure rates, model learning curves, error by stratum and Student limits.
**Phase 2:** scale adaptively using grouped splits and a predeclared holdout per stratum, separate GSG and two-signal label outputs, per-point QA/quarantine, uncertainty/error targets in fF and relative %, and Q3D re-simulated optimum candidates.
**Reports:** compare interpolation versus basic physical baselines (H scaling/coax or geometry-normalized relations), ablate topology and resistivity, model cross interactions, confidence intervals and numerical uncertainty; do not use repeated refinements as independent ML data.

## Gate
GO: DOE methodology, script architecture, Phase0 nominal four-cells and a tiny pilot.
NO claim: full professor validation fulfilled, final HBM4 physical fidelity, independently verified frequency for every case, or guaranteed high accuracy across untested strata.
