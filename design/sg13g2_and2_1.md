# Design Documentation for sg13g2_and2_1

## Substrate
```
  012345678
4 SSSSSSSSS
3 NNNNNNNSS
2 NNNNNNNSS
1 NNNNNNNSS
0 NNNNNNNSS
9 NNNNNNNSS
8 NNNNNNNSS
7 NNNNNNNSS
6 NNNNNNNSS
5 NNNNNNNSS
4 NNNNNNNSS
3 NNNNNNNSS
2 NNNNNNNSS
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
8 pppppppnS
7 NNNNNNNSS
6 NNNNNNNSS
5 pppppppnS
4 pppppppnS
3 pppppppnS
2 NNNNNNNSS
1 SSSSSSSSS
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678
4
3
2 GGGGGGG
1 GGGGGGG
0 GGGGGGG
9 GGGGGGG
8 GGGGGGG
7 GGGGGGG
6 GGGGGGG
5 GGGGGGG
4 GGGGGGG
3 GGGGGGG
2 GGGG GG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &&&&&&&&&
3 +++++++++
2 +++&+++++
1 +++++++&+
0 +++&+++&+
9  IIIIIIoO
8  IIIIIIoO
7  IIIIIIOO
6  IIiIiIOO
5  IIIIIIOO
4 ---_---_-
3 ___------
2 ___------
1 ---------
0 _________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | B | X |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 |   | X |   | X |
| NMOS3 | X |   |   | X |
| PMOS1 |   | X | X |   |
| PMOS2 | X |   | X |   |
| Poly1 | X | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | W |
| NMOS3 | W |
| PMOS1 | O |
| PMOS2 | O |
