# G02 campaign audit (2026-11-01)

Run 20261101_182605_f200da. ZIP SHA-256: 62453654b7aa0573b10e6cb785ced0cd2479d46fdb650f95c0ad26ce42ede0b5. All 18 cases solved. **G02 OPEN: not all validation tests passed.**

## Results

- C-matrix symmetry: 18/18 symmetric to exported precision.
- Matrix passivity: 18/18 with positive minimum eigenvalue.
- Geometry trends: pitch 10 to 20 um decreases mutual magnitude 4.437744 to 2.964081 fF; D 3 to 6 um increases 2.886111 to 4.687607 fF; liner 0.1 to 0.5 um decreases 3.809466 to 3.170668 fF.
- Mesh independence **not proven**: mesh_lo, mesh_mid, mesh_hi, mesh_tight stopped at the SAME 4 passes, SAME 4358 total elements, SAME 2748 surface triangles and numerically identical capacitances. Different requested settings did not produce a finer mesh.
- Domain sensitivity **fails initial 1% target**: 27 to 40 um silicon margin changes A self +0.97863%, B self +3.45128%, mutual magnitude -1.19085%.
- Charge conservation not demonstrated: reduced matrix row sums cannot be used as a full charge balance with ground excluded.
- Student mesh limit not observed: largest case had 7368 total elements. Do not blame license limitations without a recorded failure.
- Caveat: silicon in this runner has conductivity zero and relative permittivity 11.7. It is a preliminary dielectric fixture, not realistic 10 ohm-cm Si.

## Mandatory next fixes

1. Actually force finer meshes and verify differing element counts; compare self and mutual changes across multiple genuinely refined meshes.
2. Redesign/extend domain study and distinguish finite silicon geometry from artificial computational boundary truncation.
3. Add electrical reference/ground charge accounting and physical silicon conductivity considerations.
4. Repeat the important convergence checks on the finalized physics fixture before any DOE or ML.
