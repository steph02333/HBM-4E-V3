# G02 V3.2 mesh-and-silicon reference campaign

Date: 2026-11-01. Prepared script: `G02_V32_mesh_physics_campaign.py`. Syntax and dry-run ZIP verified; **no AEDT Student run yet**. G02 remains OPEN.

## Design
Do **not** change nominal GSSG geometry: D 4 um; P 15 um; H 35 um; SiO2 liner .3 um; Si margin 25 um. Silicon epsilon-r 11.7. Fixed **default** conductor-classification threshold 10000 S/m for valid lossy-material candidates; compare rho 100/10/1 ohm-cm corresponding sigma 1/10/100 S/m.

Per sigma test three *requested* meshing strategies: default with a modest 10% adaptive refinement rate, a 35 um Cu-SIG_A surface length seed with 15%, and a 16 um seed with 20%. Solver options are installed **only if recognized by the 2025.2 PyAEDT setup object**; missing percent-refinement properties are recorded. **These settings do not guarantee 4000-8000 actual mesh elements** or successful Student 8000-*surface*-element solutions. Report actual total and surface counts separately.

Add a sigma=0 lossless control, sigma=10 S/m lower-threshold unassigned-silicon case, and a matching explicit-ground-silicon case; these last two are **diagnostic conductor-limit models**, not physically representative substrate contacts. Full pilot comprises 12 simulations. Deep mode adds three adaptive-rate controls and frequency-export controls.

For each success archive complete C/G exported matrices, solver convergence and mesh statistics, material/net API readings, official AEDT messages, project metadata and full console log. For each sigma, compare only **actually distinct mesh-count results** and report changes for Cself_A, Cself_B, |Cmutual| as well as Gself and |Gmutual|. Near-zero G cannot be judged by relative percentage alone; use absolute differences and interpretation.

Important unresolved items: physical backside/ohmic substrate contact is not implemented; default-Q3D reference and lossy-medium matrix definition require confirmation; charge balance needs independent signed surface-charge audit; frequency request vs exported 1 Hz header remains unresolved; no MOS bias physics; no topology/geometry-envelope claim. A mesh sub-result <1% is not full G02 PASS. If the Student limit blocks a mesh, keep errors and adapt strategy; no manufactured PASS.

## Run
```bat
py -3.13 "C:\暂时下载\G02_V32_mesh_physics_campaign.py" --mode pilot --student --aedt-version 2025.2
```
Upload `G02_V32_results_bundle.zip` from `C:\CA2 result V2\02_numerical_convergence\V3_conductive_silicon\run_<id>\`.

Official references: Ansys Q3D CG uses triangular surface meshes and evaluates complex free/bound charges; see https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/Subsystems/Q3DExtractor/Content/Q3D/CapacitanceandConductionSolution.htm and adaptive settings https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v251/en/Subsystems/Q3DExtractor/Content/Q3D/SettingCapacitanceConductanceAnalysisParametersinQ3DExtractor.htm.
