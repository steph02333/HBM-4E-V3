# G02 Maxwell M01 v1.7 — L4 adaptive pass 8 result (2026-11-02)

Source evidence: user-uploaded `G02_M01_ADAPT8_17_diagnostic.zip` with `status.json`, `convergence.conv`, `mesh.ms`, `CG_matrix.txt`, and console. Original L4 .aedt hash pre/post identical `e74a8b6501c69b0410e219579b18d66fe46e028c3ae26fdf779280db36a16de8`. Copied .aedtresults used. Native Analyze returned 0.

## Native mesh history (same adaptive sequence)
Pass 1-8 tetrahedra: 8167, 10620, 13810, 17956, 23347, 30356, 39466, **51308**.
Loss error (%): 13.285, 7.0392, 4.2287, 3.5413, 2.9639, 2.5478, 2.3503, **2.0011**.
Pass 8 Delta Loss: **0.010455%**. Convergence file header says `Current: (1.6729, N/A)`, which differs from pass table 2.0011%; both exceed configured 1% error target. All 8 of 8 maximum passes used. **Formal native solver-error criterion NOT MET**.
Mesh distribution at pass 8: silicon 31635; oxide liner objects 2941,2925,2928,2888; Cu objects 1949,2042,2049,1951. Exact 1GHz confirmed by matrix `Adaptive Freq: 1000000000Hz`. Student limit 64000; next 30% refinement projects ~66,700, exceeding cap (estimate only). Do not attempt pass 9 blindly.

## Matrix comparison
Native Pass 8 Maxwell matrix `G,C` units mSie,pF:
- G=[[0.069444,-0.020013],[-0.020013,0.069447]] mS.
- C=[[0.036474,-0.012183],[-0.012183,0.036475]] pF.
Pass 6 L4 prior export: G_AA=.069375mS, G_AB=-.019982mS, C_AA=36.484fF, C_AB=-12.187fF.
Change Pass6->Pass8, prior denominator: C_AA -0.0274%; abs(C_AB) -0.0328%; G_AA +0.0995%; abs(G_AB) +0.1551%.
This supports **matrix-entry mesh stability under continued refinement**, though we have no separately exported pass7 matrix and loss-error target remains unmet. Symmetric positive definite reduced C/G matrices. Not proof of current conservation or physical reference correctness.

## Q3D comparison, provisional
V4.0 DOM10_M25_R18 same nominal geometry/conductivity requested 1GHz: C_AA=35.481712fF, C_AB=-11.618261fF, G_AA=.061592086mS, G_AB=-.016418221mS. Pass8 Maxwell discrepancies approx +2.80% C_AA, +4.86% abs(C_AB), +12.75% G_AA, +21.90% abs(G_AB). **Hold cross-solver validation open** because exact Q3D exported headers read 1Hz/1kHz despite requested 1GHz, and silicon outer domain, reference, boundary/current-return equivalence require independent verification. A small C discrepancy is not full semiconductor physical-model validation.

## Decision
Do not re-run L1-L4 or attempt pass 9. Preserve v1.7 solved copy .aedt/.aedtresults; make Q3D native exact-case 1GHz confirmation and geometry/reference comparator the next priority. Stage3 tox0.5/sigma1 targeted cases only if reference match is established. G02 remains OPEN; DOE qualifications still distinct.
