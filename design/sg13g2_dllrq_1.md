# Design Documentation for sg13g2_dllrq_1

## Substrate
```
  0123456789012345678901234567
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567
4 pppppppppppppppppppppppppppp
3 NNNNNNNNNNpNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNpNNNNNNNNNNNNNpppN
1 NNNNNNNNpppppppppppppppppppp
0 NNpppppppppppppppppppppppppp
9 NNpppppppppppppNNNNNpppppppp
8 NNpppppppppppppNNNNNpppppppp
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SnnnnnnSnnnSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnSSSSnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SSSnnSSnnnnnnnnnnnnnnnnnnnnS
1 SSSnnSSSSSnnnSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567
4
3
2            GG  G GG  G G G
1    GGG   G GG  G GG  G G G
0    GGG   G GG  G GG  G G G
9    GGG   G GG  GGGG  G G G
8    GGG   G GG  GGGG  G G G
7   GGGG   G GGGGG  G GG G G
6   GGGG GGGGGGGG GGGGGG GGGG
5   GGGG GGG GGGG GGGGGGGGGG
4   GGGG   G   GG GGG  GGG G
3   GGGG   G   GG GGG  GGG G
2     GG   G   GG GGG  GGG G
1          G   G         G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+
3 ++++++++++++++++++++++++++++
2    ++     &       +++  +& o
1    ++     +       +++CC++ OO
0  Cc+&CcCCCCCCCCCC &+&Cc+& oO
9  CC++CCCC    CCCCCCCCCCCCCOO
8  Cc+&CcCcCCCCcCCcCcCCCCCCCoO
7  C I ICCCCCCCCCCCCCC C ICCOO
6  C i iCcCCCcCcCCc  CcC iCcOO
5  CC   CCCCCCCCCCCC CCC I COO
4  Cc  CcCcCCC   CCCCCCc  _ oO
3  CCCCCCCCCCC   CCCC-CC  - OO
2     _     _-_  c  -_Cc  _ oO
1 ----------------------------
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | GATE_N | Q | D | RESET_B |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X | X |   |   |
| PMOS1 | X |   | X | X |   |   |
| Poly1 | X |   | X |   |   | X |
| Poly2 | X | X | X |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 | O | O |
| PMOS1 | O | O |

