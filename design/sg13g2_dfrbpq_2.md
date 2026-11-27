# Design Documentation for sg13g2_dfrbpq_2

## Substrate
```
  01234567890123456789012345678901234567890123456789
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNSSSSSSSSSSNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSNNNNNNNNNNSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789
4 pppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNpppNNNNNNNNNppNNppNNNNNNNNNN
2 pppppppNNNNpNNNNNNNNppppppNNNppNNNppNNppppNNNNNNNN
1 NppppppppppppppppNNNpppppppNppppNNppNNppppNNpppppN
0 NNNNppppppppppppppNNpppppppNppppNNppNNppppNNpppppN
9 pppppppppppppppppNNNpppppppNppppppppppppppNNpppppN
8 ppppppppNNNNNNNNNNNNpppppppNppppppppppppppNNpppppN
7 NNNNNNNNNSSSSSnSSSSNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSnnSSSSSnnnnnnSSSSSSSSSSSSSSSSSSSNNNNNNNNNNSSS
5 SSSSnnnnSSSSnnnnnnSnnnnnnnSnnnnnnSSSSSSSSSSSSSSSSS
4 SnnnnnnnSSSSSSSSSSSnnnnnnnSnnnnnnSSSSSSSnnnSnnnnnS
3 nnnnnnnnnnnnnSSSSSSnnnnnnnSSSnnnnnnnnnnnnnnSnnnnnS
2 SnnnnSSSSSSSSSSSSSSSSnnSSSSSSSnnnSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSnnSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789
4
3          GGGGGGGGGG
2      G   GGGGGGGGGG  GG G    GG     GG  G    G G
1      G   G  GG G  G  GG G    GG     GG  G    G G
0   GGGG   G  GG G     GG G    GG GGG GGG G    G G
9   GGGG   G  GG GGGGG GG G  G GG GGG GGG G    G G
8   GGGG   G  GG G  GG GG G GGGGG GGG GGG G    G G
7   GGGGG  GGGGGGG    GGG GG GGG GGGG GGG G  G G G
6 GGGG GG  GGG GGG    GGG GG  GGGGG G GGGGGG GGGGG
5   GG GG  GGG GGG    G   G   GGGG  G GGG  G   G G
4   GG GG  GGG GG     G   G   GGGG  GGGGG  G   G G
3   GG GG  GGG GG     G   G   GGGG  GGGGG  G   G G
2   GG     GGG GGGGGGGG   G     GG  GGGGG  G   G G
1     GGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3 ++++++++++++++++++++++++++++++++++++++++++++++++++
2 +& CCCCCCC & CCCC cCCCCCCCCCCCCCCCCCCc+&    &+o &
1 ++ CCCC CCC+CCCCCCCCCCCCCCCCCCCCCCCCCC++CC  ++O +
0 ++ CCCcCcCCCCCcCcC  CcCCCCCCCCC       +&Cc  &+o &
9 ++CCC   C CCC CCC  CCCCCCCCCCCCC    CC +CC  ++O +
8  & cCCCCCCCCCCCCC CcCcCCCcCcCcCcCCCCCcCCCc  & o &
7    CCCC IICC  CCC  C CC II  CCC CCC    CCCCC  OOO
6  i CC c IiCcCccCCcCC cC IiCCCCCcCCc  CcCCCCcC OOO
5    CCCCCCCCCCCCCCCCC  C IICC CCCCCCCCCCC  CC  O
4    CCCcCCCC  CCC C c  CCCcCCcCcCC      C_-cC_-o _
3 CCCC--C --CCCCCCCC    CCCCCCCCCCCCC-- CC--CC--O -
2  cCC_-  _-CCcCCCCCCCCCCCCCCCCCCCc  _- cC_-c _-o _
1 --------------------------------------------------
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | RESET_B | Q | CLK | D |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X |   |   |   |
| NMOS2 |   | X | X |   |   |   |
| NMOS3 |   | X | X |   |   |   |
| NMOS4 |   | X |   | X |   |   |
| NMOS5 |   |   | X |   |   |   |
| PMOS1 | X |   | X |   |   |   |
| PMOS2 | X |   | X |   |   |   |
| PMOS3 | X |   |   | X |   |   |
| Poly1 | X |   | X |   |   |   |
| Poly2 |   |   | X |   |   | X |
| Poly3 |   |   |   |   | X |   |
| Poly4 |   | X | X |   |   |   |
| Poly5 |   |   | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 | O |   | O |   |   |
| NMOS2 | O | O |   |   |   |
| NMOS3 |   |   |   | O |   |
| NMOS4 |   |   |   |   | O |
| NMOS5 | O |   |   |   |   |
| PMOS1 | O | O |   |   |   |
| PMOS2 | O |   | O | O |   |
| PMOS3 |   |   |   |   | O |

