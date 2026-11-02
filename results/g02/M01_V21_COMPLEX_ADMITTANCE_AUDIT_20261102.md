# G02 M01 v2.1 Complex Admittance Audit — 2026-11-02

Sources: V4.0 Q3D raw DOM10_M25_R18 `result.json` and original matrix `CG_export_default.txt`; Maxwell M01 v2.0 fresh whole-object voltage `CG_matrix.txt`. No new solve.

At f=1GHz, compute Y=G+j(2pi f)C, unit conversion Q3D C fF, Maxwell C pF, G both mSie. Q3D output `Reduce Matrix: Original`; Maxwell output `G,C` and `Re(Y), Im(Y)`.

Q3D AA: C=35.481712fF, G=.061592086mS, ImY=.222938174mS. Maxwell AA: C=36.474fF, G=.069443mS, ImY=.229172901mS. Complex Y relative difference=4.33456%.
Q3D AB: C=-11.618261fF, G=-.016418221mS, ImY=-.072999685mS. Maxwell AB: C=-12.183fF, G=-.020013mS, ImY=-.076548047mS. Complex Y relative difference=6.75067%.
Maxwell directly printed ImY .22917 and -.07655mS, matching omega*C within printed precision. G is directly Re(Y). Therefore no simple units or real-vs-imaginary-part misinterpretation explains G mismatch. G-only discrepancies AA +12.75%, mutual +21.90%; C +2.80%, +4.86%. Q3D source export misleadingly labels 1kHz, but saved native .asol LastAdaptive is 1GHz; strict matrix-to-saved-solution link still pending.

Geometry and materials and 2 signal+2 grounds match; Q3D GroundNet/Original semantics vs Maxwell grounded voltage matrix and default outer silicon boundary semantics are not yet demonstrated equivalent. Maxwell pass8 has 51308 tets; native solver Loss Error 2.0011% exceeds configured 1% despite Pass6-to-8 matrix changes below .16%; independent current conservation not checked. G02 OPEN.

Next: perform one native read-only exact saved Q3D Matrix view/readback at 1GHz, compare to archived numbers; inspect solver boundary/reference semantics. No new large DOE or new Maxwell mesh levels before targeted reference check. Full reproducible report in current user deliverable G02_M01_V21_ADMITTANCE_AUDIT.md.