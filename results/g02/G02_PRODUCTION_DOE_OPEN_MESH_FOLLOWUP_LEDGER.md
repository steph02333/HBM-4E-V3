# G02 V6.3 — CURRENT CORRECTED EVIDENCE (2026-11-04)

**Passwise Maxwell C-matrix data are NOW RECOVERED from all five MCAP/ASOL archives.** 450 DOE, 900 R3/R5 folders, 898 successful runs, 4,225 pass matrices from successful runs and 11 partial matrices from failed DOE0447 attempts. Of 897 successful runs with adjacent passes, **817 meet <1% for every individual Cself and Cmutual, 80 fail CAB <1%**. Among 450 DOE: **380 both R3/R5 meet last-pass <1%, 56 only one, 12 neither, 1 single-pass exception (DOE0402), 1 license failure (DOE0447)**. Ansys matrix Delta C <0.5% was recorded in 897 runs but DOES NOT guarantee every small CAB <1%. All native matrix SD files declare 1 GHz; older text exports still show an unexplained 1kHz header.

**The old 374 provisional ML / 75 mandatory mesh repairs, 137 P1 / 271 P2 queues, and 76-point Batch A/B continuation are RETIRED AS DECISION RULES.** R3 final vs R5 final differences are separate independent-run sensitivity, not within-run further adaptive refinement. Current passwise audit: [full evidence report](G02_V63_450POINT_PASSWISE_CSELF_CMUTUAL_AUDIT_20261104.md); [450-row DOE status table](G02_V63_ALL450_DOE_FINAL_PASS_WORST_COEFFICIENTS_20261104.csv). G02 remains OPEN; no automatic ML-label certification.

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

## 2026-11-05 — V6.5 Phase B supplemental results (LATEST)

[Phase B full 36-solve native MCAP/ASOL audit](G02_V65_PHASEB_R246_12DOE_36SOLVE_PASSWISE_AUDIT_20261105.md). All 36 R2/R4/R6 simulations solved; **8/12** old doubly failing DOE now have a passwise <1% run. **Updated 450-DOE total = 445 with at least one passing run**, four CAB last-pass failures (DOE0099, DOE0100, DOE0233, DOE0321), one Student license failure (DOE0447). The earlier 380 both R3/R5 pass and 817/897 pass results remain accurate for their ORIGINAL V6.3 runs only; they do not reflect new V6.5 extra runs. No physics/ML eligibility conclusion. G02 OPEN.

## LATEST — 2026-11-05 V6.7 Phase C (overrides earlier 445/450 count)

Verified [seven-run native MCAP Phase C audit](G02_V67_PHASEC_R1_FOUR_CAB_OUTLIERS_DOE0447_7SOLVE_AUDIT_20261105.md): **7/7 solves completed**. DOE0100 R1 is now last-pass <1% (worst 0.537153%), and license-failed DOE0447 now has three successful R1 runs (6/8/10um seed, all passwise <1%), selected original-seed 8um run (worst 0.022070%). The current operational all-DOE count is **447/450 with at least one numerically stable native C matrix**; 3 CAB outliers remain DOE0099, DOE0233, DOE0321. Selecting the last-pass-best R is **not** proof of physics accuracy; preserve every original and additional run. Never use a C matrix from an R other than the explicitly selected R as its ML label. Native 1 GHz versus textual 1kHz header remains open. **G02 OPEN.**
