# G01 — Analytical benchmark specification (draft; NOT YET RUN)

## Objective
Validate Ansys Q3D extraction against an independently calculable **single cylindrical Cu/SiO2 coaxial capacitance**. This checks solver setup and extraction under the *same electrical boundary conditions*. It does not establish a realistic semiconductor TSV model by itself.

## Governing formula
```
C_ox [F] = 2*pi*eps0*epsr_ox*h / ln((r+t_ox)/r)
eps0 = 8.8541878128e-12 F/m
epsr_ox = 3.9 (initial nominal value)
```
r, h and t_ox are in metres. Reference: Wang et al. (2014), Section 2.2, Eq. (5).

## Geometry and nets
- Inner perfectly conducting (or high-conductivity Cu) cylinder radius r, length h, net SIGNAL.
- Concentric SiO2 layer spanning r to r+t_ox.
- Outer conductor at r+t_ox, net GROUND/reference.
- The analytical result assumes a long uniform coaxial field without appreciable end effects. Ideally test with end effects suppressed, or perform length/aspect-ratio sensitivity and explain residual fringe capacitance.
- A floating Si body, Si dielectric body, or substrate with finite conductivity **does not reproduce this ideal capacitor** and cannot be substituted without modifying the benchmark.
- Ensure Cu metal/oxide/outer conductor interfaces do not overlap geometrically; define end caps and guard arrangements explicitly before running.

## Proposed initial nine-point test (fresh runs only)
| Case | r (µm) | h (µm) | tox (µm) |
|---|---:|---:|---:|
| B01 | 1.5 | 25 | 0.1 |
| B02 | 1.5 | 37.5 | 0.3 |
| B03 | 1.5 | 50 | 0.5 |
| B04 | 2.25 | 25 | 0.3 |
| B05 | 2.25 | 37.5 | 0.5 |
| B06 | 2.25 | 50 | 0.1 |
| B07 | 3.0 | 25 | 0.5 |
| B08 | 3.0 | 37.5 | 0.1 |
| B09 | 3.0 | 50 | 0.3 |

These are *design choices*, not a claim of industry TSV dimensions. For single-TSV validation, D=2r.

## Required saved results
For each Bxx: JSON/CSV manifest of units, geometry, reference treatment, material property, Ansys/PyAEDT versions, mesh settings, boundary setup, solve status; full capacitance matrix; Q3D extracted C(SIGNAL, ground); analytical value; % error; convergence pass history.

## Error
```
relative_error_percent = 100*abs(C_Q3D - C_analytical)/C_analytical
```
**Predeclared initial acceptance target:** ≤5% in ideal geometry, aligned with Prof Lim's published-paper example; the 5% is NOT a universal physical guarantee. Study sensitivity to end effects before interpreting any discrepancy.

## Exit evidence
- Script committed and run on local Ansys install, all Bxx result files present.
- Geometry and reference assignment independently inspected.
- Analytical values confirmed in SI units; C matrix convention documented.
- Error table, systematic deviations and failures explained.
- Reviewed and marked PASS in docs/VALIDATION_GATE.md.

**Current status: NOT RUN, NO V3 RESULTS.**
