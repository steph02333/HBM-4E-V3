# G02 model freeze and targeted next steps (2026-11-02)

This is a **plan**, not a validated HBM4 die stack and not a G02 PASS.

## Research
User's uploaded `ilovepdf_merged.pdf` includes Weerasekera et al., IEEE TED (2016), “An Analytical Capacitance Model for Through-Silicon Vias in Floating Silicon Substrate.” It distinguishes 2.5D passive interposers with no substrate contacts from traditional active 2D/3D ICs with p+ substrate contacts. Do not transfer interposer assumptions to HBM DRAM. Wang et al., Microelectronics Journal 45(2) (2014), DOI 10.1016/j.mejo.2013.10.015 treats MOS depletion/bias; homogeneous Q3D lossy Si does not. Find a process/cross-section source locating actual stacked-DRAM substrate ties and isolation before a final model is chosen. If unavailable, compare explicit hypotheses with qualified limitations.

## Proposed H0/H1
H0: Cu GSSG signals/grounds + finite lossy Si, **no explicit substrate electrode**, Q3D infinity reference. Not automatically a truly floating substrate.
H1: physically sourced p+ substrate tie/backside connection, with location and connectivity declared. V3.9's arbitrary edge patch is not a validated ohmic contact. Do not declare H1 realistic without source.

## Maxwell
Official 3D AC Conduction: https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v261/en/Subsystems/Maxwell/Content/Maxwell/3DACConduction.htm .
Check Student license GUI before coding. Start matched nominal GSSG D4 P15 H35 tox0.3 σ10S/m Si εr11.7 oxide εr3.9, margin25 µm 1GHz. Voltage experiment SIG_A=1V SIG_B=0V and inverse, Ground Cu=0V. Compare complete terminal current Y=G+jωC, keep same reference and outer boundaries, account for all current flux. A geometric touching patch alone cannot demonstrate real ohmic semiconductor contact. Maxwell 3D AC conduction can assess continuous lossy medium physics; not carrier depletion/inversion.

## Targeted 18-case Python script supplied separately as G02_V40_targeted_qualification.py
Six sigma1 oxide local R18 tests on OX_1/OX_2 at L12/L8/L6; six sigma10 domain variation margin25/50/100 µm × R14/R18; six sigma10 geometry pilot D3/6, P10/20, tox0.1/0.5, compared to previously verified nominal. All are **provisional no-contact fixture**, not final-model DOE. Physical finite silicon body expands in domain test, therefore interpretation cannot be called purely numerical boundary independence. Script compiled and completed 18-case DRY RUN; not run in AEDT.

## G02 acceptance and DOE
Supervisor: D3-6 µm P10-20 µm H25-50 µm tox0.1-0.5 µm rho1/10/100 Ωcm = sigma100/10/1 S/m. GSG/GSSG/GSGSG; maintain valid P>D+2 tox, consistent terminal definitions. For every final topology and representative geometry/material corners, Cself and monitored Cmutual adaptive delta target <1%; signed matrix reciprocity, passivity, independent charge/current conservation, monotonic parameter trends, physically meaningful outer boundaries. GSG has no same-label AB mutual as GSSG. Revalidate final substrate reference and H corners; current nominal results alone are inadequate. Archive raw matrices and version settings, use quality gates for each DOE point, reserve held-out geometry corners, and confirm optimized designs with Q3D.

## Current evidence
V3.9 nominal Higher baseline consecutive settings <1% C all sigma1/10/100. Orthogonal oxide test for sigma1 C disagrees ~1.49%. Sigma100 G inconsistent >10%. Sigma10 no-contact C/G best validated. G02 remains OPEN.

Official Ansys Q3D lossy conductor/reference docs:
https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/Subsystems/Q3DExtractor/Content/Q3D/TNMatrixReductionIntro.htm
