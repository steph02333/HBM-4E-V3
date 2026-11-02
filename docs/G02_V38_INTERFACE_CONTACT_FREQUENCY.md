# G02 V3.8 targeted experiment and GUI verification

Date: 2026-11-02. G02 OPEN.

Executable: G02_V38_interface_contact_frequency.py (standalone download in project chat). Built from the complete V3.7 runner, preserving unique project IDs, AEDT logs, C/G raw matrices, adaptive convergence captures and [CASE i/N] console counters. Python compilation and 41-case --dry-run ZIP tested. Not yet run in AEDT.

## Experimental rationale
- 100 S/m Higher order, default mesh PerRefine 8/10/12/14/16 (5 cases).
- 100 S/m PerRefine 12 with local length seed 20/12/8 um on **separate** Cu signal A, Cu signal B, oxide liner OX_1, oxide liner OX_2 (12 cases). Local mesh operations target the suspected high-gradient interfaces; mesh size/order cannot be assumed monotonic.
- 100 S/m Higher Direct at 10/12/14 (3).
- 1 and 10 S/m Higher at 10/12/14 (6), guarding against a solver policy tailored only to 100 S/m.
- 10 S/m no contact, edge and corner grounded metal reference hypotheses at 10/12/14 (9); report separately by contact variant, never mix their mesh convergence.
- 10 S/m independent Higher solves at 1 MHz, 100 MHz, 1 GHz, each at PerRefine 10 and 12 (6); use raw C/G and GUI cross-check before interpreting frequency.
Total 41 Q3D cases; deep adds targeted ground/OX_0/OX_3 seeds and additional material/frequency probes.

All nominal physical dimensions remain Cu D=4, pitch=15, height=35, SiO2 liner=0.3 um, Si margin=25 um. Q3D default 10000 S/m classification threshold, Higher order; sigma=1/10/100 S/m. Each per-case raw matrix includes exported header, full signed C/G, solver messages, meshes, requested setup props and net assignment map.

### Scientific limitations
An automatically created copper patch at bottom Si surface is only a **geometric/ground reference hypothesis**. The fact that its boundary is assigned ground and produces altered C/G does not establish ohmic silicon contact, semiconductor drift/diffusion, charge/current continuity or whether the actual HBM die uses that location. Final reference selection still needs the supervisor's confirmation or a defensible fabrication stack; no-contact, edge, and corner remain **different models**. Independent surface-charge integration is not yet implemented; use GUI SmoothQ as reconnaissance and consider saved-field field calculator integration only after verifying correctness.

### GUI for frequency
1. Open a solved .aedt project preserved at the run's ansys_projects folder (not in ZIP).
2. In project tree Analysis -> right-click V3_Setup -> **Matrix...**, or Results -> Solution Data.
3. In Solutions window, select V3_Setup / LastAdaptive (CG); inspect **Matrix** tab C and G, note exact simulation/frequency, compare CAA, CAB, GAA, GAB with case's CG_Maxwell_fF_mS.txt.
4. Inspect **Convergence** tab, Profile and Mesh Statistics; screenshot setup frequency under V3_Setup Properties.
5. For field charge, select a Cu object and use Q3D Extractor > Fields > CG Fields > Q > SmoothQ, solution V3_Setup : LastAdaptive and desired intrinsic frequency. A plot is NOT an independent integrated charge-conservation test.
Official Ansys 2025 R2 tutorial https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/PDFs/Q3D%20Extractor%20A%203D%20PCB%20Via%20Model.pdf
Matrix help https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v261/en/Subsystems/Q3DExtractor/Content/Q3D/ViewingMatrixDatainQ3D.htm

### Run
py -3.13 "C:\暂时下载\G02_V38_interface_contact_frequency.py" --mode pilot --student --aedt-version 2025.2
Upload G02_V38_results_bundle.zip; screenshots from the GUI requested separately.
