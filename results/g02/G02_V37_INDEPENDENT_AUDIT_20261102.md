G02 V3.7 audit (2026-11-02) — G02 remains OPEN.

Uploaded ZIP: 42/42 solved. Raw design messages have zero CG nonconvergence warnings; internal adaptive convergence alone is not mesh proof.

Higher-order GSSG same model 1GHz no contact:
sigma 1 S/m r14/seed16 total mesh 2396/2880: worst C difference 0.132%, worst G difference 0.108%.
sigma 10 S/m r14/seed16 mesh 3272/3580: worst C 0.044%, G 0.082%, but coarse/fine regime discontinuity requires caution.
sigma 100 S/m r12/r14 mesh 6248/6632: worst C 0.350%, G 1.326%; r14/seed16: C 0.160%, G 1.776%; r10/r12: G 8.373%. Higher Direct versus Iterative at r12 offdiagonal G differs 5.451%. No G qualification for 100 S/m.

At 10 S/m G_AB(mS), refinement 7/10/12: no contact -0.016600/-0.016715/-0.016872; edge contact +0.003674/+0.002706/+0.002767; corner contact -0.009907/-0.010096/-0.010190. Actual GetAssignment net mappings captured. Contact location changes sign, not a validated ohmic semiconductor contact. Charge/current continuity unverified.

Frequency: 9 separately solved Higher-order 1/100/1000 MHz cases (3 conductivities) internally converged; default matrix headers show 1Hz/100Hz/1kHz (factor 1e6 mismatch). Other explicit export selectors give inconsistent headers but exactly the same C/G values within a given LastAdaptive solution. GUI/native API verification needed; do not rewrite header and claim solved.

Full independent audit supplied as user-downloadable markdown. Keep G02 OPEN and no ML DOE until physical contact, charge, domain, topology and independent matrix interpretation are qualified.