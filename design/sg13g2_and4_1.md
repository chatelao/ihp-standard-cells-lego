# Design Documentation for sg13g2_and4_1

## Substrate
```
  01234567890123
4 NNNNNNNNNNNNNN
3 SNNNNNNNNNNNNN
2 NNNNNNNNNNNNNN
1 NNNNNNNNNNNNNN
0 NNNNNNNNNNNNNN
9 NNNNNNNNNNNNNN
8 NNNNNNNNNNNNNN
7 NNNNNNNNNNNNNN
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
2 NNpppppppppppN
1 NppppppppppppN
0 NppppppppppppN
9 NppppppppppppN
8 NNNNNNNNNppppN
7 NNNNNNNNNNNNNN
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSnnnS
4 SnnnnnnnnnnnnS
3 SnnnnnnnnnnnnS
2 SSnnnnnnnnnnnS
1 SSSSSSSSSSSSSS
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123
4
3
2   GGGGG GGGG
1   GGGGG GGGG
0   GGGGG GGGG
9   GGGGG GGGG
8   GGGGG GGGG
7   GGGGGGGGGG
6   GGGGGGGGGG
5   GGGGG GGGG
4   GGGGG GGGG
3   GGGGG GGGG
2   GGGGG GGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &+&+&+&+&+&+&+
3 ++++++++++++++
2  +&  &+  &+ oO
1  ++CC++CC++OOO
0  +&cC&+cC&+OoO
9  CCCCCCCCCCOOO
8  CCCCCCCCCCOoO
7  C I I I ICC O
6  C i i i iCc O
5  C           O
4  Cc      _-OoO
3  CC      --OOO
2  Cc      _- oO
1 --------------
0 _-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | X | A | B | C | D |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |   |   |   |
| NMOS2 | X |   | X | X |   |   |   |   |
| PMOS1 | X | X |   | X |   |   |   |   |
| PMOS2 |   | X |   |   |   |   |   |   |
| Poly1 | X | X | X |   | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |

