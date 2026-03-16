# Gold Standard Deviations Report

This document summarizes the deviations from the IHP SG13G2 "Gold Standard" as of the current build.

## Summary Statistics

| Metric | Status | Pass Rate |
|--------|--------|-----------|
| **Macro Dimensions** | 84/84 PASS | 100% |
| **Pin Existence** | 84/84 PASS | 100% |
| **Spatial Mapping** | 84/84 PASS | 100% |
| **V3 Compliance (LDR)** | 45/84 PASS | 53.6% |
| **LEF Contact Alignment (MD)** | 0/84 PASS | 0% |

## Detailed Deviations

### V3 Compliance Failures (LDR Models)
These failures are reported by `scripts/verify_models_v3.py` and indicate physical modeling errors in the `.ldr` files.

#### sg13g2_a21o_1.ldr
- PMOS contact at Stud X=1 has opposite parity (expected EVEN)
- Input contact at Stud X=2 has incorrect symmetric parity (expected ODD)
- NMOS contact at Stud X=3 has ODD parity (expected EVEN)
- PMOS contact at Stud X=3 has opposite parity (expected EVEN)
- NMOS contact at Stud X=5 has ODD parity (expected EVEN)
- PMOS contact at Stud X=5 has opposite parity (expected EVEN)
- Input contact at Stud X=6 has incorrect symmetric parity (expected ODD)
- NMOS contact at Stud X=7 has ODD parity (expected EVEN)
- PMOS contact at Stud X=7 has opposite parity (expected EVEN)
- PMOS contact at Stud X=9 has opposite parity (expected EVEN)
- NMOS contact at Stud X=11 has ODD parity (expected EVEN)
- PMOS contact at Stud X=11 has opposite parity (expected EVEN)

#### sg13g2_a221oi_1.ldr
- Input contact at Stud X=6 has incorrect symmetric parity (expected ODD)

#### sg13g2_a22oi_1.ldr
- NMOS contact at Stud X=3 has ODD parity (expected EVEN)
- NMOS contact at Stud X=7 has ODD parity (expected EVEN)

#### sg13g2_and2_1.ldr, sg13g2_and2_2.ldr
- NMOS contact at Stud X=1 has ODD parity (expected EVEN)

#### sg13g2_and3_1.ldr, sg13g2_and3_2.ldr
- NMOS contact at Stud X=5 has ODD parity (expected EVEN)
- (sg13g2_and3_2 only) Input contact at Stud X=6 has incorrect symmetric parity (expected ODD)

#### sg13g2_and4_1.ldr
- Input contact at Stud X=9 has incorrect symmetric parity (expected EVEN)

#### sg13g2_buf_16.ldr
- Input contact at Stud X=39 has incorrect symmetric parity (expected EVEN)

#### sg13g2_buf_4.ldr
- Input contact at Stud X=11 has incorrect symmetric parity (expected EVEN)

#### sg13g2_dfrbp_1.ldr, sg13g2_dfrbp_2.ldr, sg13g2_dfrbpq_1.ldr, sg13g2_dfrbpq_2.ldr
- Input contact at Stud X=9 has incorrect symmetric parity (expected EVEN)

#### sg13g2_dlhq_1.ldr
- Input contact at Stud X=25 has incorrect symmetric parity (expected EVEN)

#### sg13g2_dlhr_1.ldr, sg13g2_dlhrq_1.ldr
- Input contact at Stud X=21 has incorrect symmetric parity (expected EVEN)

#### sg13g2_dllr_1.ldr, sg13g2_dllrq_1.ldr
- Input contact at Stud X=23 has incorrect symmetric parity (expected EVEN)

#### sg13g2_ebufn_4.ldr
- PMOS contact at Stud X=3 has opposite parity (expected EVEN)

#### sg13g2_ebufn_8.ldr
- Input contact at Stud X=37 has incorrect symmetric parity (expected EVEN)
- Input contact at Stud X=41 has incorrect symmetric parity (expected EVEN)

#### sg13g2_einvn_4.ldr
- Input contact at Stud X=17 has incorrect symmetric parity (expected EVEN)

#### sg13g2_einvn_8.ldr
- Input contact at Stud X=27 has incorrect symmetric parity (expected EVEN)

#### sg13g2_inv_1.ldr
- VSS contact at Stud X=0 has EVEN parity (expected ODD)
- NMOS contact at Stud X=1 has ODD parity (expected EVEN)
- VSS contact at Stud X=2 has EVEN parity (expected ODD)
- NMOS contact at Stud X=3 has ODD parity (expected EVEN)
- VSS contact at Stud X=4 has EVEN parity (expected ODD)

#### sg13g2_inv_16.ldr
- Input contact at Stud X=31 has incorrect symmetric parity (expected EVEN)

#### sg13g2_lgcp_1.ldr
- NMOS contact at Stud X=5 has ODD parity (expected EVEN)
- NMOS contact at Stud X=17 has ODD parity (expected EVEN)

#### sg13g2_nand2_2.ldr
- NMOS contact at Stud X=7 has ODD parity (expected EVEN)

#### sg13g2_nand2b_2.ldr
- Input contact at Stud X=9 has incorrect symmetric parity (expected EVEN)

#### sg13g2_nand3_1.ldr
- Input contact at Stud X=6 has incorrect symmetric parity (expected ODD)

#### sg13g2_nor2b_2.ldr
- NMOS contact at Stud X=1 has ODD parity (expected EVEN)
- Input contact at Stud X=9 has incorrect symmetric parity (expected EVEN)

#### sg13g2_nor4_2.ldr
- Input contact at Stud X=9 has incorrect symmetric parity (expected EVEN)

#### sg13g2_or2_1.ldr, sg13g2_or2_2.ldr
- PMOS contact at Stud X=3 has opposite parity (expected EVEN)

#### sg13g2_or3_1.ldr, sg13g2_or3_2.ldr, sg13g2_or4_1.ldr, sg13g2_or4_2.ldr
- Input contact at Stud X=6 has incorrect symmetric parity (expected ODD)

#### sg13g2_sdfbbp_1.ldr
- Input contact at Stud X=2 has incorrect symmetric parity (expected ODD)
- Input contact at Stud X=6 has incorrect symmetric parity (expected ODD)
- Input contact at Stud X=51 has incorrect symmetric parity (expected EVEN)

#### sg13g2_slgcp_1.ldr
- PMOS contact at Stud X=5 has opposite parity (expected EVEN)
- Input contact at Stud X=21 has incorrect symmetric parity (expected EVEN)

### LEF Contact Alignment Failures (Markdown Design Docs)
These failures are reported by `scripts/verify_lef_contacts.py` and indicate mismatches between the ASCII art in `design/*.md` and the LEF pin/obstruction rectangles.

**Note:** All 84 cells currently fail this check. Common issues include:
- Missing rail contacts at Stud X=0, 2, 4... (even) for VDD and Stud X=1, 3, 5... (odd) for VSS.
- Extra or missing active region contacts due to strict parity enforcement in the verification script vs. manual layout decisions in the design docs.
- Parity rule implementation in `verify_lef_contacts.py` (Active/Input ODD) may conflict with "Big" model symmetric rules or specific cell requirements.
