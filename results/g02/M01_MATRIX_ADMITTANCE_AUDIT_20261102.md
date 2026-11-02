# Q3D–Maxwell nominal matrix convention audit (2026-11-02)

Inputs: original user ZIP `G02_M01_TERMINAL_FRESH20_diagnostic.zip/CG_matrix.txt`, original raw Q3D V4 `G02_V40_targeted_results_bundle.zip/cases/DOM10_M25_R18/CG_export_default.txt`, and Q3D native 1GHz `.asol` metadata checked previously.

## Units and mathematics (PASS for Maxwell internal consistency)
Maxwell exported at `Adaptive Freq: 1000000000Hz` and explicitly reports `Re(Y), Im(Y)` with admittance components in mS: diagonal SIG_A 0.069443 + j0.22917 mS, off-diagonal -0.020013 - j0.07655 mS. At 1GHz, `C = Im(Y)/(2*pi*f)` produces C_AA=0.0364735383pF=36.4735383fF and C_AB=-0.0121833109pF=-12.1833109fF. Maxwell separately reports `G,C` = (0.069443mS,0.036474pF) and (-0.020013mS,-0.012183pF). Discrepancy between reconstructed and reported C only rounding ~0.00127% diag and ~0.00255% coupling. Hence Maxwell's output is indeed consistent with Y=G+j omega C at 1GHz.

Q3D export explicitly labels `C Units:fF, G Units:mSie`, `Reduce Matrix: Original` and 2x2 nets SIG_A/SIG_B; Maxwell has matrix of V_SIG_A/V_SIG_B and two grounded references. Both have conventional symmetric off-diagonal negative mutual terms. This establishes *format/units compatibility*, NOT full physical boundary equivalence. The Q3D export frequency header reads 1kHz (alternates 1Hz), while saved native Q3D solution `Frequencies(1000000000)`; exact text-to-solution matrix data-link still unverified. Do not relabel header.

## Numbers, meaning, remaining gap
Q3D: C_AA=35.481712 fF, C_AB=-11.618261 fF, G_AA=0.061592086 mS, G_AB=-0.016418221 mS. Maxwell fresh whole-object B: 36.474 fF, -12.183 fF, 0.069443 mS, -0.020013 mS. Maxwell Pass8 former top-face A: near identical. Apparent discrepancy +2.797%, +4.862%, +12.747%, +21.896% in magnitudes. Fixed face-versus-object assignment does not explain gap. Neither finite Si external boundary nor reference-current paths yet independently confirmed equivalent. Maxwell pass8 native loss-error 2.0011% >1%; despite small matrix changes pass6->8. No C/G cross-solver threshold pre-established, so cannot assert validation pass merely by proximity.

## Decision
GO: stop mesh and terminal scope exploration; focus one targeted read-only solver boundary/reference audit and an optional single controlled diagnostic if a specific mismatch is found. NO-GO: claim physical validation complete / full DOE frozen. Stage3 tox=.5 sigma1 conditional; Q3D C-focused DOE planning can proceed with explicit caveats.
