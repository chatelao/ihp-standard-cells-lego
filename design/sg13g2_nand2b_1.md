# Design Documentation for sg13g2_nand2b_1

## Substrate
```
  012345678
4 NNNNNNNNN
3 SNNNNNNNN
2 NNNNNNNNN
1 NNNNNNNNN
0 NNNNNNNNN
9 NNNNNNNNN
8 NNNNNNNNN
7 NNNNNNNNN
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
2 NNNppppNN
1 NpppppppN
0 ppppppppN
9 ppppppppN
8 ppppppppN
7 NNNNNNNNN
6 SSSSSSSSS
5 SnnnnnnnS
4 nnnnnnnnS
3 nnnnnnnnS
2 SSSnnnnnS
1 SSSSSSSSS
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678
4
3
2    GGGG
1  GGGGGG
0  GGGGGG
9  GGGGGG
8  GGGGGG
7  GGGGGG
6  GGGGGGG
5  GGGGGG
4  GGGGGG
3  GGGGGG
2    GGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3 +++++++++
2   +&o &+
1  C++OO++
0 Cc+&oOOO
9 CCCCCC O
8  cCCCC O
7      CCO
6  i iICcO
5 CCCCCCOO
4 Cc    Oo
3   --  OO
2   -_  Oo
1 ---------
0 _-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Y | A_N | B |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 |   | X | X |   |   |
| PMOS1 | X |   | X |   |   |
| PMOS2 | X |   |   |   |   |
| Poly1 | X | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |

