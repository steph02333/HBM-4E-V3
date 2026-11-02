# G02 v22 execution erratum — 2026-11-03

## Observed blocker

The user-reported diagnostic indicates both A1 and B1 source-setting attempts stopped before field integration with Python `NameError` at `sol.EditSources(ac, cg, dc, loss)`: `dc` and `loss` were not defined in the v22 runner. Thus 0/16 integrations were attempted; no physical conclusion is supported by this failed run.

## API evidence

Ansys Electronics Desktop 2025 R2 Q3D Extractor Scripting Guide documents `EditSources(acData, capData, dcData, harmonicLossData)`. Four arguments are required; changing the call to a two-argument form is not a sound fix. The DC and HarmonicLoss arguments must be valid AEDT array structures, consistent with actual design source names/settings. Reference: https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/Subsystems/Q3DExtractor/Subsystems/Q3DExtractor%20Scripting/Content/EditSources.htm

## Repair gate

1. Recover the exact `G02_Q3D_two_source_all_conductor_flux_v22.py` code and v22 diagnostic ZIP (not presently tracked in this repository).
2. Inspect current `ac`, `cg`, source names, existing DC/harmonic-loss source settings, and source-edit result.
3. Define valid `dc`/`loss` arrays (or reuse known-working arrays) before calling EditSources; do not guess that empty arrays will be accepted.
4. Preserve v21 native field-calculator stack and no-solve/copy-only safeguards; locally compile, lint undefined variables, test CLI, then run AEDT on a copied project.
5. Check both excitation setups and all 16 raw E-flux integrals, report signal vs C/G agreement, source reciprocity, conditional ground charges, and explicitly keep infinity-reference closure OPEN.

Status: repair analysis recorded; corrected AEDT runner NOT YET runtime validated.
