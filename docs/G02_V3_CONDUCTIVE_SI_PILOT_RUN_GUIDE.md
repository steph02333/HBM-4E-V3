# V3 conductive-silicon Q3D material/reference feasibility pilot (2026-11-01)

**STATUS: script created and dry-run checked; not yet executed on Ansys Student. G02 OPEN.**

The full standalone script is delivered in the same project chat as **G02_V3_conductive_silicon_pilot.py**. It is not yet stored in this repository's scripts folder; source SHA256 in each returned run manifest must identify the version. Prior V2.5/V2.7 nominal mesh data are **method-development evidence**, not validation of the new material model.

## Why this pilot is essential
Official Ansys Q3D documentation says objects at or below the insulator/conductor conductivity threshold are treated as insulating, while materials between conductor thresholds carry volumetric current. PyAEDT documents `Q3d.set_material_thresholds(insulator_threshold, perfect_conductor_threshold, magnetic_threshold)` and defaults its insulator threshold to **10,000 S/m**. Prof Lim's Si resistivities 1,10,100 ohm-cm correspond to only 100,10,1 S/m. Assigning conductivity without interrogating material classification may therefore give misleading C/G labels. Simply lowering the threshold is **not sufficient proof** of a physically faithful grounded substrate; it can turn silicon into an unwanted conductor/net.

Vendor references:
- https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v251/en/Subsystems/Q3DExtractor/Content/Q3D/SettingtheMaterialThresholdinQ3DExtractor.htm
- https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.q3d.Q3d.set_material_thresholds.html
- https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.q3d.Q2d.export_matrix_data.html

## Physical fixture
Fresh four-TSV **GSSG** row, nominal D=4, P=15, H=35, tox=0.3 micrometres; SiO2 epsilon-r 3.9, silicon epsilon-r 11.7 and variable sigma; 25 micrometre finite silicon margin. Four Cu nets are ground-left, signal-A, signal-B, ground-right. **NO backside substrate electrode**, hybrid-bond pad, or voltage-dependent MOS semiconductor physics in this pilot. Its purpose is diagnosis, not final ML dataset generation.

## Runs
First **pilot** (3 cases):
1. `control_dielectric`, sigma=0 S/m, threshold=10000 S/m;
2. `rho10_default_threshold`, sigma=10 S/m, threshold=10000 S/m;
3. `rho10_lower_threshold`, sigma=10 S/m, threshold=0.1 S/m.

Then only after inspection, **extended** adds sigma 1 and 100 S/m at both thresholds, selected mesh controls from the earlier successful V2 method, and finite-body sensitivity.

## Windows command
Save downloaded script into `C:\暂时下载` and run:

```bat
py -3.13 "C:\暂时下载\G02_V3_conductive_silicon_pilot.py" --mode pilot --student --aedt-version 2025.2
```

The results are under `C:\CA2 result V2\02_numerical_convergence\V3_conductive_silicon\run_<id>\G02_V3_results_bundle.zip`.

Upload **only** the ZIP: it includes the full console transcript, per-case AEDT messages, matrices, conductivity/net classification, mesh diagnostics, errors, and an explicit outstanding-audit checklist. The script does not stop subsequent independent tests at the first case failure; every case receives a unique AEDT project name.

## Interpretation and decision gate
- Verify whether Si is classified as conductor/dielectric and whether the extracted matrix has expected signal/ground nets. Zero G or differences in C across thresholds do not by themselves prove the correct lossy-substrate physics.
- Record the original C and G exports and Q3D solver warnings; distinguish actual Student mesh limit from API/geometry errors.
- This script **does not demonstrate substrate charge conservation** and does not represent semiconductor bias effects. We must specify and separately validate actual physical substrate grounding/reference and field-charge balance.
- **No G02 PASS**, final DOE, or ML until geometry/material/reference definitions and representative numerical validation are credible.
