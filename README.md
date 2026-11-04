## 2026-11-04 G02 evidence update

The original 450-point G02 V6.3 campaign (449 paired DOE; 898 successful Q3D solves) has now been **re-analysed using native successive Adaptive Pass Maxwell C matrices**. Of 897 runs with adjacent-pass evidence, **817 meet <1% for all individual Cself/Cmutual terms, and 80 fail on Cmutual (CAB)**. At DOE level, **380 both R3 and R5 meet the <1% pass-level criterion**, 56 one run meets it, 12 neither, 1 lacks two passes, and DOE0447 failed Student license. These are *numerical last-pass stability observations*; G02 and physics validation gates remain OPEN.

Old 374-retain/75-remediate R3-vs-R5 final-matrix screen and V6.4 76-point rerun plan are retired as convergence/ML decisions. See [full G02 MCAP audit](results/g02/G02_V63_450POINT_PASSWISE_CSELF_CMUTUAL_AUDIT_20261104.md) and [all 450 point-level statuses](results/g02/G02_V63_ALL450_DOE_FINAL_PASS_WORST_COEFFICIENTS_20261104.csv). The complete 900-run and 4,236-pass local analysis artifacts are kept separately; historical documents are marked as superseded.

# HBM-4E-V3 — CA2 Research Reboot

NUS FYP: validation-led modelling of HBM-relevant TSV interconnect parasitics using Ansys Q3D as a **reference EM solver** (not experimental ground truth).

## Non-negotiable research policy
- **All prior CA2 simulation labels, DOE datasets, ML results and optima are excluded from V3 validation.** Prior work provides lessons only.
- **One task at a time.** A stage can advance only after its evidence, quantitative checks, documented limitations, and review sign-off are recorded in `docs/VALIDATION_GATE.md`.
- No DOE / ML / optimization before Prof Lim's validation and fidelity requirements have been addressed.
- Every run must have a unique ID, configuration, source code version, solver version, outputs, and QA result.
- Do not claim experiments have passed until new solver evidence has been inspected.
- Keep scripts, documentation, summaries and small curated outputs in Git; retain heavy Ansys projects and raw solver files locally.

## Local results root (Windows)
`C:\CA2 result V2`

This is a **path on the researcher's computer**, not a directory GitHub or ChatGPT can directly access. Set it as the output root in future scripts. Never hard-code another machine's user profile or desktop folders.

Proposed local structure:
```text
C:\CA2 result V2\
  01_analytical_benchmark\
    configs\
    ansys_projects\
    raw_exports\
    analysis\
    reports\
  02_numerical_convergence\
  03_independent_solver\
  04_material_topology\
  05_sentaurus_pilot\
  06_final_doe_ml\
```

## Current research gate
**GATE 01: Analytical benchmark — PASSED (ideal coax only); GATE 02: numerical/physical consistency — OPEN**

First reproduce the simple cylindrical Cu/SiO2 capacitor benchmark at multiple radius, height and oxide-thickness combinations. Distinguish an ideal coaxial test from real Cu/SiO2/semiconductor TSV capacitance. Compare identical geometries and electrical boundary conditions.

See:
- [Validation roadmap](docs/VALIDATION_GATE.md)
- [Analytical benchmark specification](docs/01_ANALYTICAL_BENCHMARK.md)
- [Decisions and evidence log](docs/DECISION_LOG.md)

## Source direction
Prof Lim's 25–26 September 2026 email: analytical benchmark; adaptive-mesh convergence and matrix sanity checks; domain sensitivity; independent-solver comparison; then realistic Si resistivity and GSG/GSSG/GSGSG layouts; finally Sentaurus pilot to determine whether voltage is justified as an ML input.

Literature (CA1): Wang et al., *Microelectronics Journal* 45 (2014), 205–210, cylindrical TSV oxide capacitance equation (Eq. 5) and MOS-effect discussion. The paper's <5% agreement is its **published finding**, not our own V3 result.

## Latest G02 V6.5 targeted refinement (2026-11-05)

[Audited Phase B: 36 new R2/R4/R6 solves](results/g02/G02_V65_PHASEB_R246_12DOE_36SOLVE_PASSWISE_AUDIT_20261105.md). **36/36** solved, **8/12** previously unresolved DOE found individual last-pass Cself/Cmutual <1% solutions. In total **445/450** DOE have at least one successful run meeting this *numerical stability screen*. Remaining: DOE0099, DOE0100, DOE0233, DOE0321 and Student-license DOE0447. G02 physical/numerical validation remains OPEN.

## CURRENT G02 V6.7 status (2026-11-05; supersedes Phase B 445/450)

**Phase C 7/7 solved; 447/450 DOE have at least one last-pass all-coefficient <1% run. DOE0447 was recovered with R1 original 8um mesh seed. The three remaining CAB numerical stability outliers are DOE0099, DOE0233 and DOE0321.** The prior 445/450 from Phase B remains a historical count, not the latest. Every ML label candidate C matrix must be sourced from its selected R and selected case. [Detailed V6.7 audit](results/g02/G02_V67_PHASEC_R1_FOUR_CAB_OUTLIERS_DOE0447_7SOLVE_AUDIT_20261105.md). Physical validation G02 OPEN.
