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
0 ppppppppppppppppppppppppppppppppppppppppppppppppppppN
9 NpppppppppppppppppppppppppppppppppppppppppppppppppppN
8 ppppppppppppppppppppppppppppppppppppppppppppppppppppN
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
2   G                    G G
1   G     G              G G
0   G                    G G
9   G     G G            G G
8   G                    G G
7 G G     G G            G G
6 GGGG G  GGG G G G G G GGGGG G G G G G G       G G
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
  01234567890123456789012345678901234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3  +         +                           +  +   +   +
2 &+CcCcCccC&+cCcCcCcCcCcCcCcCcCcCcCcCcC&+  &   & o &
1  +CCCCCCCCC+CCCCCCCCCCCCCCCCCCCCCCCCCC + O+ CC+ OO+
0 &+CcCcCccCcCcCcCcC  cCcCcCcCcCc       &+oO& cC& oO&
9  +CCCCCCCCCCCCCCC CCCCCCCCCCCCCCC   CC   O+ CC+ OO+
8 & CcCcCccCcCcCcCc cCcCcCcCcCcCcCcCcCcCcCoO& cC& oO&
7   CCCCC IICC  CCC  CCCC II  CCCCCCC    C O  CCCCCO
6  iCcCcC iiiCcCcCcCcCcCc iIcCcCcCcCc cCcC OO  CcCcOO
5   CCCCCCCCCCCCCCCCCCC C IICCCCCCCCCCCCCC  O  CC   OOO
4   CcCcCccCcCcCcCcCcCc cCcCcCcCcCcCc    C  o  Cc_- oOo
3 CCCC- CC- CCCCCCCC    CCCCCCCCCCCCC-  CC- O -CC - O -
2 CcCc-_  -_cCcCcCcCcCcCcCcCcCcCcCcCc_  cC-_o -_c_- o_-
1     -   -                          -    -   -   -   -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
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
| Poly2 |   |   | X |   |   |   |   |
| Poly4 |   | X | X |   |   |   |   |
| Poly5 |   |   | X |   |   |   |   |
| Poly6 |   |   | X |   |   |   |   |
| Poly7 |   |   | X |   |   |   |   |
| Poly8 |   |   | X |   |   |   |   |
| Poly9 |   |   | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 | Poly19 | Poly20 | Poly21 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | N |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | O | O |   | S |   |   |   |   |   |   |   |   |   |   |   |   |   |   | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
