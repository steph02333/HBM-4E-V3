# Report and slides: final G02 ML evidence guide (2026-11-05)

## Fast lookup
Full methodology, provenance, limitations, exact results: [Final ML experiment record](../results/ml/G02_ML_FINAL_450DOE_20261105.md). Numeric tables: [test per-topology](../results/ml/G02_ML_FINAL_TEST_TOPOLOGY_METRICS_20261105.csv), [test per-component](../results/ml/G02_ML_FINAL_TEST_COMPONENT_METRICS_20261105.csv), [architecture CV](../results/ml/G02_ML_ARCHITECTURE_CV_COMPARISON_20261105.csv).

## Suggested report outline (avoid invented claims)
1. **Motivation:** Q3D extraction is expensive across DOE parameter space; surrogate estimates capacitance coefficients quickly at inference (no measured inference latency benchmark yet; do not claim numerical speedup).
2. **Reference generation:** 450 DOE across three TSV topologies, numerical selected-R/adjacent-pass convergence criteria; three documented GSGSG numerical exceptions.
3. **Feature definition:** ρ, D, P, H, tox. Optional log10 rho; derived gap mathematically redundant. Topology one-hot in pooled model. Explain GSG output shape versus GSSG/GSGSG.
4. **Training protocol:** 315/67/68 stratified split, seed 2026; training-only five-fold CV; preprocessing and algorithms; SVR/ExtraTrees/MLP. One figure of CV progress.
5. **Architecture question:** pooled target-wise model vs topology-specific target-wise baseline, fixed SVR settings (Section 9). Show 3-pair bar plot: GSG 0.07163→0.06125, GSSG 0.07341→0.06867, GSGSG 0.07998→0.07116 (specific→pooled).
6. **Final held-out comparison:** report all 7 topology/model combinations, rather than only cherry-picked winners. GSG MLP ensemble: MAE 2.066 fF, R² 0.9761. Pooled GSSG 0.06776 NMAE/R² 0.9875, GSGSG 0.05080/R² 0.9890.
7. **Coefficient-level error:** seven relevant outputs for observed best methods, CAA/CBB/CAB individually. Mutual CAB is negative in Q3D convention; use absolute errors in fF and avoid unstable percentage claims near zero.
8. **Failure analysis:** DOE0158 GSG MLP CAA prediction 121.898 vs Q3D 109.099 fF; DOE0436 GSSG pooled CAA 105.642 vs 114.920 fF; DOE0364 GSGSG pooled CBB 59.499 vs 52.469 fF.
9. **Limitations and next steps:** interpolation only; no measured-device check, unseen geometry/topology ranges, frequency/bias-dependent effects, full Maxwell-matrix physical consistency test, or unbiased post-selection hybrid test.
10. **Decision disclosure:** A pooled SVR prediction *system* consists of three independently trained per-target SVRs; the system outputs only existing GSG coefficients. Test table was viewed before recommending pooled as the default architecture; do not claim an unbiased test estimate of a hybrid subsequently selected using the test.

## Slide flow (7 slides)
1. FYP aim, parameterised TSV topologies and physical features.
2. Q3D selected-R simulation dataset + numerical provenance (447 pass, 3 exceptions).
3. 315/67/68 split + training-only CV / model families.
4. SVR tuning and comparison with Extra Trees/MLP.
5. Pooling ablation on five matching folds (paired bars).
6. Final held-out performance: full comparison + per-component MAE.
7. Physical interpretation, anomalous DOE cases, limits and future scope.

## Figure/caption guidance
- 'Test NMAE' = MAE per target divided by median |label| of *topology-specific training set*, then unweighted mean over target coefficients. It is **not** percent mean relative error.
- 'Mean R²' = equal mean across output components; also display component-specific R².
- For plots of actual/predicted values use fF and `C_AB` negative sign as exported by Q3D.
- Do not mistake 3-seed average validation *metrics* for prediction-averaged MLP ensemble used on test.
- Do not describe the test-selected best-of-each-topology mix as an independently validated universal final hybrid.
- Do not claim that Section 10 used all 382 non-test designs; its `train10` was the original 315 training samples.
