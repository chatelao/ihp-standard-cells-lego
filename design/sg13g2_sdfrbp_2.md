# Design Documentation for sg13g2_sdfrbp_2

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNSSSSSSSSSSSSNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNSSSSSSSSSSSSNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4 ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3                                         pp          p
2                   ppppp                 pp          p
1    pppppppppppppp     ppp   pp        pppppp  ppp   p   ppppp   ppppp
0  pppppppppppppppp     ppp ppppppppp   pppppp  ppp   p   ppppppp ppppp
9  pppppppppppppppp ppppppp             pppppp  ppppppppppppppppp ppppp
8  pppppppppppppppp                     pppppp  ppppppppppppppppp ppppp
7
6                               nnnnnn
5                       nnn            nnnnnnn nnnnn
4  nnnnnnnnnnnnnnnn     nnn            nnnnnnn nnnnn        nnnnnnn nnnnn
3  nnnnnnnnnnnnnnnn nnnnnnn nnnnn      nnnnnnn    nn nnnnnn nnnnnnn nnnnn
2                                        n         n
1                                        n
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4
3
2                        G   G        G     G           GG         G G
1   G                    G   G   G G        G                  G   G G
0   G                    G   G   G G        G       G          G   G G
9   G                    G   G   G GGGG     G       G          G   G G
8   G                    G   G   G G  G     G  G    G          G   G G
7   GGG                G GG  G G G G        G       GGG        G   G G
6   GGG G G G  G G   G G G   G     G    GG  GG     G    GGGGGGGGGG GGGG
5   G                  G G   G     G    G   G           G    G G G
4   G                  G G   G          G   G         G G    G G G
3   G                  G G   G          G   G         G G    G G G
2                      G     G    GGGGGGG   G         G G    G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3     +        +     +                                    +   +   +   +
2     +CCCCCCCC+    c+ CCCCCCCc       c                 c +   +   & c &
1     +C      C+ CC  +       C      C                     + I +   + I +
0  c c C  c   C+cCc  +  CCc cC    c c   cCCCCCCCCC        & i & cC& i &
9  C     CC   C+ CC  +C C   C     C     C       C  C    C   I + CC+ I +
8  c   CC     C+cCc c c C CCCCCCCCC   cCc CCcCcCc cCC CCcCCCi & cC& i &
7  C      I I C   C     C C II C  C    C   III  C   C C    CI    C
6  CIi  Ici i cCcCCCcC  C c iIc c c cC CcC IiICCC cCC c  CcCIII  CcC II
5  C    I   I     C     C       C    C C   IIIC     CCCCCC C  I   C   II
4  c _  IIIII CCC c       c     c    Cc     c C c c        C  i   c _ iI
3  C - CCCCCCC -  C  CC -   -   CCCCCC        C CCCCCC -  CC- I - C - I-
2    _   c     -c c c   _   _ CCCCCCCCCCCCCCCCCCCCCCc c-c c _ c _ c _ c-c
1    -         -        -   -                          -    -   -   -  -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD4 | VSS | Input1 | Input2 | Input3 | Input4 | Input5 | Input7 | Internal1 | Internal10 | Internal11 | Internal13 | Internal15 | Internal16 | Internal17 | Internal18 | Internal19 | Internal2 | Internal4 | Internal6 | Internal7 | Internal9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS3 |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X |   |   |   |
| NMOS4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| NMOS5 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS6 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS7 |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| NMOS8 |   |   | X |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS9 |   |   |   |   |   |   |   |   |   | X |   | X |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | X | X |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   | X | X |   |   |   |
| PMOS2 | X |   |   | X |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   | X | X |   |
| PMOS3 | X |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS4 | X |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS5 |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly3 |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly4 |   |   |   |   |   |   | X |   |   | X |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |
| Poly6 |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
| Poly7 |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly8 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly9 |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly10 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly11 |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly12 |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly13 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly14 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly15 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly16 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly17 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly18 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly19 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly20 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly21 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly22 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |
| Poly23 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 | Poly19 | Poly20 | Poly21 | Poly22 | Poly23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | N |   |   |   |   |   |   |   |
| NMOS3 |   |   |   |   |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS4 | O |   |   |   |   |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS5 |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS6 |   |   |   |   | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS7 |   |   |   |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS8 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS9 |   |   |   |   |   |   |   |   | O |   |   |   |   |   |   |   |   |   | N |   |   |   |   |
| PMOS1 |   |   |   |   |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS2 |   |   |   | O |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   | O | W |   |   |
| PMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | O |   |   |   |   |   |   |
| PMOS4 |   |   |   |   |   |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS5 |   | O |   |   |   |   |   |   | O |   |   |   |   |   |   |   |   |   | O |   |   |   |   |
