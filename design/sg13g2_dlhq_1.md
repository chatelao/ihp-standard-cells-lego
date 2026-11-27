# Design Documentation for sg13g2_dlhq_1

## Substrate
```
  012345678901234567890123456789
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSNNNNNNNNSSSSSSS
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
3 NNNNNNppNNNNNNNNNNppNNNNNNNNNN
2 NNNNNpppNNppppppNNppNNNNNNpppN
1 NpppppppNNppppppppppNNNNpppppN
0 NpppppppppppppppppppppNppppppN
9 NpppppppppppppNNppppppNppppppN
8 NNNNNppppppppNNNppppppNppppppN
7 NNNNNNNNNNNNNNNNNpppppNNNNNNNN
6 SSSSSSSSSSSSSSSNNNNNNNNSSSSSSS
5 SSSSSnnnnnnnnnnSSnnnnnnnnnnnnS
4 SnnnSnnnnnnnnnnSSnnnnnnnnnnnnS
3 SnnnSnnnSSSSnnnSSnnnnnnnnnnnnS
2 SSSSSnnnSSSSnnnSSnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSnnSSSSnnSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789
4
3
2   G   G    GGGG            G
1   G   G    GGGG  GG      G G
0   G   GGG  GGGG  GG G    G G
9   G   GGG  GGGG  GG G    G G
8   G   GGG  GGGG  GG G    G G
7  GGGG GGGGGGGGG  GG G GGGGGG
6  GGGGGG  GGGGGG GGG GGGGGGGG
5   GGG G  GGG G GGGGGGG  GGGG
4   G   G  GGG G GG GGGG  GGGG
3   G   G  GGG G    GGGG  GGGG
2   G   G GGG  G    GGGG  GGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3 ++++++++++++++++++++++++++++++
2  & c c+& Cc CCc   +&     ++ o
1  + CCCCCCCC CCCCCCCCCCCCC++OO
0  & cCc  CCCCC CCCCCCCCCCc+&Oo
9  + CCC  CCCCCCCCCCCCCCCCC++OO
8    CCc  c CC cCCCcC CcCCc &Oo
7  IICC     CCCCCC CC CCCCIICCO
6  IiCcCCCCCCcCCcC CC CCcCiIcCO
5    CCCC-CCCCCCCCCCC CC CC COO
4  _ cCcC_CCCCcCcCcCc CCcc  CoO
3  --CCCC- C CCCC  CCCCCCCCCCOO
2  --    -CcCCCCCCCCcC_CCC _  o
1 ------------------------------
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | Q | D | GATE |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X | X |   |   |
| NMOS2 |   | X | X |   |   |   |
| NMOS3 |   | X | X |   |   |   |
| PMOS1 | X |   | X |   |   |   |
| PMOS2 | X |   | X | X |   |   |
| Poly1 |   |   | X |   | X |   |
| Poly2 |   | X | X | X |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   | O |
| NMOS2 | O | E |
| NMOS3 | O |   |
| PMOS1 | O | O |
| PMOS2 |   | O |

