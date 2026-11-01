# G01 runner — Windows execution and evidence handoff

## Scope
This is Prof Lim's level-1 analytical benchmark only, not a realistic doped-silicon TSV or final HBM model. It uses a Cu center cylinder, SiO2 cylindrical liner (relative permittivity 3.9), and a coaxial grounded Cu outer shell. Outer shield thickness is 0.2 µm (fixed modelling choice). Finite axial ends produce fringing; the ideal analytical expression is a uniform-coax approximation.

Do not run legacy scripts or import an old Q3D project.

## Verified user environment (2026-11-01)
- Script download folder supplied by researcher: `C:\暂时下载`.
- Ansys installed edition: **Ansys EM Student 2025 R2** (PyAEDT version argument `2025.2`).
- Reported Windows Start Menu shortcut folder: `D:\ProgramData\Microsoft\Windows\Start Menu\Programs\Ansys EM Student 2025 R2`; this folder is **not confirmed as the Ansys installation root** and should not be used as one.
- Experiment output root remains `C:\CA2 result V2`.
- Exact B01 Windows CMD command:

```bat
py "C:\暂时下载\G01_coax_benchmark.py" --case B01 --student --aedt-version 2025.2
```

If the `py` launcher is unavailable, check Python installation and PATH before retrying. Do **not** invoke the script from the AEDT built-in scripting environment; it requires the normal Python interpreter with PyAEDT.

## First run: B01 only
1. Download or clone scripts/G01_coax_benchmark.py to Windows.
2. Install Python 3 and PyAEDT in the same Python installation: py -m pip install -U pyaedt
3. Ensure Ansys Electronics Desktop with Q3D Extractor and a valid license is installed. Run from Windows Command Prompt / PowerShell, not the AEDT IronPython scripting console.
4. Navigate to wherever the script was downloaded, e.g. cd /d "%USERPROFILE%\Downloads" (Command Prompt).
5. Run: py G01_coax_benchmark.py --case B01
6. If using AEDT Student, add --student. If version detection fails, add --aedt-version 2026.1 (substitute your installed version).
7. If PyAEDT/AEDT fails, share the failure bundle.

Optional test without AEDT: py G01_coax_benchmark.py --dry-run.
After B01 is reviewed, use: py G01_coax_benchmark.py --all.

## Expected B01 analytical target
r=1.5 µm, D=3 µm, h=25 µm, oxide thickness=0.1 µm.
C_ox = 2*pi*eps0*3.9*h / ln((r+tox)/r).
Calculated value: **84.045449519 fF**. This is NOT a solver result.

## Outputs
Each invocation creates a unique directory:
C:\CA2 result V2\01_analytical_benchmark\runs\<run_id>

Its folders contain:
- configs/B01.json; configs/run_manifest.json
- ansys_projects/B01_G01.aedt
- raw_exports/B01_C_Maxwell_fF.txt
- raw_exports/B01_convergence.txt, B01_mesh_stats.txt, B01_profile.prof (when exported successfully)
- analysis/G01_summary.csv
- reports/runner.log
- G01_results_bundle.zip

## Send us
Upload **G01_results_bundle.zip**, even on failure. The bundle excludes large AEDT project and solver files. If requested, attach an AEDT screenshot of the model and net assignments.

SOLVED_EXPORT_READY_FOR_REVIEW is NOT a G01 PASS. We must inspect the exported capacitance convention and the SIGNAL self term, verify units and errors, and explain any discrepancy before running additional cases.

G01 remains OPEN until the full nine-case benchmark is reviewed and documented. No G02, DOE, or ML before that.
