# Design Documentation for sg13g2_and4_2

## Substrate
```
  0123456789012345
4 NNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345
4 pppppppppppppppp
3 NNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NppppppppppppppN
0 NppppppppppppppN
9 NppppppppppppppN
8 NppppppppppppppN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345
4
3
2     G G G G
1     G G G G
0     G G G G
9  GG G G G G
8  GG G G G G
7  GG G G G G
6  GGGGGGGG G
5  GG G G G G
4  GG G G G
3  GG G G G
2  GG G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 ++++++++++++++++
3   +  +   +    +
2 & +  +& &+& & +
1   +C + C +  OO+
0   +Cc+ Cc+  oO+
9  CCCCCCCCCC OO+
8  C    c   c oO
7  C I I IIICC O
6  c i i iiIcC O
5  C I I I     O
4  Cc      -  oO-
3  CC      -  OO-
2         _-_ _ -
1          -    -
0 ----------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | B | C | Internal1 | X |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS2 |   |   |   |   |   | X | X |
| PMOS1 |   |   |   |   |   | X | X |
| Poly1 | X | X | X | X | X | X |   |
| Poly2 | X |   |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | N |
| PMOS1 | O | O |
| PMOS2 |   |   |
