# Design Documentation for sg13g2_dfrbp_2

## Substrate
```
  01234567890123456789012345678901234567890123456789012
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNSSSSSSSSSSNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSNNNNNNNNNNSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012
4 ppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNpppNNNNNNNNNppNNNNNNNNNNNNNNNNN
2 pppppppNNNNpNNNNNNNNppppppNNNppNNNppNNNNNNNNNNNNNNNNN
1 NppppppppppppppppNNNpppppppNppppNNppNNpppppppNpppppNN
0 NNNNppppppppppppppNNpppppppNppppNNppNNpppppppppppppNN
9 pppppppppppppppppNNNpppppppNpppppppppppppppppppppppNN
8 ppppppppNNNNNNNNNNNNpppppppNpppppppppppppppppppppppNN
7 NNNNNNNNNSSSSSnSSSSNNNNNNNNNNNNNNNNNNNNppppppNNNNNNNN
6 SSSSSnnSSSSSnnnnnnSSSSSSSSSSSSSSSSSSSNNNNNNNNNNSSSSSS
5 SSSSnnnnSSSSnnnnnnSnnnnnnnSnnnnnnSSSSSSSnnnnnSSSSSSSS
4 SnnnnnnnSSSSSSSSSSSnnnnnnnSnnnnnnSSSSSSSnnnnnnnSnnnnn
3 nnnnnnnnnnnnnSSSSSSnnnnnnnSSSnnnnnnnnnnnnnnnnnnSnnnnn
2 SnnnnSSSSSSSSSSSSSSSSnnSSSSSSSnnnSSSSSSSnnnnnnnSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSnnSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012
4
3          GGGGGGGGGG
2      G   GGGGGGGGGG  GG G    GG     GG GGGG    GGG
1      G   G  GG G  G  GG G    GG     GG GGGGGG  GGG
0   GGGG   G  GG G     GG G    GG GGG GGGGGGGGG  GGG
9   GGGG   G  GG GGGGG GG G  G GG GGG GGGGGGGGG  GGG
8   GGGG   G  GG G  GG GG G GGGGG GGG GGGGGGGGG  GGG
7   GGGGG  GGGGGGG    GGG GG GGG GGGG GGGGGGGGG  GGG
6 GGGG GG  GGG GGG    GGG GG  GGGGG G GGGGGGGGGG GGGGG
5   GG GG  GGG GGG    G   G   GGGG  G GGG  G G G   G G
4   GG GG  GGG GG     G   G   GGGG  GGGGG  G G G   G G
3   GG GG  GGG GG     G   G   GGGG  GGGGG  G G G   G G
2   GG     GGG GGGGGGGG   G     GG  GGGGG  G G G   G G
1     GGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3 +++++++++++++++++++++++++++++++++++++++++++++++++++++
2 +& CCCCCCC & CCCC cCCCCCCCCCCCCCCCCCCc++  ++  &+o &+
1 ++ CCCC CCC+CCCCCCCCCCCCCCCCCCCCCCCCCC++OO++CC++OO++
0 ++ CCCcCcCCCCCcCcC  CcCCCCCCCCC       +&Oo&+cC&+oO&+
9 ++CCC   C CCC CCC  CCCCCCCCCCCCC    CC +OO++CC++OO++
8  & cCCCCCCCCCCCCC CcCcCCCcCcCcCcCCCCCcCCOo&+cC&+oO&+
7    CCCC IICC  CCC  C CC II  CCC CCC    COO+ CCCCOO
6  i CC c IiCcCccCCcCC cC IiCCCCCcCCc  CcCOOOO CCcOOO
5    CCCCCCCCCCCCCCCCC  C IICC CCCCCCCCCCC  OO  C  OOOO
4    CCCcCCCC  CCC C c  CCCcCCcCcCC      C  oO  c-_OoOO
3 CCCC--C --CCCCCCCC    CCCCCCCCCCCCC-- CC--OO- C--OO--
2  cCC_-  _-CCcCCCCCCCCCCCCCCCCCCCc  _- cC_-o _ c-_ o-_
1 -----------------------------------------------------
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Internal1 | RESET_B | Q | Q_N | CLK | D |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   | X |   |   |   |   |
| NMOS2 |   | X |   | X |   |   |   |   |
| NMOS3 |   | X | X | X |   | X |   |   |
| NMOS4 |   | X |   |   | X |   |   |   |
| NMOS5 |   |   |   | X |   |   |   |   |
| PMOS1 | X |   | X | X | X | X |   |   |
| PMOS2 | X |   |   | X |   |   |   |   |
| Poly1 | X |   |   | X |   |   |   |   |
| Poly2 |   |   |   | X |   |   |   | X |
| Poly3 |   |   |   |   |   |   | X |   |
| Poly4 | X | X | X | X |   | X |   |   |
| Poly5 |   |   | X |   | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 | O |   | O |   |   |
| NMOS2 | O | O |   |   |   |
| NMOS3 |   |   |   | O |   |
| NMOS4 |   |   |   |   | O |
| NMOS5 | O |   |   |   |   |
| PMOS1 | O |   | O | O | O |
| PMOS2 | O | O |   |   |   |

