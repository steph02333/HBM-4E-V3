# G02 v23 EditSources repair handoff (2026-11-03)

User provided v22 Python and diagnostic ZIP. ZIP contains only `status.json`: A1 and B1 both failed with `NameError("name 'dc' is not defined")`, with 0/16 integrations; original AEDT SHA unchanged. v22 incorrectly reported extraction as its stage despite failed source edits.

A corrected v23 Python file was supplied as a chat download (`G02_Q3D_two_source_all_conductor_flux_v23.py`), **not yet committed to this GitHub repository**. Edits: explicitly pass named, empty DC and HarmonicLoss structures into Q3D's documented four-argument `EditSources` call; fail closed on source-edit exception; count successful source edits (2 required) and registers (16 required); detect identical A/B field responses; return nonzero on incomplete runs; preserve v21 E→Real/Imag→Normal→Dot→EnterSurf→Integrate method and copied-project, no Analyze, no Save safeguards. `py_compile` and `--help` passed locally, AEDT runtime untested.

Caution: empty DC/HarmonicLoss arrays are a provisional, not-yet-verified format for this saved project. A successful `EditSources` return does not constitute independent readback. Source switching, numerical values, and matrix agreement must be checked from new diagnostic. Source: https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v252/en/Subsystems/Q3DExtractor/Subsystems/Q3DExtractor%20Scripting/Content/EditSources.htm

Next Windows command: `py -3.13 "C:\暂时下载\G02_Q3D_two_source_all_conductor_flux_v23.py" --student --aedt-version 2025.2`. Expected diagnostic: `G02_Q3D_EN_ALL23_diagnostic.zip`. Charge closure still OPEN; four Cu object sums are not automatically full Gauss-law balance because Cu endcap media and infinity-reference field contributions have not been independently checked.
