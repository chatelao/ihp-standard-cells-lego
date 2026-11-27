# Design Documentation for sg13g2_einvn_4

## Substrate
```
  01234567890123456789012
4 NNNNNNNNNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012
4 ppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNN
1 NpppNNppppppppppppppppN
0 NpppNNppppppppppppppppN
9 NpppNNppppppppppppppppN
8 NpppNNppppppppppppppppN
7 NNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SnnnSSnnnnnnnnnnnnnnnnn
3 SnnnSSnnnnnnnnnnnnnnnnn
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012
4
3
2   G   GGGGGGG G G G G
1   G   GGGGGGG G G G G
0   G   GGGGGGG G G G G
9   G   GGGGGGG G G G G
8   G   GGGGGGG G G G G
7  GGGGGGGGGGGG GGGGGGGG
6   G  GGGGGGGGG GGGGGGG
5   G GGGGGGGGGG G G GGG
4   G GG G G G G G G GGG
3   G GG G G G G G G GGG
2   G  G G G G G G G GGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&
3 +++++++++++++++++++++++
2  &+c  c+&c &+cCCCcCCCc
1  ++CCCC++CC++CC  C  CC
0  &+cCCc+&cC&+cCo cOoCc
9  ++CCCC++CC++CCOOOOOCC
8  & cCCc &cC& cCoOOOo c
7  IICCCCCCCCCCCCOOIIII
6  IiCC  CCCCCCCCOOiiIi
5    CC CCCCCCCCCOOOOOO
4  _-cCccC_-cC_ cOoOOOocC
3  --CCCCC--CC- CCCCC OCC
2  _-cCc  _-c _ cCCCcCCcC
1 -----------------------
0 _-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Internal1 | Z | A | TE_B |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X | X |   |   |   |
| NMOS3 |   | X | X | X |   |   |
| PMOS1 | X |   | X |   |   |   |
| PMOS2 | X |   | X | X |   |   |
| PMOS3 | X |   |   |   |   |   |
| Poly1 | X |   | X |   |   | X |
| Poly2 |   |   | X | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| NMOS3 | O | O |
| PMOS1 | O |   |
| PMOS2 | O | O |
| PMOS3 |   |   |

