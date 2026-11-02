# G02 v25 face-level field-selection audit — 2026-11-03

Evidence: user-uploaded `G02_Q3D_FACE25_diagnostic.zip` with `status.json` and `A1_CU_SIG_A_whole_Real.reg`.

- Stage: `FACE_ID_NOT_SUPPORTED_OR_FAILED`.
- A1 EditSources succeeded; original whole-object `CU_SIG_A` Real normal E flux succeeded (integral `0.0010253533352638739`, assuming epsr=3.9 candidate `35.40681691913817 fC`) and agrees with prior v23 result.
- `EnterSurf("140")` for `CU_SIG_A` curved sidewall failed: `GrpcApiError('Failed to execute gRPC AEDT command: EnterSurf')`. This indicates numeric face-ID string is not accepted by this method in this setup; it does **not** establish that all face-resolved methods are impossible.
- No other face attempts, B1, or partition closure performed; no evidence for material-specific D or infinity charge.
- `did_analyze=false`, `did_save=false`, original project SHA before and after `b52a00eb189d37356b8ae960f42a879ca4aa1dc282e49a2cf66df336ef4f3b81`.

**Decision:** v25 face ID experiment FAIL / API unsupported; retain v23/v24 PASS. Do not claim global charge conservation. Given previously agreed bounded stop rule, avoid repeated undocumented EnterSurf guesses. Either investigate a specifically documented, physically safe face/sheet selection workflow (must establish selection, solve preservation and partition) or close this route as NOT VERIFIED and prioritize outstanding sigma1 mesh, sigma100 G, domain, topology, height and cross-solver boundary evidence. A partition identity alone would not prove Gauss closure or infinity reference.
