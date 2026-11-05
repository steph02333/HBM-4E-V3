# Section 13 — One-shot automation for all four pre-registered Q3D candidates

**Created 2026-11-05. Status: package generated, four-candidate dry run executed successfully; new three-candidate Q3D runs still pending on the user's Windows machine.**

After OPT03671 R3/R5 had been solved and independently checked, the user requested that all remaining verification work be launched with **one command rather than manual per-candidate commands**. A new orchestration script `G02_SECTION13_RUN_ALL.py` and double-clickable Windows batch file `RUN_ALL_FOUR_Q3D.bat` were created. They call the **existing unchanged** `G02_SECTION13_FRESH_Q3D_VERIFY.py` for all four fixed candidate IDs in order: `OPT03671`, `OPT01697`, `OPT02901`, `OPT00662`. Each candidate requests both R3 and R5 configurations, up to eight solves total. Completed SOLVED cases are resumed/skipped based on the original result files, so **the completed OPT03671 run need not be repeated**.

The orchestrator continues through subsequent candidates after a failed subprocess, preserves individual result JSONs and logs, and emits `SECTION13_ALL_FOUR_EVIDENCE_<timestamp>.zip` containing each candidate's evidence-only ZIP, launcher logs and a cumulative summary. Previous failures are not automatically deleted or overwritten; explicit `--retry-failed` is required for retrial. The original candidate geometry and the suspect `OPT00662` are not changed. No retraining or optimizer rerun is performed.

**Verified preparation, not physics:** The updated all-four orchestrator passed a no-solver subprocess dry run for each candidate (four successful process exits). No claim is made here that the remaining three Q3D simulations have completed.

**Windows command** (all files extracted into `C:\CA2 result V2\SECTION13_VERIFY`):

```bat
py -3.13 "C:\CA2 result V2\SECTION13_VERIFY\G02_SECTION13_RUN_ALL.py" --execute --student --new-desktop --aedt-version 2025.2
```

The user also received the one-shot package `G02_SECTION13_ONE_SHOT_ALL_FOUR_20261105.zip` containing the original validated solver source, the per-candidate runner, the new orchestrator, all original candidates and Windows run instructions. Package is a chat sandbox deliverable, not uploaded into GitHub with this documentation record.

**Original unaltered problems:** Near-zero predicted CAB at OPT00662, 83 invalid Sobol matrix outputs, 4/9 local positive-CAB invalid predictions, unreconciled reconstructed-vs-original candidate-manifest SHA256, and Q3D requested-1GHz vs exported 1kHz header discrepancy. None is resolved by automating the execution.

See [first fresh Q3D result](G02_SECTION13_OPT03671_FRESH_Q3D_FIRST_EVIDENCE_20261105.md) and [failure-oriented preregistration](G02_SECTION12B_VERIFICATION_PROTOCOL_20261105.md).
