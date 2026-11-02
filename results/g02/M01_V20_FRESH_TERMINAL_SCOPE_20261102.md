# M01 v2.0 fresh terminal-scope A/B audit

Evidence: user-supplied G02_M01_TERMINAL_FRESH20_diagnostic.zip; original A is the 1 GHz 8-pass Maxwell top-face-voltage solution. B uses whole-Cu-object voltage assignments 0/1/1/0 V on object IDs 69/113/157/201, in a new project without prior `.aedtresults`. Analyze returned 0 and wrote new Matrix, mesh, convergence evidence.

A: C_AA 36.474 fF, C_AB -12.183 fF, G_AA 0.069444 mS, G_AB -0.020013 mS. B: C_AA 36.474 fF, C_AB -12.183 fF, G_AA 0.069443 mS, G_AB -0.020013 mS. Both show 51,308 tetrahedra and 8 adaptive passes. Result: changing Maxwell voltage assignment from TSV top face to whole Cu object did not materially affect exported C/G, so it does not explain Q3D-v-Maxwell G discrepancy. This does not prove Q3D and Maxwell terminal/reference semantics are identical; similar mesh/pass history is a caveat. Solver loss-error 2.0011% > configured 1%.

Next priority: compare matrix reduction and complex admittance conventions plus effective outer/reference boundaries; no more terminal scope sweeps. G02 remains OPEN.