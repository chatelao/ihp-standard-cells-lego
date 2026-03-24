# Design Documentation for sg13g2_buf_16

## Substrate
```
  01234567890123456789012345678901234567890123
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 pppppppppppppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppppppppppppN
0 pppppppppppppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppppppppppppN
8 pppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 Snnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 Snnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123
4
3
2                                       G G
1                                       G G
0                                       G G
9                                       G G
8                                       G G
7                                       G G
6    G   GG G   G   G   G               GGG G
5                                       G G
4                                       G G
3                                       G G
2                                       G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3 ++++++++++++++++++++++++++++++++++++++++++++
2 &+Oo&+Oo&+oO&+oO&+o+&Oo+&Oo+&Oo+&C&+cC&+cC&+
1 ++OO++OO++OO++OO++O++OO++OO++OO++C++CC++CC++
0 &+Oo&+Oo&+oO&+oO&+o+&Oo+&Oo+&Oo+&C&+cC&+cC&+
9 ++OO++OO++OO++OO++O++OO++OO++OO++C++CC++CC++
8 &+OoOoOo&+oOoOoOoOoOoOoOoOoOoOoCcCcCcCcCcC&+
7   OO  OOOOOO  OO OO  OOCCCCCCCCC      IIIII
6   Oo  OooOoO  oO Oo  OoCcCcCcCcC      iIiIi
5   OO  OO  OO  OO OO  OO        C
4 -_Oo-_Oo-_oO-_oO-_o_-OoOoOoOoOoCcCcCcCcCcC-_
3 --OO--OO--OO--OO--O--OO--OO--OO--C--CC--CC--
2 -_Oo-_Oo-_oO-_oO-_o_-Oo_-Oo_-Oo_-C__cC-_cC-_
1 --------------------------------------------
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | VSS2 | X | VDD | VSS |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   | X |
| NMOS2 |   | X | X |   | X |
| PMOS1 |   | X | X | X |   |
| PMOS2 |   |   |   | X |   |
| Poly1 | X | X |   | X |   |
| Poly2 |   |   | X |   |   |
| Poly3 |   |   | X |   |   |
| Poly4 |   |   | X |   |   |
| Poly5 |   |   | X |   |   |
| Poly6 |   |   | X |   |   |
| Poly7 |   |   | X |   |   |
| Poly8 | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |
| NMOS2 | O |   |   |   |   |   |   |   |
| PMOS1 | O |   |   |   |   |   |   |   |
| PMOS2 |   |   |   |   |   |   |   |   |
