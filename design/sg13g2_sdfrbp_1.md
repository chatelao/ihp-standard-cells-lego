# Design Documentation for sg13g2_sdfrbp_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901234567
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNSSSSSSSSSSNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSNNNNNNNNNNNNSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901234567
4 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNppNNNNNNNNNNppNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNppppNpppppppNNNppNNNNNNNNppppppNNpppNNNppNNNNNNNNNNNNNN
1 NppppppppppppppppNpppppppNpppppppppNNNppppppNNpppNNNppNNpppppppNpppN
0 NppppppppppppppppNNNNNpppppppppppppNNNppppppNNpppNNNppNNpppppppppppN
9 NppppppppppppppppNpppppppNpppppppppNNNppppppNNpppppppppppppppppppppN
8 NppppppppppppppppNpppppppNNNNNNNNNNNNNppppppNNpppppppppppppppppppppN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNSSSSSnSSSSNNNNNNNNNNNNNNNNNNNNppNpppNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSnnnSSSSSnnnnnnSSSSSSSSSSSSSSSSNNNNNNNNNNNNSSSS
5 SnnnnnnnnnnnnnnnnSSSSSnnnnSSSSnnnnnnnnnnnnnnSnnnnnnSSSSSSSnnnSSSSSSS
4 SnnnnnnnnnnnnnnnnSnnnnnnnnSSSSSSSSSSnnnnnnnnSnnnnnnSSSSSSSnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnSnnnnnnnnnnnnnSSSSSnnnnnnnnSSSnnnnnnnnnnSnnnnnnnnnS
2 SSSnnnnnnnnnnnnnnSnnnnnSSSSSSSSSSSSSSSnnSSSSSSSSnnnSSSSSSSnnnnnSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnnSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901234567
4
3                            GGGGGGGGGG
2      G G  G G G        G   GGGGGGGGGG  G  G    G      GG GG  G   G
1   G GG GGGG G G        G   G  GG G  G  G  G    G     GGG GG  G   G
0   G GG GGGG G G    GGGGG   G  GG G     G  G    G  GG GGGGGG  G   G
9   G GG GGGG G G    GGGGG   G  GG GGGGG G  G  G G  GG GGGGGG  G   G
8   G GG GGGG G G    GGGGG   G  GG G  GG G  G GGGG  GG GGGGGG  G   G
7   GGGG GGGG GGGG   GGGGGG GGGGGG G    GG  GG GGG GGGGGGGGGG  G GGG
6   GGGGGGGGG GGGG  GGGG GG  GGG G G    GGG GG  G GGGGG GGGGGGGGGGGG
5   G GGG GGG G G    GGG G   GGG G G    G   G   G G  GG GG   G G   G
4   G GGG GG  G G    GGG G   GGG G G    G   G   G G  GG GG   G G   G
3   G GGG GG  G G    GGG G   GGG G      G   G   G G   G GG   G G   G
2   G GGG GG  G G    GGG G   GGG GGGGGGGG   G     G   G GG   G G   G
1                      GGGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901234567
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
2    ++CCCCCCCC++CC +&CCCCCCCC&+ CCCCCcCCCCCCCCCCCCCCCCCcC++  ++  & o
1  C ++C      C++CC ++CCCCC CC++CCCCC CCCCCCCCCCCCCCCCCCC ++OO++C + O
0  cCC&C  cC  C&+Cc ++CCCCc cCCCCCcCc  CcCCCCCCCCCC       &+oO&+cC& o
9  CCCCCCCCC  C++CC ++CCC   CCCCC CCC CCCCCCCCCCCCCC    CC+ OO++CC+ O
8  c  CCCC    C&+Cc  &cCCCCCCCCCCCCCC cCcCCCCcCccCCcCCCCcCCCoO&+cC& o
7  C  CC  I IICC CC   CCCCC IICC  CCC CC CCIII  CCC CCC    COO+ CC OO
6  CiICCi i iICcCcCCCcCCC c IiCccCcCCcCCCcCIIiCCCCCcC c  cCCOO  Cc OO
5  C  CCI   II  CCCCCCCCCCCCCCCCCCCCCCCC CCIIIC  CCCCCCCCCCCOOOOCC  O
4  c _CCIIIIIICCCCc   CCCCcCCCC  CCC C c CCCCcCcCcCCC      CoOOOcC_ o
3  CC-CCCCCCCCC-- C CCCC- C -CCCCCCCCC    CCCCCCCCCCCCC-- CCOO--CC- O
2    _ CCcCCCC _- c  cC _   _CCcCCCCCCCCCCCCCCCCCCCcCc _- cCo _-c _ o
1 --------------------------------------------------------------------
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Internal1 | SCE | Q | Q_N | CLK | D | RESET_B | SCD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   | X |   |   |   |   |   |   |
| NMOS2 |   | X |   | X |   |   |   |   |   |   |
| NMOS3 |   | X |   | X |   |   |   |   |   |   |
| NMOS4 |   |   |   | X |   |   |   |   |   |   |
| NMOS5 |   | X | X |   | X | X |   |   |   |   |
| PMOS1 | X |   | X | X | X | X |   |   |   |   |
| PMOS2 | X |   |   | X |   |   |   |   |   |   |
| PMOS3 | X |   |   | X |   |   |   |   |   |   |
| Poly1 | X |   |   | X |   |   |   |   | X |   |
| Poly2 | X |   |   | X |   |   |   | X |   | X |
| Poly3 |   |   |   | X |   |   |   |   |   |   |
| Poly4 |   |   |   |   |   |   | X |   |   |   |
| Poly5 | X |   | X | X |   | X |   |   |   |   |
| Poly6 |   |   |   | X |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | O |   |   | O |   |   |
| NMOS2 |   | O | O |   |   |   |
| NMOS3 | O |   |   |   |   |   |
| NMOS4 |   |   |   |   | O | O |
| NMOS5 |   |   |   |   | O |   |
| PMOS1 | O |   |   | O | O | O |
| PMOS2 |   | O | O |   |   |   |
| PMOS3 | O |   |   |   |   |   |

