# Design Documentation for sg13g2_sdfrbpq_2

## Substrate
```
  0123456789012345678901234567890123456789012345678901234567890123
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNSSSSSSSSSSNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNppNNNNNNNNNNppNNNNNNNNNN
2 NNNNNNNNNNNNNppppNpppppppNNNppNNNNNNNNppppppNNpppNNNppNNpppppNNN
1 NppppppppppppppppNpppppppNpppppppppNNNppppppNNpppNNNppNNppppppNN
0 NppppppppppppppppNNNNNpppppppppppppNNNppppppNNpppNNNppNNppppppNN
9 NppppppppppppppppNpppppppNpppppppppNNNppppppNNppppppppppppppppNN
8 NppppppppppppppppNpppppppNNNNNNNNNNNNNppppppNNppppppppppppppppNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNSSSSSnSSSSNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSnnnSSSSSnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SnnnnnnnnnnnnnnnnSSSSSnnnnSSSSnnnnnnnnnnnnnnSnnnnnnSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnSnnnnnnnnSSSSSSSSSSnnnnnnnnSnnnnnnSSSSSSSnnnnnS
3 SnnnnnnnnnnnnnnnnSnnnnnnnnnnnnnSSSSSnnnnnnnnSSSnnnnnnnnnnSnnnnnS
2 SSSnnnnnnnnnnnnnnSnnnnnSSSSSSSSSSSSSSSnnSSSSSSSSnnnSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnnSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901234567890123
4
3                            GGGGGGGGGG
2      G G  G G G        G   GGGGGGGGGG  G  G    G      GG GGG
1   G GG GGGG G G        G   G  GG G  G  G  G    G     GGG GGG
0   G GG GGGG G G    GGGGG   G  GG G     G  G    G  GG GGGGGGG
9   G GG GGGG G G    GGGGG   G  GG GGGGG G  G  G G  GG GGGGGGG
8   G GG GGGG G G    GGGGG   G  GG G  GG G  G GGGG  GG GGGGGGG
7   GGGG GGGG GGGG   GGGGGG GGGGGG G    GG  GG GGG GGGGGGGGGGG
6   GGGGGGGGG GGGG  GGGG GG  GGG G G    GGG GG  G GGGGG GGGGGGGG
5   G GGG GGG G G    GGG G   GGG G G    G   G   G G  GG GG   G G
4   G GGG GG  G G    GGG G   GGG G G    G   G   G G  GG GG   G G
3   G GGG GG  G G    GGG G   GGG G      G   G   G G   G GG   G G
2   G GGG GG  G G    GGG G   GGG GGGGGGGG   G     G   G GG   G G
1                      GGGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
2    ++CCCCCCCC++CC +&CCCCCCCC&+ CCCCCcCCCCCCCCCCCCCCCCCcC++  ++
1  C ++C      C++CC ++CCCCC CC++CCCCC CCCCCCCCCCCCCCCCCCC ++OO++
0  cCC&C  cC  C&+Cc ++CCCCc cCCCCCcCc  CcCCCCCCCCCC       &+oO&+
9  CCCCCCCCC  C++CC ++CCC   CCCCC CCC CCCCCCCCCCCCCC    CC+ OO++
8  c  CCCC    C&+Cc  &cCCCCCCCCCCCCCC cCcCCCCcCccCCcCCCCcCCCoO&+
7  C  CC  I IICC CC   CCCCC IICC  CCC CC CCIII  CCC CCC    COO
6  CiICCi i iICcCcCCCcCCC c IiCccCcCCcCCCcCIIiCCCCCcC c  cCcOOOO
5  C  CCI   II  CCC   CCCCCCCCCCCCCCCCCC CCIIIC  CCCCCCCCCCC OOO
4  c _CCIIIIIICCCCc   CCCCcCCCC  CCC C c CCCCcCcCcCCC      C_Oo-_
3  CC-CCCCCCCCC-- C CCCC- C -CCCCCCCCC    CCCCCCCCCCCCC-- CC- O--
2    _ CCcCCCC _- c  cC _   _CCcCCCCCCCCCCCCCCCCCCCcCc _- cC_ o-_
1 ----------------------------------------------------------------
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | SCE | Q | CLK | D | RESET_B | SCD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X |   |   |   |   |
| NMOS2 |   | X | X |   |   |   |   |
| NMOS3 |   | X | X |   |   |   |   |
| NMOS4 |   | X |   |   |   |   |   |
| NMOS5 |   |   | X |   |   |   |   |
| PMOS1 | X | X |   |   |   |   |   |
| PMOS2 | X | X |   |   |   |   |   |
| PMOS3 | X | X | X |   |   |   |   |
| Poly1 | X | X |   |   |   | X |   |
| Poly2 | X | X |   |   | X |   | X |
| Poly3 |   | X |   |   |   |   |   |
| Poly4 |   |   |   | X |   |   |   |
| Poly5 | X | X | X |   |   |   |   |
| Poly6 |   | X |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | O |   |   | O |   |   |
| NMOS2 |   | O | O |   |   |   |
| NMOS3 | O |   |   |   |   |   |
| NMOS4 |   |   |   |   | O | O |
| NMOS5 |   |   |   |   | O |   |
| PMOS1 |   | O | O |   |   |   |
| PMOS2 | O |   |   |   |   |   |
| PMOS3 | O |   |   | O | O | O |

