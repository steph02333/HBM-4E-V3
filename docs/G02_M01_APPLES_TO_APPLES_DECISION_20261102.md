# G02 M01 apples-to-apples decision — 2026-11-02

Decision: **CONDITIONAL GO** for frequency/reference verification and narrowly targeted Stage 3; **NO-GO** for declaring solver-independent physics validation completed or final DOE model frozen.

Evidence reviewed: real V4.0 raw `G02_V40_targeted_results_bundle.zip` DOM10_M25_R18; Q3D construction `G02_V40_targeted_qualification.py`; Maxwell build `G02_M01_maxwell_build_v06.py`; actual M01 v1.7 8-pass `G02_M01_ADAPT8_17_diagnostic.zip`.

## Geometry/material match established by code
Both GSSG, core D4 um, center pitch15 um, height35 um, oxide liner.3 um, Si margin25 um, eps Si11.7, eps oxide3.9, sigma Si10 S/m, four Cu TSVs, both without explicit substrate contact, Si and TSV extent z=0..35um. Q3D assigns four Cu as Signal/Signal/Ground/Ground nets and Si as lossy dielectric via `insulator_threshold=10000`; Maxwell assigns voltage faces (0,1,1,0)V at Cu tops and MatrixElectric signal/ground sources. **Ground boundary/current return and Matrix reduction still not proven equivalent**.

## Quantitative evidence
Q3D C_AA=35.481712fF, C_AB=-11.618261fF, G_AA=.061592086mS, G_AB=-.016418221mS. Maxwell pass8 C_AA=36.474fF, C_AB=-12.183fF, G_AA=.069444mS, G_AB=-.020013mS. Maxwell relative magnitude deviations +2.80%, +4.86%, +12.75%, +21.90%.

Maxwell L4 native continued adaptive mesh 30356 -> 39466 -> 51308 tets, pass6->pass8 matrix changes C_AA .027%, |C_AB| .033%, G_AA .099%, |G_AB| .155%, so matrix entry refinement stability supported. Native AC Conduction loss error at pass8 2.0011%, above 1% setup target. DO NOT call native solver convergence criterion met. Q3D V4 nominal 6-pass CG convergence current delta .11761% vs .5% target, but exact-case frequency export headers conflict (1Hz vs 1kHz depending export control), despite setup requested 1000MHz. Need native GUI/project readback from exact case before declaring actual 1GHz.

## Priority ordered tasks
1. Exact Q3D V4 case DOM10_M25_R18 source AEDT design: inspect setup / solution's actual frequency, compare native CG values at 1GHz against exported values. If source .aedt missing, rerun ONE exact-case Q3D with all config frozen and export native evidence; do not relabel frequency headers.
2. Inspect Q3D and Maxwell physical reference: Cu Ground L/R, Si no-contact finite volume, external boundaries, Matrix reduction and admittance semantics; use read-only native project checks where possible, and one controlled diagnostic if needed. No broad sweep.
3. Only when nominal comparability established, run targeted tox=.5 and sigma=1 S/m representative Maxwell checks with mesh adequacy and same Q3D configurations. Focus cross-solver trends and explain G discrepancies.
4. Continue independent Q3D DOE planning but do NOT claim all previous G02 gaps closed; local oxide sigma1, sigma100 G mesh, finite Si domain and physical HBM substrate tie remain open.

G02 status: internal Q3D nominal C convergence supported; Maxwell 1GHz extracted and 8-pass matrix stability supported but solver error still >1%; cross solver C near (2.8–4.9%) and G off (12.8–21.9%); physical cross-validation remains conditional. This decision is recorded for later sessions, rather than inflating an exploratory comparison into proof.
