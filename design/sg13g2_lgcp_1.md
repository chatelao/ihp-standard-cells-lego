# Design Documentation for sg13g2_lgcp_1

## Substrate
```
  012345678901234567890123456
4 NNNNNNNNNNNNNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456
4 ppppppppppppppppppppppppppp
3 NNNNNNNNNNNppNNNNNNNNNNNNNN
2 NppppppppppppNNNNNNNNNpppNN
1 NpppppppppppppppppppppppppN
0 NpppppppppppppppppppppppppN
9 NppppppppNNpppppppppppppppN
8 NpppppppNNNNpppNppppppppppN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSnnnnnnSSSSSSSSS
5 SnnnnnnnnnnnnnnnnnnnnnSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456
4
3
2   G  GGG GGG           G
1   G  GGG GGGGG  GGGGG  G
0   G  GGG GGGGG  GGGGG  G
9   G  GGGGGGGGG  GGGGG  G
8   G  GGG G GGG  GGGGG  G
7   GGGG GGGGGGG  GGG G GG
6   GG GGGGG GGG  GGGGG GGG
5   G  GGG GGGGG  GGGGG  GG
4   G  GGG GG GG  GGGGG  GG
3   G  GGG GGGGG  GGGGG  GG
2   G  GGG  GG       GG  GG
1            GGGGGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&
3 +++++++++++++++++++++++++++
2  c &+      +&    ++   &+o
1  CC++ CCC   CCCCC++CC ++OO
0  cC   CCc  CCCCCc& cC &+oO
9  CCCCCCCCCCCCCCCCI CC ++OO
8  cCC i Cc  CC cCCIICCC& oO
7  C C I CCCCCCCCCCII CCC OO
6  CCc   cCcCCcCccCIi CCcCOO
5  C CCCCC CCCCCCCC-- CC -OO
4  cCCCCCCc  -_Cc  _- Cc-_oO
3  CC-CCCCC  -- C  -- CC--OO
2  c _-CCCCCCc-    --   -_o
1 ---------------------------
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | Internal1 | GCLK | CLK | GATE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |   |   |
| NMOS2 |   | X | X | X | X |   |   |
| PMOS1 | X | X |   | X | X |   | X |
| Poly1 | X | X | X | X |   | X | X |
| Poly2 |   |   | X | X | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 | N |   |
| NMOS2 | O | O |
| PMOS1 | O | O |

