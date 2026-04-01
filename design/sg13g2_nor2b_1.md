# Design Documentation for sg13g2_nor2b_1

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
5 SnnnnnnnS
4 SnnnnnnnS
3 SnnnnnnnS
2 SnnnnnnnS
1 SSSSSSSSS
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  012345678
4
3
2  G GGGGG
1  GGGGGGG
0  GGGGGGG
9  GGGGGGG
8  GGGGGGG
7  GGGGGGG
6  GGGGGGG
5  GGGGGGG
4  GGGGGGG
3  GGGGGGG
2  G GGGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &&&&&&&&&
3 +++++++++
2 +++++&+++
1 ++++++&&+
0 +&+++&&&+
9  IIIIOoo
8  iIIIOOo
7  IIIIOOO
6  iIiIIoi
5 ---------
4 -_-_-_--_
3 ---------
2 --------_
1 ---------
0 _________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | Y |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 |   | X | X | X |
| NMOS3 | X |   | X | X |
| PMOS1 | X |   | X | X |
| Poly1 | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| NMOS3 | O |
| PMOS1 | O |
