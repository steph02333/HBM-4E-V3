# G02 V6.3 — CURRENT CORRECTED EVIDENCE (2026-11-04)

**Passwise Maxwell C-matrix data are NOW RECOVERED from all five MCAP/ASOL archives.** 450 DOE, 900 R3/R5 folders, 898 successful runs, 4,225 pass matrices from successful runs and 11 partial matrices from failed DOE0447 attempts. Of 897 successful runs with adjacent passes, **817 meet <1% for every individual Cself and Cmutual, 80 fail CAB <1%**. Among 450 DOE: **380 both R3/R5 meet last-pass <1%, 56 only one, 12 neither, 1 single-pass exception (DOE0402), 1 license failure (DOE0447)**. Ansys matrix Delta C <0.5% was recorded in 897 runs but DOES NOT guarantee every small CAB <1%. All native matrix SD files declare 1 GHz; older text exports still show an unexplained 1kHz header.

**The old 374 provisional ML / 75 mandatory mesh repairs, 137 P1 / 271 P2 queues, and 76-point Batch A/B continuation are RETIRED AS DECISION RULES.** R3 final vs R5 final differences are separate independent-run sensitivity, not within-run further adaptive refinement. Current passwise audit: [full evidence report](G02_V63_450POINT_PASSWISE_CSELF_CMUTUAL_AUDIT_20261104.md); [450-row DOE status table](G02_V63_ALL450_DOE_FINAL_PASS_WORST_COEFFICIENTS_20261104.csv). G02 remains OPEN; no automatic ML-label certification.

# SUPERSEDED — historical R3/R5 2% sensitivity screening

**Retired 2026-11-04 as a convergence/ML eligibility decision rule.** See [corrected G02 ledger](G02_PRODUCTION_DOE_OPEN_MESH_FOLLOWUP_LEDGER.md).

449 paired DOE (898 successful solves), one double-failed DOE0447; R3-vs-R5 worst individual C differences: 312 <1%, 62 in 1–<2%, 64 in 2–<5%, 11 >=5%. These are authentic **independent adaptive-run final-matrix differences**, not the professor's pass-to-pass further-refinement test.

The prior claim "374 points provisionally eligible for ML, 75 definitively require mesh remediation" is **withdrawn** as a conclusion from this test. Likewise, the old 76-point remediation plan is stopped.

The five raw ZIPs contain 898 CG adaptive histories with 4225 pass rows. In 897 runs with available final matrix Delta C, 897 are <0.5%; DOE0402 R3 has only one pass. However, matrix Delta C alone does **not** certify each Cself and Cmutual changed <1%. Archived ZIP files lack full per-pass C matrices, but native AEDT Solution Data > Matrix > Pass may expose them if original project/results are saved.

DOE0447 exceeded the Student 8000 surface-element cap with 8030/8340. Exported total mesh element counts are not the license surface counter. Frequency header mismatch and H0 model validity remain OPEN.

**Do not run the old V6.4 76-point remediation without a new evidence-led decision.**
