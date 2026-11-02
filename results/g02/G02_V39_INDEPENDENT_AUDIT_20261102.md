# G02 V3.9 independent audit — 2026-11-02

Evidence: uploaded G02_V39_results_bundle.zip (66 case results), independently checked raw matrices, solver messages, CG profiles and mesh files. **G02 remains OPEN; final ML DOE not authorized.** Full detailed audit is available as downloadable project chat artifact.

**Run:** 65/66 solved; FREQ_s10_1MHz_r16 failed because 8,354 *surface* elements exceed Student 8,000 cap. No CG adaptive nonconvergence warnings found for 65 successes. Each success exports SIG_A/SIG_B symmetric positive C and G matrices, but these do NOT independently prove charge conservation.

**Higher-order 1 GHz, no-contact GSSG baseline:**
- 1 S/m R16=2592 vs R18=2800 reported total elements: worst C 0.027%, worst G 0.055%. Local oxide L8 still deviates **1.49% mutual C** from R18.
- 10 S/m R16=3872 vs R18=4512: worst C 0.261%, worst G 0.941%. All eight separate Cu/Oxide local refinements deviate <0.37% C and <0.93% G relative to R18 — **strongest nominal numerical evidence** so far.
- 100 S/m R16=6716 vs R18=6580: worst C 0.064%, G 0.035%, BUT R18 is not a larger mesh. Orthogonal local-refinement C differs up to ~0.80%, G by **up to ~12.62%**. No cross-strategy G qualification.

**Substrate-reference and gap diagnostics, sigma10, R16, G_AB in mS:**
- no contact -0.016263714;
- touching edge +0.002787901;
- touching corner -0.009492004;
- edge with 0.05um air gap -0.004970921;
- 0.5um gap -0.015434877;
- 2um gap -0.015951318.
Gap moves values toward no-contact, but touching metal is NOT proof of ohmic semiconductor connection or current continuity. R12/R16 relative G deviations for gap cases reach 8.94%, 1.59%, 4.78%. Do not choose contact location based on lowest numerical error.

**Frequency:** 1 MHz R16 failed surface-element cap; 100 MHz and 1 GHz complete at two settings. Frequency headers still show 1Hz/100Hz/1kHz for requested 1/100/1000MHz. Prior GUI 1GHz original export matched corresponding V3.7 Python C/G exactly; label/export bug proven for that individual case only.

**Decision:** Stop broad nominal mesh experiments. Freeze a physically justified substrate/contact and frequency convention before representative final GSG/GSSG/GSGSG plus domain/charge tests. Keep 1S oxide C and 100S G deficiencies explicit. Student surface cap does not establish fundamental unsolvability of high-conductivity G. G01 stays PASS, G02 OPEN.
