# Design Documentation for sg13g2_sdfrbp_2

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4 ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
1 NpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
0 NpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
9 NpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
8 NpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 Snnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4
3
2   G      G G             G G             G G
1   G    G G G             G G             G G
0   G    G G G             G G             G G
9   G G  G G G             G G             G G
8   G G    G G             G G             G G
7   G G  G G G             G G             G G
6  GGGGG GGGGGG G G G G G GGGGG G G G G G GGGGG G G G G   G     G G
5   G G  G G G             G G             G G
4   G    G G G             G G             G G
3   G    G G G             G G             G G
2   G      G G             G               G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3     +        +     +         +                          +   +   +   +
2     &cCccCcCc+&Cc &+cCcCcCcC&+cCcCcCcCcCcCcCcCcCcCcCcCcC&   &   & o &
1  CC +CC CC  C+ CC  +CCCCCCCC +CCCCCCCCCCCCCCCCCCCCCCCCCC+ O + CC+ OO+
0  cCc&cC cC  c+&Cc &+cCcCc cCcCcCcCc  CcCcCcCcCcCc       & o & cC& oO&
9  CCCCCCCCC  C+ CC  +CCCCCCCCCCCCCCC CCCCCCCCCCCCCC    CC  O + CC+ OO+
8  cC CcCcc   c+&Cc & cCcCcCcCcCcCcCc cCcCcCcCcCcCcCcCcCcCcCo & cC& oO&
7  C  CC  I I CCCCC   CCCCC IICC  CCC CCCCCIII  CCCCCCC   CCO   CCCC O
6  cIiCcIii i cCcCcCcCcCcCc iIcCcCcCcCcCcCcIiIcCcCcCcCc  CcCOOO cCcC OO
5  C  CCI   I   CCC   CCCCCCCCCCCCCCCCCC CCIIICCCCCCCCCCCCCC  O  CC   OO
4  cC_CcIIIIICcCcCc   cCcCcCcCcCcCcCcCcC CcCcCcCcCcCcCc   cC  o  Cc_- oOo
3  CC-CCCCCCCCC-  C CCCC- CC-CCCCCCCCC   CCCCCCCCCCCCCC-  CC- O -CC - O-
2    _CcCccCcCc_  c cCc_-   -_cCcCcCcCcCcCcCcCcCcCcCcCc_  cC-_o_-Cc_- o_
1    -         -        -   -                          -    -   -   -  -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | CLK | RESET_B | SCD | SCE | D | Q | Q_N | VDD | VSS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   | X |
| NMOS2 |   |   |   |   | X | X | X |   | X |
| PMOS1 |   |   |   |   | X | X | X | X |   |
| PMOS2 |   |   |   |   |   |   |   | X |   |
| Poly1 |   |   |   | X | X |   |   |   |   |
| Poly10 |   |   |   |   | X |   |   |   |   |
| Poly11 |   |   |   |   | X |   |   |   |   |
| Poly12 |   |   |   |   | X |   |   |   |   |
| Poly13 |   |   |   |   | X |   |   |   |   |
| Poly14 |   |   |   |   | X |   |   |   |   |
| Poly15 |   |   |   |   | X |   |   |   |   |
| Poly16 |   |   |   |   | X |   |   |   |   |
| Poly17 |   |   |   |   | X |   |   |   |   |
| Poly18 |   |   |   |   | X |   |   |   |   |
| Poly19 |   |   |   |   | X |   |   |   |   |
| Poly2 |   |   | X |   | X |   |   |   |   |
| Poly20 |   |   |   |   | X |   |   |   |   |
| Poly21 |   |   |   |   | X |   |   |   |   |
| Poly3 |   | X |   |   | X |   |   |   |   |
| Poly4 | X |   |   |   | X |   |   |   |   |
| Poly5 |   |   |   |   | X |   |   |   |   |
| Poly6 |   |   |   |   | X |   |   |   |   |
| Poly7 |   |   |   |   | X |   |   |   |   |
| Poly8 |   |   |   |   | X |   |   |   |   |
| Poly9 |   |   |   |   | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 | Poly19 | Poly20 | Poly21 | Poly22 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | O | O | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
