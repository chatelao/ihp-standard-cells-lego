# Design Documentation for sg13g2_dfrbp_1

## Substrate
```
  0123456789012345678901234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNSSSSSSSSSSNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456789012345678901
4 pppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNppNNNNNNNNNNNppNNNNNNNNNNNNNNN
2 pppppppNNNNpNNNNNNNNppppppNNNppNNNNppNNNpppNNNNNNNNN
1 NppppppppppppppppNNNpppppppNppppNNNppNNNppppNpppppNN
0 NNNNppppppppppppppNNpppppppNppppNNNppNNNppppNpppppNN
9 pppppppppppppppppNNNpppppppNppppppppppppppppNpppppNN
8 ppppppppNNNNNNNNNNNNpppppppNppppppppppppppppNpppppNN
7 NNNNNNNNNSSSSSSSSSSNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSnnSSSSSnnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSnnnnSSSSnnnnnnSSnnnnnnSnnnnnnSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnSSSSSSSSSSSSnnnnnnSnnnnnnSSSSSSSnnnSSnnnnnSS
3 nnnnnnnnnnnnnSSSSSSSnnnnnnSSSnnnnnnnnnnnnnnSSnnnnnSS
2 SnnnnSSSSSSSSSSSSSSSSSnnSSSSSSnnnSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSnnSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901
4
3          GGGGGGGGGG
2      G   GGGGGGGGGG  GG G    GG     GG   G    G G
1      G   G  GGGG  G  GG G    GG     GG   G    G G
0   GGGG   G  GGGG     GG G    GG G GGG G  G    G G
9   GGGG   G  GGGGGGG  GG G  G GG G GGG G  G    G G
8   GGGG   G  GGGG  G  GG G GGGGG G GGG G  G    G G
7   GGGGG  GGGGGGG     GG G  GGG GG GGG G  G    G G
6 GGGG GG  GGG GGG     GG GG  GGGGG GGGGGGGGGGGGG G
5  GGG GG  GGG GGG     GG G   GGGG  GGGGGGGGGGGGG G
4   GG GG  GGG GG      GG G   GGGG  GGGGG  G    G G
3   GG GG  GGG GG      GG G   GGGG  GGGGG  G    G G
2   GG     GGG GGGGGGGGGG G     GG  GGGGG  G    G G
1     GGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3 ++++++++++++++++++++++++++++++++++++++++++++++++++++
2 +& CCCCCCC &CCCCC cCCCCCCCCCCCCCCCCCCc  &+o  c+& o
1 ++ C    CCC+C   C CCCCCCCCCCCCCCCCCCCC  ++OO C++OOO
0 ++ CCCcCcCCCC cCcC  CcCCCCCCCCC         &+oO c+&OoO
9 ++CCCCC C CCC CCC CCCCCCCCCC  CCCC   CC + OO C++OOO
8  & cCCCCCCCCCCCCC cCCcCCCcCcCcCcCCCCCcCCC oO c+&OoO
7  I CCCC II C  CCC  C CC     CCCCCCCC    C OO C   OO
6  i CC c Ii cCccCCcCC cC iICCCCCcCCc  Cc C OO CCCcOO
5  I CCCCCCCCCCCCCCCCC  C   CCCCCCCCCCCCC C OO C  COO
4  I CCCcCCCCc CCCCCCCCcCCCcCCcCcCC      CC oO c-_OoO
3 CCCC--C --CCCCCCCCC       CCCCCCCCC-- CC--OO C--OOO
2  cCC_-  _-CCCCCCCCCCCCCCCCCCCCCCc  _- cC_-o  c-_ o
1 ----------------------------------------------------
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | Internal1 | Q | Q_N | CLK | D | RESET_B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X |   |   |   |   |   |   |
| NMOS2 |   | X | X |   |   |   |   |   |   |
| NMOS3 |   | X |   |   |   | X |   |   |   |
| NMOS4 |   |   | X | X | X |   |   |   |   |
| NMOS5 |   | X |   |   |   |   |   |   |   |
| PMOS1 | X | X |   |   |   |   |   |   |   |
| PMOS2 | X | X |   |   |   | X |   |   |   |
| PMOS3 | X |   |   | X | X |   |   |   |   |
| Poly1 | X | X |   |   |   |   |   |   | X |
| Poly2 |   | X |   |   |   |   |   | X |   |
| Poly3 |   |   |   |   |   |   | X |   |   |
| Poly4 |   | X |   |   |   |   |   |   |   |
| Poly5 |   | X | X |   |   |   |   |   |   |
| Poly6 |   |   |   | X |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | O |   | O |   |   |   |
| NMOS2 | O | O |   |   |   |   |
| NMOS3 |   |   |   | O | O |   |
| NMOS4 |   |   |   |   | O | O |
| NMOS5 | O |   |   |   |   |   |
| PMOS1 | O | O |   |   |   |   |
| PMOS2 | O |   | O | O | O |   |
| PMOS3 |   |   |   |   | O | O |

