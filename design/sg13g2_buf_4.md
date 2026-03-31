# Design Documentation for sg13g2_buf_4

## Substrate
```
  01234567890123
4 NNNNNNNNNNNNNN
3 NNNNNNNNNNNNNN
2 NNNNNNNNNNNNNN
1 NNNNNNNNNNNNNN
0 NNNNNNNNNNNNNN
9 NNNNNNNNNNNNNN
8 NNNNNNNNNNNNNN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 SSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123
4 pppppppppppppp
3 NNNNNNNNNNNNNN
2 NNNNNNNNNNNNNN
1 NppppppppppppN
0 NppppppppppppN
9 NppppppppppppN
8 NppppppppppppN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SnnnnnnnnnnnnS
3 SnnnnnnnnnnnnS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123
4
3
2        G  G
1        G  G
0        G  G
9        G  G G
8        G  G G
7        GG G G
6        GG G G
5        GG G G
4        GG G G
3        GG   G
2        GG G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 ++++++++++++++
3  +   +  +   +
2 &+  &+& + & +
1  + O + O+   +
0  + O +oO+ c +
9  + O   O+ C C
8  + OoOoO+ cCc
7    O      IIC
6  oOo  Ccc iIc
5    O    C   C
4  - OoOoOcCcCc
3  - O - O -- C
2 _-  _-_  -_
1  -   -   -
0 --------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD2 | VSS | A | Internal1 | X |
| --- | --- | --- | --- | --- | --- |
| NMOS2 |   |   |   | X | X |
| PMOS1 |   |   |   | X | X |
| Poly1 |   |   |   | X |   |
| Poly2 |   | X |   |   |   |
| Poly3 |   |   |   | X |   |
| Poly4 | X |   | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |
| NMOS2 | O | S | O | O |
| PMOS1 | O |   | O | O |
| PMOS2 |   |   |   |   |
