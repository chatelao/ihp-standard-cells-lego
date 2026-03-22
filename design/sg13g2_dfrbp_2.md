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
2 ppppppppppppppppppppppppppppppppppppppppppppppppppppN
1 NpppppppppppppppppppppppppppppppppppppppppppppppppppN
0 NpppppppppppppppppppppppppppppppppppppppppppppppppppN
9 NpppppppppppppppppppppppppppppppppppppppppppppppppppN
8 NpppppppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 Snnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
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
2 G G     G G            G G
1 G G     G G            G G
0 G G     G G            G G
9 G G     G G            G G
8 G G     G G            G G
7 G G     G G            G G
6 GGG     GGG            GGG                G       G
5 G G     G G            G G
4 G G     G G            G G
3 G G     G G            G G
2 G G     G G            G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3  +         +                           +  +   +   +
2 &+ cCcCccC&+ CcCC cCcCcCcCcCcCcCcCcCcC&+  &   &   &
1  + C      C+ C  C                      + O+   + OO+
0  + cCcC c cCcCc c   cCcCcCcCcCc        + O& cC& oO&
9  + CC   C     C C   C        CCC     C   O+ CC+ OO+
8    cCcCccCcCcCc c  Cc cCcCcCcCcCcCcCcCcCoO& cC& oO&
7    CC C II C  C C  C  C II   CC  CC    C O   C   O
6  I cC   iIcCcCc cCcCcCc II CcCcCcC  c cC Oo  CcC Oo
5    CCCCCCCCC CCCCC C  C II C  CCCCCCCCCC  O   C   OOO
4    c  Cc  c   c  Cc   cCcCcCcCcCCC     C  o   c - oOo
3  CCC-   - C CCCCCC         C      C-  CC- O - C - O -
2  c  -_  -_cCcCcCcCcCcCcCcCcCcCcCc c_  c -_  -_ _-  _-
1     -   -                          -    -   -   -   -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | CLK | D | Q | Q_N | RESET_B | Int1 | Int2 | Int3 | Int4 | VDD | VSS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   | X |
| NMOS2 |   |   | X | X |   | X |   | X | X |   | X |
| PMOS1 |   |   | X | X |   | X | X |   | X | X |   |
| PMOS2 |   |   |   |   |   |   |   |   |   | X |   |
| Poly1 |   |   |   |   |   |   |   |   |   | X |   |
| Poly2 |   |   |   |   | X | X |   |   |   | X |   |
| Poly3 |   |   |   |   |   |   |   |   |   |   |   |
| Poly4 |   |   |   | X |   |   |   |   |   |   |   |
| Poly5 |   |   | X |   |   |   |   |   |   |   |   |
