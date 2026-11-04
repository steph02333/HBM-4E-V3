# G02 V6.3 — CURRENT CORRECTED EVIDENCE (2026-11-04)

**Passwise Maxwell C-matrix data are NOW RECOVERED from all five MCAP/ASOL archives.** 450 DOE, 900 R3/R5 folders, 898 successful runs, 4,225 pass matrices from successful runs and 11 partial matrices from failed DOE0447 attempts. Of 897 successful runs with adjacent passes, **817 meet <1% for every individual Cself and Cmutual, 80 fail CAB <1%**. Among 450 DOE: **380 both R3/R5 meet last-pass <1%, 56 only one, 12 neither, 1 single-pass exception (DOE0402), 1 license failure (DOE0447)**. Ansys matrix Delta C <0.5% was recorded in 897 runs but DOES NOT guarantee every small CAB <1%. All native matrix SD files declare 1 GHz; older text exports still show an unexplained 1kHz header.

**The old 374 provisional ML / 75 mandatory mesh repairs, 137 P1 / 271 P2 queues, and 76-point Batch A/B continuation are RETIRED AS DECISION RULES.** R3 final vs R5 final differences are separate independent-run sensitivity, not within-run further adaptive refinement. Current passwise audit: [full evidence report](G02_V63_450POINT_PASSWISE_CSELF_CMUTUAL_AUDIT_20261104.md); [450-row DOE status table](G02_V63_ALL450_DOE_FINAL_PASS_WORST_COEFFICIENTS_20261104.csv). G02 remains OPEN; no automatic ML-label certification.

# V6.4 four-solve smoke test — HISTORICAL; campaign STOPPED

**The remaining Batch A solves are not authorized under the superseded 76-point remediation plan.** See [corrected ledger](G02_PRODUCTION_DOE_OPEN_MESH_FOLLOWUP_LEDGER.md).

Four extra independent solutions: DOE0380 and DOE0240 under M_A (PerRefine=7) and M_B (oxide surface length multiplier 0.8). Historical final-solution observations:

| DOE/term | Old R3/R5 C difference | R5 total | M_A total | M_B total | R5/M_A C difference | R5/M_B C difference |
|---|---:|---:|---:|---:|---:|---:|
| DOE0380 CAA | 6.2131% | 3944 | 4248 | 5468 | 0.1463% | 0.1295% |
| DOE0240 abs(CAB) | 7.8223% | 10354 | 14074 | 10354 | 0.8560% | 0.0005% |

DOE0240 M_B matched R5 total elements with near-identical C; this does not independently establish a finer mesh. All comparisons shown are final outputs of *independent* solves, not the within-run successive adaptive pass Cself/Cmutual analysis. Requested 1 GHz versus export 1 kHz frequency issue remains OPEN.

**Preserve these four results, but do not launch the remaining batch based on the retired screen.** Inspect native Solution Data > Matrix > Pass first.
