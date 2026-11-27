# Design Documentation for sg13g2_dlhrq_1

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
2 NppppppNNNpppppppppppppppNN
1 NpppppppppppppppppppppppppN
0 NpppppppppppppppppppppppppN
9 NppppppppppppppNNNppppppppN
8 NNNNNppNppppppNNNNNpppppppN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SnnnnnnnnnSSSSSSSSSSSSSSSSS
4 nnnnnnnnnnnnnnnSSSnnnnnnnSS
3 nnnnnnnnnnnnnnnnnnnnnnnnnSS
2 SSSSnnnnnnnnnnnnnnSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456
4
3
2   G G     GGG G GG G G G
1   G G   GGGGG G GG G G G
0   G G   GGGGG GGGG G G G
9   G G   GGGGG GGGG G G G
8   G G   GGGGGGG GG G G G
7  GG GGGGGGGGGGGGGGGGGGGG
6  GGGGGGGGGGGGGGGGGGGGGGGG
5   GG G   GGGGGGGGG GGG G
4   GG G   GGGG G G  GGG G
3   GG G   GGGG G G  GGG G
2      G   GGGG G G  GGG G
1             G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&
3 +++++++++++++++++++++++++++
2  c &+    +&CCCCC  & c & oO
1  CC++    ++CCCCC  + CC+ OO
0  cCCCCCCCCCCCcCc    cC& oO
9  CCC CC C CCCCCCCCCCCC+ OO
8   CC cC c C CCCCCcCCc & oO
7  ICCIICCC CCCCCCCCCCCI   O
6  iCCiICcC cCcCCc  cCCi cCO
5  CCC  CCCCCCCCCC  CCCCCCCO
4 CcCC CcCcCCCCcCC  Cc  _ oO
3    --CC   -CCC C--CC --OOO
2    -_ c  -_CCCCC-_ c --
1 ---------------------------
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | D | Q | GATE | RESET_B |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X | X | X |   |   |
| PMOS1 | X |   | X | X |   |   |
| PMOS2 | X |   |   |   |   |   |
| Poly1 | X | X | X |   | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 | N |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |

