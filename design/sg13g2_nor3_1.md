# Design Documentation for sg13g2_nor3_1

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
3
2  GG GGGG
1  GG GGGG
0  GG GGGG
9  GG GGGG
8  GG GGGG
7  GG GGGG
6  GG GGGG
5  GG GGGG
4  GG GGGG
3  GG GGGG
2  GG GGGG
1   G  G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &&&&&&&&&
3 +++++++++
2 +++&+++++
1 +++++++++
0 +++&+++&+
9 ++++&&&&+
8 +++++++&+
7    OOOOOO
6  iIIIiOiO
5  IIIIIOOO
4 ---_-_-_-
3 ---------
2 ---_-----
1 ---------
0 _________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | B | C | Y |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 | X |   |   |   | X |
| PMOS1 | X |   |   |   | X |
| Poly1 |   |   | X |   |   |
| Poly2 | X | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 | N | N |
| NMOS2 | O | O |
| PMOS1 | O | O |
