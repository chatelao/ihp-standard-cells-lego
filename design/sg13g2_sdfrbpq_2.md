# Design Documentation for sg13g2_sdfrbpq_2

## Substrate
```
  0123456789012345678901234567890123456789012345678901234567890123
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppNpNNNpNNNNNpppppNNNNNNNNNNNpppppNNNNNNNNNNNpNNNpNNN
1 NppppppppppppNNNNNNNNNNNpppppNNNNNNNNNNNpppppNNNNNNNNNNNNNNNNNNN
0 NppppppppppppNNNNNNNNNNNpppppNNNNNNNNNNNpppppNNNNNNNNNNNpNpNpNNN
9 NppppppppppppNNNNNNNNNNNpppppNNNNNNNNNNNpppppNNNNNNNNNNNNNNNNNNN
8 NppppppppppppNNNNNNNNNNNpppppNNNNNNNNNNNpppppNNNNNNNNNNNNNpNpNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnSSSSSSSSSSSnnnnnSSSSSSSSSSSnnnnnSSSSSSSSSSSSSSSnSSS
3 SnnnnnnnnnnnnSSSSSSSSSSSnnnnnSSSSSSSSSSSnnnnnSSSSSSSSSSSSSSSSSSS
2 SnnnnnnnnnnnnnSSSSSSSnSSnnnnnSSSSSSSSSSSnnnnnSSSSSSSSnSSSSSnSnSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901234567890123
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
  0123456789012345678901234567890123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +        +     +         +                          +   +
2     + CCCCCCC+&   &+ CcCCCCC&+ CcCC cCcCCCCCCCcCcCcCcCcC&   &
1     + C     C+ CC  + C     C + C  C                     + OO+
0  CCCCCC CC  C+cCc  +cCcCC CCCCcCc c   cCCCCCCCcCC       & oO&
9  C     CCC  C+ CC  +CCC   C     C C   C       C CC    C   OO+
8  C   CCC    C+ Cc   cCc CCCCCCcCc c cCc CCCCCCc cCc cCcCcCoO&
7  C   C  I I C   C    CC C II C  C C  C  CIII  C C C C    C O
6  cII cIii I cCcCcCcC Cc c IIcCc c cCcC CcIIIcCc cCc c  CcC OO
5  C   CI   I    CC    CCCCCCCCCCCCCCC C  CIIIC  CCCCCCCCC C  O
4  C _ CIIIII CCcCc    Cc C   C   c cC  c CCCCC cCcCCC     C- o -
3  C - CCCCCCCC-  C  CCC-   - C CCCCCC        C      C -  CC- O -
2    _         _      c_-   - CCcCcCcCcCcCCCCCCCcCcCc c_  c -_ _-
1    -         -        -   -                          -    -   -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
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
| NMOS8 |   |   |   | X |
| NMOS9 |   | X |   |   |
| PMOS10 |   |   | X |   |
| PMOS11 |   |   | X |   |
| PMOS12 |   |   | X |   |
| PMOS13 |   |   | X |   |
| PMOS2 |   |   | X |   |
| PMOS4 |   | X |   |   |
| PMOS5 |   |   | X |   |
| PMOS6 |   |   | X |   |
| PMOS7 |   | X |   |   |
| PMOS8 |   |   | X |   |
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
| NMOS9 |   |   |   |   |
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
