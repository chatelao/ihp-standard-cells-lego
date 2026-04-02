# Design Documentation for sg13g2_dfrbp_2

## Substrate
```
  01234567890123456789012345678901234567890123456789012
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNSSSSSSSSSSSSNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNSSSSSSSSSSSSNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012
4 ppppppppppppppppppppppppppppppppppppppppppppppppppppp
3                        p          pp
2  pppp                  p          pp
1      pp    p        pppppp   pp   pp   pppp   ppppp
0      pp ppppppppp   pppppp   pp   pp   pppppp ppppp
9  pppppp             pppppp   pppppppppppppppp ppppp
8                     pppppp   pppppppppppppppp ppppp
7
6             nnnnnn
5      nn            nnnnnnn  nnnnn
4      nn            nnnnnnn  nnnnn       nnnnnnn nnnnn
3  nnnnnn nnnnn      nnnnnnn    nnnnnnnnnnnnnnnnn nnnnn
2                      n          n
1                      n
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012
4
3
2          G        G     G            G
1          G  G  G        G
0          G  G  G        G       G
9          G  G  GGGGG    G       G
8          G  G      G    G  G    G
7       G  G GG           G       G G
6  G                  GG  GG     G  G G GGGGGGGG GGGG
5                     G   G         G G      G G   G
4                     G   G         G G      G G   G
3                     G   G                  G G   G
2               GGGGGGG   G                  G G   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3  +         +                           +  +       +
2  & CCCCCCCc+      c                 cC +  +   c c &
1  + C       +    C                      + I+     I +
0  + CCCCcc     c c   cCCCCCCCCCC       c+cI& cCc i &
9  + CC   C     C     C         CC     C   I+ CC  I +
8  c cC CCCCCCCCC   cCc CCCCcCc CCc CCcCCCcI& cCc i &
7    CC C II C  C    C  C II    C   C    C I   C
6  i CCc  IIc cCc cC C Cc iI CC cC  c   cC II  CCCcII
5    CC        C   C C  C II       CCCCC C  I   C   III
4    C  Cc  C c    C  c C   c c c        C  i   c _ iII
3  CCC-   - C CCCCCC          CCCCCC -  CC- I - C - I -
2  c  -c  _ CCCCCCCCCCCCCCCCCCCCCCc c-c c _ c _ c _ c _
1     -   -                          -    -   -   -   -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VDD3 | VSS | Input1 | Input2 | Input3 | Input4 | Input6 | Internal1 | Internal10 | Internal13 | Internal2 | Internal3 | Internal4 | Internal7 | Internal9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |   |   |   |   |   |   |   | X |   |   |   |   |   |
| NMOS2 |   |   |   |   | X |   |   |   |   | X |   |   |   |   | X |   |   |
| NMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS5 |   |   |   | X |   | X |   |   |   |   |   |   |   |   |   |   |   |
| NMOS6 |   |   |   |   |   |   |   |   |   | X |   |   | X |   |   |   |   |
| PMOS1 | X |   |   |   | X |   |   |   |   |   |   |   |   | X | X | X |   |
| PMOS2 | X | X | X |   |   |   |   |   | X |   |   |   |   |   |   |   |   |
| PMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS4 |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   | X |
| PMOS5 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly2 |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |
| Poly3 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
| Poly5 |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly7 |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |
| Poly8 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly9 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly10 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly11 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly12 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| Poly13 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly14 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly15 |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |
| Poly16 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   | O |   | N | N |   | N |   |   |   |   |   |   |   |   |
| NMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS5 |   |   |   | O |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS6 |   |   |   |   |   |   |   |   |   |   | N |   |   |   |   |   |
| PMOS1 |   | O |   |   | S |   |   |   |   |   |   | O | W |   |   |   |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS4 |   |   |   |   |   |   |   |   |   | O | O |   | O |   |   |   |
| PMOS5 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
