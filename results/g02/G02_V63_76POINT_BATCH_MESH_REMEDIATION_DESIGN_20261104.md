# RETIRED — 76-point remediation batch plan

**DO NOT EXECUTE. Superseded 2026-11-04.**

Old 23+52+1 Batch A/B plan selected 75 points using R3/R5 **final-run** C coefficient difference >=2% plus the separate DOE0447 surface-license failure. These differences are independent-solve sensitivity measurements, not within-run adaptive-refinement convergence. The 2% operational filter and optional 5%/10% final-element growth rules were not professor requirements.

New evidence: 898 successful runs, 4225 recorded adaptive passes, 897 defined final Ansys matrix Delta C results <0.5%. These do not prove every small Cmutual term is individually stable <1%. Original ZIPs contain only final full C matrices; native Q3D Matrix > Pass may expose per-pass C matrices if projects/results are retained.

**Next:** test retrieving two adjacent-pass full Maxwell matrices from a single original project; then decide whether targeted follow-up solving is needed. Preserve all frozen geometries and solver output. DOE0447 still needs a Student-safe solve.

Current guidance: [corrected evidence ledger](G02_PRODUCTION_DOE_OPEN_MESH_FOLLOWUP_LEDGER.md).
