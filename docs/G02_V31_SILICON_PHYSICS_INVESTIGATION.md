# V3.1 Q3D conductive silicon interpretation study (2026-11-01)

G02 remains **OPEN**. New experiment script: `G02_V31_silicon_physics_probe.py` delivered in project chat; locally syntax-checked and dry-run packaged, not yet executed in Ansys. The file SHA is recorded in the returned bundle.

## Crucial vendor finding
Ansys Q3D documentation says **unassigned conducting objects are grounded** in CG computations, rather than necessarily floating. Accordingly, our previous lower-threshold silicon result is compatible with an unintended grounded shielding body. Net classification versus lossy-dielectric participation must be established experimentally. Default-threshold 10 S/m has nonzero G and is promising, but not yet a certified physical lossy substrate.

Official evidence:
- https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v261/en/Subsystems/Q3DExtractor/Content/Q3D/RLGCParameterMatrices.htm
- https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/Subsystems/Q3DExtractor/Content/Q3D/ReduceMatrixGroundNet.htm
- https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/Subsystems/Q3DExtractor/Content/Q3D/FormulationoftheCapacitanceConductanceSolution.htm
- https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/Subsystems/Q3DExtractor/Content/Q3D/CapacitanceandConductionSolution.htm

## V3.1 controls
Pilot: 6 cases at requested 1 GHz: sigma=0/1/10/100 S/m under unchanged 10000 S/m threshold; plus 10 S/m under threshold 0.1 S/m both **unassigned** and **explicitly grounded** silicon. Explicit silicon net is diagnostic, not a fabricated substrate contact. Deep mode: pilot + 4 nominal frequency probes at 1 MHz, 100 MHz, 10 GHz, 20 GHz + two mesh refinements per sigma + 40/60 um physical-body margin tests (20 cases total).

All preserve same GSSG geometry and source nets; archive AEDT module diagnostics, matrices, mesh stats, solver messages, unique projects, complete console transcript, run hashes.

**Important**: V3.1's frequency configuration is untested inside user's AEDT; inspect returned setup props and exported matrix headers and any setup/API errors, do not assume successful frequency dependence. Mesh validation must use at least two genuinely distinct successful meshes under 1% change in each C observable, and analogous checks for G where nonzero, with physical relevance.

## Why not call this charge conservation
Q3D exposes signed `SmoothQ` surface charge density and field calculator, but independent integration over all electrodes and physically justified exterior requires a separate validated workflow. GSSG test has no explicit backside ohmic substrate contact, so cannot establish the intended DRAM substrate return condition.

## Command
Save `G02_V31_silicon_physics_probe.py` into `C:\暂时下载`:
```bat
py -3.13 "C:\暂时下载\G02_V31_silicon_physics_probe.py" --mode pilot --student --aedt-version 2025.2
```
Then upload `G02_V31_results_bundle.zip`; use `--mode deep` after reviewing pilot behaviour. G02 PASS and ML DOE are prohibited until model/reference and representative numerical conditions are verified.
