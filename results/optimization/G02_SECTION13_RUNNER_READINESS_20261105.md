# Section 13: Fresh Q3D verification preparation (2026-11-05)

Status: **READY FOR LOCAL DRY-RUN / NOT YET Q3D VERIFIED**.

Four fixed candidate IDs: OPT03671 (GSG rho10), OPT01697 (GSSG rho10), OPT02901 (GSGSG rho10), and OPT00662 (GSGSG rho100). The last remains a deliberate model failure stress-test.

Implementation: a new guarded Python launcher calls the original G02 V6.3 PyAEDT production solver function directly. It uses the same conductor/oxide/silicon geometry, topology net assignments, mesh seeds and requested 1 GHz setup. Both R3 and R5 configurations per case can be run sequentially. Solver execution requires an explicit command-line flag. All four configurations passed no-solver dry runs. No new AEDT solve has occurred.

## Manifest accuracy
We reconstructed four unrounded Sobol **geometry** records from the existing 450 DOE source and frozen training split using the original Section 12A random seed and bounds. All four match Section 12B printed geometry to six decimal places. This reconstructed CSV is NOT the same file as the prior SHA256-frozen Section 12B manifest, which was not attached. Prior hash: af7ec78d526ab976c665754475ad22f9c7d6ee3877946afd81212a3c40b44891. Reconstructed CSV hash: 7fad44d0085a752673e0e8fc68a62667ddd87c9cd77c5f0b54cfe4668f99f1d4. The included ML predictions are rounded from the user's printed evidence; exact full-precision verification errors require the original manifest/prediction CSV.

## Evidence packaging
Generated a user-downloadable ZIP `G02_SECTION13_Q3D_VERIFICATION_READY_20261105.zip` with unchanged V63 original solver script, new guarded verification launcher, reconstructed manifest, source-only reconstruction utility, Windows instructions and four dry-run configurations. The ZIP is present in the conversation sandbox, **not in GitHub**. This markdown is the archived method/provenance record.

## Scientific constraints
Neither solver completion nor a pair of R3/R5 runs automatically proves numerical convergence. Extract native full matrices and mesh/adaptive-pass evidence, verify the 1 GHz header independently, and retain failed attempts. The known 83 invalid new-design matrix predictions and OPT00662's four positive-CAB local perturbations must remain in the report. No claim of optimized Q3D improvement until independent new simulations and a proper matched baseline.

Related: [Section 12B actual findings](G02_SECTION12B_PREFLIGHT_ACTUAL_RESULTS_20261105.md).
