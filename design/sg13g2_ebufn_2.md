# Design Documentation for sg13g2_ebufn_2

## Substrate
```
  012345678901234567
4 NNNNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567
4 pppppppppppppppppp
3 NNNNNNNpNNNNNNNNNN
2 NpppppppppNNNpNNNN
1 NppppppppppppppppN
0 NppppppppppppppppN
9 NppppppppppppppppN
8 NppppppppppppppppN
7 NNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnSnnnnnSS
3 SnnnnnnnnnSnnnnnSS
2 SnnnnnnnnnSnnnnnSS
1 SSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567
4
3
2   G G G G   G G
1   G G G G   G G
0   G G G G   G G
9   G G G G   G G
8   G G G G   G G
7   G G GGGGGGG G
6   GGGG     GGGG
5   G GGGGGGG G G
4   G GGGGG   G G
3   G GGGGG   G G
2   G GGGGG   G G
1   G         G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567
4 &+&+&+&+&+&+&+&+&+
3 ++++++++++++++++++
2  cCCCc & c   &
1  CCCCCCCCC   + CC
0  cCo c  CCCCCCCcC
9  C O C  CCCC   CC
8   Oo c  CCCc   cC
7   OO    CCC    CC
6   OOcCCCCCc i iCC
5   OO      C    CC
4  cOoCcCCcCCcC_-cC
3  C OCC--CC CC--CC
2  cCCCc-_cC c _-c
1 ------------------
0 _-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Internal1 | Z | A | TE_B |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X | X | X |   |   |
| NMOS3 |   | X | X |   |   |   |
| PMOS1 | X |   | X | X |   |   |
| Poly1 |   | X | X |   |   |   |
| Poly2 |   |   |   |   | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 | N | N |
| NMOS2 | O |   |
| NMOS3 |   | O |
| PMOS1 | O | O |

