# Design Documentation for sg13g2_nand3_1

## Substrate
```
  012345678
4 NNNNNNNNN
3 SNNNNNNNN
2 NNNNNNNNN
1 NNNNNNNNN
0 NNNNNNNNN
9 NNNNNNNNN
8 NNNNNNNNN
7 NNNNNNNNN
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
3 NNNNNNNNN
2 NpppppppN
1 NpppppppN
0 NpppppppN
9 NpppppppN
8 NpppppppN
7 NNNNNNNNN
6 SSSSSSSSS
5 SnnnnnnnS
4 SnnnnnnnS
3 SnnnnnnnS
2 SSSSSSSSS
1 SSSSSSSSS
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678
4
3   G G
2   G G G
1   G G G
0   G G G
9   G G G
8   G G G
7  GGGG GG
6  GGGG GG
5   G G G
4   G G G
3   G G G
2   G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3 +++++++++
2  & o+& o
1  + O++OO
0  & o+&Oo
9  + OOOOO
8      O
7  I IIOII
6  i IiOiI
5      O
4  _   OOo
3  -    OO
2  _     o
1 ---------
0 _-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Y | A | B | C |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X | X |   |   |   |
| PMOS1 | X |   | X |   |   |   |
| PMOS2 | X |   |   |   |   |   |
| Poly1 |   |   |   |   | X | X |
| Poly2 |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O | O |
| PMOS2 | S |   |

