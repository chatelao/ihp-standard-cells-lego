# Design Documentation for sg13g2_dfrbpq_2

## Substrate
```
  01234567890123456789012345678901234567890123456789
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789
4 pppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 pppppppppppppppppppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppppppppppppppppppN
0 pppppppppppppppppppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppppppppppppppppppN
8 pppppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789
4
3
2   G                    G G
1   G     G              G G
0   G                    G G
9   G     G G            G G
8   G                    G G
7 G G     G G            G G
6 GGGG G  GGG G G G G G GGGGG G G G G G G G G G
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
  01234567890123456789012345678901234567890123456789
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +         +                           +    +   +
2 &+CcCcCccC&+cCcCcCcCcCcCcCcCcCcCcCcCcC&+    & o &
1  +CCCCCCCCC+CCCCCCCCCCCCCCCCCCCCCCCCCC +CC  + O +
0 &+CcCcCccCcCcCcCcC  cCcCcCcCcCc       &+cC  & o &
9  +CCCCCCCCCCCCCCC CCCCCCCCCCCCCCC   CC  CC  + O +
8 & CcCcCccCcCcCcCc cCcCcCcCcCcCcCcCcCcCcCcC  & o &
7   CCCCC IICC  CCC  CCCC II  CCCCCCC    CCCCCC O
6  iCcCcC iiiCcCcCcCcCcCc iIcCcCcCcCc cCcCcCcCc OOO
5   CCCCCCCCCCCCCCCCCCC C IICCCCCCCCCCCCCC  CC  O
4   CcCcCccCcCcCcCcCcCc cCcCcCcCcCcCc    C-_cC-_o -
3 CCCC- CC- CCCCCCCC    CCCCCCCCCCCCC-  CC- CC- O -
2 CcCc-_  -_cCcCcCcCcCcCcCcCcCcCcCcCc_  cC-_cC-_o_-
1     -   -                          -    -   -   -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
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
