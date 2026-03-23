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
2 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
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
  01234567890123456789012345678901234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +        +     +         +                          + +
2     &cCccCcCc+&Cc &+cCcCcCcC&+cCcCcCcCcCcCcCcCcCcCcCcCcC& &
1  CC +CC CC  C+ CC  +CCCCCCCC +CCCCCCCCCCCCCCCCCCCCCCCCCC+ + O
0  cCc&cC cC  c+&Cc &+cCcCc cCcCcCcCc  CcCcCcCcCcCc       & & o
9  CCCCCCCCC  C+ CC  +CCCCCCCCCCCCCCC CCCCCCCCCCCCCC    CC  + O
8  cC CcCcc   c+&Cc & cCcCcCcCcCcCcCc cCcCcCcCcCcCcCcCcCcCcC& o
7  C  CC  I I CCCCC   CCCCC IICC  CCC CCCCCIII  CCCCCCC   CCC O
6  cIiCcIii i cCcCcCcCcCcCc iIcCcCcCcCcCcCcIiIcCcCcCcCc  CcCc O
5  C  CCI   I   CCCCCCCCCCCCCCCCCCCCCCCC CCIIICCCCCCCCCCCCCC OO
4  cC_CcIIIIICcCcCc   cCcCcCcCcCcCcCcCcC CcCcCcCcCcCcCc   cC Oo
3  CC-CCCCCCCCC-  C CCCC- CC-CCCCCCCCC   CCCCCCCCCCCCCC-  CC- O
2    _CcCccCcCc_  c cCc_-   -_cCcCcCcCcCcCcCcCcCcCcCcCc_  cC-_o
1    -         -        -   -                          -    -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | CLK | RESET_B | SCD | SCE | VDD | Q | VSS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   | X |
| NMOS2 |   |   |   |   | X | X | X |
| PMOS1 |   |   |   |   | X | X |   |
| PMOS2 |   |   |   |   | X |   |   |
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
