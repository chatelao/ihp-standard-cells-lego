# Design Documentation for sg13g2_sdfbbp_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901
4 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
4
3
2  G G G G G   G G         G GGGG   G G G           G G
1  G G G G G   G G         G G G                    G G
0  G G G G G   G G         G GGGG   G   G           G G
9  G G G G G   G G         GGG G                    G G
8  G G G G G   G G         G GGG  G       G G       G G
7  G GGG G G   G G         G GGG                    G G
6  GGG GGG G   GGGG        G GGG            G       GGG G     G
5  G G G G G   G G         G G G                    G G
4  G G G GGG   GGGG        G G G                    G G
3  G G G G G   G G         G G G                    G G
2  G G G G G   G G         G G G                    G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
2  cC+&cCccC&+cCcC&+cC     +&IiIiI&+iIiIiI&+& cC +&   & oO +&OoO
1  CC++CCCCC++CCCC++CCCC   ++IICCI++IICCCI+++CCC ++   + OOC++OOO
0  cCcCcCc   CcCcC&+cCcCcCc+&IiCiI&+iIcCiIcCcCcCcCcCcCcCoOc+&OoO
9  IIICCCCCCCCCCCC  CCCCCCC++IICCIIIIICCCICCIICCCCCCCCCCOOC++OOO
8  iIiIiIicCcC CcCcCcCcCcCcCcIiCcCiCcCcCcIiIiIcCc  CcCcCoOc  OoO
7  IIIIIIiCC C CIIICCCCCCCCCCIICCCCCCCCCCIIIII  CCCCIICCOOCC OOO
6  iIi  IicC CcCIIiCcCcCcCcCcIiCcCcCcCcCcCcCiIcCcCcCiIcCoOcC OoO
5  III CCCCCCC CIIICCCCCCCCCCCCCCCCCC CCCCCCCCCCCCCCIICCOOC  OOO
4  _-  c  -_cCcCiIiCcCcCcCcCcCcCcCcC__cCcCc -CcCcCcCcC-OoOc -OoO
3  --  C  --CC CCCCCCCCCCCC-- CCCCCC--CCCCC -CCCCCCCCC-OOOC -OOO
2  _-     -_cCcCc_-        _- cCcCcC-_cCcCc_-CcCcCc  _-OoO  -_oO
1 --------------------------------------------------------------
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | CLK | RESET_B | SCE | SET_B | VSS2 | VSS3 | Q | Q_N | VDD | VSS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   | X |
| NMOS2 | X |   |   |   | X | X | X | X |   | X |
| PMOS1 |   |   | X | X | X | X | X | X | X |   |
| PMOS2 |   |   |   |   |   |   |   |   | X |   |
| Poly1 |   |   | X |   | X |   |   |   |   | X |
| Poly10 |   |   |   | X |   |   |   |   |   |   |
| Poly11 |   |   |   | X |   |   |   |   |   |   |
| Poly12 |   |   |   | X | X |   |   |   |   |   |
| Poly13 |   |   |   | X |   |   |   |   |   |   |
| Poly14 |   |   |   | X |   |   |   |   |   |   |
| Poly15 |   |   |   | X |   |   |   |   |   |   |
| Poly2 | X |   |   |   | X |   |   |   |   | X |
| Poly3 |   |   |   | X | X |   |   |   |   | X |
| Poly4 |   | X |   |   | X |   |   |   | X |   |
| Poly5 |   |   |   | X | X |   |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   | X |   |   |
| Poly7 |   |   |   |   |   |   | X |   |   |   |
| Poly8 |   |   |   | X | X |   |   |   |   |   |
| Poly9 |   |   |   | X | X |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | O | O | O | O |   |   |   | O | O | O | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
