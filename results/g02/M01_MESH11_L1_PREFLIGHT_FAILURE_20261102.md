# G02 Maxwell M01 v1.1 five-level run — diagnostic outcome (2026-11-02)

Source: user returned `G02_M01_MESH11_diagnostic.zip` at 18:43 SGT. ZIP contains `summary.json`, `mesh_summary.csv`, `L1/status.json`, logs.

## Result
Only L1 attempted; stopped before meshing or Analyze. `BUILD_OR_PREFLIGHT_FAILED` with `RuntimeError("Missing solids: ['SILICON_BODY']")`. Native saved design's actual nine solids are `SI_BODY`, `OX_0`, `CU_GROUND_L`, `OX_1`, `CU_SIG_A`, `OX_2`, `CU_SIG_B`, `OX_3`, `CU_GROUND_R`. Script was incorrectly hardcoded to `SILICON_BODY`. L2–L5 were not run. No new element counts, C/G, convergence, or Maxwell-Q3D comparison resulted. This is a script-object naming mismatch, **not** a mesh convergence result.

## Preserved successful checks
AC Conduction, setup `M01_Setup`, native voltage face IDs 72/116/160/204 and voltage magnitudes 0/1/1/0V, `M01_CG_Matrix` object present. Original project SHA256 before/after `ce8cc07078a166da5b95db148aa7fcbbd25b7e464fcbe10d7f1ca5750eed8d59`; untouched.

## Correction
v1.2 runner changes `SILICON_BODY` to `SI_BODY`; records native solids in preflight and retains fail-fast behavior. Python compilation and CLI parsing verified offline; mesh operation / solver remains unverified in user AEDT. Recommended `--levels 1` first to validate the operation without wasting time; then run remaining levels.

## Matched Q3D comparator and open gates
Raw V4.0 DOM10_M25_R18 nominal reference: GSSG D4/P15/H35/tox0.3 sigma10 S/m margin25um. C_AA=35.48171237 fF, C_AB=-11.61826068 fF, G_AA=0.061592086 mS, G_AB=-0.0164182208 mS. Export labels frequency as 1kHz despite requested setup 1000MHz; that particular case requires independent frequency verification. Maxwell physical outer boundary/reference equivalence and Matrix role native readback still open. G02 OPEN; no final DOE qualification.
