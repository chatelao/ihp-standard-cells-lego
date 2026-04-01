# Design Documentation for sg13g2_and2_1

## Substrate
```
  012345678
4 NNNNNNNNN
3 NNNNNNNNN
2 NNNNNNNNN
1 NNNNNNNNN
0 NNNNNNNNN
9 NNNNNNNNN
8 NNNNNNNNN
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 SSSSSSSSS
3 SSSSSSSSS
2 SSSSSSSSS
1 SSSSSSSSS
0 SSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678
4 ppppppppp
3 NNNNNNNNN
2 NNNNNNNNN
1 NpppppppN
0 NpppppppN
9 NpppppppN
8 NNNNNpppN
7 SSSSSSSSS
6 SSSSSSSSS
5 SnnnnnnnS
4 SnnnnnnnS
3 SnnnnnnnS
2 SSSSSSSSS
1 SSSSSSSSS
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678
4
3
2  GGG G
1  GGG G
0  GGG G
9  GGG G
8  GGG G
7  GGG G
6  GGG GG
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
  012345678
4 &+&+&+&+&
3  +   +
2  +   +
1  + C +OOO
0  + c +Ooo
9    C  OOO
8  cCcCcOoo
7  C I C  O
6  c i iC o
5  C      O
4      -Ooo
3 III  -OOO
2 IiI  -
1      -
0 _-_-_-_-_
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
| Poly2 |   |   |   |   | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O | O |
| PMOS2 |   |   |
