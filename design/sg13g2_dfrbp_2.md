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
2 ppppNNNppppppNNNNNNNNNpppppNNNNNNNNNNNpNNNpNNNpNNNpNN
1 ppppNNNpppppNNNNNNNNNNpppppNNNNNNNNNNNNNNNNNNNNNNNNNN
0 ppppNNNpppppNNNNNNNNNNpppppNNNNNNNNNNNNNNNpNNNpNpNpNN
9 ppppNNNpppppNNNNNNNNNNpppppNNNNNNNNNNNNNNNNNNNNNNNNNN
8 ppppNNNpppppNNNNNNNNNNpppppNNNNNNNNNNNNNpNpNNNpNpNpNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 nnnnSSSnnnnnSSSSSSSSSSnnnnnSSSSSSSSSSSSSSSnSSSSSSSnSn
3 nnnnSSSnnnnnSSSSSSSSSSnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSS
2 nnnnSnSnnnnnSSSSSSSSSSnnnnnSSSSSSSSnSSSSSnSSSnSnSSSnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012
4
3
2 G G     G G            G G
1 G G     G G            G G
0 G G     G G            G G
9 G G     G G            G G
8 G G     G G            G G
7 G G     G G            G G
6 GGG     GGG            GGG
5 G G     G G            G G
4 G G     G G            G G
3 G G       G            G G
2 G G       G            G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3  +         +                           +  +   +   +
2  + CCcCCCC +&CcCC cCcCCCCCCCcCcCcCcCcC&+  &   &   &
1  + C      C+ C  C                      + O+   + OO+
0  + CCcC C CCcCc c   cCCCCCCCcCc        + O& cC& oO&
9  + CC   C     C C   C        CCC     C   O+ CC+ OO+
8    CCcCCCCCCcCc c  Cc CCCCCCcCcCcCcCcCcCoO& cC& oO&
7    CC C II C  C C  C  C II   CC  CC    C O   C   O
6  I cC  ciI CcCc cCcCcCc IIcCcCcCcC  c cC OO  CcC OO
5    CCCCCCCCC CCCCC C  C II C  CCCCCCCCCC  O   C   OOO
4    C cC   C c c  Cc c CCCC CcCcCCC     C  o   c - oOo
3  CCC-   - C CCCCCC         C      C-  CC- O - C - O -
2     -_  -_CCcCcCcCcCcCCCCCCCcCcCc c_  c -_  -_ _-  _-
1     -   -                          -    -   -   -   -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | RESET_B | Q | Q_N | VDD | VSS |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   | X |
| NMOS10 |   |   |   |   | X |
| NMOS11 |   |   | X |   |   |
| NMOS12 |   | X |   |   |   |
| NMOS13 |   | X |   |   |   |
| NMOS3 |   |   |   |   | X |
| NMOS4 |   |   |   |   | X |
| NMOS6 |   |   |   |   | X |
| NMOS7 |   |   |   |   | X |
| NMOS8 |   |   |   |   | X |
| NMOS9 |   |   |   |   | X |
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
| PMOS6 |   |   |   | X |   |
| PMOS7 |   | X |   |   |   |
| PMOS8 |   |   |   | X |   |
| PMOS9 |   |   |   | X |   |
| Poly2 | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O |   |   |
| NMOS3 |   |   |   |
| NMOS4 |   | O |   |
| NMOS5 |   |   | O |
| NMOS6 |   |   |   |
| NMOS7 |   |   |   |
| NMOS8 |   |   |   |
| NMOS9 |   |   |   |
| NMOS10 |   |   |   |
| NMOS11 |   |   |   |
| NMOS12 |   |   |   |
| NMOS13 |   |   |   |
| PMOS1 | O |   |   |
| PMOS2 |   | O |   |
| PMOS3 |   |   | O |
| PMOS4 |   |   |   |
| PMOS5 |   |   |   |
| PMOS6 |   |   |   |
| PMOS7 |   |   |   |
| PMOS8 |   |   |   |
| PMOS9 |   |   |   |
| PMOS10 |   |   |   |
| PMOS11 |   |   |   |
| PMOS12 |   |   |   |
| PMOS13 |   |   |   |
| PMOS14 |   |   |   |
| PMOS15 |   |   |   |
| PMOS16 |   |   |   |
| PMOS17 |   |   |   |
