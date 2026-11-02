# Maxwell M01 v0.8 diagnostic audit — 2026-11-02

User returned `G02_M01_VERIFY08_bundle.zip` with `full_console_log.txt` and `verification_v08.json`.

## Actual result
- PyAEDT 1.9.0 started AEDT 2025.2 SV Student, PID 65172.
- `od.OpenProject(path)` returned a live AEDT proxy (`Instance of an Aedt object:11`).
- `od.GetActiveProject()` also returned a live AEDT proxy.
- v0.8 `probe` helper serialized **the return object itself** to a string before passing it to the caller. Consequently `hasattr(pr, 'GetDesign')` was false, generating `RuntimeError('Cannot get native project')`.
- No excitation/Matrix/outer boundary audit was executed. This is a **Python instrumentation bug, not Maxwell physics failure**.

## v0.9 code fix
`probe` returns the raw live API object to the caller but stores only JSON-safe serialization in the output record. New v0.9 file `G02_M01_excitation_matrix_boundary_audit_v09.py`, Python compilation passed; not yet executed on user AEDT. Original `.aedt` is opened read-only, no insert/assign/save/analyze. v0.9 output expected `G02_M01_VERIFY09_bundle.zip`.

## Remaining G02 gates
Native face ID verification v0.7 passed 16/16 (72,116,160,204); voltage/matrix stored config was read from project static evidence; native excitation assignment + Matrix roles + outer boundary/reference equivalence still open. No Maxwell solve; do not claim G02 closed.
