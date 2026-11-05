## 2026-11-05 — Section 13 FIRST fresh Q3D solver evidence: OPT03671 GSG rho10
- Original `SECTION13_EVIDENCE_ONLY.zip` inspected: two successful independent R3/R5 runs with 1x1 native Maxwell C matrix; both Q3D adaptive CG runs report normal completion. CAA R3=**15.5314544921 fF**, R5=**15.5283125724 fF**; R3–R5 difference **0.0202%**.
- Frozen ML prediction **16.281986 fF**, absolute error **0.753673 fF** and relative error **~4.85%** against R5. This error is reported, not suppressed or retroactively tuned away.
- R3/R5 final reported adaptive deltas **0.012532% / 0.005157%**, with 3 passes each. Previous exact native adjacent-pass per-entry gate is not independently rederived from the files here.
- **Unresolved solver/export frequency header mismatch:** setup requests 1000 MHz but native matrix text header reports **1 kHz**; alternate selector headers 1 Hz with same C matrix. Do NOT claim resolved 1 GHz until investigated.
- **No optimization improvement claim yet**; no baseline comparison, and no runs yet for remaining OPT01697, OPT02901, OPT00662.
- [First verification evidence record](../results/optimization/G02_SECTION13_OPT03671_FRESH_Q3D_FIRST_EVIDENCE_20261105.md).

## 2026-11-05 — Section 13 Q3D verification runner prepared; simulations NOT run
- Reused G02 V63 original PyAEDT production `run_case` (no geometry rewrite); four fixed candidate geometries, R3/R5 policy, four dry-runs succeeded. Downloadable script package supplied in conversation.
- The earlier exact 12B manifest CSV was missing; four **full-precision geometries were deterministically reconstructed** from frozen 450 DOE train data, seed 2026 Sobol run, and original candidate indices, matching six-decimal Section 12B printout. New hash differs from old 12B hash; no claim of byte-identical manifest. Prediction labels in reconstructed file are only rounded to six places.
- Solver execution has **not occurred**. Do not infer fresh Q3D accuracy, numerical convergence or verified optimization improvement.
- [Full runner readiness and integrity record](../results/optimization/G02_SECTION13_RUNNER_READINESS_20261105.md). Flagged OPT00662 and all previous surrogate validity failures remain frozen and disclosed.

## 2026-11-05 — Section 12B: executed preflight FAIL evidence preserved
- 4 pre-registered verification candidates checked, **36 local perturbation cases**; 35 in preliminary geometry envelope. Three candidates (OPT03671, OPT01697, OPT02901) passed simplified local matrix checks, though **none has been approved by the actual Q3D builder**.
- **OPT00662 (GSGSG, rho=100)** predicted CAB=-0.003095 fF but **4/9 local variants predicted positive Maxwell mutual CAB**: +0.005718 (D-0.03um), +0.001604 (P-0.10um), +0.011462 (H-0.25um), +0.005319 (tox-0.004um). Flag as surrogate-zero-crossing / optimization exploitation; do not delete, relabel, or claim it represents physically verified near-zero coupling.
- All four candidates are new relative to original 450 designs at identical topology and resistivity; nearest **same topology and rho TRAINING** geometry distances are .487287/.413240/.395788/.436801 (scaled 4D Euclidean), not calibrated uncertainty.
- No new Q3D run, no retraining, no candidate replacement. Local preflight manifest SHA-256: `af7ec78d526ab976c665754475ad22f9c7d6ee3877946afd81212a3c40b44891`. [Full actual executed audit](../results/optimization/G02_SECTION12B_PREFLIGHT_ACTUAL_RESULTS_20261105.md).
- Decision: **FYP is not invalidated**; random DOE prediction result remains, but robust optimization validity is NOT established. Next gate is real Q3D build/mesh/solver verification including deliberately retained failed-mode stress test. No further model tuning based on the final test or post-Q3D outcomes.

## 2026-11-05 — Section 12A sampled optimization and Pareto front
- Executed `ML (14).ipynb`; **4096** scrambled Sobol geometries → **4092** provisional gap-feasible → **36,828** topology×resistivity model predictions; **94** sampled Pareto points and **18** MinCap/Balanced selection rows. No ML retraining or new Q3D validation.
- **83/36,828 predicted 2×2 Maxwell matrices fail the tested physical matrix filters**, concentrated at **GSGSG rho=100 (82)** and **GSSG rho=100 (1)**. Section 11A's zero violations at existing DOE do NOT establish global surrogate physical validity.
- Most suspicious predicted 'optimum': **GSGSG rho=100 OPT00662 |CAB|=0.00310 fF**, unverified and likely a model-risk stress-test. Do not claim actual coupling reduction or model validation from this number.
- Objective: GSG CAA or two-signal |CAB| against P² proxy; simplified gap ≥3.5µm and training min/max bounds are *not complete manufacturing/solver feasibility constraints*. Need exact geometry gate and fresh selected-point Q3D verification.
- Evidence: [method + caveats](../results/optimization/G02_SECTION12A_PARETO_AUDIT_20261105.md), [summary](../results/optimization/G02_SECTION12A_PARETO_SUMMARY_20261105.csv), [selected candidates](../results/optimization/G02_SECTION12A_SELECTED_CANDIDATES_20261105.csv). **Status: exploratory only.**

## 2026-11-05 — Section 11B: pooled SVR physical sensitivity inspected and archived
- Actual source: executed `ML (13).ipynb` Section 11B (2,196 predicted evaluation points; no retraining or tuning). Experiment details, per-scenario endpoints and warnings: [Section 11B sensitivity record](../results/ml/G02_ML_SECTION11B_PHYSICAL_SENSITIVITY_20261105.md).
- Observed CAA endpoints: D↑ and H↑ yield higher CAA; pitch↑ and oxide↑ yield lower CAA, for all 3 topologies × 3 resistivity levels. CAB magnitude has generally corresponding trends, **except** GSGSG at ρ=100 Ω·cm, where increasing oxide causes |CAB| to **increase** (0.2268→0.6488 fF). **Surrogate prediction only; not Q3D verified**.
- Critical limitation: Section 11B used conditional one-factor-at-a-time curves at training medians, with only a simplified gap ≥3.5µm check. It did **not** establish global monotonicity or full physical constraints. 2196=all grid points, so none were excluded by this check.
- Decision: accept as exploratory physical-sensitivity evidence and preserve anomaly; do not tune after test; next objective is constrained optimization and new independent Q3D checks.


## 2026-11-05 — Final 450-DOE ML study completed (fresh experiment)
- The fresh ML notebook `ML (11).ipynb` has been executed through Section 10. **This is a new experimental split (315 train, 67 validation, 68 test, seed 2026), not the superseded V1/V2 split**. 450 final selected-R Q3D labels retained; 447/450 passed the numerical adjacent-pass <1% gate, three approved GSGSG-R1 exceptions (DOE0099/0233/0321) belong to training.
- Training-only CV screened preprocessing, seven algorithms, tuned SVR/ExtraTrees/MLP, and compared cross-topology pooling vs topology-specific models at matched SVR parameters. Pooled CV improvement: GSG 0.071633→0.061253; GSSG 0.073412→0.068666; GSGSG 0.079981→0.071164 NMAE.
- Final held-out test (68 DOE) was completed; among tested methods, GSG MLP three-seed prediction ensemble NMAE 0.059548/R² 0.976115; pooled SVR GSSG NMAE 0.067763/mean R² 0.987502; pooled SVR GSGSG NMAE 0.050801/mean R² 0.988971.
- **Architectural terminology:** the pooled prediction system consists of THREE *target-wise* SVRs (CAA, CBB, CAB), with topology encoding and structural label exclusion for GSG. It is NOT a single multi-output model; does not equal three separate topology-specific models. Pooled fixed parameters from Section 9 were C=100, gamma=0.3, epsilon=0.01; it was not separately retuned.
- **Selection disclosure:** the above per-topology best observed test scores must NOT be presented as an unbiased accuracy estimate of a newly selected post-test hybrid. A pooled SVR has been recommended as a unified prediction interface, but the recommendation was articulated after viewing test scores. Do not retune based on held-out test.
- **Locked evidence archive:** [complete report-ready ML record](../results/ml/G02_ML_FINAL_450DOE_20261105.md), [report/slides guide](G02_ML_FINAL_REPORT_SLIDE_GUIDE_20261105.md), [topology metrics](../results/ml/G02_ML_FINAL_TEST_TOPOLOGY_METRICS_20261105.csv), [component metrics](../results/ml/G02_ML_FINAL_TEST_COMPONENT_METRICS_20261105.csv), [paired architecture CV summary](../results/ml/G02_ML_ARCHITECTURE_CV_COMPARISON_20261105.csv).
- **Still missing from GitHub:** raw 4.3 MB executed notebook, exact 450-row CSV and frozen split manifest; these are separate artifacts requiring repository file upload. The GitHub Markdown summary is a verified record of notebook outputs, not a substitute for full computational reproducibility.

# Decision and evidence log

## 2026-11-01 — CA2 V3 restart
- New GitHub repository: `steph02333/HBM-4E-V3`.
- Local Windows results root: `C:\CA2 result V2` (not directly accessible by connector).
- Previous datasets, previous mesh outputs, previous optimizer predictions and ML training are retired as experimental evidence. No old datapoints will be carried into V3.
- Stage-gated workflow adopted. Prof Lim's first requirement (single-TSV analytical benchmark) is current task.
- Q3D termed **reference EM solver** rather than ground truth.
- Physical model changes trigger revalidation of impacted numerical results.
- This log documents decisions, not a record of an Ansys solver execution.
- Next action: implement and run the fresh G01 benchmark on the user's Ansys machine; return raw outputs, then evaluate against the gate.

## Evidence ledger
| Gate | Evidence | Status |
|---|---|---|
| G01 | Prof Lim email + CA1 Wang 2014 formula + benchmark design | SPECIFIED, NOT RUN |
| G02–G07 | Not yet generated | NOT STARTED |

## 2026-11-01 17:57 (SGT) — G01 B01 first-run failure (environment)
- Command: `py "C:\暂时下载\G01_coax_benchmark.py" --case B01 --student --aedt-version 2025.2`
- Run ID: `20261101_175731_2c15db`.
- Script SHA-256 reported: `18e2fc8c7c5982e54e524f2fcb0518343ae24dcb18459312629ac16dc5de4cbf`.
- Analytical B01 value calculated: `84.045449519 fF`.
- Failure during `from ansys.aedt.core import Q3d`: `ModuleNotFoundError: No module named 'ansys'`.
- No Q3D simulation was performed; G01 remains OPEN / NOT PASSED.
- User-side next step: install PyAEDT into same `py` interpreter with `py -m pip install -U pyaedt`, verify import, then retry B01.
- Local log/bundle folder: `C:\CA2 result V2\01_analytical_benchmark\runs\20261101_175731_2c15db` (not available to connector; results based on pasted console log).

## 2026-11-01 17:58 (SGT) — G01 B01 second import failure despite successful command-line import
- Successful command: `py -c "from ansys.aedt.core import Q3d; print('PyAEDT import OK')"` printed `PyAEDT import OK`.
- Failed script invocation: `py "C:\暂时下载\G01_coax_benchmark.py" --case B01 --student --aedt-version 2025.2`.
- New run ID: `20261101_175846_8e90b4`; same reported source SHA-256 `18e2fc8c7c5982e54e524f2fcb0518343ae24dcb18459312629ac16dc5de4cbf`.
- Script still failed on `from ansys.aedt.core import Q3d` with `ModuleNotFoundError: No module named 'ansys'`, **before** creating/solving Q3D geometry.
- Diagnosis **not yet confirmed**: Windows Python launcher may honor script's `#!/usr/bin/env python3` shebang and select a different interpreter from `py -c`. A conflicting module in the script folder is an alternative possibility.
- Next diagnostic: confirm `py -3.13 -c "import sys; from ansys.aedt.core import Q3d; print(sys.executable)"`, then rerun B01 using explicit `py -3.13 "C:\暂时下载\G01_coax_benchmark.py" --case B01 --student --aedt-version 2025.2`. If it fails again, inspect import with `sys.path.insert(0, r'C:\暂时下载')`.
- G01 remains OPEN; no numerical Q3D result exists from either failed run.

## 2026-11-01 17:59–18:00 (SGT) — G01 B01 fresh AEDT solve completed; numerical validation pending

- User launched with explicit interpreter: `py -3.13 "C:\暂时下载\G01_coax_benchmark.py" --case B01 --student --aedt-version 2025.2`.
- Run ID: `20261101_175942_4a2c83`. Source SHA-256 reported: `18e2fc8c7c5982e54e524f2fcb0518343ae24dcb18459312629ac16dc5de4cbf`.
- Runtime: Python 3.13.5, PyAEDT 1.9.0, AEDT 2025.2SV Student, Q3D Extractor.
- AEDT installation path from log: `C:\ANSYS Inc\ANSYS Student\v252\AnsysEM`.
- Fresh project `CA2V3_B01_af470450`, design `Coax_B01`; three reported final objects: `Cu_SIGNAL`, `SiO2_LINER`, `Cu_GROUND_SHELL`; signal and ground nets created.
- `G01_Setup` reported solved correctly in 18 seconds; script reported `SOLVED_EXPORT_READY_FOR_REVIEW` and C-Maxwell matrix export success.
- Analytical value: **84.045449519 fF**. **Actual Q3D value and relative error not yet available** in pasted console log.
- User's evidence bundle path: `C:\CA2 result V2\01_analytical_benchmark\runs\20261101_175942_4a2c83\G01_results_bundle.zip`.
- **G01 remains OPEN / NOT PASSED** pending upload and inspection of exported matrix, unit conventions and solver convergence, plus eventual completion of B01–B09 and formal gate review. Do not run additional cases until B01 review.

## 2026-11-01 — G01 B01 ZIP independently inspected (preliminary numeric success)
- User provided `G01_results_bundle.zip` (SHA256: `1ae6b6a5d228773b0c209ed7110729d47a63e958b9f497cc688f6adca4d08680`).
- Original Maxwell C matrix has one non-reference signal coefficient: `C(SIGNAL,SIGNAL) = 84.87557931367954 fF`. Ground is the reference net.
- Analytical Eq. (5) prediction: `84.04544951915052 fF`; difference +0.83012979452902 fF; absolute relative error **0.9877153365%** (<5% initial target).
- CG adaptive mesh: **6 passes**, final **0.18624%**, configured target **0.5%**; normal solver completion.
- The error's cause (possibly finite-end fringing) has NOT been demonstrated. Single-coax test cannot validate semiconductor effects or mutual TSV coupling.
- Detailed traceable report: [B01 independent review](../results/g01/B01_20261101_175942_4a2c83_review.md).
- **Gate G01 remains OPEN**. Next: run B02–B09 with the same frozen version of `G01_coax_benchmark.py` (the existing `--all` command also repeats B01 in a new run); inspect complete new evidence before moving to G02.

## 2026-11-01 G02 pilot evidence
Run 20261101_182327_f0dcfa: new three-TSV G-S-S extraction solved. Maxwell C matrix (fF): [[7.73364348, -3.46365160], [-3.46365160, 5.80995368]]. Symmetry exact to exported digits. Eigenvalues positive (approximately 3.1771 and 10.3665 fF). Q3D CG adaptive 4 passes, final delta 0.18863% against 2% setting; 4358 total reported mesh elements. Source material is epsilon-r 11.7 and silicon conductivity 0 S/m, so this is a software/geometry feasibility pilot, not validation of 10 ohm-cm silicon. Charge/reference balance, cross-run mesh independence, physical trend, and domain checks remain open. No mesh license failure observed. G02 NOT PASSED.

## 2026-11-01 21:09 G02 revised pilot failure
Uploaded ZIP: run dated 2026-11-01 21:09, containing pilot_base and pilot_refine, both FAILED at Q3D solve. The requested explicit surface-length mesh seeds were 1.5 um and 1.2 um. Neither produced a C matrix. Reported exception: RuntimeError Q3D solve unsuccessful. The bundle omitted AEDT messages, saved solver profile and mesh-failure diagnostics, so no evidence currently proves Student mesh ceiling or its cause. A downloadable diagnostic v2.1 script was prepared with default no-mesh-operation baseline, gentler 6.0 um and 4.32 um length seeds, and best-effort AEDT GetMessages / failure mesh and profile exports. The diagnostic script has been syntax checked and dry-run tested but not yet tested in AEDT. G02 remains OPEN; do not run full campaign until diagnostic pilot reviewed.

## 2026-11-01 21:18–21:20 — G02 V2.2 student surface-mesh limit confirmed
User-uploaded G02 diagnostic bundle already includes full_console_transcript.txt and multiple cases/*/AEDT_messages_*.txt. pilot_base SOLVED. AEDT diagnostics from pilot_refine explicitly state mesh size 9956 surface elements greater than Student simulation limit; pilot_refine2 states 9516 surface elements greater than Student limit. These are observed solver failures, not inferred limitations. These failed finer-mesh cases do not establish <1% convergence. V2.2 also prints a shutdown-only logging ValueError because PyAEDT atexit still writes to a Tee whose file is closed; the ZIP itself was created beforehand. V2.3 Python artifact has been locally syntax/dry-run tested: safeguards closed streams, rebinds lingering logging handlers, includes final console transcript and logging status in rebuilt ZIP, labels verified mesh limit errors, starts with gentler mesh seeds (12 um then 9.6 um). Actual AEDT verification remains pending. G02 OPEN.

## 2026-11-01 21:23–21:26 — G02 V2.3 diagnostic pilot evidence
Uploaded run 20261101_212314_4c2266. ZIP includes full_console_transcript.txt, LOGGING_STATUS.txt, raw matrix, mesh statistics and AEDT case messages. Default adaptive pilot SOLVED with Cself_A 7.804917051324241 fF, Cself_B 6.079538816134794 fF, signed Cmutual_AB -3.443468923433664 fF; 4388 total mesh elements, 2758 final convergence triangles; symmetric 2x2 Maxwell C and min eigenvalue 3.392339098812323 fF. Explicit 12 um and 9.6 um surface-length seeds FAILED. Current-case AEDT messages for pilot_refine/pilot_refine2 report 9194 surface elements beyond Student simulation limit. Diagnostic messages are cumulative and ALSO contain old-run errors; failure classification should filter by current project/design and time. Repeated 'Cannot perform command because multiple projects are named pilot_base/refine/refine2' suggests AEDT session/project naming collisions, which require isolation. Both failures retain mesh_failure.txt (13412 total reported mesh elements) but no successful refined C matrix. Evidence confirms a Student limitation for these specific mesh settings; <1% independent mesh convergence is NOT demonstrated. G02 remains OPEN. Next: unique project names for every run, case-specific message filtering, and a controlled search for intermediate successful mesh settings rather than endlessly demanding over-limit meshes.

## 2026-11-04 — G02 V6.3: recovered per-pass Cself/Cmutual validation (new evidence)

**Direct original MCAP evidence now available.** Researcher supplied all five `G02_Chunk{1..5}_Adaptive_C_MCAP_asol.zip` archives plus the 900-run collection manifest. Extracted 4,225 individually mapped adaptive-pass Maxwell capacitance matrices from 898 successful R3/R5 solutions, plus 11 partial matrices from two license-failed DOE0447 runs. All 4,225 successful-run pass matrices match the prior `convergenceCG.txt` pass history by DOE/run/pass; 698 original final-matrix text exports from Chunks 2–5 match corresponding recovered last-pass values. Every native SD declares `Frequency=1000000000` Hz, although old exported text headers say `1kHz` (header mismatch still needs explanation).

For each successful run with >=2 adaptive passes, compute the last-pass relative change in each applicable Maxwell coefficient (GSG: CAA; GSSG and GSGSG: CAA,CBB,CAB). **817 of 897 evaluable runs** satisfy <1% for every entry, while **80 runs** exceed 1% for **CAB only**. DOE0402 R3 has one pass only; DOE0447 R3/R5 failed surface-license limits. Among 450 original DOE points: **380** have R3 and R5 both <1%, **56** have exactly one of R3/R5 <1%, **12** have neither <1%, **1** has missing adjacent-pass evidence, **1** has license failure. Actual median last-pass triangle growth ~3.264925% (897 evaluable runs).

**Decision correction:** Previous 374/75/1 grouping used two independently computed *final* matrices (R3 versus R5) and was not the professor's direct "further adaptive mesh refinement" check. Retire the 2% provisional ML-eligibility and 76-point follow-up plan; preserve historical R3/R5 differences as a separate sensitivity measure. Q3D matrix Delta C <0.5% does NOT imply small mutual coefficient relative changes (80 counterexamples). Despite new numerical evidence, **G02 remains OPEN** until representative coefficient-specific convergence, domain, symmetry/passivity, boundary conditions and physical model gate criteria are adjudicated; no blanket ML-label qualification.

Links: [full 450-point MCAP audit](../results/g02/G02_V63_450POINT_PASSWISE_CSELF_CMUTUAL_AUDIT_20261104.md); [all 450 DOE worst per-run final-pass coefficient percentages](../results/g02/G02_V63_ALL450_DOE_FINAL_PASS_WORST_COEFFICIENTS_20261104.csv).

## 2026-11-05 — phase B 12 DOE / 36 simulations completed

Received native `G02_V65_PhaseB_RESULTS.zip` and `G02_V65_PhaseB_MCAP_ASOL.zip`. All **36/36** new R2/R4/R6 solves completed; per-pass `MCAP` matrices and convergence logs checked, final matrix exports match native last-pass data. R2: **7/12** runs meet <1% individual C last-pass criterion; R4: **2/12**; R6: **3/12**. Selecting best measured last-pass coefficient delta across old R3/R5 and new R2/R4/R6 recovers **8/12** previously failing DOE. **445/450** frozen DOE now have at least one successful run with last-two-pass individual-C <1%; remaining four numerical outliers DOE0099, DOE0100, DOE0233, DOE0321 plus DOE0447 license failure. See [Phase B original-data audit](../results/g02/G02_V65_PHASEB_R246_12DOE_36SOLVE_PASSWISE_AUDIT_20261105.md). This does not certify 445 ML labels or full physical-model validation. **G02 OPEN**.

## 2026-11-05 — Phase C V6.7 FINAL R1/DOE0447 update (supersedes earlier 445/450 status)

**All 7 Phase C Q3D R1 simulations SOLVED; full native MCAP adaptive-pass matrices and 7/7 final text exports cross-checked.** Original four outstanding CAB DOE: DOE0100 now passes (R1 last-pass max delta **0.537153%**), while DOE0099 (**1.156310%**, best R1), DOE0233 (**1.243862%**, best old R4) and DOE0321 (**1.249977%**, best R1) remain above 1%. **DOE0447, previously blocked by Student 8000-surface-element license, now SOLVED under R1 with 6/8/10um oxide seeds, all last-pass coefficient <1%; selected R1, original 8um seed, worst delta 0.022070%.**

**Updated count: 447/450 DOE have at least one fully solved run with all Cself/Cmutual last-two-adaptive-pass changes <1%. Exactly 3 DOE remain unresolved: DOE0099, DOE0233, DOE0321.** Older 445/450, 4 CAB + 1 license statistics refer to historical V6.5 *before* Phase C and are superseded. Selected-R ML label candidates **MUST** use the final CAA/CBB/CAB matrix from precisely the selected run. The 3 failures have provisional best-available matrices but are **not** <1% certified and must be excluded from a strict-pass training subset. See [Phase C native 7-solve report](../results/g02/G02_V67_PHASEC_R1_FOUR_CAB_OUTLIERS_DOE0447_7SOLVE_AUDIT_20261105.md). **G02 remains OPEN** due to physical/domain and further numerical validation, and the contradictory 1GHz native-vs-1kHz textual frequency header still requires explanation.
