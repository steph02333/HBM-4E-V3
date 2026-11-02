# M01 v1.2 actual L1 meshing result and v1.3 plan (2026-11-02)

User-returned `G02_M01_MESH12_diagnostic.zip` includes `summary.json`, `mesh_summary.csv`, `L1/status.json`, native AEDT messages, full console.

## v1.2 confirmed result
- Fresh copied-project L1 solved preflight (9 solids incl. `SI_BODY`); AC Conduction, excitation faces 72/116/160/204, 0V/1V/1V/0V, matrix presence passed.
- Native `MeshSetup.AssignTrueSurfOp` call returned without exception; script recorded it as added. Analyze attempted.
- Native error: `M01_Setup: Mesh size (80935 volume elements) is greater than the limit for simulation in Ansys Electronics Desktop Student.` No C/G or solver convergence produced. Same number as v1.0 baseline 80935; no verified mesh reduction. Only L1 attempted. Five-level convergence cannot be inferred.
- Original .aedt SHA before/after `ce8cc07078a166da5b95db148aa7fcbbd25b7e464fcbe10d7f1ca5750eed8d59`; unchanged.

## v1.3 experiment
- v1.3 Python runner delivered separately in chat, compile checked but no AEDT runtime validation.
- Use documented `MeshSetup.InitialMeshSettings` to fix **Classic** initial mesher and vary global initial surface slider 1..5 across independent copied projects. Do not mix mesher types within the 5-level sensitivity sequence. Preserve geometry, materials, excitation and matrix.
- First run `--levels 1` only. If element count changes / solve succeeds, assess whether full five-level campaign is warranted. Student ceiling 64,000 **volume** elements; ideally leave headroom for adaptive mesh refinement. Do not claim a numerical convergence result based on undercap mesh alone.
- Ansys source: https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/Subsystems/Maxwell/Subsystems/Maxwell%20Scripting/Content/InitialMeshSettings.htm

## Remaining open physics gates
Q3D V4 DOM10_M25_R18 nominal GSSG D4 P15 H35 tox0.3 sigma10 margin25 requested 1GHz, but exported frequency header says 1kHz; independent exact-case GUI verification needed. Maxwell outer reference equivalence and actual matrix export need audit. G02 and final DOE remain OPEN.
