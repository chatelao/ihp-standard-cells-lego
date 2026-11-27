# Design Documentation for sg13g2_ebufn_4

## Substrate
```
  012345678901234567890123456
4 NNNNNNNNNNNNNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456
4 ppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NpppppNNNpppppppppppppppppN
0 NpppppNNNpppppppppppppppppN
9 NpppppNNNpppppppppppppppppN
8 NpppppNNNpppppppppppppppppN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnSSSnnnnnnnnnnnnnnnnnS
3 SnnnnnSSSnnnnnnnnnnnnnnnnnS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456
4
3
2   G G     GGG G G G G G G
1   G G     GGG G G G G G G
0   G G     GGG G G G G G G
9   G G     GGG G G G G G G
8   G G     GGG G G G G G G
7   G GGGGGGGGGGGGG GGGGGGG
6   GGGGG GGGGGGGGG GGGGGGG
5   G GGGGGGGGGGGGG G G G G
4   G G  GG GGG G G G G G G
3   G G  GG GGG G G G G G G
2   G G  GG GGG G G G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&
3 +++++++++++++++++++++++++++
2  c &+    c &+c &+cCCCcCCCc
1  CC++    CC++CC++C  CC  CC
0  cCCCCCC CCCCcC&+c oCcOoCc
9  C   C CCCCC CC  C OOOOOCC
8  CIIIcCCCCCC cCCCc oOOOo c
7  CII CCCC  CCCCCCCCCCC O
6  CiIIIiCC  CCCCCCCcCcc O
5  C  IIICCCCCCCCCCC OOOOO
4  c _II CccC_-cC_-c oOOOoCc
3  C -CCCCCCC--CC--C  CC  CC
2  c _ cCCcc _-c _-cCCCcCCCc
1 ---------------------------
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Internal1 | Z | A |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 |   | X | X |   |   |
| NMOS3 |   | X | X | X |   |
| PMOS1 |   |   | X |   |   |
| PMOS2 | X |   | X | X |   |
| PMOS3 | X |   |   |   |   |
| Poly1 | X | X | X |   | X |
| Poly2 |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| NMOS3 | O | O |
| PMOS1 | O |   |
| PMOS2 | O | O |
| PMOS3 |   |   |

