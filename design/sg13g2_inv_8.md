# Design Documentation for sg13g2_inv_8

## Substrate
```
  012345678901234567
4 NNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567
4 pppppppppppppppppp
3 NNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNN
1 NppppppppppppppppN
0 NppppppppppppppppN
9 NppppppppppppppppN
8 NppppppppppppppppN
7 SSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnS
2 SSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567
4
3
2        G
1        G
0        G
9      G GG
8      G GG
7      G GG
6    G G GG
5      G GG
4      G GG
3        G
2        G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567
4 ++++++++++++++++++
3  +   +  +   +   +
2 &+  &+  + & + & +
1  + O +O + O + O +
0  +oO +o + o + o +
9  + OOOOOOOO + O +
8           o   o
7           O   O
6    iIiIii oOoOo
5           O   O
4  -oOoOoOoOo - o -
3  - O -O - O - O -
2 _-  _-  - _ - _ -
1  -   -  -   -   -
0 ------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | Y |
| --- | --- | --- |
| NMOS2 |   | X |
| PMOS1 |   | X |
| Poly1 | X | X |
| Poly2 | X |   |
| Poly3 | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | O |   |
| PMOS1 | O | O |   |
| PMOS2 |   |   |   |
