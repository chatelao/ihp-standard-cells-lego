# Design Documentation for sg13g2_sdfbbp_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901
4 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3
2                                         ppp
1  ppppppppp ppp ppppp               ppppppppppppp    ppp ppppp
0  ppppppppp ppp ppppp ppppppppppppppppp    pppppp  ppppp ppppp
9                ppppp ppppppppppppppppp    pppppp  ppppp ppppp
8                ppppp       pppppppp               ppppp   ppp
7
6
5              nnnnnn       nnn
4  nnnnnnnnnnn nnnnnn nnnnnnnnnnnnnn nnnn   nnnnnnn nnnnn nnnnn
3  nnnnnnnnnnn nnnnnn nnnnn n nnnnnn nnnnnnnnnnnnnn   nnn nnnnn
2                nn         n nn   n
1                nn
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
4
3
2   G G G G                              G   G G       G   G G
1   G G G G                  G  G        G   G G       G   G G
0   G G G G                  G  G        G   G G     G G   G G
9   G G G GG                 G  G       GGGG G G     G G   G G
8   G G G  GG                G  G       G  G G G     G G  GG G
7   G G GG G           G     G  G     G G  G G G     G G     G
6   G G G  GGG  GG GGG GGG G GG G G G   G  G G G GG  G G   GGG
5   G G GG  G   G        G   G         G GGG G G     G G     G
4   G G GG  G   G      G G   G         G G G G G     G G   G G
3   G G GG  G   G      G G   G         G G G G G     G G   G G
2     G     G   G    GGG G             G G G G G       G   G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3    +       +              +      +      +++    +    +     +
2  c & CCCcCc+c c c c       + IIII +IIIIII&+& c  +c   & c   &
1  C + C   C + C C  C       + I  I +I    I    C  +    + I C + I
0  c   C c    cCcCc c c c   & ICcIc+I cC ICCCCc         i c & i
9        CC  C   C  CC      + IC IIII CC ICC  CCC       I C   I
8   IcI   C cC CcCC cC CC CCC ICcCCCC c  Ic  Ic C  Cc   i C   i
7   I I IIC  C C     C        I     C C      I  C  C      C   I
6   Ic  IiC  C CiI CcCcC  cC  c c c c C CCCCc cCC cCcIcC  cC  I
5   I  CCCCCCC C I   C CC  C CCCC     C CC CCCCCC  C      C   I
4  c   c  _ CCcC    c c c  CCCCCcCCCc-C cCc _ c c cCc _ i c _ i
3  -      - C         C C            -C  C  - C   C   - I C - I
2  -      - CCCCC _         _ cCCCcC -CCCC  _ cCCCc   - c   _ c
1  -      -       -         -        -      -         -     -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | Input1 | Input2 | Input4 | Input7 | Input9 | Internal1 | Internal13 | Internal14 | Internal15 | Internal17 | Internal2 | Internal3 | Internal4 | Internal5 | Internal6 | Internal7 | Internal8 | Internal9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |
| NMOS2 |   |   | X |   |   |   |   |   |   |   |   |   |   | X |   | X | X |   | X |   |   |
| NMOS3 |   |   | X |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   | X |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |
| NMOS5 |   |   | X | X |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |
| NMOS6 |   |   | X |   | X |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| PMOS1 |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |   |   |   | X |
| PMOS3 |   |   |   |   |   |   |   | X |   |   |   |   |   |   | X |   |   |   |   |   |   |
| PMOS4 | X |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| PMOS5 |   |   |   |   |   |   |   |   | X | X |   |   |   |   |   |   |   |   |   |   |   |
| PMOS6 |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS7 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly2 |   |   |   |   |   |   |   |   | X |   | X |   |   |   |   |   |   |   |   |   |   |
| Poly3 |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly8 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly9 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly10 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly11 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly12 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly13 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly14 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly15 |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly16 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly17 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly18 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly19 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |
| Poly20 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| Poly21 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| Poly22 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |
| Poly23 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly24 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 | Poly19 | Poly20 | Poly21 | Poly22 | Poly23 | Poly24 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   | N |   |   |   |   |   |   |   |
| NMOS2 |   |   |   | O | O |   |   |   |   |   |   |   |   |   | O |   |   |   |   |   |   |   |   |   |
| NMOS3 | O | O |   |   |   |   |   |   |   |   |   |   | O | O |   |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   |   |   |   | O | O | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS5 |   |   |   |   |   |   |   |   |   | O |   |   |   |   |   | O |   |   |   |   |   |   |   |   |
| NMOS6 |   |   |   |   |   |   |   |   |   |   | O | O |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS2 |   |   |   |   |   |   | O | O | O |   |   |   |   |   | O |   |   |   | O |   |   |   |   |   |
| PMOS3 |   |   |   |   |   |   |   |   |   | O |   |   |   |   |   | O |   |   |   |   |   |   |   |   |
| PMOS4 |   |   |   |   |   |   |   |   |   |   |   | O |   |   |   |   |   |   |   |   |   |   |   | O |
| PMOS5 | O | O |   |   |   |   |   |   |   |   |   |   | O | O |   |   |   |   |   |   |   |   |   |   |
| PMOS6 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS7 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
