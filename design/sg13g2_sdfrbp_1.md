# Design Documentation for sg13g2_sdfrbp_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901234567
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901234567
4 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppNpNNNpNNNNNpppppNNNNNNNNNNNpppppNNNNNNNNNNNpNNNpNNNpNNN
1 NppppppppppppNNNNNNNNNNNpppppNNNNNNNNNNNpppppNNNNNNNNNNNNNNNNNNNNNNN
0 NppppppppppppNNNNNNNNNNNpppppNNNNNNNNNNNpppppNNNNNNNNNNNpNpNpNNNpNpN
9 NppppppppppppNNNNNNNNNNNpppppNNNNNNNNNNNpppppNNNNNNNNNNNNNNNNNNNNNNN
8 NppppppppppppNNNNNNNNNNNpppppNNNNNNNNNNNpppppNNNNNNNNNNNNNpNpNNNNNpN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnSSSSSSSSSSSnnnnnSSSSSSSSSSSnnnnnSSSSSSSSSSSSSnSnSSSSSnS
3 SnnnnnnnnnnnnSSSSSSSSSSSnnnnnSSSSSSSSSSSnnnnnSSSSSSSSSSSSSSSSSSSSSSS
2 SnnnnnnnnnnnnnSSSSSSSnSSnnnnnSSSSSSSSSSSnnnnnSSSSSSSSnSSSSSSSnSSSnSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901234567
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
  01234567890123456789012345678901234567890123456789012345678901234567
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +        +     +         +                          +   +   +
2     + CCCCCCC+&   &+ CcCCCCC&+ CcCC cCcCCCCCCCcCcCcCcCcC&   &   &
1     + C     C+ CC  + C     C + C  C                     + O +   + O
0  CCCCCC CC  C+cCc  +cCcCC CCCCcCc c   cCCCCCCCcCC       & o & c & o
9  C     CCC  C+ CC  +CCC   C     C C   C       C CC    C   O + C + O
8  C   CCC    C+ Cc   cCc CCCCCCcCc c cCc CCCCCCc cCc cCcCcCo & c   o
7  C   C  I I C   C    CC C II C  C C  C  CIII  C C C C    CO   C   O
6  cII cIii I cCcCcCcC Cc c IIcCc c cCcC CcIIIcCc cCc c  CcCO   cC OO
5  C   CI   I    CC    CCCCCCCCCCCCCCC C  CIIIC  CCCCCCCCC COOO C   O
4  C _ CIIIII CCcCc    Cc C   C   c cC  c CCCCC cCcCCC     CoOo c - o
3  C - CCCCCCCC-  C  CCC-   - C CCCCCC        C      C -  CCO - C - O
2    _         _      c_-   - CCcCcCcCcCcCCCCCCCcCcCc c_  c   -_  -_
1    -         -        -   -                          -      -   -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | D | Q | Q_N | VDD | VSS |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   | X |
| NMOS10 |   |   | X |   |   |
| NMOS11 |   | X |   |   |   |
| NMOS2 |   |   |   |   | X |
| NMOS3 |   |   |   |   | X |
| NMOS6 |   |   |   |   | X |
| NMOS7 |   |   |   |   | X |
| NMOS8 |   |   |   |   | X |
| NMOS9 |   |   | X |   |   |
| PMOS10 |   |   |   | X |   |
| PMOS11 |   | X |   |   |   |
| PMOS12 |   |   |   | X |   |
| PMOS13 |   |   |   | X |   |
| PMOS14 |   |   |   | X |   |
| PMOS15 |   |   |   | X |   |
| PMOS16 |   |   |   | X |   |
| PMOS17 |   |   |   | X |   |
| PMOS2 |   |   |   | X |   |
| PMOS4 |   |   | X |   |   |
| PMOS5 |   |   |   | X |   |
| PMOS6 |   | X |   |   |   |
| PMOS7 |   |   |   | X |   |
| PMOS8 |   |   | X |   |   |
| PMOS9 |   |   |   | X |   |
| Poly2 | X |   |   |   |   |

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
| NMOS10 |   |   |   |   |
| NMOS11 |   |   |   |   |
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
| PMOS14 |   |   |   |   |
| PMOS15 |   |   |   |   |
| PMOS16 |   |   |   |   |
| PMOS17 |   |   |   |   |
