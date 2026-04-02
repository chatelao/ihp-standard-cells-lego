# Design Documentation for sg13g2_dfrbpq_1

## Substrate
```
  012345678901234567890123456789012345678901234567
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNSSSSSSSSSSSNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNSSSSSSSSSSSNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678901234567
4 pppppppppppppppppppppppppppppppppppppppppppppppp
3                        p           p   p
2  pppp                  p           p   p
1      pp    p        pppppp   pp    p   p  ppppp
0      pp ppppppppp   pppppp   pp    p   p  ppppp
9  pppppp             pppppp   ppppppppppp  ppppp
8                     pppppp   ppppppppppp  ppppp
7
6             nnnnnn
5      nn              nnnnn  nnnnn
4      nn              nnnnn  nnnnn         nnnnn
3  nnnnnn nnnnn        nnnnn    nnnnnnnnnn  nnnnn
2                        n        n
1                        n
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456789012345678901234567
4
3
2          G        G     G            G       G
1          G  G           G                    G
0          G  G           G             G      G
9          G  G   GGG     G             G      G
8          G  G     G     G  G          G      G
7       G  G GG           G         G   G      G
6  G                   G  G      G      GGGGG GG
5                         G             G      G
4                         G                    G
3                         G                    G
2               GGGGGGGG  G                    G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789012345678901234567
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +         +                           +    +
2  & CCCCCCCc+CCCCC c                 cC +c c & c
1  + C       +C   C                      +  C + I
0  + CCCCcc   C c c   cCCCCCCCCCC        +c c & i
9  + CC   C     C C    C        CCC    C +  C + I
8  c cC CCCCCCCCC C cCcCCCCCcCc C c    Cc c c & i
7  I CC C II C  C C  C  C       C   CCCCCC  C   I
6  i CCc  IIcCcCc CCcC Cc iI CC cC  c   c   CCcCI
5  I CC      C C  C  C  C                   C   I
4  I C  Cc  C c      CcCCCCCc c c        C  c _Ii
3  CCC-   - C CCCCCC          CCCCCC -  CC  C -II
2  c  -c  _ CCCCCCCCCCCCCCCCCCCCCCc c-c c   c _ c
1     -   -                          -        -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Input2 | Input4 | Internal1 | Internal2 | Internal4 | Internal6 | Internal8 | Internal9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   | X |   |   |   |   |   |
| NMOS3 |   |   |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   |   |   |   |   |   |   |   |   |   |
| NMOS5 |   | X | X |   |   |   |   | X |   |   |   |
| NMOS6 |   |   |   |   |   |   | X |   |   |   |   |
| PMOS1 | X |   |   |   |   |   |   |   | X | X |   |
| PMOS2 | X |   | X |   |   |   |   | X |   |   |   |
| PMOS3 |   |   |   |   |   |   |   |   |   |   |   |
| PMOS4 |   |   |   |   |   |   | X |   | X |   |   |
| PMOS5 | X |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   |   |   |   |
| Poly2 |   |   |   |   | X |   |   |   |   |   |   |
| Poly3 |   |   |   |   |   |   |   | X |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   |   | X |   |
| Poly5 |   |   |   | X |   |   |   |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   |   |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   |   |   |
| Poly8 |   |   |   |   |   |   |   |   |   |   |   |
| Poly9 |   |   |   |   |   |   |   |   |   |   |   |
| Poly10 |   |   |   |   |   |   |   |   |   |   |   |
| Poly11 |   |   |   |   |   |   |   |   |   |   |   |
| Poly12 |   |   |   |   |   |   |   |   | X |   |   |
| Poly13 |   |   |   |   |   |   |   |   |   |   |   |
| Poly14 |   |   |   |   |   |   |   |   |   |   | X |
| Poly15 |   |   |   |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | S | O |   |   |   | N |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   | N |   |   |   |   |   |   |   |   |
| NMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS5 |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS6 |   |   |   |   |   |   |   |   |   | N |   |   |   |   |   |
| PMOS1 |   | O |   | O |   |   |   |   |   |   | S |   |   |   |   |
| PMOS2 |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS4 |   |   |   |   |   |   |   |   | O | O |   | S |   |   |   |
| PMOS5 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
