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
4 SnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345
4
3
2     G GGG G
1     G GGG G
0     G GGG G
9  GG G GGGGG
8  GG G GGGGG
7  GG G GGGGG
6  GGGGGGGGGG
5  GG G GGGGG
4  GG G GGG
3  GG G GGG
2  GG G GGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &+&+&+&+&+&+&+&+
3   +  +   +    +
2   +  &   +    &
1   +C + C +  OO+
0   +c & c +  oO&
9  CCCCCCCCCC OO+
8  c   c    c oO
7  C I I IIICC O
6  c i i iiIcC O
5  C I I I     O
4  cC      -  oO_
3  CC      -  OO-
2          -    _
1          -    -
0 _-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | A | B | D | X |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |
| NMOS2 |   | X | X |   |   |   | X |
| PMOS1 | X |   | X |   |   |   | X |
| PMOS2 | X |   |   |   |   |   |   |
| Poly1 |   |   | X | X | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |
