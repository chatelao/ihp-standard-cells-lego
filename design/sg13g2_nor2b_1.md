# Design Documentation for sg13g2_nor2b_1

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
1 NNNppppNN
0 NppppppNN
9 NppppppNN
8 NppppppNN
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
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
2  G GG
1  GGGG
0  GGGG
9  GGGG
8  GGGG
7  GGGG
6  GGGG GG
5  GGGG G
4  GGGG G
3  GGGG G
2  G GG G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3    +
2    +
1    +  OO
0  c +  Oo
9  C   OOO
8  cCc o
7  I C OII
6  i c oIi
5    C O
4  cCc o -
3    - O -
2    -   -
1    -   -
0 _-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | B_N | Internal1 | Y |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   |   |   |   | X | X |
| PMOS1 |   |   |   |   | X | X |
| PMOS2 | X |   |   |   |   |   |
| Poly1 |   |   |   | X | X |   |
| Poly2 |   |   | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O |   |
| PMOS2 |   |   |
