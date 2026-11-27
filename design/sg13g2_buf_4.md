# Design Documentation for sg13g2_buf_4

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
2 NppppppppNNNNN
1 pppppppppppppN
0 pppppppppppppp
9 pppppppppppppp
8 pppppppppppppp
7 NNNNNNNNNNNNNN
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SnnnnnnnnnnnnS
3 SnnnnnnnnnnnnS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123
4
3
2   G GGGGG
1   G GGGGGG G
0   G GGGGGG G
9   G GGGGGG G
8   G GGGGGG G
7   G GGGGGGGG
6   GGGGGGG GG
5   G GGGGG  G
4   G GGGGG  G
3   G GGGGG  G
2   G GGGGG  G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &+&+&+&+&+&+&+
3 ++++++++++++++
2 +&  +&  ++  ++
1 ++OO++OO++  ++
0 +&Oo+&Oo&+cC&+
9 ++OO +OO++CCC
8 +&OoOOOo&+cCCC
7  OOOOOOOC IICC
6  OOO  ccC IiCC
5   OO    C   CC
4 -_OoOOOoCCCCcC
3 --OO--OO--- CC
2 -_ o-_ o __ c
1 --------------
0 _-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Internal1 | X | A |
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

