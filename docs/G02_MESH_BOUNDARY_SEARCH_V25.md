# G02 V2.5 — Student-edition mesh-boundary search

**Status: RUNNER READY FOR WINDOWS TEST; G02 NOT PASSED.**

The complete script was delivered as `G02_validation_v2_5.py` in the associated project chat, with syntax and dry-run ZIP checks. It is not yet committed as a .py file to GitHub, so retain the downloaded file and its `script_sha256` run manifest.

## One command

Save the script to `C:\暂时下载\G02_validation_v2_5.py` and execute from Windows CMD:

```bat
py -3.13 "C:\暂时下载\G02_validation_v2_5.py" --mode mesh-search --student --aedt-version 2025.2
```

Send back **only** the final `G02_results_bundle.zip` found under
`C:\CA2 result V2\02_numerical_convergence\runs\<run-id>\`.

## Search design

- Always run a **default adaptive** baseline, then explicit **single-Cu-surface** mesh seeds (80,60,45,35,27,21,16,12,9 µm; increasingly restrictive). These are coarse, heuristic initial parameters, not estimates of actual mesh size. Seed length does not guarantee increasing element count.
- If the first explicit seed fails, attempt up to two gentler recovery settings. When an actual Ansys mesh-cap error brackets a solved explicit setting, probe intermediate settings; stop the impossible branch rather than pursuing progressively finer known-to-fail settings.
- Every case has a **new unique AEDT project**, per-case raw matrix and solver logs, and a JSON status. Failure does not destroy earlier successes. A Student limit is reported as verified only when current-case AEDT diagnostics identify it.
- Compare **actual mesh element counts** rather than relying on changed adaptive settings. Only distinct, solved mesh resolutions qualify for a cross-solution comparison of `Cself_A`, `Cself_B`, and `|Cmutual_AB|`. Intended target: all changes <1%. Near-zero coupling needs an absolute fF tolerance.
- Includes `full_console_transcript.txt`, AEDT messages and a `mesh_resolution_comparison.json` report in the final ZIP. Logs are finalized before the ZIP handoff.

## Critical ML transferability rule

A mesh policy is **not portable solely by fixed seed length or number of adaptive passes**. The current search uses an idealized **nonconductive** silicon block (relative permittivity 11.7), two signals and one ground; it is **not the final doped-silicon HBM TSV model**.

Before final DOE/ML:
1. Freeze the final conductor topology, silicon resistivity, ground/exterior boundary, pad/liner geometry and reference matrix convention.
2. Re-run mesh convergence with **those exact physical assumptions** at nominal and geometrically difficult corners (large D, close P, thin tox, tall H; also weak-coupling far corners).
3. Use an adaptive mesh setup/protocol with observed element-count ceilings. Audit a subset of DOE corner cases and log matrix/mesh quality for **every** label.
4. If Student cap blocks <1% consistency, document the achieved mesh changes and limit; **do not silently claim high-fidelity labels**. Evaluate uncertainty, simplify geometry with justification or obtain unrestricted academic AEDT access.
5. Do not begin DOE, surrogate training or optimization until the final solver reliability gate has explicit documented approval.

This script solves **only the mesh-resource calibration** subtask. Matrix symmetry/passivity and earlier geometric trends are preliminary; domain independence and field-level charge balance are unresolved, so G02 stays OPEN.
