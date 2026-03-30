# Design Documentation for sg13g2_slgcp_1

## Substrate
```
  012345678901234567890123456789
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789
4 pppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNpppppppppN
2 NNNNNNNNNNNNNNNNNNNNpppppppppN
1 NpppppNpppNppppppppNpppppppppN
0 NpppppNpppNppppppppNpppppppppN
9 NpppppNpppNppppppppNpppppppppN
8 NNNNNNNpppNppppppppNpppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789
4
3
2   GGGGG G G G G   G G G G
1   GGGGG G G G G   G G G G
0   GGGGGGG G G G G G G G G
9  GGGGGGGG G G G G G G G G
8  GGGGGGGG G G G G G G G G G
7  GGGGGGGG G G G G G G G G G
6  GGGGGGGG G G G G G G G G G
5  GGGGGGGG G G G G G G G G G
4   GGGGGGG G G G G G G G G
3   GGGGGGG G G G G G G G G
2   GGG GGG G G G G G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789
4 ++++++++++++++++++++++++++++++
3  +     +        +         +
2 &+    &+      & +       & +
1  +   C +        + CCCCC C +OO
0  +  cCcCcCcC C    c c c c +Oo
9       C    C C    CCC C C +OO
8  IiIiIc cC CcCcCcCcCc c cC Oo
7  I  I CCCCCCCC   C C IC  C  O
6  i cCcCcc cCcCcCcC CiIcC CcCo
5    C   C CC C    C C     C  O
4  -cC  cC  c cCcCcCcCc-  cC- o
3  - CCCCCCCCCCC -C  C -  CC- O
2 _-  _-  c cCcC_-cCcC_-    - _
1  -   -         -     -    -
0 ------------------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VDD3 | VSS | VSS2 | CLK | SCE | Internal1 | Internal2 | GCLK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X | X |   |   | X | X | X |
| PMOS1 |   |   |   |   |   |   |   | X |   |   |
| PMOS2 |   |   |   |   |   |   |   | X |   |   |
| PMOS3 |   |   | X |   |   |   |   | X | X | X |
| PMOS4 |   |   |   |   |   |   |   | X |   |   |
| Poly1 | X |   |   | X |   |   | X | X |   |   |
| Poly10 |   |   |   |   |   |   |   |   | X |   |
| Poly2 |   |   |   |   |   |   |   | X |   |   |
| Poly3 |   |   |   |   |   |   |   | X |   |   |
| Poly4 |   | X |   | X |   |   |   | X |   |   |
| Poly5 |   |   |   |   |   |   |   | X |   |   |
| Poly6 |   |   |   |   |   |   |   | X |   |   |
| Poly7 |   |   |   | X |   | X |   | X |   |   |
| Poly8 |   |   |   |   |   |   |   | X |   |   |
| Poly9 |   |   | X |   |   |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | O | O | O | O | O | O | O | O | O | N |
| PMOS1 | O | E |   |   |   |   |   |   |   |   |
| PMOS2 |   | W | O | O | O | O |   |   |   |   |
| PMOS3 |   |   |   |   |   |   | O | O | O | O |
| PMOS4 | O |   |   |   |   |   |   |   |   |   |
