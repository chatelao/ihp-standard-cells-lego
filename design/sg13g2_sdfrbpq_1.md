# Design Documentation for sg13g2_sdfrbpq_1

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
2 NppppppppppppNpNNNpNNNNNpppppNNNNNNNNNNNpppppNNNNNNNNNNNpNpNNN
1 NppppppppppppNNNNNNNNNNNpppppNNNNNNNNNNNpppppNNNNNNNNNNNNNNNNN
0 NppppppppppppNNNNNNNNNNNpppppNNNNNNNNNNNpppppNNNNNNNNNNNpNpNpN
9 NppppppppppppNNNNNNNNNNNpppppNNNNNNNNNNNpppppNNNNNNNNNNNNNNNNN
8 NppppppppppppNNNNNNNNNNNpppppNNNNNNNNNNNpppppNNNNNNNNNNNNNpNpN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnSSSSSSSSSSSnnnnnSSSSSSSSSSSnnnnnSSSSSSSSSSSSSSSnS
3 SnnnnnnnnnnnnSSSSSSSSSSSnnnnnSSSSSSSSSSSnnnnnSSSSSSSSSSSSSSSSS
2 SnnnnnnnnnnnnnSSSSSSSnSSnnnnnSSSSSSSSSSSnnnnnSSSSSSSSnSSSSSnSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
4
3
2   G    G G G             G G             G G
1   G    G G G             G G             G G
0   G G  G G G             G G             G G
9   G G  G G G             G G             G G
8   G G  G G G             G G             G G
7   G G  G G G             G G             G G
6   GGG  GGGGG             GGG             GGG
5   G G  G G G             G G             G G
4   G G  G G G             G G             G G
3   G G  G G G             G G             G G
2   G G  G G G             G G             G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +        +     +         +                          + +
2     + CCCCCCC+&   &+ CcCCCCC&+ CcCC cCcCCCCCCCcCcCcCcCcC& &
1     + C     C+ CC  + C     C + C  C                     + + O
0  CCCCCC CC  C+cCc  +cCcCC CCCCcCc c   cCCCCCCCcCC       & & o
9  C     CCC  C+ CC  +CCC   C     C C   C       C CC    C   + O
8  C   CCC    C+ Cc   cCc CCCCCCcCc c cCc CCCCCCc cCc cCcCcC& o
7  C   C  I I C   C    CC C II C  C C  C  CIII  C C C C    C  O
6  cII cIii I cCcCcCcC Cc c IIcCc c cCcC CcIIIcCc cCc c  CcCc O
5  C   CI   I    CC    CCCCCCCCCCCCCCC C  CIIIC  CCCCCCCCC C OO
4  C _ CIIIII CCcCc    Cc C   C   c cC  c CCCCC cCcCCC     C Oo
3  C - CCCCCCCC-  C  CCC-   - C CCCCCC        C      C -  CC- O
2    _         _      c_-   - CCcCcCcCcCcCCCCCCCcCcCc c_  c -_
1    -         -        -   -                          -    -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | D | Q | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS2 |   |   |   | X |
| NMOS3 |   |   |   | X |
| NMOS6 |   |   |   | X |
| NMOS7 |   |   |   | X |
| NMOS8 |   | X |   |   |
| PMOS10 |   |   | X |   |
| PMOS11 |   |   | X |   |
| PMOS12 |   |   | X |   |
| PMOS13 |   |   | X |   |
| PMOS2 |   |   | X |   |
| PMOS4 |   |   | X |   |
| PMOS5 |   | X |   |   |
| PMOS6 |   |   | X |   |
| PMOS7 |   |   | X |   |
| PMOS8 |   | X |   |   |
| PMOS9 |   |   | X |   |
| Poly2 | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |
| NMOS2 | O | O |   |   |
| NMOS3 |   |   |   |   |
| NMOS4 |   |   | O |   |
| NMOS5 |   |   |   | O |
| NMOS6 |   |   |   |   |
| NMOS7 |   |   |   |   |
| NMOS8 |   |   |   |   |
| PMOS1 | O | O |   |   |
| PMOS2 |   |   | O |   |
| PMOS3 |   |   |   | O |
| PMOS4 |   |   |   |   |
| PMOS5 |   |   |   |   |
| PMOS6 |   |   |   |   |
| PMOS7 |   |   |   |   |
| PMOS8 |   |   |   |   |
| PMOS9 |   |   |   |   |
| PMOS10 |   |   |   |   |
| PMOS11 |   |   |   |   |
| PMOS12 |   |   |   |   |
| PMOS13 |   |   |   |   |
