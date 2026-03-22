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
2 pppppppppppppN
1 NppppppppppppN
0 NppppppppppppN
9 NppppppppppppN
8 NppppppppppppN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SnnnnnnnnnnnnS
3 SnnnnnnnnnnnnS
2 SnnnnnnnnnnnnS
1 SSSSSSSSSSSSSS
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123
4
3
2           G G
1           G G
0           G G
9           G G
8           G G
7           G G
6  G G      GGG
5           G G
4           G G
3           G G
2           G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &+&+&+&+&+&+&+
3  +   +  +   +
2 &+  &+  &   &
1  + O + O+   +
0  + o + o& c &
9  + O   O+ C
8  + oOoOo& cCcC
7    O      II C
6  oOo  Ccc iIcC
5    O    C    C
4  _ oOoOocCcCcC
3  - O - O -- CC
2  _   _   _
1  -   -   -
0 -_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | Internal1 | X | VDD | VSS |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   | X |
| NMOS2 |   | X | X |   | X |
| PMOS1 |   | X | X | X |   |
| PMOS2 |   |   |   | X |   |
| Poly1 | X | X |   | X |   |
| Poly2 |   |   | X |   |   |
| Poly3 |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | NMOS1 | NMOS2 | PMOS1 | PMOS2 | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   | O |   |   |
| PMOS1 |   |   |   |   | O |   |   |
| PMOS2 |   |   |   |   |   |   |   |
| Poly1 |   | O | O |   |   |   |   |
| Poly2 |   |   |   |   |   |   |   |
| Poly3 |   |   |   |   |   |   |   |
