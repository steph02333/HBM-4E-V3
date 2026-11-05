# G02 Section 13 — FIRST independent Q3D verification: OPT03671 (2026-11-05)

## Source and scope
Evidence file supplied by user: `SECTION13_EVIDENCE_ONLY.zip`, containing result JSON, native Maxwell matrix exports, convergenceCG.txt, mesh_stats.txt, profileCG.prof, AEDT before/after snapshots, runner logs for **both** `VFY13_OPT03671_GSG_S10_R3` and `VFY13_OPT03671_GSG_S10_R5`. This GitHub markdown records the outputs; the 21.8 KB original evidence ZIP is not itself committed in this operation. Only the FIRST of four preregistered verification candidates has been run. No retraining, candidate replacement, or deletion.

## Actual first verification comparison
- Candidate: `OPT03671`; GSG topology, substrate rho=10 Ω·cm; sigma=10 S/m, mesh target SIGNAL_OXIDE 8 µm, original validated G02 V6.3 builder; geometry reconstructed from deterministic Sobol D=3.6659563428397477 µm, P=10.181201057492821 µm, H=25.27172571356686 µm, tox=0.47402100537375547 µm.
- Pre-Q3D frozen model output from executed Section 12B: **CAA=16.281986 fF** (display precision six decimals; exact underlying original manifest has not been uploaded).
- R3 native Maxwell extraction: **CAA=15.5314544920992 fF**.
- R5 native Maxwell extraction: **CAA=15.52831257239893 fF**.
- Using R5 as the independent Q3D reference: absolute surrogate error ≈ **0.7536734276 fF**; relative absolute error ≈ **4.854%**. This result is neither suppressed nor presented as an exact match. Error from six-decimal frozen prediction has rounding below 1e-6 fF.
- R3/R5 difference: abs **0.0031419197 fF**; relative to R5 ≈ **0.02023%**.
- The source native matrix for GSG contains one signal term `SIG_A` (1x1) only; no CBB or CAB is expected or should be imputed.

## Adaptive convergence and evidence
| Item | R3 | R5 |
|---|---:|---:|
| `PerRefine` | 3% | 5% |
| Completed passes | 3 | 3 |
| Solver criterion target | 0.5% | 0.5% |
| Current reported delta | 0.012532% | 0.005157% |
| Last-pass triangles | 1516 | 1550 |
| Total mesh elements | 2420 | 2488 |
| Native CAA fF | 15.5314544920992 | 15.52831257239893 |

Both `profileCG.prof` logs state `Adaptive Passes converged` and normal completion. The final percentage printed by Q3D is its CG convergence metric; with one signal term it is relevant evidence, but **separate extraction of native consecutive-pass CAA matrices would be needed to rigorously reproduce the earlier per-entry ΔC<1% audit definition**. Low R3–R5 difference and the convergence printouts support numerical stability, **not physical validation of the entire electrostatic semiconductor abstraction**.

## UNRESOLVED frequency/header discrepancy — DO NOT ERASE
Both default exports contain `Frequency: 1kHz`, although `setup_props_frequency` and requested configuration are `1000MHz` (1 GHz). Alternate export methods with `freq=1000,freq_unit=MHz` and `freq=1000000000,freq_unit=Hz` returned `Frequency: 1Hz`, with **identical C values**; string `freq=1000MHz` did not succeed. The discrepancy remains unresolved and must be explicitly declared instead of claiming independently confirmed 1 GHz export. It may involve an exporter convention, but cause has NOT been verified.

## Interpretation and decisions
1. **First fresh Q3D verification succeeded as a solver run and showed a nonzero 4.85% ML discrepancy.** The 4.85% relative error is not a convergence failure; it is a new external check at an optimizer-selected geometry.
2. Single GSG result does not establish that optimization achieves improved physical objective versus comparable same-topology/rho Q3D baseline. Baseline evaluation remains needed; nearest DOE data are a neighborhood diagnostic, not necessarily a fair matched optimization baseline.
3. Continue with the **three other pre-registered candidates** OPT01697, OPT02901, OPT00662, retaining any failures. The last is deliberately expected to stress the surrogate near-zero CAB crossing.
4. Do not change the frozen models or select only flattering verification results. Report numerical labels and limitations separately from semiconductor/frequency physics.

Upstream: [preregistration](G02_SECTION12B_VERIFICATION_PROTOCOL_20261105.md), [actual preflight](G02_SECTION12B_PREFLIGHT_ACTUAL_RESULTS_20261105.md), [Section 13 runner readiness](G02_SECTION13_RUNNER_READINESS_20261105.md).
