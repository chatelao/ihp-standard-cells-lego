# Design Documentation for sg13g2_einvn_2

## Substrate
```
  0123456789012345
4 NNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNN
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
1 NNpppNpppppppppN
0 NNpppNpppppppppN
9 NNNNNNpppppppppN
8 NNNNNNpppppppppN
7 NNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SSSSSSnnnnnnnnnS
3 SSnnnSnnnnnnnnnS
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
2    GGGGGGG GGG
1    G   G G GGG
0    G   G G GGG
9    G   G G GGG
8   GG   G G GGG
7   GG G G G GGG
6   GG GGGGG GGGG
5   GG   G G G GG
4    G   G G G G
3    G   G G G G
2    G   G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &+&+&+&+&+&+&+&+
3 ++++++++++++++++
2   &+c c &CcCCCc
1   ++CCC +CC  CC
0   &+cCc &Cc oCc
9     CCCCCCC OCC
8  IIiCCcCCCc o c
7  IIICC      O
6  IIiCcC     O i
5  IIICC      O I
4     cCcCCCc o I
3   --CCC -CCCCCC
2   _-  c _ cCCCc
1 ----------------
0 _-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | Z | A | TE_B |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |   |
| NMOS2 |   |   |   |   |   |   |
| NMOS3 | X |   |   | X |   |   |
| PMOS1 | X | X |   | X |   |   |
| PMOS2 | X | X |   |   |   |   |
| PMOS3 |   | X |   |   |   |   |
| Poly1 | X | X |   |   |   | X |
| Poly2 |   |   |   | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| NMOS3 | O | O |
| PMOS1 | O | O |
| PMOS2 | O |   |
| PMOS3 |   |   |

