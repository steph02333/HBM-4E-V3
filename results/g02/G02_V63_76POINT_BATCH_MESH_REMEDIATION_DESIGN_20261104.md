# G02 V6.3 — CURRENT CORRECTED EVIDENCE (2026-11-04)

**Passwise Maxwell C-matrix data are NOW RECOVERED from all five MCAP/ASOL archives.** 450 DOE, 900 R3/R5 folders, 898 successful runs, 4,225 pass matrices from successful runs and 11 partial matrices from failed DOE0447 attempts. Of 897 successful runs with adjacent passes, **817 meet <1% for every individual Cself and Cmutual, 80 fail CAB <1%**. Among 450 DOE: **380 both R3/R5 meet last-pass <1%, 56 only one, 12 neither, 1 single-pass exception (DOE0402), 1 license failure (DOE0447)**. Ansys matrix Delta C <0.5% was recorded in 897 runs but DOES NOT guarantee every small CAB <1%. All native matrix SD files declare 1 GHz; older text exports still show an unexplained 1kHz header.

**The old 374 provisional ML / 75 mandatory mesh repairs, 137 P1 / 271 P2 queues, and 76-point Batch A/B continuation are RETIRED AS DECISION RULES.** R3 final vs R5 final differences are separate independent-run sensitivity, not within-run further adaptive refinement. Current passwise audit: [full evidence report](G02_V63_450POINT_PASSWISE_CSELF_CMUTUAL_AUDIT_20261104.md); [450-row DOE status table](G02_V63_ALL450_DOE_FINAL_PASS_WORST_COEFFICIENTS_20261104.csv). G02 remains OPEN; no automatic ML-label certification.

# RETIRED — 76-point remediation batch plan

**DO NOT EXECUTE. Superseded 2026-11-04.**

Old 23+52+1 Batch A/B plan selected 75 points using R3/R5 **final-run** C coefficient difference >=2% plus the separate DOE0447 surface-license failure. These differences are independent-solve sensitivity measurements, not within-run adaptive-refinement convergence. The 2% operational filter and optional 5%/10% final-element growth rules were not professor requirements.

New evidence: 898 successful runs, 4225 recorded adaptive passes, 897 defined final Ansys matrix Delta C results <0.5%. These do not prove every small Cmutual term is individually stable <1%. Original ZIPs contain only final full C matrices; native Q3D Matrix > Pass may expose per-pass C matrices if projects/results are retained.

**Next:** test retrieving two adjacent-pass full Maxwell matrices from a single original project; then decide whether targeted follow-up solving is needed. Preserve all frozen geometries and solver output. DOE0447 still needs a Student-safe solve.

Current guidance: [corrected evidence ledger](G02_PRODUCTION_DOE_OPEN_MESH_FOLLOWUP_LEDGER.md).
