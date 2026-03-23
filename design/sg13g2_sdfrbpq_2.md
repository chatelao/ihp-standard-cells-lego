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
2 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901234567890123
4
3
2   G      G G             G G             G G
1   G    G G G             G G             G G
0   G    G G G             G G             G G
9   G G  G G G             G G             G G
8   G G    G G             G G             G G
7   G G  G G G             G G             G G
6  GGGGG GGGGGG G G G G G GGGGG G G G G G GGGGG G G G G   G G
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
  0123456789012345678901234567890123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +        +     +         +                          +   +
2     &cCccCcCc+&Cc &+cCcCcCcC&+cCcCcCcCcCcCcCcCcCcCcCcCcC&   &
1  CC +CC CC  C+ CC  +CCCCCCCC +CCCCCCCCCCCCCCCCCCCCCCCCCC+ OO+
0  cCc&cC cC  c+&Cc &+cCcCc cCcCcCcCc  CcCcCcCcCcCc       & oO&
9  CCCCCCCCC  C+ CC  +CCCCCCCCCCCCCCC CCCCCCCCCCCCCC    CC  OO+
8  cC CcCcc   c+&Cc & cCcCcCcCcCcCcCc cCcCcCcCcCcCcCcCcCcCcCoO&
7  C  CC  I I CCCCC   CCCCC IICC  CCC CCCCCIII  CCCCCCC   CCCO
6  cIiCcIii i cCcCcCcCcCcCc iIcCcCcCcCcCcCcIiIcCcCcCcCc  CcCcOO
5  C  CCI   I   CCC   CCCCCCCCCCCCCCCCCC CCIIICCCCCCCCCCCCCC  O
4  cC_CcIIIIICcCcCc   cCcCcCcCcCcCcCcCcC CcCcCcCcCcCcCc   cC-_o_-
3  CC-CCCCCCCCC-  C CCCC- CC-CCCCCCCCC   CCCCCCCCCCCCCC-  CC- O -
2    _CcCccCcCc_  c cCc_-   -_cCcCcCcCcCcCcCcCcCcCcCcCc_  cC-_o_-
1    -         -        -   -                          -    -   -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | CLK | RESET_B | SCD | SCE | VSS | Q | VDD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   | X |   |   |
| NMOS2 |   |   |   |   | X | X |   |
| PMOS1 |   |   |   |   | X | X | X |
| PMOS2 |   |   |   |   |   |   | X |
| Poly1 |   |   |   | X | X |   |   |
| Poly10 |   |   |   |   | X |   |   |
| Poly11 |   |   |   |   | X |   |   |
| Poly12 |   |   |   |   | X |   |   |
| Poly13 |   |   |   |   | X |   |   |
| Poly14 |   |   |   |   | X |   |   |
| Poly15 |   |   |   |   | X |   |   |
| Poly16 |   |   |   |   | X |   |   |
| Poly17 |   |   |   |   | X |   |   |
| Poly18 |   |   |   |   | X |   |   |
| Poly19 |   |   |   |   | X |   |   |
| Poly2 |   |   | X |   | X |   |   |
| Poly20 |   |   |   |   | X |   |   |
| Poly3 |   | X |   |   | X |   |   |
| Poly4 | X |   |   |   | X |   |   |
| Poly5 |   |   |   |   | X |   |   |
| Poly6 |   |   |   |   | X |   |   |
| Poly7 |   |   |   |   | X |   |   |
| Poly8 |   |   |   |   | X |   |   |
| Poly9 |   |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 | Poly19 | Poly20 | Poly21 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | O | O | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
