# Design Documentation for sg13g2_dfrbp_1

## Substrate
```
  0123456789012345678901234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456789012345678901
4 pppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 pppppppppppppppppppppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppppppppppppppppppppN
0 pppppppppppppppppppppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppppppppppppppppppppN
8 pppppppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901
4
3
2   G                    G G
1   G     G              G G
0   G                    G G
9   G     G G            G G
8   G                    G G
7 G G     G G            G G
6 GGGG G GGGG G G G G G GGGGG G G G G G G G   G G G
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
  0123456789012345678901234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +         +                            +      +
2 &+CcCcCccC&+cCcCc cCcCcCcCcCcCcCcCcCcC  & o cC&+o o
1  +CCCCCCCCC+CCCCCCCCCCCCCCCCCCCCCCCCCC  + O CC + O
0 &+CcCcCccCcCcCcCcC  cCcCcCcCcCc         & o cC&+oOo
9  +CCCCCCCCCCCCCCC CCCCCCCCCCCCCCCC   CC   O CC + O
8 & CcCcCccCcCcCcCc cCcCcCcCcCcCcCcCcCcCcCc o cC&+oOo
7  ICCCCC IICC  CCC  CCCC     CCCCCCCC    C O CC   O
6  iCcCcCiiiiCcCcCcCcCcCc iIcCcCcCcCcCcCc c O cCcCcO
5  ICCCCCCCCCCCCCCCCCCC C   CCCCCCCCCCCCC C O CC CCO
4  ICcCcCccCcCcCcCcCcCcCcCcCcCcCcCcCc   cCc o cC _oOo
3 CCCC- CC- CCCCCCCCCCCC   CCCCCCCCCC-  CC- O CC - O
2 CcCc-_  -_cCcCcCcCcCcCcCcCcCcCcCcCc_  cC-_o cC _o o
1     -   -                          -    -      -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | D | RESET_B | CLK | Q | Q_N | VDD | VSS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   | X |
| NMOS2 |   |   | X | X | X |   | X |
| PMOS1 |   |   | X | X | X | X |   |
| PMOS2 |   |   |   |   |   | X |   |
| Poly1 | X |   | X |   |   |   |   |
| Poly10 |   |   | X |   |   |   |   |
| Poly11 |   |   | X |   |   |   |   |
| Poly12 |   |   | X |   |   |   |   |
| Poly13 |   |   | X |   |   |   |   |
| Poly14 |   |   | X |   |   |   |   |
| Poly15 |   |   | X |   |   |   |   |
| Poly16 |   |   | X |   |   |   |   |
| Poly17 |   |   | X |   |   |   |   |
| Poly18 |   |   | X |   |   |   |   |
| Poly19 |   |   | X |   |   |   |   |
| Poly2 |   |   | X |   |   |   |   |
| Poly20 |   |   | X |   |   |   |   |
| Poly4 |   | X | X |   |   |   |   |
| Poly5 |   |   | X |   |   |   |   |
| Poly6 |   |   | X |   |   |   |   |
| Poly7 |   |   | X |   |   |   |   |
| Poly8 |   |   | X |   |   |   |   |
| Poly9 |   |   | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 | Poly19 | Poly20 | Poly21 | Poly22 | Poly23 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | N |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | O | O |   | S |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
