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
3 NNNNNNNNNNNNNNNNNNNNNNpNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNpNNNNNNN
1 NpppppNpNNNNNppppppNpppppppppN
0 NpppppNpppNppppppppNpppppppppN
9 NpppppNpppNpppNNpppNpppppppppN
8 NNNNNNNpppNpppNNpppNNNNNNNpppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnSnnnSSSSnnSnnnnnnSnnnS
3 SnnnnnnnSnnnnnnnnnSnnnnnnSnnnS
2 SSSSSnSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSnSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789
4
3
2  GG  G  G G G GGGG  G GGG
1  GG  G  G G G GGGG  G GGG
0  GG  G  G G G GGGG  G GGG
9  GG  G  G G G GGGG  G GGG
8  GG GG  G G G GGGG  GGGGG
7  GG GG  G GGG G GG  GGG G  G
6  GG  G  G G G G GG  GGGGG  G
5  GG  GG GGG G G G   G GGG  G
4  GG  GG G G G G G   G GGG  G
3  GG  GG G G G G G   G GGG  G
2  G   GG G G G G G   G GGG  G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +     +        +         +
2  +     +        +         +
1  +   C +        + CCCCC C +OO
0  +   cCccCcC C    c c c c +Oo
9       C    C C    CCC C C +OO
8  i iIiCccC CcCcCcCcCc c cC Oo
7  I  I CCCCCCCC   C C IC  C  O
6  i cCcCcc cCcCcCcC CiIcC CcCo
5    C   C CC C    C C     C  O
4  - c c c  c cCcCcCcCc-  cC- o
3  - CCCCCCCCCCC -C  C -  CC- O
2  -   -  c cCcC -cCcC -    -
1  -   -         -     -    -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | CLK | GATE | SCE | Internal1 | Internal2 | GCLK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   | X |   |   |
| NMOS2 |   |   |   |   |   | X |   |   |
| NMOS3 |   |   |   |   |   | X | X |   |
| NMOS4 |   |   |   |   |   |   |   | X |
| PMOS1 |   |   |   |   |   | X |   |   |
| PMOS2 |   |   |   |   |   | X |   |   |
| PMOS3 | X |   |   |   |   | X | X | X |
| PMOS4 |   |   |   |   |   | X |   |   |
| Poly1 |   |   |   |   | X |   |   |   |
| Poly2 |   |   |   | X |   | X |   |   |
| Poly3 |   |   |   |   |   | X |   |   |
| Poly4 |   |   |   |   |   | X |   |   |
| Poly5 |   |   | X |   |   | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | O | O | E |   |   |   |
| NMOS2 |   |   | O | O |   |   |
| NMOS3 |   |   |   |   | O |   |
| NMOS4 |   |   |   |   |   | O |
| PMOS1 |   |   | O |   |   |   |
| PMOS2 |   |   | O | O |   |   |
| PMOS3 |   |   |   |   | O | S |
| PMOS4 | O | O |   |   |   |   |
