# Design Documentation for sg13g2_sdfrbp_2

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNSSSSSSSSSSNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSNNNNNNNNNSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4 ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNppNNNNNNNNNNppNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNppppNpppppppNNNppNNNNNNNNppppppNNpppNNNppNNNNNNNNNNNNNNNNN
1 NppppppppppppppppNpppppppNpppppppppNNNppppppNNpppNNNppNNpppppppNpppppNN
0 NppppppppppppppppNNNNNpppppppppppppNNNppppppNNpppNNNppNNpppppppppppppNN
9 NppppppppppppppppNpppppppNpppppppppNNNppppppNNpppppppppppppppppppppppNN
8 NppppppppppppppppNpppppppNNNNNNNNNNNNNppppppNNpppppppppppppppppppppppNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNSSSSSnSSSSNNNNNNNNNNNNNNNNNNNNppppppNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSnnnSSSSSnnnnnnSSSSSSSSSSSSSSSSSSSNNNNNNNNNSSSSSSS
5 SnnnnnnnnnnnnnnnnSSSSSnnnnSSSSnnnnnnnnnnnnnnSnnnnnnSSSSSSSnnnnnSSSSSSSS
4 SnnnnnnnnnnnnnnnnSnnnnnnnnSSSSSSSSSSnnnnnnnnSnnnnnnSSSSSSSnnnnnnnSnnnnn
3 SnnnnnnnnnnnnnnnnSnnnnnnnnnnnnnSSSSSnnnnnnnnSSSnnnnnnnnnnSnnnnnnnSnnnnn
2 SSSnnnnnnnnnnnnnnSnnnnnSSSSSSSSSSSSSSSnnSSSSSSSSnnnSSSSSSSnnnnnnnSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnnSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4
3                            GGGGGGGGGG
2      G G  G G G        G   GGGGGGGGGG  G  G    G      GG GGG G   G G
1   G GG GGGG G G        G   G  GG G  G  G  G    G     GGG GGG G   G G
0   G GG GGGG G G    GGGGG   G  GG G     G  G    G  GG GGGGGGG G   G G
9   G GG GGGG G G    GGGGG   G  GG GGGGG G  G  G G  GG GGGGGGG G   G G
8   G GG GGGG G G    GGGGG   G  GG G  GG G  G GGGG  GG GGGGGGG G   G G
7   GGGG GGGG GGGG   GGGGGG GGGGGG G    GG  GG GGG GGGGGGGGGGG G   G G
6   GGGGGGGGG GGGG  GGGG GG  GGG G G    GGG GG  G GGGGG GGGGGGGGGGGGGGGG
5   G GGG GGG G G    GGG G   GGG G G    G   G   G G  GG GG   G G G  GGGG
4   G GGG GG  G G    GGG G   GGG G G    G   G   G G  GG GG   G G G  GGGG
3   G GGG GG  G G    GGG G   GGG G      G   G   G G   G GG   G G G  GGGG
2   G GGG GG  G G    GGG G   GGG GGGGGGGG   G     G   G GG   G G G  GGGG
1                      GGGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
2    ++CCCCCCCC++CC +&CCCCCCCC&+ CCCCCcCCCCCCCCCCCCCCCCCcC++  ++  &+o &
1  C ++C      C++CC ++CCCCC CC++CCCCC CCCCCCCCCCCCCCCCCCC ++OO++CC++OO+
0  cCC&C  cC  C&+Cc ++CCCCc cCCCCCcCc  CcCCCCCCCCCC       &+oO&+cC&+oO&
9  CCCCCCCCC  C++CC ++CCC   CCCCC CCC CCCCCCCCCCCCCC    CC+ OO++CC++OO+
8  c  CCCC    C&+Cc  &cCCCCCCCCCCCCCC cCcCCCCcCccCCcCCCCcCCCoO&+cC&+oO&
7  C  CC  I IICC CC   CCCCC IICC  CCC CC CCIII  CCC CCC    COO+ CCCCOO
6  CiICCi i iICcCcCCCcCCC c IiCccCcCCcCCCcCIIiCCCCCcC c  cCCOOOO CCcOOO
5  C  CCI   II  CCC   CCCCCCCCCCCCCCCCCC CCIIIC  CCCCCCCCCCC OOO CC  OOOO
4  c _CCIIIIIICCCCc   CCCCcCCCC  CCC C c CCCCcCcCcCCC      C OoO Cc-_OoOO
3  CC-CCCCCCCCC-- C CCCC- C -CCCCCCCCC    CCCCCCCCCCCCC-- CC- O--CC--OO--
2    _ CCcCCCC _- c  cC _   _CCcCCCCCCCCCCCCCCCCCCCcCc _- cC_ o-_ c-_ o_-
1 -----------------------------------------------------------------------
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Internal1 | SCE | Q | Q_N | CLK | D | RESET_B | SCD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   | X |   |   |   |   |   |   |
| NMOS2 |   | X |   | X |   |   |   |   |   |   |
| NMOS3 |   | X |   | X |   |   |   |   |   |   |
| NMOS4 |   |   |   | X |   |   |   |   |   |   |
| NMOS5 |   | X | X |   |   | X |   |   |   |   |
| NMOS6 |   | X |   |   | X |   |   |   |   |   |
| PMOS1 | X |   | X | X | X | X |   |   |   |   |
| PMOS2 | X |   |   | X |   |   |   |   |   |   |
| PMOS3 | X |   |   | X |   |   |   |   |   |   |
| Poly1 | X |   |   | X |   |   |   |   | X |   |
| Poly2 | X |   |   | X |   |   |   | X |   | X |
| Poly3 |   |   |   | X |   |   |   |   |   |   |
| Poly4 |   |   |   |   |   |   | X |   |   |   |
| Poly5 | X | X | X | X | X | X |   |   |   |   |
| Poly6 |   |   |   | X |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | O |   |   | O |   |   |
| NMOS2 |   | O | O |   |   |   |
| NMOS3 | O |   |   |   |   |   |
| NMOS4 |   |   |   |   | O | O |
| NMOS5 |   |   |   |   | O |   |
| NMOS6 |   |   |   |   | O |   |
| PMOS1 | O |   |   | O | O | O |
| PMOS2 |   | O | O |   |   |   |
| PMOS3 | O |   |   |   |   |   |

