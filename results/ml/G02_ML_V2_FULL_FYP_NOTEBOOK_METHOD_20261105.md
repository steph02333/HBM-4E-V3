# G02 ML V2 — Complete FYP Notebook Method (2026-11-05)

## Source and reproducibility
A **27-cell notebook** named `G02_FYP_ML_V2_End_to_End.ipynb` was generated as an independent deliverable packaged with the exact 450-DOE selected-R CSV, the V1 **frozen** 314/68/68 train/validation/test split, source-provenance QA CSV, `requirements.txt`, and instructions. **Notebook binary/JSON content is not yet committed to this repository**; do not claim it is present until uploaded. Save the package in the repo at `notebooks/g02_ml_v2/` and rerun all cells from that directory. The repo's [V1 results](G02_ML_V1_BASELINE_450DOE_20261105.md) remain historical and not full tuning.

## Data QA
450 unique frozen DOE, topologies GSG/GSSG/GSGSG (150 each), resistivity 1/10/100 ohm-cm (150 each), signed Maxwell labels (GSG: CAA only; other topologies: CAA/CBB/CAB). Every label must be sourced from the **same actual selected-run native final matrix** as its `selected_R`. Selection distribution: R1=5, R2=3, R3=275, R4=2, R5=162, R6=3. Exactly three user-accepted R1 numerical exceptions DOE0099, DOE0233, DOE0321 have CAB last-pass changes >=1%, and are **not falsely described as converged**. Physical G02 validation remains OPEN.

## End-to-end methodology
1. Audit source, missing values, topology masks, numerical warnings and fixed split.
2. EDA: target distributions, feature distributions, Spearman correlations (descriptive).
3. Input physics predictors: `log10(rho_ohm_cm),D_um,P_um,H_um,tox_um,gap_um`. Exclude DOE_ID, selected_R, mesh seed, convergence and target-derived values. Avoid redundant sigma for known rho.
4. Fit StandardScaler **within each training fold** through a pipeline; fit target StandardScaler through TransformedTargetRegressor; no cross-fold estimator leakage.
5. Use the original 314 train / 68 validation / 68 **reused held-out benchmark test** assignment from V1. Development=382 rows for five-fold CV.
6. Compare DummyMean, Ridge, RandomForest, ExtraTrees, RBF-SVR (MultiOutputRegressor), MLP (early-stopped neural network); different target dimensionality models for each topology.
7. Evaluate 5-fold shuffled KFold with fixed seed 42 and fold-comparable score: average across targets of MAE divided by target median absolute scale computed from original training partition only. Keep fold SD.
8. **Explicitly sweep every listed principal hyperparameter** for every model and topology using 5-fold CV, plot mean±SD and show minima/1-SE plateaus; never invent a mathematical knee.
9. Tune joint hyperparameters via reproducible 5-fold RandomizedSearchCV (12 combinations per algorithm and topology in full mode) to test interactions beyond one-factor sweeps.
10. Perform feature drop-one CV ablation, sample-size learning curves with CV error bands.
11. Lock algorithm/params; refit train+val; evaluate the same V1 benchmark test **once** for comparison with original results. Export per-target MAE/RMSE/R2/MAPE/P95, parity, residual, boxplots and worst DOE list.
12. Optional exploratory 447-only numerical-quality sensitivity comparison on identical split IDs and common benchmark test rows; assess self-positive, mutual-negative, positive-definite predicted 2x2 matrix.
13. Save all CSV/figures/model joblib and JSON input SHA256/versions.

## Limits and reporting controls
- V1 has *already examined* the benchmark test; hence V2 is not a pristine independent external confirmation. Repeated model design based on that test is forbidden; collect independent DOE/domain holdout later.
- Hyperparameter sweeps optimize **only over prespecified finite grids**; 1-SE band is not an intrinsically proven 'knee'. Full mode is computationally intensive; quick mode is for smoke tests and not final scientific results.
- This commit documents the correct methodology and notebook artifact name; the full 5-fold tuning and new final test numbers have **not yet been executed in full mode**, so no results should be attributed to them.
- ML prediction errors measure agreement with Q3D numerical labels, not measured physical capacitance. Q3D native matrices indicate 1 GHz while old text headers show 1kHz and physical/domain gates remain open.
