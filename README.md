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
**GATE 01: Analytical benchmark — OPEN / NOT PASSED**

First reproduce the simple cylindrical Cu/SiO2 capacitor benchmark at multiple radius, height and oxide-thickness combinations. Distinguish an ideal coaxial test from real Cu/SiO2/semiconductor TSV capacitance. Compare identical geometries and electrical boundary conditions.

See:
- [Validation roadmap](docs/VALIDATION_GATE.md)
- [Analytical benchmark specification](docs/01_ANALYTICAL_BENCHMARK.md)
- [Decisions and evidence log](docs/DECISION_LOG.md)

## Source direction
Prof Lim's 25–26 September 2026 email: analytical benchmark; adaptive-mesh convergence and matrix sanity checks; domain sensitivity; independent-solver comparison; then realistic Si resistivity and GSG/GSSG/GSGSG layouts; finally Sentaurus pilot to determine whether voltage is justified as an ML input.

Literature (CA1): Wang et al., *Microelectronics Journal* 45 (2014), 205–210, cylindrical TSV oxide capacitance equation (Eq. 5) and MOS-effect discussion. The paper's <5% agreement is its **published finding**, not our own V3 result.
