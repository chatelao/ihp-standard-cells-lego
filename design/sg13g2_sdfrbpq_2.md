# Design Documentation for sg13g2_sdfrbpq_2

## Substrate
```
  0123456789012345678901234567890123456789012345678901234567890123
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNSSSSSSSSSSSSNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNSSSSSSSSSSSSNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3                                         pp          p
2                   ppppp                 pp          p
1    pppppppppppppp     ppp   pp        pppppp  ppp   p   ppppp
0  pppppppppppppppp     ppp ppppppppp   pppppp  ppp   p   ppppp
9  pppppppppppppppp ppppppp             pppppp  ppppppppppppppp
8  pppppppppppppppp                     pppppp  ppppppppppppppp
7
6                               nnnnnn
5                       nnn            nnnnnnn nnnnn
4  nnnnnnnnnnnnnnnn     nnn            nnnnnnn nnnnn        nnnnn
3  nnnnnnnnnnnnnnnn nnnnnnn nnnnn      nnnnnnn    nn nnnnnn nnnnn
2                                        n         n
1                                        n
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901234567890123
4
3
2                        G   G        G     G           GG
1   G                    G   G   G G        G
0   G                    G   G   G G        G       G
9   G                    G   G   G GGGG     G       G
8   G                    G   G   G G  G     G  G    G
7   GGG                G GG  G G G G        G       GGG
6   GGG G G G  G G   G G G   G     G    GG  GG     G    GG GGGGG
5   G                  G G   G     G    G   G           G    G G
4   G                  G G   G          G   G         G G    G G
3   G                  G G   G          G   G         G G    G G
2                      G     G    GGGGGGG   G         G G    G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +        +     +                                    +   +
2     +CCCCCCCC+    c+ CCCCCCCc       c                 c +   +
1     +C      C+ CC  +       C      C                     + I +
0  c c C  c   C+cCc  +  CCc cC    c c   cCCCCCCCCC        & i &
9  C     CC   C+ CC  +C C   C     C     C       C  C    C   I +
8  c   CC     C+cCc c c C CCCCCCCCC   cCc CCcCcCc cCC CCcCCCi &
7  C      I I C   C     C C II C  C    C   III  C   C C    C
6  CIi  Ici i cCcCCCcC  C c iIc c c cC CcC IiICCC cCC c  CcCcII
5  C    I   I     C     C       C    C C   IIIC     CCCCCC C  I
4  c _  IIIII CCC c       c     c    Cc     c C c c        C_ i _
3  C - CCCCCCC -  C  CC -   -   CCCCCC        C CCCCCC -  CC- I -
2    _   c     -c c c   _   _ CCCCCCCCCCCCCCCCCCCCCCc c-c c _ c _
1    -         -        -   -                          -    -   -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD4 | VSS | Input1 | Input2 | Input3 | Input4 | Input6 | Internal1 | Internal10 | Internal12 | Internal14 | Internal15 | Internal16 | Internal17 | Internal18 | Internal2 | Internal4 | Internal6 | Internal8 | Internal9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS3 |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X |   |   |   |
| NMOS4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| NMOS5 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS6 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS7 |   |   | X | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS8 |   |   |   |   |   |   |   |   | X | X |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | X | X |   |   |   |   |   |   |   |   | X |   |   |   |   |   | X | X |   |   |   |
| PMOS2 | X |   |   |   |   |   |   | X | X |   |   |   |   |   |   |   |   |   | X |   |   |
| PMOS3 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| PMOS4 |   |   |   |   |   |   |   |   |   | X |   | X |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly3 |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly4 |   |   |   |   |   | X |   |   | X |   |   |   |   |   | X |   |   |   |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly6 |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
| Poly8 |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly9 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly10 |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly11 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly12 |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly13 |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly14 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly15 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly16 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly17 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly18 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly19 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly20 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly21 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly22 |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |
| Poly23 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 | Poly19 | Poly20 | Poly21 | Poly22 | Poly23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | N |   |   |   |   |   |   |
| NMOS3 |   |   |   |   |   |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS4 | O |   |   |   |   |   |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS5 |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS6 |   |   |   |   | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS7 |   |   |   |   |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS8 |   |   |   |   |   |   |   |   |   | O |   |   |   |   |   |   |   |   | N |   |   |   |   |
| PMOS1 |   |   |   |   |   |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS2 |   |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | O | W |   |   |
| PMOS3 |   |   |   |   |   |   |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS4 |   | O |   |   |   |   |   |   |   | O |   |   |   |   |   |   |   |   | O |   |   |   |   |
