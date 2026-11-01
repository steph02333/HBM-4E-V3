# G02 V2.7 — Mesh-verified domain and corner checks

**2026-11-01. G02 remains OPEN.** Downloadable executable: `G02_validation_v2_7.py` (provided in the conversation; this page documents methodology, not an AEDT result).

## Why V2.7 supersedes V2.6

V2.6 compared domain sizes at default adaptive meshing, despite discovering that mesh resolution can materially affect capacitance. V2.7 uses the **successful V2.5 mesh calibration** and reruns a mesh series for **each independent physical geometry**. The goal is not to use precisely 7,152 elements everywhere: actual mesh counts vary across dimensions.

## Test plan

For each of 7 finite silicon block margins `25, 40, 60, 90, 130, 180, 250 µm`, run:
- Default adaptive mesh
- Cu-SIG_A length mesh, nominal maximum 35 µm
- Cu-SIG_A length mesh, nominal maximum 16 µm

Repeat the same 3-level mesh checks for two demanding corners:
- Strong coupling: D=6, P=10, H=50, tox=0.1 µm; margin=40 µm.
- Weak coupling: D=3, P=20, H=25, tox=0.5 µm; margin=40 µm.

**27 initial simulations, expandable on evidence.** Failed configurations still produce diagnostic files; one failure does not abort other configurations.

## Strict numerical interpretation

1. Mesh counts must **actually differ**. Identical adaptive element counts do not establish independent refinement.
2. At least two *distinct successfully solved* mesh resolutions are required **per geometry**, with <1% relative change in **both self coefficients and mutual coupling magnitude** for the last two distinct mesh levels. One solved mesh is **not sufficient**.
3. `per_geometry_mesh_verification.json` stores the per-geometry result.
4. `domain_MESH_VERIFIED_stability.json` compares only mesh-qualified domain points, requires two consecutive adjacent domain increments with all self/mutual differences <1%; skipped/unqualified intermediate sizes do not count as consecutive.
5. The simultaneous domain+mesh tests are much stronger than just applying the V2.5 7152-element result to a different silicon size.
6. Note: This is still **finite nonconductive silicon block-size sensitivity**, not an independent artificial-domain boundary check or semiconductor/doping validation.
7. Reduced Maxwell C-matrix inferred ground charge is algebraic bookkeeping, **not independent physical charge conservation**; that requirement remains open.

## Windows execution

Download `G02_validation_v2_7.py` to `C:\暂时下载`, then run:

```bat
py -3.13 "C:\暂时下载\G02_validation_v2_7.py" --mode domain-check --student --aedt-version 2025.2
```

Upload only the new `G02_results_bundle.zip` from `C:\CA2 result V2\02_numerical_convergence\runs\<run_id>`. Full console transcript, AEDT messages, matrices, mesh counts, and pass/fail reports are included.

**Transfer to ML:** the same per-geometry mesh QA policy should be applied to representative final reference-model corners and audit samples after fixing silicon resistivity, conductor topology and electrical reference. Do not train on unvalidated V2 dielectric-fixture outputs.
