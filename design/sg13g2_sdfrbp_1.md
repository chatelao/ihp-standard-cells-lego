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
2 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901234567
4
3
2   G      G G             G G             G G
1   G    G G G             G G             G G
0   G    G G G             G G             G G
9   G G  G G G             G G             G G
8   G G    G G             G G             G G
7   G G  G G G             G G             G G
6  GGGGG GGGGGG G G G G G GGGGG G G G G G GGGGG G G G G   G     G
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
  01234567890123456789012345678901234567890123456789012345678901234567
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3     +        +     +         +                          +   +   +
2     &cCccCcCc+&Cc &+cCcCcCcC&+cCcCcCcCcCcCcCcCcCcCcCcCcC&   &   & o
1  CC +CC CC  C+ CC  +CCCCCCCC +CCCCCCCCCCCCCCCCCCCCCCCCCC+ O + CC+ O
0  cCc&cC cC  c+&Cc &+cCcCc cCcCcCcCc  CcCcCcCcCcCc       & o & cC& o
9  CCCCCCCCC  C+ CC  +CCCCCCCCCCCCCCC CCCCCCCCCCCCCC    CC  O + CC+ O
8  cC CcCcc   c+&Cc & cCcCcCcCcCcCcCc cCcCcCcCcCcCcCcCcCcCcCo & cC& o
7  C  CC  I I CCCCC   CCCCC IICC  CCC CCCCCIII  CCCCCCC   CCO   CC  O
6  cIiCcIii i cCcCcCcCcCcCc iIcCcCcCcCcCcCcIiIcCcCcCcCc  CcCO   cC OO
5  C  CCI   I   CCCCCCCCCCCCCCCCCCCCCCCC CCIIICCCCCCCCCCCCCCOOO CC  O
4  cC_CcIIIIICcCcCc   cCcCcCcCcCcCcCcCcC CcCcCcCcCcCcCc   cCoOo cC- o
3  CC-CCCCCCCCC-  C CCCC- CC-CCCCCCCCC   CCCCCCCCCCCCCC-  CCO - CC- O
2    _CcCccCcCc_  c cCc_-   -_cCcCcCcCcCcCcCcCcCcCcCcCc_  cCo -_cC-_o
1    -         -        -   -                          -      -   -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | CLK | RESET_B | SCD | SCE | Q | Q_N | VDD | VSS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   | X |
| NMOS2 |   |   |   | X | X | X |   | X |
| PMOS1 |   |   |   | X | X | X | X |   |
| PMOS2 |   |   |   |   |   |   | X |   |
| Poly1 |   |   |   | X |   |   |   |   |
| Poly10 |   |   |   | X |   |   |   |   |
| Poly11 |   |   |   | X |   |   |   |   |
| Poly12 |   |   |   | X |   |   |   |   |
| Poly13 |   |   |   | X |   |   |   |   |
| Poly14 |   |   |   | X |   |   |   |   |
| Poly15 |   |   |   | X |   |   |   |   |
| Poly16 |   |   |   | X |   |   |   |   |
| Poly17 |   |   |   | X |   |   |   |   |
| Poly18 |   |   |   | X |   |   |   |   |
| Poly19 |   |   |   | X |   |   |   |   |
| Poly2 |   |   | X | X |   |   |   |   |
| Poly20 |   |   |   | X |   |   |   |   |
| Poly3 |   | X |   | X |   |   |   |   |
| Poly4 | X |   |   | X |   |   |   |   |
| Poly5 |   |   |   | X |   |   |   |   |
| Poly6 |   |   |   | X |   |   |   |   |
| Poly7 |   |   |   | X |   |   |   |   |
| Poly8 |   |   |   | X |   |   |   |   |
| Poly9 |   |   |   | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 | Poly19 | Poly20 | Poly21 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | O | O | O | O |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
