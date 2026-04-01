# Design Documentation for sg13g2_nand3_1

## Substrate
```
  012345678
4 SSSSSSSSS
3 NNNNNNNSS
2 NNNNNNNSS
1 NNNNNNNSS
0 NNNNNNNSS
9 NNNNNNNSS
8 SSSSSSSSS
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 SSSSSSSSS
3 SSSSSSSSS
2 SSSSSSSSS
1 SSSSSSSSS
0 SSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678
4 ppppppppp
3 pppppppnn
2 pppppppnn
1 pppppppnn
0 pppppppnn
9 pppppppnn
8 SnnnnnnnS
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 SSSSSSSSS
3 SSSSSSSSS
2 SSSSSSSSS
1 SSSSSSSSS
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  012345678
4
3       G
2  GGGG GG
1  GGGG GG
0  GGGG GG
9  GGGG GG
8  GGGG GG
7  GGGG GG
6  GGGG GG
5  GGGG GG
4  GGGG GG
3  GGGG GG
2  GGGG GG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &&&&&&&&&
3 +++++++++
2 +++&+++&+
1 +++++++&+
0 +++&+++&+
9 +++++++&+
8    oOOOo
7  IIIIIOO
6  iIiiIoi
5  IIIIIOO
4 -------_-
3 ---------
2 ---_-----
1 ---------
0 _________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | C | Y |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 | X |   |   | X |
| PMOS1 | X |   |   | X |
| Poly1 | X | X | X | X |
| Poly2 | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O | O |
