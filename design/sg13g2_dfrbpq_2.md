# Design Documentation for sg13g2_dfrbpq_2

## Substrate
```
  01234567890123456789012345678901234567890123456789
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNSSSSSSSSSSSSNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNSSSSSSSSSSSSNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789
4 pppppppppppppppppppppppppppppppppppppppppppppppppp
3                        p          pp   p
2  pppp                  p          pp   p
1      pp    p        pppppp   pp   pp   ppp  ppppp
0      pp ppppppppp   pppppp   pp   pp   ppp  ppppp
9  pppppp             pppppp   ppppppppppppp  ppppp
8                     pppppp   ppppppppppppp  ppppp
7
6             nnnnnn
5      nn            nnnnnnn  nnnnn
4      nn            nnnnnnn  nnnnn       nnn nnnnn
3  nnnnnn nnnnn      nnnnnnn    nnnnnnnnnnnnn nnnnn
2                      n          n
1                      n
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901234567890123456789
4
3
2          G        G     G            G       G G
1          G  G  G        G                    G G
0          G  G  G        G       G            G G
9          G  G  GGGGG    G       G            G G
8          G  G      G    G  G    G            G G
7       G  G GG           G       G G          G G
6  G                  GG  GG     G  G G GGGG GGGGG
5                     G   G         G G        G G
4                     G   G         G G        G G
3                     G   G                    G G
2               GGGGGGG   G                    G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +         +                           +    +   +
2  & CCCCCCCc+      c                 cCc+c   & c &
1  + C       +    C                      + C  + I +
0  + CCCCcc     c c   cCCCCCCCCCC       c+cC  & i &
9  + CC   C     C     C         CC     C   C  + I +
8  c cC CCCCCCCCC   cCc CCCCcCc CCc CCcCCCcC  c i c
7    CC C II C  C    C  C II    C   C    C C    I
6  i CCc  IIc cCc cC C Cc iI CC cC  c   cC CCCc III
5    CC        C   C C  C II       CCCCC C  C   I
4    C  Cc  C c    C  c C   c c c        C_ c _ i _
3  CCC-   - C CCCCCC          CCCCCC -  CC- C - I -
2  c  -c  _ CCCCCCCCCCCCCCCCCCCCCCc c-c c _ c _ c _
1     -   -                          -    -   -   -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Input2 | Input3 | Internal1 | Internal13 | Internal2 | Internal3 | Internal6 | Internal8 | Internal9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   | X |   |   |   |   |   |
| NMOS2 |   | X |   |   |   | X |   |   | X |   |   |   |
| NMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS5 |   | X | X |   |   |   |   |   |   |   |   |   |
| NMOS6 |   |   |   |   |   | X |   | X |   |   |   |   |
| PMOS1 | X |   |   |   |   |   |   |   | X | X |   |   |
| PMOS2 | X |   | X |   |   |   |   |   |   |   |   |   |
| PMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS4 |   |   |   |   |   |   |   | X |   |   | X |   |
| PMOS5 | X |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly2 |   |   |   | X |   |   |   |   |   |   |   |   |
| Poly3 |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly6 |   |   |   |   | X |   |   |   |   |   |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly8 |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly9 |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly10 |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly11 |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly12 |   |   |   |   |   |   |   |   |   | X |   |   |
| Poly13 |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly14 |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly15 |   |   |   |   |   |   |   |   |   |   |   | X |
| Poly16 |   |   |   |   |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   | N | N |   | N |   |   |   |   |   |   |   |   |   |
| NMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS5 |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS6 |   |   |   |   |   |   |   |   |   |   | N |   |   |   |   |   |
| PMOS1 |   | O |   | S |   |   |   |   |   |   |   | O | W |   |   |   |
| PMOS2 |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS4 |   |   |   |   |   |   |   |   |   | O | O |   | O |   |   |   |
| PMOS5 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
