# G02 ML V1 — selected-R 450-DOE baseline (2026-11-05)

## Dataset and non-negotiable label provenance

Source: frozen 450 DOE, native Q3D **final Maxwell C matrix from each record's selected mesh strategy** (V6.3 R3/R5, V6.5 R2/R4/R6, V6.7 R1). **Never select one R and label with another R's capacitance matrix.** Final selected-R distribution: R1=5, R2=3, R3=275, R4=2, R5=162, R6=3 (450 total). Three explicit accepted R1 exceptions: DOE0099, DOE0233, DOE0321, **all CAB last-two-pass changes >=1%** and clearly marked as lower-confidence numerical labels. 447 others pass the last-pass coefficient <1% stability screen, **not** full physics validation. DOE0447 uses the license-recovered R1 original 8um seed solution.

Three topologies **GSG/GSSG/GSGSG**, exactly **150 each**; resistivity **1/10/100 ohm-cm**, exactly 150 records per level. GSG has CAA only; two-signal GSSG/GSGSG have signed Maxwell coefficients CAA, CBB, CAB. Do not replace GSG's nonexistent CBB/CAB with zero or turn negative CAB into an absolute value without explicitly redefining the target.

Physical predictors only: `log10(rho_ohm_cm)`, `D_um`, `P_um`, `H_um`, `tox_um`, `gap_um`. Topology-specific models (not passed numerically as a feature). The redundant `sigma_Spm` is omitted because it is determined by resistivity. Never include `DOE_ID`, `selected_R`, `mesh_seed_um`, convergence flags, result file paths, adaptive pass count or C-derived quantities as predictors.

## Leakage-controlled methodology

- Fixed `random_state=42`. Split **by topology×resistivity stratum**, held-out test **15% first**, then validation split of the remaining observations using `test_size=0.15/0.85` and seed 43. Exact realized counts: **314 train, 68 validation, 68 untouched test**. Within topology: GSG 105/22/23; GSSG 104/23/23; GSGSG 105/23/22.
- All feature/output scalers are fit **only on training fold** during model comparison. Compare 5 models independently per topology: DummyMean, Ridge(alpha=10), RandomForest(220 trees, min leaf 2), ExtraTrees(220 trees, min leaf 2), RBF SVR(C=10, epsilon=.08). No tuning against the test set.
- Validation model selection minimizes the mean over target components of `MAE(target)/median(abs(target))`, with normalization denominator computed from TRAIN only. This equalizes relative importance of CAA, CBB and lower-magnitude signed CAB.
- Retrain the validation winner on train+validation data; inspect the held-out test **once**. Save row-level test predictions, actual/final C matrix labels, per-target fF absolute and percentage errors, model snapshots and split manifest.
- **Important caveat:** This is a first baseline, one fixed split, no nested CV, no held-out external geometry/domain/physical validation. Low test error against Q3D selected labels does not establish experimental device accuracy.

## Actual measured held-out test metrics

| Topology | Selected model | Target | Test MAE (fF) | RMSE (fF) | R² | MAPE (%) |
|---|---|---|---:|---:|---:|---:|
| GSG | ExtraTrees | CAA | 4.073 | 5.707 | 0.901 | 11.65 |
| GSSG | ExtraTrees | CAA | 3.571 | 5.502 | 0.974 | 7.98 |
| GSSG | ExtraTrees | CBB | 3.496 | 5.433 | 0.974 | 7.88 |
| GSSG | ExtraTrees | CAB | 1.417 | 2.009 | 0.969 | 9.60 |
| GSGSG | RandomForest | CAA | 3.972 | 6.015 | 0.947 | 8.91 |
| GSGSG | RandomForest | CBB | 3.943 | 5.954 | 0.948 | 8.85 |
| GSGSG | RandomForest | CAB | 0.783 | 1.401 | 0.945 | 10.44 |

Exact validation selection scores (average per-target train-median-normalized MAE): GSG ExtraTrees **0.131715**, GSSG ExtraTrees **0.116909**, GSGSG RandomForest **0.150225**. Exact held-out test normalized MAE GSG **0.129651**, GSSG **0.122369**, GSGSG **0.114949**.

**Reproduction files generated in project workspace:** `G02_FINAL_ML_450_ALL_SELECTED_R.csv` (450 row full provenance), `G02_FINAL_ML_450_TRAINING_COLUMNS_ONLY.csv`, `G02_FINAL_ML_447_STRICT_LT1.csv`, `G02_FINAL_ML_450_PROVENANCE_QA.csv`, `G02_FINAL_ML_3_ACCEPTED_EXCEPTIONS.csv`, xlsx review, `run_ml_v1.py`, `FROZEN_SPLIT_450.csv`, `MODEL_METRICS.csv`, `SELECTED_MODELS.csv`, `HELDOUT_TEST_PREDICTIONS.csv`, `SUMMARY.json`, test plots and saved models. **Those locally generated binary/data artifacts are not represented as uploaded to GitHub by this report**; GitHub publication must be separately verified. Keep the complete downloadable archive with the project and transfer it to the repo to guarantee permanent reproducibility.

## Follow-up work

1. Place exact selected-R CSVs, frozen split and script in repository; verify SHA256 after upload.
2. Include a 447-only training sensitivity study using identical fixed test assignments to quantify effect of three accepted exceptions. DOE0099 is in the held-out test, DOE0233 in validation, DOE0321 in train for this seed/split.
3. Repeat multiple stratified grouped splits/CV, compare learning curves, and investigate worst relative CAB errors.
4. Validate physical-model assumptions, matrix passivity/symmetry, domain independence and solver frequency export `1GHz` native vs `1kHz` header. **G02 physics validation remains OPEN.**
