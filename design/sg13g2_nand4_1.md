# Design Documentation for sg13g2_nand4_1

## Substrate
```
  01234567890
4 SSSSSSSSSSS
3 NNNNNNNSSSS
2 NNNNNNNSSSS
1 NNNNNNNSSSS
0 SSSSSSSSSSS
9 SSSSSSSSSSS
8 SSSSSSSSSSS
7 SSSSSSSSSSS
6 SSSSSSSSSSS
5 SSSSSSSSSSS
4 SSSSSSSSSSS
3 SSSSSSSSSSS
2 SSSSSSSSSSS
1 SSSSSSSSSSS
0 SSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890
4 ppppppppppp
3 pppppppnnnn
2 pppppppnnnn
1 pppppppnnnn
0 SnnnnnnnSSS
9 SSSSSSSSSSS
8 SSSSSSSSSSS
7 SSSSSSSSSSS
6 SSSSSSSSSSS
5 SSSSSSSSSSS
4 SSSSSSSSSSS
3 SSSSSSSSSSS
2 SSSSSSSSSSS
1 SSSSSSSSSSS
0 nnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  01234567890
4
3  G
2  GGGGGGGG
1  GGGGGGGG
0  GGGGGGGG
9  GGGGGGGG
8  GGGGGGGG
7  GGGGGGGG
6  GGGGGGGG
5  GGGGGGGG
4  GGGGGGGG
3  GGGGGGGG
2  GGGGGGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
4 &&&&&&&&&&&
3 +++++++++++
2 +++&++++&++
1 +++++++&+++
0 +++&+++&&++
9 +++++++&+++
8    oOOOoOO
7    OOIOIOO
6  iIiIiIiIO
5  IIIIiIIIO
4 --------_--
3 -------_---
2 ---_-------
1 -----------
0 ___________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | C | Y |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 | X |   |   | X |
| PMOS1 | X |   |   | X |
| Poly1 | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
