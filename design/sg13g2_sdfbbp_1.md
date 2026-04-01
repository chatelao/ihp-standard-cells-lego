# Design Documentation for sg13g2_sdfbbp_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901
4 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNpppNNNNNNNNNNNNNNNNNNN
1 NpppppppppNpppNpppppNNNNNNNNNNNNNNNpppppppppppppNNNNpppNpppppN
0 NpppppppppNpppNpppppNpppppppppppppppppNNNNppppppNNpppppNpppppN
9 NNNNNNNNNNNNNNNpppppNpppppppppppppppppNNNNppppppNNpppppNpppppN
8 NNNNNNNNNNNNNNNpppppNNNNNNNppppppppNNNNNNNNNNNNNNNpppppNNNpppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSnnnnnnSSSSSSSnnnSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnSnnnnnnSnnnnnnnnnnnnnnSnnnnSSSnnnnnnnSnnnnnSnnnnnS
3 SnnnnnnnnnnnSnnnnnnSnnnnnSnSnnnnnnSnnnnnnnnnnnnnnSSSnnnSnnnnnS
2 SSSSSSSSSSSSSSSnnSSSSSSSSSnSnnSSSnSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSnnSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
4
3
2   GGGGGGG G G G   G G G G G G G G G G GGG  G G  G    G  GG G
1   GGGGGGG G G G   G G G G GGG G G G G GGG  G G  G    G  GG G
0   GGGGGGG G G G   G G G G GGG G G G G GGG  G G  G  G G  GG G
9   GGGGGGGGG G G   G G G G GGG G G G G GGGG G G  G  G G  GG G
8   GGGGGGGGG G G   G G G G GGG G G G G G GG G G  G  G G  GG G
7   GGGGGGGGG G G   G GGG G GGG G G G G G GG G G  G  G G  G  G
6   GGGGGGGGGGG GG GGGGGGGGGGGG G G G G G GG G G GG  G G  GGGG
5   GGGGGGG G G G   G G GGG GGG G G G GGGGGG G G  G  G G  G  G
4   GGGGGGG G G G   G GGGGG GGG G G G GGGGGG G G  G  G G  GG G
3   GGGGGGG G G G   G GGGGG GGG G G G GGGGGG G G  G  G G  GG G
2    GGG GG G G G   GGGGGGG G G G G G GGGGGG G G  G    G  GG G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3    +       +     +        +      +      +++    +    +     +
2    + cCccC +     +        + iIiI +iIiIiI+++    +    +     +
1  C + C   C + C C +C       + I  I +I    I    C  +    + OOC + O
0  cCcCc c    cCcC +c cCcC  + iCiI +i cCiIcCcCcCcCcCcCc oOc + o
9        CC  CCC C  CC C  C + IC IIII CCCICC  CCC     C OOC   O
8   I Ii  c cC CcCcC C Cc cCc iCcCiCc c cIi  I  c  Cc c oOc   o
7   I I IiC  C C   CCCCCC C C I    CC C CIIIII  C  C  C  OCC  O
6   Ii iIic  CcCiI CcCcCc iCc i c cCc c cCcCi cCc iCiIcC OcC  o
5   I  CCCCCCC CII  CCCCC CCCCCCC  C  C CC CCCCCC  C     OC   O
4      c  - cC&C    c c c cC_CcCcCcC -c cCc - c c cCc - oOc - o
3  -      - C   CCCCCCC CCC          -C  C  - C   C   - OOC - O
2  -      - cCcCc -         - cCcCcC -cCcC  - cCcCc   -     -
1  -      -       -         -        -      -         -     -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | VSS2 | CLK | D | Input1 | Input2 | SCD | SCE | SET_B | Internal1 | Internal2 | Internal3 | Internal4 | Internal5 | Internal6 | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |
| NMOS2 |   |   |   | X |   |   |   |   |   |   |   | X | X |   |   |   |   |   |   |
| NMOS3 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |
| NMOS4 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| NMOS5 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   | X |
| NMOS6 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |
| PMOS1 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |
| PMOS2 |   |   |   |   |   |   |   |   |   |   | X | X |   | X |   | X |   |   |   |
| PMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   | X |
| PMOS4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |
| PMOS5 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   | X |   |   |
| PMOS6 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |
| PMOS7 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   | X |   |   |   | X |   |   | X | X |   | X |   |   |   |   | X |   |   |
| Poly2 |   |   |   |   | X |   |   |   |   |   |   | X |   |   |   |   |   |   |   |
| Poly3 |   |   |   | X |   |   | X |   |   |   | X | X | X |   |   |   |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   |   |   | X | X | X |   |   | X |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   |   |   | X | X | X |   |   |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   |   |   | X | X |   |   |   |   |   |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |   |   |   |
| Poly8 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly9 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly10 |   |   |   |   |   |   |   | X |   |   |   |   |   | X |   |   |   |   |   |
| Poly11 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly12 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly13 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | W | O | O |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   | O | O | O | E |   |   |   |   |   |   |   |
| NMOS3 | O |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   |   |   |   | W | O | O | O | O |   |   |   |
| NMOS5 |   |   |   |   |   |   |   |   |   |   | O |   | O |
| NMOS6 |   |   |   |   |   |   |   |   |   |   |   | O |   |
| PMOS1 |   | W | O |   |   |   |   |   |   |   |   |   |   |
| PMOS2 |   |   | O | O | O | O | O | O | O | E |   |   |   |
| PMOS3 |   |   |   |   |   |   |   |   |   |   | O |   | O |
| PMOS4 |   |   |   |   |   |   |   |   |   |   |   | O |   |
| PMOS5 | O |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS6 | O | E |   |   |   |   |   |   |   |   |   |   |   |
| PMOS7 |   |   |   |   |   |   |   |   |   |   |   |   |   |
