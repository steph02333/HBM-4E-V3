# V3.5 fixed-GSSG mesh, contact and frequency investigation

**Status: prepared and locally dry-run validated, not solved in AEDT; G02 OPEN.**

Script delivered: `G02_V35_mesh_contact_frequency.py`, SHA256 `04cbcd657358e8cd85e590144539e9972ebea08a8c7c6eb57c69b1c0b9a5fe42`. 37 pilot cases. The full Python source is delivered separately as a downloadable artifact, not committed in this documentation change.

## Why 10,724 is possible despite Student 8,000
V3.4 `sigma100_R15_default/mesh_stats.txt` explicitly says `Total number of mesh elements: 10724`. Per-object contributions: SILICON_BODY 2806, four OX liners 5318, and four Cu TSVs 2600. This report is **not a transparent count of license-limited 3D surface mesh elements**. Ansys Student specifies 8,000 3D surface and 64,000 3D volume elements separately. Do not equate per-object report totals with license surface count or claim the license was bypassed. Capture both official error lines and mesh statistics; count interpretation remains unresolved.

Official: https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v251/en/Subsystems/Q3DExtractor/Content/GettingStarted/Q3DStudentLimitations.htm

## Controlled design
Preserve four TSVs G-S-S-G, Cu D=4um, pitch 15um, H=35um, oxide=.3um, silicon margin 25um, Si epsilon_r=11.7, default material classification threshold. 1/10/100 S/m silicon (rho=100/10/1 ohm cm), no MOS bias physics.

37 attempts:
- conductivity mesh: three sigma values × five Cap.PerRefine levels 5/7/10/12/15 plus two earlier Cu-A 35/16um mesh seeds = 21.
- high-conductivity bridge: sigma100 additional PerRefine=8/9/11/13/14 to investigate discontinuous C/G jumps = 5.
- matched reference: sigma10, 4 PerRefine levels 5/7/10/12 each with and without localized backside metal patch = 8. Hypothesis tests only; does not prove ohmic semiconductor contact.
- independent setup frequency: sigma10, 1MHz/100MHz/1GHz = 3.

Per-run outputs: raw signed original C and G matrices, requested/actual setup data, two independent frequency selector exports with **numeric freq and explicit MHz unit** (V3.4 incorrectly combined unit-bearing strings with freq_unit), AEDT messages, convergence files, raw mesh statistics and per-object mesh breakdown, errors, full console transcript, and stratified comparisons that prevent mixing grounded and ungrounded objects. Failure and signs are preserved.

## Explicit interpretation caveats
More reported elements do not guarantee better or nested meshes. A flat C can coexist with unstable G. Matrix-export header differences are not proof of actual field-solution frequency; independent setup solves are required. Signed small off-diagonal G needs passivity/reference review, not just percent difference. Charge conservation, realistic semiconductor substrate contact, independent solver and domain convergence remain unresolved. This is *not* final DOE/ML data.

## Run
```bat
py -3.13 "C:\暂时下载\G02_V35_mesh_contact_frequency.py" --mode pilot --student --aedt-version 2025.2
```
Upload only `G02_V35_results_bundle.zip` found under `C:\CA2 result V2\02_numerical_convergence\V3_conductive_silicon\run_<id>\`.
