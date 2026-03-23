# Design Documentation for sg13g2_dfrbpq_1

## Substrate
```
  012345678901234567890123456789012345678901234567
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678901234567
4 pppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 pppppppppppppppppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppppppppppppppppN
0 pppppppppppppppppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppppppppppppppppN
8 pppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789012345678901234567
4
3
2   G                    G G
1   G     G              G G
0   G                    G G
9   G     G G            G G
8   G                    G G
7 G G     G G            G G
6 GGGG G GGGG G G G G G GGGGG G G G G G G G G G
5 G G     G G            G G
4 G G                    G G
3 G G       G            G G
2 G G                    G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789012345678901234567
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +         +                           +    +
2 &+CcCcCccC&+cCcCc cCcCcCcCcCcCcCcCcCcC +&Cc & o
1  +CCCCCCCCC+CCCCCCCCCCCCCCCCCCCCCCCCCC + CC + O
0 &+CcCcCccCcCcCcCcC  cCcCcCcCcCc        +&Cc & o
9  +CCCCCCCCCCCCCCC CCCCCCCCCCCCCCCC   CC+ CC + O
8 & CcCcCccCcCcCcCc cCcCcCcCcCcCcCcC  cCc &Cc & o
7  ICCCCC IICC  CCC  CCCC     CCCCCCCCCCCCCCC   O
6  iCcCcCiiiiCcCcCcCcCcCc iIcCcCcCcCcCcCcCcCcCcCO
5  ICCCCCCCCCCCCCCCCCCC C   CCCCCCCCCCCCCCCCC CCO
4  ICcCcCccCcCcCcCcCcCcCcCcCcCcCcCcCc   cCcCc_-Oo
3 CCCC- CC- CCCCCCCCCCCC   CCCCCCCCCC-  CC CC -OO
2 CcCc-_  -_cCcCcCcCcCcCcCcCcCcCcCcCc_  cC Cc_- o
1     -   -                          -        -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | D | RESET_B | CLK | Q | VDD | VSS |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   | X |
| NMOS2 |   |   | X | X |   | X |
| PMOS1 |   |   | X | X | X |   |
| PMOS2 |   |   |   |   | X |   |
| Poly1 | X |   | X |   |   |   |
| Poly10 |   |   | X |   |   |   |
| Poly11 |   |   | X |   |   |   |
| Poly12 |   |   | X |   |   |   |
| Poly13 |   |   | X |   |   |   |
| Poly14 |   |   | X |   |   |   |
| Poly15 |   |   | X |   |   |   |
| Poly16 |   |   | X |   |   |   |
| Poly17 |   |   | X |   |   |   |
| Poly18 |   |   | X |   |   |   |
| Poly19 |   |   | X |   |   |   |
| Poly2 |   |   | X |   |   |   |
| Poly4 |   | X | X |   |   |   |
| Poly5 |   |   | X |   |   |   |
| Poly6 |   |   | X |   |   |   |
| Poly7 |   |   | X |   |   |   |
| Poly8 |   |   | X |   |   |   |
| Poly9 |   |   | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 | Poly19 | Poly20 | Poly21 | Poly22 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | N |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | O | O |   | S |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
