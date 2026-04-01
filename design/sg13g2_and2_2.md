# Design Documentation for sg13g2_and2_2

## Substrate
```
  01234567890
4 NNNNNNNNNNN
3 NNNNNNNNNNN
2 NNNNNNNNNNN
1 NNNNNNNNNNN
0 NNNNNNNNNNN
9 NNNNNNNNNNN
8 NNNNNNNNNNN
7 SSSSSSSSSSS
6 SSSSSSSSSSS
5 SSSSSSSSSSS
4 SSSSSSSSSSS
3 SSSSSSSSSSS
2 SSSSSSSSSSS
1 SSSSSSSSSSS
0 SSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890
4 ppppppppppp
3 NNNNNNNNNNN
2 NNNNNNNNNNN
1 NpppppppppN
0 NpppppppppN
9 NpppppppppN
8 NNNNNpppppN
7 SSSSSSSSSSS
6 SSSSSSSSSSS
5 SnnnnnnnnnS
4 SnnnnnnnnnS
3 SnnnnnnnnnS
2 SSSSSSSSSSS
1 SSSSSSSSSSS
0 nnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890
4
3
2  GGG G
1  GGG G
0  GGG G
9  GGG G
8  GGG G
7  GGG GGG
6  GGG GGG
5  GGG G
4  GGG G
3  GGG G
2 GGGG G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
4 &+&+&+&+&+&
3  +   +  +
2  +   +  +
1  + C +OO+
0  + c +Oo+
9    C  OO+
8  cCcCc o
7  C I CCO
6  c i iCo
5  C     O
4      -Oo-
3 III  -OO-
2 IiI  -  -
1      -  -
0 _-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | B | Input1 | Internal1 | X |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   | X |
| PMOS1 |   |   |   |   |   | X | X |
| PMOS2 | X |   |   |   |   |   |   |
| Poly1 |   |   | X | X |   | X |   |
| Poly2 |   |   |   |   | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O | O |
| PMOS2 |   |   |
