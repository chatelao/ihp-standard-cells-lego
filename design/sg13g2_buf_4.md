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
1 NppppppppNNNNN
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
2   G    GG G
1   G    GG G
0   G    GG G
9   G    GG G
8   G    GG G
7   G    GG GG
6   GGGGGGG GG
5   G    GG G
4   G    GG G
3   G    GG G
2   G    GG G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &+&+&+&+&+&+&+
3  +   +  +   +
2  +   +  +   +
1  + O + O+   +
0  + o + o+ c +
9  + O   O+ C C
8  + oOoOo+ cCc
7    O      IIC
6  oOo  Ccc iIc
5    O    C   C
4  - oOoOocCcCc
3  - O - O -- C
2  -   -   -_
1  -   -   -
0 _-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | Internal1 | X |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 |   |   |   | X | X |
| PMOS1 |   |   |   | X | X |
| PMOS2 | X |   |   |   |   |
| Poly1 |   |   |   | X | X |
| Poly2 |   | X | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O | O |
| PMOS2 |   |   |
