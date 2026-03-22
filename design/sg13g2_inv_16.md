# Design Documentation for sg13g2_inv_16

## Substrate
```
  0123456789012345678901234567890123
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123
4
3
2                               G G
1                               G G
0                               G G
9                               G G
8                               G G
7                               G G
6    G   G  G   G   G   G   G   GGG
5                               G G
4                               G G
3                               G G
2                               G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +   +   +   +  +   +   +   +   +
2  +& &+  &+  &+  &   &   &   &   &
1  + O + O + O +O + O + O + O + O +
0  + o + o + O +o & o & o & o & o &
9  + O   O   O  O   O   O   O   O +
8    oOoOooOoOoOoOoOoOoOoOoOoOoOo
7    O   O   O  O   O   O   O
6    o   o  oO  o   o   o   o   iIi
5    O   O   O  O   O   O   O
4  _ o _ o _ O _o - o - o - oOoOo_
3  - O - O - O -O - O - O - O - O-
2  _   _   _   _  -_  -_ _-  _-  _
1  -   -   -   -  -   -   -   -  -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | Y | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS2 |   | X |   | X |
| PMOS1 |   |   | X |   |
| PMOS2 |   | X | X |   |
| Poly1 |   | X |   |   |
| Poly2 |   | X |   |   |
| Poly3 |   | X |   |   |
| Poly4 |   | X |   |   |
| Poly5 |   | X |   |   |
| Poly6 |   | X |   |   |
| Poly7 |   | X |   |   |
| Poly8 | X | X | X |   |
