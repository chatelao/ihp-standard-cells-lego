# Design Documentation for sg13g2_dfrbp_1

## Substrate
```
  0123456789012345678901234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
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
3 NNNNNNNNNNNNNNNNNNNNNNNpNNNNNNNNNNNpNNNNNNNNNNNNNNNN
2 NppppNNNNNNNNNNNNNNNNNNpNNNNNNNNNNNpNNNNNNNNNNNNNNNN
1 NNNNNppNNNNpNNNNNNNNppppppNNNppNNNNpNNNNpppNNpppppNN
0 NNNNNppNpppppppppNNNppppppNNNppNNNNpNNNNpppNNpppppNN
9 NppppppNNNNNNNNNNNNNppppppNNNppppppppppppppNNpppppNN
8 NNNNNNNNNNNNNNNNNNNNppppppNNNppppppppppppppNNpppppNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSnnSSSSSSSSSSSSSSnnnnnSSnnnnnSSSSSSSSSSSSSSSSSSS
4 SSSSSnnSSSSSSSSSSSSSSnnnnnSSnnnnnSSSSSSSnnnSSnnnnnSS
3 SnnnnnnSnnnnnSSSSSSSSnnnnnSSSSnnnnnnnnnnnnnSSnnnnnSS
2 SSSSSSSSSSSSSSSSSSSSSSSnSSSSSSSSnSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSnSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901
4
3
2  G   G   G  G G G G G G G         G  GG G   G G G
1  G   G   G  G G G G G G G         G   G G   G G G
0  G   G   G  G G G G G G G         G   G G   G G G
9  G   G   G  G G GGG G G G         G   G G   G G G
8  G   G   G  G G G G G G G  G      G   G G   G G G
7  G   GG  G GG G G G G G G         G   G G   G G G
6  G   G      G G G G GGG G      G  G   GGGGGGGGG G
5  G   G      G G G G G G G         G   G G   G G G
4  G   G      G G G G G G G         G   G G   G G G
3  G   G      G G G G G G G         G   G G   G G G
2  G   G      G GGGGGGGGG G         G   G G   G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +         +                            +      +
2  + cCcCccC +cCcCc cCcCcCcCcCcCcCcCcCcC  +      +
1  + C     C +C   C                       + O  C + O
0  + cCcC cCcCc c c   cCcCcCcCcCc         + o  C +oO
9  + CC   C     C C  CCC       CCCC    C    O  C + O
8    cCcCccCcCcCc c cCcCcCcCcCcCc c cCcCcCc o  C + O
7  I CC C II C  C C  C  C      CC C C     C O  C   O
6  i cCi  iIcCcCc cCcC Ci iIcCcCcCc     c c o cCcCcOo
5  I CCCCCCCCCCCCCCC C  C   C  CCCCCCCCCC C OO C   O
4  i c  Cc  c   c  C CcCcCcCc c c       cCc oO C -oO
3  CCC- C - CCCCCCCC        C CCCCCCC-  CC- O  C - O
2  c  -   - cCcCcCcCcCcCcCcCcCcCcCc c-  c -      -
1     -   -                          -    -      -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | CLK | D | RESET_B | Internal1 | Internal2 | Internal3 | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   | X |   |   |   |   |
| NMOS2 |   |   |   |   |   | X |   |   |   | X |
| NMOS5 |   |   |   |   |   |   |   |   | X |   |
| NMOS6 |   |   |   |   |   | X |   |   |   |   |
| PMOS1 | X |   |   |   |   | X |   |   |   | X |
| PMOS2 |   |   |   |   |   |   |   |   | X |   |
| PMOS3 |   |   |   |   |   | X |   |   |   |   |
| PMOS4 |   |   |   |   |   | X |   |   |   |   |
| PMOS5 |   |   |   |   |   | X |   |   |   |   |
| Poly1 |   |   |   | X |   | X |   |   |   |   |
| Poly2 |   |   |   |   | X | X |   |   |   |   |
| Poly3 |   |   |   |   |   | X |   |   |   |   |
| Poly4 |   |   | X |   |   | X |   | X |   |   |
| Poly5 |   |   | X |   |   | X |   | X |   |   |
| Poly6 |   |   |   |   |   | X |   | X |   |   |
| Poly7 |   |   |   |   |   | X | X |   |   | X |
| Poly8 |   |   |   |   |   |   | X |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | O | O |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   | O | O |   | N |   |   |
| NMOS3 | O | O |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   | O |   |   |   |   |   |   |   |   |
| NMOS5 |   |   |   |   |   |   | O | O |   |   |   |
| NMOS6 |   |   | O | O |   |   |   |   |   |   |   |
| PMOS1 |   |   |   | O | O | O | O |   |   |   |   |
| PMOS2 |   |   |   |   |   |   | O | O |   |   |   |
| PMOS3 | O | O |   |   |   |   |   |   |   |   |   |
| PMOS4 |   |   | O | O |   |   |   |   |   | O |   |
| PMOS5 | O | E |   |   |   |   |   |   |   |   |   |
