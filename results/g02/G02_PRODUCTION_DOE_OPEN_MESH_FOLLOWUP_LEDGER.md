# G02 numerical evidence — CORRECTED 2026-11-04

**CURRENT interpretation: G02 OPEN. The prior "374 ML provisionally retained / 75 mandatory repair", P1/P2 final-mesh separation screening and the 76-point V6.4 remediation plan are RETIRED as action criteria.**

## Verified raw-data findings
- 450 original DOE; 449 successful R3/R5 pairs (898 Q3D solves); DOE0447 failed the 8000 3D-surface-element Student limit (8030 R3, 8340 R5).
- All 898 successful runs have adaptive-pass convergence logs containing 4225 pass records. Of 897 runs with a defined final Ansys *matrix* Delta C, 897 are <0.5%. DOE0402 R3 had only one pass.
- R3 and R5 are separate adaptive solves, PerRefine 3 vs 5. **Their final total-element difference is NOT a within-run adaptive-pass refinement measurement.**
- Historical R3/R5 worst coefficient differences: 312 <1%; 62 from 1 to <2%; 64 from 2 to <5%; 11 >=5%. These are **independent-solve sensitivity statistics**, not a professor-mandated convergence pass/fail classification.
- Final total mesh growth median R3-to-R5 +5.16%; 12 R5 total counts are smaller than R3. Exported total-element mesh counts differ from the surface-element license counter.
- The ZIP exports have only the final full C matrices, not the full matrix for each pass. Ansys matrix Delta C does **not guarantee that each Cself/Cmutual coefficient** changed <1%, especially small off-diagonals.
- OPEN provenance/physics: requested 1 GHz vs exported 1 kHz headers, simplified H0 conductive-silicon representation, domain effects and professor validation gates.

## What the professor's further-refinement criterion requires
Within **one** adaptive Q3D solution, compare successive passes p and p+1; report actual pass triangle counts and relative change in individual Cself and Cmutual matrix coefficients (target ~<1%). Q3D Solution Data > Matrix > Pass can select an adaptive pass *if native project/result data are retained*. The internal matrix Delta C is supporting matrix-level evidence, not a universal per-coefficient bound. A fixed +5% or +10% final total-element increase was never an official or professor requirement.

## Action
1. **Stop** the old 76-point Batch A/B execution plan; no automatic 44-run continuation.
2. **Preserve** all original DOE geometry, C matrices, logs, scripts and historical independent-solve evidence; do not delete raw scientific results.
3. Test one saved native AEDT project via Results > Solution Data > Matrix > View > Pass. Export two adjacent passes' Maxwell C matrices. Only then determine whether per-pass coefficient validation can be automated for the remaining runs.
4. Until that check, neither the 374 former "provisional retain" label nor the 75 former "mandatory repair" queue is an approved status. **G02 remains OPEN.**

Original per-chunk audits and the retired screening summaries remain historical snapshots, not current solver-convergence certification.
