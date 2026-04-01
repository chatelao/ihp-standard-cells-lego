# Design Documentation for sg13g2_dfrbp_1

## Substrate
```
  0123456789012345678901234567890123456789012345678901
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNSSSSSSSSSSSNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNSSSSSSSSSSSNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456789012345678901
4 pppppppppppppppppppppppppppppppppppppppppppppppppppp
3                        p           p
2  pppp                  p           p
1      pp    p        pppppp   pp    p    ppp  ppppp
0      pp ppppppppp   pppppp   pp    p    ppp  ppppp
9  pppppp             pppppp   pppppppppppppp  ppppp
8                     pppppp   pppppppppppppp  ppppp
7
6             nnnnnn
5      nn              nnnnn  nnnnn
4      nn              nnnnn  nnnnn       nnn  nnnnn
3  nnnnnn nnnnn        nnnnn    nnnnnnnnnnnnn  nnnnn
2                        n        n
1                        n
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901
4
3
2          G        G     G            G        G G
1          G  G           G                     G G
0          G  G           G             G       G G
9          G  G   GGG     G             G       G G
8          G  G     G     G  G          G       G G
7       G  G GG           G         G   G       G G
6  G                   G  G      G      GGGGGGGGG G
5                         G             G       G G
4                         G                     G G
3                         G                     G G
2               GGGGGGGG  G                     G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +         +                            +      +
2  & CCCCCCCc+CCCCC c                 cC  & c c c+c
1  + C       +C   C                       + I  C + I
0  + CCCCcc   C c c   cCCCCCCCCCC         & i cCc+cI
9  + CC   C     C C    C        CCC    C    I  C + I
8  c cC CCCCCCCCC C cCcCCCCCcCc C c CCCCcCC i cCc+cI
7  I CC C II C  C C  C  C       C   C     C I  C   I
6  i CCc  IIcCcCc CCcC Cc iI CC cC  c   c C I  CCCcI
5  I CC      C C  C  C  C                 C I  C   I
4  I C  Cc  C c      CcCCCCCc c c        CC i cCc-cI
3  CCC-   - C CCCCCC          CCCCCC -  CC- I  C - I
2  c  -c  _ CCCCCCCCCCCCCCCCCCCCCCc c-c c _ c c c-c
1     -   -                          -    -      -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Input2 | Input3 | Input5 | Input6 | Input7 | Internal1 | Internal2 | Internal3 | Internal4 | Internal6 | Internal8 | Internal9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   | X |   |   |   |   |   | X |   |   |   |   |   |   |
| NMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS5 |   | X |   | X |   |   |   |   |   |   |   |   |   |   |   |
| NMOS6 |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| PMOS1 | X |   | X |   |   |   |   |   |   |   | X |   | X |   |   |
| PMOS2 | X |   |   | X |   |   |   |   |   |   |   |   |   |   |   |
| PMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS4 |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |
| PMOS5 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly2 |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |
| Poly3 | X | X |   |   |   |   |   |   |   |   | X |   |   | X |   |
| Poly4 |   |   |   | X |   |   | X | X |   |   |   | X |   |   |   |
| Poly5 |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly8 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly9 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly10 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly11 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly12 |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
| Poly13 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly14 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| Poly15 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | S | O |   |   |   | N |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   | N |   |   |   |   |   |   |   |   |
| NMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS5 |   |   | O | O |   |   |   |   |   |   |   |   |   |   |   |
| NMOS6 |   |   |   |   |   |   |   |   |   | N |   |   |   |   |   |
| PMOS1 |   | O | O |   |   |   |   |   |   |   | S |   |   |   |   |
| PMOS2 |   |   | O | O |   |   |   |   |   |   |   |   |   |   |   |
| PMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS4 |   |   |   |   |   |   |   |   | O | O |   | S |   |   |   |
| PMOS5 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
