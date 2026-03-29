# Design Documentation for sg13g2_dfrbp_2

## Substrate
```
  01234567890123456789012345678901234567890123456789012
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012
4 ppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NpppppppppppppppppppppppppppppppppppppppppppppppppppN
1 NpppppppppppppppppppppppppppppppppppppppppppppppppppN
0 NpppppppppppppppppppppppppppppppppppppppppppppppppppN
9 NpppppppppppppppppppppppppppppppppppppppppppppppppppN
8 NpppppppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012
4
3
2 G GG   G GG G G G G   GG GG G G G   G G
1 G GG   G GG G G G G   GG GG G G G   G G
0 G GG   G GG G G G G   GG GG G G G   G G
9 G GG   G GG G G G G   GG GG G G G   G G
8 G GG   G GG G G G G   GG GG G G G   G G
7 G GG   G GG G G G G   GG GG G G G   G G       G
6 GGGG   GGGG G G G G   GGGGG G G G   G G       G
5 G GG   G GG G G G G   GG GG G G G   G G       G
4 G GG   G GG G G G G   GG GG G G G   G G       G
3 G GG   G GG G G G G   GG GG G G G   G G       G
2 G GG   G GG G G G G   GG GG G G G   G G       G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3  +         +                           +  +   +   +
2  & cCcCccC +  c   cCcCcCcCcCcCcCcCcCcC +  &   &   &
1  + C     C + CCCC                      + O+   + OO+
0  & cCcC cCcCcCc c   cCcCcCcCcCc        + O& cC& oO&
9  + CC   C     C C  CCC       CCC     C   O+ CC+ OO+
8    cCcCccCcCcCc c  CcCcCcCcCcCcCc cCcCcCoO& cC& oO&
7    CC C II C  C C  C CCIII   CC C C    C O   C   O
6  i cC   iIcCcCc cCcC CcIiIcCcCcCc   c cC Oo  CcC Oo
5    CCCCCCCCC CCCCC C  CIIIC  CCCCCCCCCCC  O   C   OOO
4    c  Cc  c   c  Cc   c c c c c        C  o   c _ oOo
3  CCC- C - C CCCCCC    CCCCC CCCCCCC-  CC- O - C - O -
2  c  -   _ cCcCcCcCcCcCcCcCcCcCcCc c-  c _   _   _   _
1     -   -                          -    -   -   -   -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | CLK | D | Internal1 | Internal2 | RESET_B | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |
| NMOS2 |   | X |   |   | X |   | X | X | X |
| PMOS1 | X |   |   |   | X | X | X | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   | X |   |   | X |   |   |
| Poly10 |   |   |   |   |   | X | X |   |   |
| Poly11 |   |   |   |   |   | X | X |   |   |
| Poly12 |   |   |   |   |   |   | X |   |   |
| Poly13 |   |   |   |   | X |   |   |   |   |
| Poly2 |   |   |   |   |   |   | X |   |   |
| Poly3 |   |   |   |   |   |   | X |   |   |
| Poly4 |   |   |   |   |   |   | X |   |   |
| Poly5 |   |   |   |   |   |   | X |   |   |
| Poly6 |   |   |   |   |   | X | X |   |   |
| Poly7 |   |   | X |   |   | X | X |   |   |
| Poly8 |   |   |   |   |   | X | X |   |   |
| Poly9 |   |   |   |   |   | X | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | O | O | O | O | O | O | O | O |
| PMOS1 | O | O | O | O | O | O | O | O | O | O | O | O | S |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |
