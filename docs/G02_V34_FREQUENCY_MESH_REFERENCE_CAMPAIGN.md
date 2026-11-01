# G02 V3.4 — matched-mesh, substrate-reference and frequency investigation

**2026-11-01 | PLANNED / PYTHON DRY-RUN ONLY | G02 OPEN**

The standalone executable `G02_V34_frequency_mesh_reference.py` is supplied in the project conversation; it has passed Python syntax compilation and dry-run ZIP packaging. AEDT execution is **not yet verified**. Record its SHA256 from the run manifest before interpreting results. No final ML labels.

## Scientific scope and preserved model
Cu/SiO2/Si four-TSV GSSG unchanged from V3.3: D=4 um, P=15 um, H=35 um, tox=.3 um, Si margin=25 um, epsr(Si)=11.7; copper G-S-S-G. Default dielectric/conductor threshold 10000 S/m. Silicon sigma=1/10/100 S/m (rho 100/10/1 ohm-cm), not lowered threshold in physical candidates. No doping/space-charge MOS model.

## Campaign (29 initial independent Q3D projects)
- 21 conductivity-mesh trials: each sigma x five verified adaptive refinements (Cap.PerRefine=5,7,10,12,15%) plus two Cu SIG_A surface mesh seeds (35 and 16 um at PerRefine=10). Mesh count and identity must genuinely differ; total mesh element count is NOT the Student 8000 *surface*-element limit.
- 6 matched reference tests: sigma 10 S/m, with and without localized far-margin grounded metal contact, at each 5,10,12% refinement; **do not mix reference cases with no-contact in a convergence comparison**. The metal contact is a boundary-condition hypothesis, not demonstrated ohmic semiconductor contact.
- 2 independent requested frequency solutions: nominal sigma=10 at 1 MHz and 1 GHz, separately from exporter-frequency variations.
- `--mode deep` adds 6 extra mesh attempts at sigma=1/100, 4 extra contact trials at sigma=1/100, and independent 100 MHz and 10 GHz cases.

## Export and frequency audit
Official PyAEDT `export_matrix_data` has distinct `freq` and `freq_unit` selectors (see https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.q3d.Q2d.export_matrix_data.html). A script's AdaptiveFreq=1GHz does not guarantee header=1GHz when exporter defaults to another selection. For each solved case script attempts explicit export at that case's requested frequency, with documented fallback to default, then separately exports default, 1MHz and 1GHz from *same solved field*. That only tests **export selection**, not three independent field solutions; latter addressed by separate 1MHz vs 1GHz setups.

The script preserves original signed C/G matrices and explicit net labels. If requested-frequency export fails, investigate file's actual header and AEDT messages; do not infer physical frequency response from labels alone.

## Interpretation criteria
1. For each conductivity record at least two genuinely distinct successful meshes; look at all self and mutual C and G. Particularly sigma100 V3.3 prior mesh disagreements C=2.213%, G=17.911% invalidate selecting the most convenient pair.
2. For each geometry/reference/frequency, compare same physical setup only. Evaluate symmetry/passivity and selected cross-mesh deltas. Different total-element counts alone do not prove nested refinement or absolute numerical error.
3. Contact/no-contact comparisons need matching numerical credibility and actual conductive-path/terminal interpretation. Ground entire Si is not the same as a local backside contact.
4. All Q3D reference/field charge conservation, physical-substrate size independence, final GSG/GSSG/GSGSG corners and independent solver confirmation remain separate future gates.
5. Student limit case diagnostics must be retained and failures not concealed.

## Run
Save source to `C:\暂时下载\G02_V34_frequency_mesh_reference.py`.
```bat
py -3.13 "C:\暂时下载\G02_V34_frequency_mesh_reference.py" --mode pilot --student --aedt-version 2025.2
```
The runner writes `G02_V34_results_bundle.zip` under `C:\CA2 result V2\02_numerical_convergence\V3_conductive_silicon\run_<id>`. Upload only ZIP for analysis.

## Vendor source
- PyAEDT Q3D setup template: https://aedt.docs.pyansys.com/version/stable/API/SetupTemplatesQ3D.html
- Ansys CG adaptive parameters: https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/Subsystems/Q3DExtractor/Content/Q3D/SettingCapacitanceConductanceAnalysisParametersinQ3DExtractor.htm
