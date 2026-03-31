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
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123
4
3
2
1
0
9
8                                 G
7                                 G
6                               G G
5                                 G
4                                 G
3                                 G
2                                 G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123
4 ++++++++++++++++++++++++++++++++++
3  +   +   +   +  +   +   +   +   +
2  +& &+  &+  &+  + & + & + & + & +
1  + O + O + O +O + O + O + O + O +
0  + O + O + O +o + o + o + o + o +
9  + O   O   O  O   O   O   O   O +
8    OoOoOoOoOoOoOoOoOoOoOoOoOoOo
7    OOOOOOOOOOOOOOOOOOOOOOOO   III
6    o   o   O  o   o   o   o   iIi
5    O   O   O  O   O   O   O
4  - O - O - O -o - o - o - oOoOo-
3  - O - O - O -O - O - O - O - O-
2  -_ _-  _-  _-  - _ - _ - _ -  -_
1  -   -   -   -  -   -   -   -  -
0 ----------------------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VSS | A | Y |
| --- | --- | --- | --- |
| NMOS2 |   |   | X |
| PMOS1 |   |   | X |
| Poly1 | X | X |   |
| Poly2 |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| PMOS1 | O |   |
| PMOS2 |   |   |
