# Design Documentation for sg13g2_dfrbpq_1

## Substrate
```
  012345678901234567890123456789012345678901234567
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNSSSSSSSSSSNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678901234567
4 pppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNppNNNNNNNNNNNppNNppNNNNNNN
2 pppppppNNNNpNNNNNNNNppppppNNNppNNNNppNNppNNNNNNN
1 NppppppppppppppppNNNpppppppNppppNNNppNNppNpppppN
0 NNNNppppppppppppppNNpppppppNppppNNNppNNppNpppppN
9 pppppppppppppppppNNNpppppppNpppppppppppppNpppppN
8 ppppppppNNNNNNNNNNNNpppppppNpppppppppppppNpppppN
7 NNNNNNNNNSSSSSSSSSSNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSnnSSSSSnnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSnnnnSSSSnnnnnnSSnnnnnnSnnnnnnSSSSSSSSSSSSSSS
4 SnnnnnnnSSSSSSSSSSSSnnnnnnSnnnnnnSSSSSSSSSnnnnnS
3 nnnnnnnnnnnnnSSSSSSSnnnnnnSSSnnnnnnnnnnnSSnnnnnS
2 SnnnnSSSSSSSSSSSSSSSSSnnSSSSSSnnnSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSnnSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789012345678901234567
4
3          GGGGGGGGGG
2      G   GGGGGGGGGG  GG G    GG     GG     G G
1      G   G  GGGG  G  GG G    GG     GG     G G
0   GGGG   G  GGGG     GG G    GG G GGG G    G G
9   GGGG   G  GGGGGGG  GG G  G GG G GGG G    G G
8   GGGG   G  GGGG  G  GG G GGGGG G GGG G    G G
7   GGGGG  GGGGGGG     GG G  GGG GG GGG G    G G
6 GGGG GG  GGG GGG     GG GG  GGGGG GGGGGGGGGGGG
5  GGG GG  GGG GGG     GG G   GGGG  GGGGGGGGGG G
4   GG GG  GGG GG      GG G   GGGG  GGGGG    G G
3   GG GG  GGG GG      GG G   GGGG  GGGGG    G G
2   GG     GGG GGGGGGGGGG G     GG  GGGGG    G G
1     GGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789012345678901234567
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3 ++++++++++++++++++++++++++++++++++++++++++++++++
2 +& CCCCCCC &CCCCC cCCCCCCCCCCCCCCCCCCc &+ c+& o
1 ++ C    CCC+C   C CCCCCCCCCCCCCCCCCCCC ++CC++OO
0 ++ CCCcCcCCCC cCcC  CcCCCCCCCCC        &+Cc+&Oo
9 ++CCCCC C CCC CCC CCCCCCCCCC  CCCC   CC++CC++OO
8  & cCCCCCCCCCCCCC cCCcCCCcCcCcCcCC   cC& Cc+&Oo
7  I CCCC II C  CCC  C CC     CCCCCCCCCCCCCCC   O
6  i CC c Ii cCccCCcCC cC iICCCCCcCCc  CcCCCCCCcO
5  I CCCCCCCCCCCCCCCCC  C   CCCCCCCCCCCCCCCCC  CO
4  I CCCcCCCCc CCCCCCCCcCCCcCCcCcCC      CCCc-_Oo
3 CCCC--C --CCCCCCCCC       CCCCCCCCC-- CC CC--OO
2  cCC_-  _-CCCCCCCCCCCCCCCCCCCCCCc  _- cC  c-_Oo
1 ------------------------------------------------
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | Q | CLK | D | RESET_B |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X |   |   |   |   |
| NMOS2 |   | X | X |   |   |   |   |
| NMOS3 |   | X |   |   |   |   |   |
| NMOS4 |   | X | X | X |   |   |   |
| NMOS5 |   | X |   |   |   |   |   |
| PMOS1 | X | X |   |   |   |   |   |
| PMOS2 | X | X |   |   |   |   |   |
| PMOS3 | X | X |   | X |   |   |   |
| Poly1 | X | X |   |   |   |   | X |
| Poly2 |   | X |   |   |   | X |   |
| Poly3 |   |   |   |   | X |   |   |
| Poly4 |   | X |   |   |   |   |   |
| Poly5 |   | X | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 | O |   | O |   |   |
| NMOS2 | O | O |   |   |   |
| NMOS3 |   |   |   | O | O |
| NMOS4 |   |   |   |   | O |
| NMOS5 | O |   |   |   |   |
| PMOS1 | O | O |   |   |   |
| PMOS2 | O |   | O | O | O |
| PMOS3 |   |   |   |   | O |

