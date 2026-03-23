# Design Documentation for sg13g2_einvn_8

## Substrate
```
  012345678901234567890123456789012345678
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678
4 ppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NpppppppppppppppppppppppppppppppppppppN
1 NpppppppppppppppppppppppppppppppppppppN
0 NpppppppppppppppppppppppppppppppppppppN
9 NpppppppppppppppppppppppppppppppppppppN
8 NpppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789012345678
4
3
2 G
1 G                         G G
0 G
9 G                         G G
8 G
7 G G                       G G
6 GGGG G GG G G G G G G G   GGG G G G G
5 G G                       G G
4 G
3 G                         G G
2 G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789012345678
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3  +     +   +   +  +
2  +&cCcC+&C&+cC&+cC&  CcCcCcCcCcCcCcCcC
1  + CCCC+ C +CC +CC+  CCCCCCCCCCCCCCCCC
0  +&cCcC+&C&+cC&+cC&  CcOoCoOcCoOcCoOcC
9  + CCCC+ C +CC +CCCCCCCO   OCC O   OCC
8  +&cCcCc&C&CcC&CcCcCcCcOoOoOoOoOoOoOcC
7    CCCCCCCCCCCCCCC     OOO
6  i cCcCccCcCcCcCcCcCcCcOOO iiIiIiIiIi
5    CCCCC  C  CC  CC  CCOOOOOOOOOOOOOCC
4  _ cCcCc-_c_-Cc_-Cc_ CcOo oOo oOo oOcC
3  - CCCCC- C -CC -CC- CCCCCCCCC  CC  CC
2  _ cCcCc-_ _-  _-Cc_ CcCcCcCcCcCcCcCcC
1  -      -   -   -  -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | TE_B | VSS | Z | VDD |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |
| NMOS2 |   |   | X | X |   |
| PMOS1 |   |   | X | X | X |
| PMOS2 |   |   |   |   | X |
| Poly1 |   | X | X |   |   |
| Poly10 |   |   | X |   |   |
| Poly11 |   |   | X |   |   |
| Poly12 |   |   | X |   |   |
| Poly13 |   |   | X |   |   |
| Poly14 | X |   |   |   |   |
| Poly15 | X |   |   |   |   |
| Poly16 | X |   |   |   |   |
| Poly17 | X |   |   |   |   |
| Poly4 | X |   |   |   |   |
| Poly5 |   |   | X |   |   |
| Poly6 |   |   | X |   |   |
| Poly7 |   |   | X |   |   |
| Poly8 |   |   | X |   |   |
| Poly9 |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 | Poly13 | Poly14 | Poly15 | Poly16 | Poly17 | Poly18 | Poly19 | Poly20 | Poly21 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 | NW | O | O | N |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | SW |   |   | S |   |   |   |   |   |   |   |   |   |   |   |   |   | O | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
