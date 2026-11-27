# Design Documentation for sg13g2_mux4_1

## Substrate
```
  0123456789012345678901234567890123456
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSNNNNNNNNNNNNNNNSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456
4 ppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNpNppppppppNNNNNNNNpppppp
1 NppppppppppppppppppppppppppppNppppppp
0 NppppppppppppppppppppppppppppNppppppp
9 NppppppppppppppppppppppppppppNppppppp
8 NpppppppppppppppppppppppNNNNNNppppppp
7 NNNNppppppppppppNNNNNNNNNNNNNNNNNNNNN
6 SSNNNNNNNNNNNNNNNSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSnnnnnSSnnnnnn
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnSSnnnnnn
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnSSnnnnnn
2 SSSSSSSSSSSSSSSSSSSSSSnnnSSSSSSSSSnnn
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456
4
3    GGGGGGGGGGGGGG
2    GGGGGGGGGGGGGG   GG   G G    G GG
1    G G  G G G G G   GG   G G    G GG
0    G G  G G G G G   GG   G G    G GG
9    G G  G G G G G   GG   G G    G GG
8    G G  G G G G GGG GG   G G    G GG
7    G G  G G G G GGGGGGGG G GGGG GGGG
6   GGGGGGGGGGGGGGGGGGGGGG G GGG  GGGG
5   GG GGGGGGGG G GGGGGG   G G    GGGG
4   G  GG GG  G G G GGG    G G    GGGG
3   G  GG GG  G G G GGG    G G    GGGG
2   G  GG GG  G G G GGG    GGGGGGGGGGG
1                          GGGGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3 +++++++++++++++++++++++++++++++++++++
2    ++        &CCCCCCCC&+c cCCCCCC+&
1  CC++   CC   +CC CCCCC++CCC     C++OO
0  Cc+&   CcCCCCCCCcCcCCCCcCcCcCCcC+&Oo
9  CC++   CCCCCCCCCCCCCC  CCCCCCCCCCCOO
8  Cc+&   CcC I I  cCcCC  cCcCc CcCCCOO
7  C I I  CC  I I  CCCCCIICCCCCCC I COO
6  C i iCcC cCi i cCCcCCIiCCCCCcC i cOO
5  C    CCC CC    CCCCCCCCCCCCCCCCC- OO
4  cCCCCCCc CCCCCCCCCCCcCcCCcCcCCcC_-oO
3  CC-- C C C  -  CCCC--CCCCCC CCCC--OO
2  c -_ CCCCC  _   cCC--CcCCCCCC   --oO
1 -------------------------------------
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A1 | X | A0 | A2 | A3 | S0 | S1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |
| NMOS2 |   |   | X |   |   |   |   |   |   |
| NMOS3 |   | X | X | X |   |   |   |   |   |
| PMOS1 | X |   | X |   |   |   |   |   |   |
| PMOS2 | X |   | X | X |   |   |   |   |   |
| PMOS3 | X |   |   |   |   |   |   |   |   |
| Poly1 | X | X | X | X |   |   |   |   | X |
| Poly2 | X |   | X |   | X | X | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 | N |   |
| NMOS2 | O | O |
| NMOS3 | O |   |
| PMOS1 | O | O |
| PMOS2 | O |   |
| PMOS3 |   | S |

