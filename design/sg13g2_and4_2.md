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
2 NppppppppppppppN
1 NppppppppppppppN
0 NppppppppppppppN
9 NppppppppppppppN
8 NppppppppppppppN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 Snnnnnnnnnnnnnnn
3 SnnnnnnnnnnnnnnS
2 Snnnnnnnnnnnnnnn
1 SSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345
4
3
2     G
1     G  GG
0     G
9   G G GGGG
8   G G G  G
7   G G GGGG
6  GGGGGGGGGG
5   G G GGGG
4   G G GGG
3   G G GGG
2   G G GGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &+&+&+&+&+&+&+&+
3   +  +   +    +
2   &cC+&cc+& o &
1   +CC+ CC+  OO+
0   &cC+&cc+& oO&
9  CCCCCCCCCCCOO+
8  cCcCcCccCcCoO&
7  C I I IIICC O
6  c i i iiIcC O
5  C           O
4  cC      _  oO-_
3  CC      -  OO-
2  cC      _  o -_
1          -    -
0 -_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | B | D | VSS | X | VDD |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |   |   |
| NMOS2 |   |   |   | X | X |   |
| PMOS1 |   |   |   | X | X | X |
| PMOS2 |   |   |   |   |   | X |
| Poly1 | X | X | X | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| PMOS1 | O | O |
| PMOS2 |   |   |
