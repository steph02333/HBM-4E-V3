# G02 progress ledger — 2026-11-02 (Maxwell M01 v0.7)

## Scope and status
**G02 remains OPEN.** Follow supervisor requirements: numerical Cself/Cmutual adaptive convergence (<1% representative checks); reciprocity; positive/passive matrix; independent charge/current conservation; domain adequacy; expected D/P/tox trends; representative H and GSG/GSSG/GSGSG geometries. Do not say final DOE is qualified yet.

## Numerical history and evidence
- V3.7: Higher-order C/G reference; Q3D PyAEDT frequency header/selector discrepancy: GUI native 1 GHz export numerically matched Python 1 kHz-labelled matrix for ONE verified case, not universally.
- V3.8: baseline and contact refinements; touching edge/corner/no-contact dramatically altered G_AB; avoid treating a metal patch as validated ohmic semiconductor contact.
- V3.9: 65/66 solved. Student failed 1MHz/10S/m R16 with 8354 surface elements (>8000 cap). Sigma 1/10/100 S/m baseline worst C delta 0.027/0.261/0.064%; orthogonal sigma1 oxide local C discrepancy ~1.49%; sigma100 local G disagreement ~12.6%. Nominal baseline adaptive C is conditionally qualified only, not whole DOE.
- V4.0: 18/18 solved in 3 families: sigma1 oxide local 6, sigma10 silicon lateral extent 6, sigma10 geometry trend 6. L12 vs L8/L6 sigma1 C_AB approximately 1.13% different; extent margin 25/50/100um shifts sigma10 C_AA approximately 35.482/35.823/36.166 fF. Changing silicon body extent is not purely an external boundary test. At 10 S/m trends: D 3->6 increases |C|, pitch 10->20 decreases |C_AB|, tox 0.1->0.5 decreases |C|.
- Literature: Wang/Asgari/Salman (INTEGRATION VLSI Journal 47, 2014) substrate contact arrangements; Araga et al. 2018 measured via-middle stacked silicon substrate noise; Araga et al. 2021 distinguishes R_sub vs R_gnd; Weerasekera et al. IEEE TED 2016 floating passive silicon interposer vs contacted active IC. HBM4 DRAM physical substrate tie locations **not confirmed**, so no-contact model remains a provisional reference, not demonstrated reality.

## Maxwell M01 experimental history
- Original v0.1/0.2 PyAEDT 1.9.0 Maxwell3d new-design init failed in AEDT 2025.2 Student: NoneType.GetName.
- v0.3 native InsertDesign attempts failed. v0.4 demonstrated valid native NewProject -> InsertDesign Electrostatic -> SetSolutionType AC Conduction -> SaveAs. Cleanup call was incompatible with PyAEDT 1.9.0.
- v0.5 created geometry, 4 voltages, CG matrix, 1GHz setup but native AEDT messages flagged 10S/m / 0S/m string expression errors.
- v0.6 used conductivity numeric 10.0 / 0.0; saved project **M01_GSSG_Maxwell.aedt** statically audited. Material epsr silicon 11.7, oxide 3.9, voltages GROUND_L=0V, SIG_A=1V, SIG_B=1V, GROUND_R=0V. Matrix signal IDs 1,2, grounds 0,3. Four assigned face IDs 72/116/160/204. Setup AC Conduction 1000MHz. Nine model objects; Si slab z=0..35um like Cu TSVs. **No solve yet.**
- Static project inspection is not native geometric face verification, nor proof of Q3D-equivalent outer boundary. No independent current conservation yet.

## Current v0.7 step — read-only native face/configuration verification
Script delivered: `G02_M01_native_face_configuration_verify_v07.py` (local user download). Open the **existing** saved M01_GSSG_Maxwell.aedt without editing it. For each voltage face ID cross-check native `oEditor.GetFaceIDs('CU_*')`, `GetObjectNameByFaceID(face_id)`, and `GetFaceByPosition(['NAME:FaceParameters','BodyName:=',object,'XPosition:=',x,'YPosition:=','0um','ZPosition:=','35um'])`. Export JSON and ZIP with error handling. No InsertDesign, SaveAs, Assign, or Analyze. This script has passed Python compilation, **not yet user AEDT runtime**. Do not assert pass in advance.

## Next gates
1. User runs v0.7 on original v0.6 .aedt; audit ZIP provides face ownership and top-position truth.
2. Check actual native Voltage/M01_CG_Matrix assignment and reference as possible; resolve disputed properties with focused GUI ONLY if necessary.
3. Evaluate Maxwell vs Q3D outer boundary equivalence. Then authorize first Maxwell 1GHz solve, check matrix unit and real frequency against native GUI, compare Y=G+jωC and independent current flux.
4. Freeze a physically sourced HBM substrate reference, and requalify representative H/corner/topology/Si rho meshes prior to launch of final DOE.
5. Archive raw outputs, scripts, results, pass/fail gates and model metadata in repo. Do not commit proprietary source PDFs or heavy .aedt as plaintext.

## Paths on user Windows
`C:\CA2 result V2\02_numerical_convergence\V3_conductive_silicon\Maxwell_M01_BUILD06_20261102_175348\M01_GSSG_Maxwell.aedt`
`C:\暂时下载\G02_M01_native_face_configuration_verify_v07.py`
User CLI: `py -3.13 "C:\暂时下载\G02_M01_native_face_configuration_verify_v07.py" "C:\CA2 result V2\02_numerical_convergence\V3_conductive_silicon\Maxwell_M01_BUILD06_20261102_175348\M01_GSSG_Maxwell.aedt" --student --aedt-version 2025.2`

## Source anchors
Ansys 2025 R2 scripting: `GetFaceIDs` https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/Subsystems/Maxwell/Subsystems/Maxwell%20Scripting/Content/GetFaceIDs.htm ; `GetFaceByPosition` https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v261/en/Subsystems/Maxwell/Subsystems/Maxwell%20Scripting/Content/GetFaceByPosition.htm .
