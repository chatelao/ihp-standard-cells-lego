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
0 NppppppppppppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppppppppppppN
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
2 &+  &+  &+  &+  &   &  +&  +&  +& &+  &+  &+
1  + O++OO++OO++O + O +OO++OO++OO+ C + C++CC++
0  + o&+Oo&+oO&+o & o &Oo+&Oo+&Oo+ Cc+cC&+cC&+
9  + OOOOO++OOOOOOOOOOOOOOOOOOOOOCCCCCCCCCCC++
8  + oOoOo&+oOoOoOoOoOoOoOoOoOoOoCcCcCcCcCcC&+
7    O  OOOOOO  O   O  OOCCCCCCCCC      IIIII
6    o  OooOoO  o   o  OoCcCcCcCcC      iiiIi
5    O  OO  OO  O   O  OO        C
4  c o cOo coO co   o  OoOoOoOoOoCcCcCcCcCcC c
3    O  OO  OO  O   O  OO  OO  OO  C   C  CC
2  c o cOo coO co  coc Ooc Ooc Ooc C c C ccC c
1
0  c c c c c c c c c c c c c c c c c c c c c c
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | VSS10 | VSS11 | VSS12 | VSS13 | VSS14 | VSS15 | VSS16 | VSS17 | VSS18 | VSS19 | VSS2 | VSS20 | VSS21 | VSS22 | VSS23 | VSS24 | VSS25 | VSS26 | VSS27 | VSS28 | VSS29 | VSS3 | VSS30 | VSS31 | VSS32 | VSS33 | VSS34 | VSS35 | VSS36 | VSS37 | VSS38 | VSS39 | VSS4 | VSS5 | VSS6 | VSS7 | VSS8 | VSS9 | A | X |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   | X | X | X | X | X | X |   |   |
| NMOS2 |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X | X | X | X | X | X |   | X | X | X | X | X | X | X | X | X | X |   |   |   |   |   |   |   | X |
| PMOS1 | X | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 | X | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| Poly2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| Poly3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| Poly4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| Poly5 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| Poly6 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| Poly7 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| Poly8 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |
| NMOS2 | O |   |   |   |   |   |   |   |
| PMOS1 | O |   |   |   |   |   |   |   |
| PMOS2 |   |   |   |   |   |   |   |   |
