# G02 v24 geometry/material face inventory — 2026-11-03

Evidence: user-uploaded `G02_Q3D_GEOM24_diagnostic.zip` containing status.json, faces.json, objects.json and corresponding CSVs. `INVENTORY_COMPLETE`; 9 solids, 38 faces, 4/4 Cu objects, no Analyze, no Save; original SHA256 unchanged `b52a00eb189d37356b8ae960f42a879ca4aa1dc282e49a2cf66df336ef4f3b81`.

| Cu object | x coordinate (um) | curved wall face ID | z=35 endcap ID | z=0 endcap ID |
|---|---:|---:|---:|---:|
| CU_GROUND_L | -22.5 | 109 | 111 | 110 |
| CU_SIG_A | -7.5 | 140 | 142 | 141 |
| CU_SIG_B | +7.5 | 171 | 173 | 172 |
| CU_GROUND_R | +22.5 | 202 | 204 | 203 |

Every Cu: radius 2 um, height 35 um, cylindrical curved-face area 439.8229715026 um2; each endcap area 12.5663706144 um2. Oxide objects OX_0..3 span r=2 to 2.3 um and z=0..35 um; inner cylinder faces each have matching 439.8229715026 um2 area, consistent with Cu-sidewall/oxide contact. Oxide ring end-face areas are 4.05265452313 um2; outer sidewall area 505.796417228 um2. Silicon body spans x ±49.8 um, y ±27.3 um, z=0..35 um. The oxide and silicon material names were captured, but actual epsilon/permittivity was not verified. Both Cu endcaps coincide with top/bottom body plane; do not assume these are oxide-adjacent. Curved-face centers fail by gRPC but area and topology are sufficient to classify.

**Pass:** object/face geometry inventory and sidewall-vs-endcap identification. **Open:** field-side / surface normal orientation and material-specific D, infinity reference, independent charge closure. A face inventory is not conservation proof. Geometry suggests sidewall-only epsr3.9 may be physically motivated, but using that on entire Cu object is not established.

**Next bounded experiment:** select individual Cu sidewalls and endcaps from saved solution and compare their field-integral contributions separately; read back actual oxide and silicon material permittivity and verify orientation. **Caution:** documented `FieldsReporter.EnterSurf` takes a 3D Modeler surface name; direct numeric face IDs might not be supported, so API feasibility must be checked first, without altering solved topology or running Analyze. If face selection cannot be achieved safely, mark independent full Gauss closure NOT VERIFIED and prioritize independent solver / mesh / domain qualification.
