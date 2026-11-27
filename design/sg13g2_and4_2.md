# Design Documentation for sg13g2_and4_2

## Substrate
```
  0123456789012345
4 NNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNN
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
2 NNpppppppppppppN
1 Nppppppppppppppp
0 Nppppppppppppppp
9 Nppppppppppppppp
8 NNNNNNNNNppppppp
7 NNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSnnnnnS
4 Snnnnnnnnnnnnnnn
3 Snnnnnnnnnnnnnnn
2 SSnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345
4
3
2   GGGGG GGGG G
1   GGGGG GGGG G
0   GGGGG GGGG G
9   GGGGG GGGG G
8   GGGGG GGGG G
7   GGGGGGGGGGGG
6   GGGGGGGGGGGG
5   GGGGG GGGG G
4   GGGGG GGGG G
3   GGGGG GGGG G
2   GGGGG GGGG G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &+&+&+&+&+&+&+&+
3 ++++++++++++++++
2  +&c &+c &+ oO&+
1  ++CC++CC++OOO++
0  +&cC&+cC&+OoO&+
9  CCCCCCCCCCOOO++
8  CCCCCCCCCCCoO&
7  C I I IIICC O
6  C i i iIiCc O
5  C I I I    OO
4  Cc      _-OoO_-
3  CC      --OOO--
2  Cc      _- oO_-
1 ----------------
0 _-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | X | A | B | C |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X | X |   |   |   |
| PMOS1 | X |   | X |   |   |   |
| PMOS2 | X |   |   |   |   |   |
| Poly1 | X | X | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |

