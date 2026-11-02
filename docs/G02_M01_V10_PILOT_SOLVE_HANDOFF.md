# G02 Maxwell M01 v1.0 Pilot Solve & Export (2026-11-02)

**Status:** runner compiled / command-line help tested in assistant environment, not yet runtime-tested with Windows AEDT Student 2025.2. USER ACTION pending. G02 physics and Q3D validation remain OPEN.

## Script
`G02_M01_pilot_solve_export_v10.py` delivered to user as downloadable script. Uses existing validated v0.6 project, copied to a timestamped folder before any AEDT modifications.

## Gates / method
1. Hash original file SHA256; copy to separate `Maxwell_M01_PILOT10_.../M01_GSSG_PILOT10.aedt`.
2. Start fresh AEDT Student 2025.2 desktop and open copy. Confirm AC Conduction; `M01_Setup` exists; live `GetAssignment` and `Excitations` child readbacks match expected voltage faces (72,116,160,204 and 0V/1V/1V/0V). Confirm Matrix `M01_CG_Matrix` exists under `Parameters`. Matrix internal roles not natively reverified.
3. Execute blocking native `oDesign.Analyze('M01_Setup', True)`, Ansys documented return 0 success. Save only copied project.
4. Best-effort PyAEDT `Maxwell3d.export_matrix('M01_CG_Matrix', ... , setup='M01_Setup')`, convergence/mesh/profile exports. Record failures without negating a completed solver run. Do not guess `ExportMatrixData` arguments or pretend header frequency trustworthy.
5. Collect native messages, full console, `run_status.json`, export text, diagnostic ZIP excluding binary `.aedt`. Hash original again and record unchanged.

## Command
`py -3.13 "C:\暂时下载\G02_M01_pilot_solve_export_v10.py" --student --aedt-version 2025.2`

Optional dry gate: append `--preflight-only` (copies and checks without analyzing).

## Expected output
`G02_M01_PILOT10_diagnostic.zip` from new timestamped output directory; `.aedt` solved copy remains separately in the same directory. User uploads diagnostic ZIP; if needed `.aedt` or solver files separately.

## IMPORTANT
- A successful native `Analyze` does not prove physics equivalence. Outer-boundary/reference and real HBM substrate contact geometry still not validated.
- No final DOE until solver-independent C/G matrices, units, actual frequency, reciprocity/passivity, current flux and representative convergence are established.
- No broad sweep or reconstruction of model in this step.

## Documentation references
https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/Subsystems/Maxwell/Subsystems/Maxwell%20Scripting/Content/Analyze.htm
https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.maxwell.Maxwell3d.html
