# Maxwell M01 v0.7 native face verification — 2026-11-02

Source: user-returned `G02_M01_VERIFY07_bundle.zip`, `verification.json` and console. **Native face identity/position gate PASS.** This is not a Maxwell solver validation or G02 closure.

| Terminal | Native face ID | Native GetObjectNameByFaceID | GetFaceByPosition at (x,0,35 um) | All checks |
|---|---:|---|---:|---|
| GROUND_L | 72 | CU_GROUND_L | 72 | PASS |
| SIG_A | 116 | CU_SIG_A | 116 | PASS |
| SIG_B | 160 | CU_SIG_B | 160 | PASS |
| GROUND_R | 204 | CU_GROUND_R | 204 | PASS |

Four per-terminal checks: face ID member of GetFaceIDs; owner name; top-position face lookup; face centroid z=35um. All 16 Boolean checks true. Native GetSolutionType AC Conduction. Existing project opened read-only, no save/analyze.

**Open:** `BoundarySetup.GetBoundaries()` returned `[]` (cannot assume lack of voltage excitations); `GetExcitationAssignment` does not exist in AEDT interface (AttributeError). Static .aedt previously showed 0/1/1/0V and Matrix signal IDs 1,2 / ground 0,3 but need independent native excitation/matrix query where possible. Q3D/Maxwell reference and finite silicon outer-boundary equivalence not established; no independent flux conservation, no Maxwell solve, no HBM4 real substrate-tie evidence.

**Next:** compare and inspect full native excitation/matrix assignment using `GetExcitations()` or `GetExcitationNames()` where available and `GetPropertyValue`/PyAEDT BoundaryObject; capture unknown methods without false FAIL; investigate outer boundary then authorize a single pilot solve, native 1GHz matrix readback, and current-flux check. No geometry re-creation or broad sweep.
