# Design Documentation for sg13g2_dlygate4sd3_1

## Substrate
```
  0123456789012345
4 NNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345
4 pppppppppppppppp
3 NNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NppppppNpppppppN
0 NppppppNpppppppN
9 NppppppNpppppppN
8 NNNNNNNNpppppppN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SSSSSSSSnnnnnnnS
3 SnnnnnnSnnnnnnnS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345
4
3
2  GG G GGG G
1  GG G GGG G
0  GG G GGG G
9  GG G GGG G G
8  GG G GGG G G
7  GG G GGG G G
6  GGGG GGG G G
5  GG G GGG G G
4  GG G GGG G G
3  GG G GGG G
2  GG G GGG G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 ++++++++++++++++
3    +        +
2   &+    & & +
1    +  C C   +OO
0  Cc+  c c   +Oo
9  CCCC C C    OO
8   c c c cCcCcOo
7  II C C     C O
6  iIiC CccCc c o
5     C C     COO
4  CcCc c cCcCcOo
3  C -  C     -OO
2   _-    _ _ -
1    -        -
0 ----------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VDD3 | VSS | VSS2 | VSS3 | A | Internal1 | Internal2 | Internal3 | X |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS3 |   |   |   |   |   |   |   |   |   | X | X |
| PMOS1 |   |   |   |   |   |   |   |   |   | X | X |
| PMOS2 |   |   |   |   |   |   |   | X | X |   |   |
| Poly1 | X |   |   | X |   |   | X | X |   |   |   |
| Poly2 |   | X |   |   | X |   |   |   | X | X |   |
| Poly3 |   |   | X |   |   | X |   |   | X | X |   |
| Poly4 |   |   |   |   |   |   |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |
| NMOS2 | O | O |   |   |
| NMOS3 |   | O | O | O |
| PMOS1 |   | O | O | O |
| PMOS2 | O | O |   |   |
| PMOS3 |   |   |   |   |
