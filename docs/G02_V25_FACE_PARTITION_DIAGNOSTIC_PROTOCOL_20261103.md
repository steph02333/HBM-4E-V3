# G02 v25 face-partition diagnostic protocol — 2026-11-03

v24 identified 4 cylindrical Cu conductors with side/bottom/top face IDs: GROUND_L 109/110/111; SIG_A 140/141/142; SIG_B 171/172/173; GROUND_R 202/203/204. v23 confirmed 16/16 E flux integrals, A/B response, <0.608% nominal C/G agreement, but global charge balance OPEN.

Experiment: `G02_Q3D_face_level_flux_probe_v25.py` delivered via chat downloadable artifact, locally Python compiled and CLI help tested. Runtime AEDT 2025.2 Student untested. It copies AEDT and saved results, checks face IDs, changes source excitations without Solve/Save, evaluates native E→Real/Imag→Normal→Dot→EnterSurf→Integrate with trial numeric face ID string 140, then if numeric and nonzero checks all whole-object integrals vs sum of three faces. Stores all raw `.reg`, status.json and ZIP `G02_Q3D_FACE25_diagnostic.zip`.

**Important:** The 2025 R2 Q3D scripting guide documents `EnterSurf(surface_name)` for named modeler surfaces, not numeric face IDs. This is exploratory API feasibility only: rejection is expected/acceptable and must be recorded as a failed feasibility gate, not treated as a field problem. A successful numeric response additionally requires partition consistency; even partition PASS cannot prove material-adjacent D flux or global Gauss conservation. No new solves; original `.aedt` SHA before/after verified.

Stop rule: if face IDs do not work, do not mutate solved geometry or repeatedly try speculative surface-name syntax. Mark route unsupported and prioritize alternative independent closure or documented limitation before resuming the remaining model mesh/domain/topology gates.
