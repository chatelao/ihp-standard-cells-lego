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
2 NppppppppppNNNpN
1 NppppppppppNNNNN
0 NppppppppppNpNpN
9 NppppppppppNNNNN
8 NppppppppppNpNNN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SnnnnnnnnnnSnSSS
3 SnnnnnnnnnnSSSSS
2 SnnnnnnnnnnSSSSn
1 SSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345
4
3
2     G GGG
1     G GGG
0     G GGG
9   G G GGGG
8   G G GGGG
7   G G GGGG
6   GGGGGGGG
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
2   +  +   +&   &
1   +C + C +  OO+
0   +C + C +  oO&
9  CCCCCCCCCC OO+
8  C         CoO
7  C I I III C O
6  c I I IIIcC O
5  C           O
4  CC      -  oO-
3  CC      -  OO-
2          -    -_
1          -    -
0 -_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | X | VDD | VSS |
| --- | --- | --- | --- |
| NMOS1 |   |   | X |
| NMOS3 |   |   | X |
| NMOS4 | X |   |   |
| PMOS1 |   | X |   |
| PMOS2 | X |   |   |
| PMOS3 | X |   |   |
| PMOS4 |   | X |   |
| PMOS5 |   | X |   |
| PMOS6 |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| NMOS3 |   |
| NMOS4 |   |
| PMOS1 | O |
| PMOS2 |   |
| PMOS3 |   |
| PMOS4 |   |
| PMOS5 |   |
| PMOS6 |   |
