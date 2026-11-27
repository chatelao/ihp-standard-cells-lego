# Design Documentation for sg13g2_and2_2

## Substrate
```
  01234567890
4 NNNNNNNNNNN
3 SNNNNNNNNNN
2 NNNNNNNNNNN
1 NNNNNNNNNNN
0 NNNNNNNNNNN
9 NNNNNNNNNNN
8 NNNNNNNNNNN
7 NNNNNNNNNNN
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
2 NpppppppppN
1 ppppppppppN
0 ppppppppppN
9 ppppppppppN
8 NNNNNpppppN
7 NNNNNNNNNNN
6 SSSSSSSSSSS
5 nnnnnnnnnnS
4 nnnnnnnnnnS
3 nnnnnnnnnnS
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
2   G GGGGG
1   G GGGGG
0   G GGGGG
9   G GGGGG
8   G GGGGG
7   GGGGGGG
6   GGGGGGG
5   G GGGGG
4   G GGGGG
3 GGG GGGGG
2 GGG  GGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
4 &+&+&+&+&+&
3 +++++++++++
2  & c+& o&+
1  +CC++OO++
0  &Cc+&Oo&+
9   CC  OO++
8  CCCCC o&
7  C   CCO
6  C i cCO
5  C     O-
4  c  -_Oo_-
3 III --OO--
2 iIi --  --
1 -----------
0 _-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | X | A | B |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 |   | X | X | X |   |
| PMOS1 | X |   | X | X |   |
| PMOS2 | X |   |   |   |   |
| Poly1 | X | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |

