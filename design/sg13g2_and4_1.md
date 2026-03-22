# Design Documentation for sg13g2_and4_1

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
2 NpppppppppppNN
1 NpppppppppppNN
0 NppppppppppppN
9 NpppppppppppNN
8 NppppppppppppN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SnnnnnnnnnnnnS
3 SnnnnnnnnnnnSS
2 SnnnnnnnnnnnSS
1 SSSSSSSSSSSSSS
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123
4
3
2     G G G G
1     G G G G
0     G G G G
9   G G G G G
8   G G G G G
7   G G G G G
6   GGGGGGGGG
5   G G G G G
4   G G G G G
3   G G G G G
2   G G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &+&+&+&+&+&+&+
3   +  +   +
2   +  +   +  c
1   +C + C +  OO
0   +C + C +  oO
9  CCCCCCCCCC OO
8  C         CoO
7  C I I I I C O
6  c I I I I CcO
5  C           O
4  CC      _  oO
3  CC      -  OO
2          _
1          -
0 -_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | X | VDD | VSS |
| --- | --- | --- | --- |
| NMOS1 |   |   | X |
| NMOS2 | X |   | X |
| PMOS1 | X |   |   |
| PMOS2 |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |
