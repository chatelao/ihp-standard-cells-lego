# Design Documentation for sg13g2_dllr_1

## Substrate
```
  0123456789012345678901234567890123
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123
4
3
2   G G G               G G
1   G G G               G G
0   G G G               G G
9   G G G               G G
8   GGGGG               G G
7   G G G               G G
6   GGGGG               GGG G     G
5   G G G               G G
4   G G G               G G
3   G G G               G G
2   G G G               G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3 ++++++++++++++++++++++++++++++++++
2  cC+&cCcc &+cCcCc &+&+ +&     &OoO
1  CC++CCCCCCCCCCCC ++++C++OOOC +OOO
0  cC  cCccCcCcCcCc &+&+c+&OoOc &OoO
9  CCCCCCCCCCCCCCCCCCCCCC++OOOC +OOO
8  cIiIiCccCcCcCcCcCcCcCcCcOoOc &OoO
7  CIIIICCCCCCCCCCCCCCCCIICOOOCCCCOO
6  cIIIICccCcCcCcCcCcCcCiIcCoOcCcCoO
5  C --CCCCCCCCCCCCCCCCCII OOOC   OO
4  cC_-cCccCcCcCcCcC__cC _-OoOc_-OoO
3  CC--CCCC --  CCCC--CC --OOOC--OOO
2    _-cCcc -_  cCcC-_cC _-OoO _-OoO
1 ----------------------------------
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | GATE_N | RESET_B | VSS2 | VSS3 | Q | Q_N | VDD | VSS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   | X |
| NMOS2 |   |   | X | X | X | X |   | X |
| PMOS1 | X |   | X | X | X | X | X |   |
| PMOS2 |   |   |   |   |   |   | X |   |
| Poly1 | X |   | X |   |   |   | X |   |
| Poly2 |   | X | X |   |   |   | X |   |
| Poly3 |   |   | X |   | X |   |   |   |
| Poly4 |   |   |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |
| NMOS2 | O | O |   |   |
| PMOS1 | O | O |   |   |
| PMOS2 |   |   |   |   |
