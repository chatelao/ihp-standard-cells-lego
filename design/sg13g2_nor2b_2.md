# Design Documentation for sg13g2_nor2b_2

## Substrate
```
  012345678901
4 NNNNNNNNNNNN
3 SNNNNNNNNNNN
2 NNNNNNNNNNNN
1 NNNNNNNNNNNN
0 NNNNNNNNNNNN
9 NNNNNNNNNNNN
8 NNNNNNNNNNNN
7 NNNNNNNNNNNN
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SSSSSSSSSSSS
3 SSSSSSSSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 SSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901
4 pppppppppppp
3 NNNNNNNNNNNN
2 NNNppppppppp
1 Nppppppppppp
0 Nppppppppppp
9 Nppppppppppp
8 Nppppppppppp
7 NNNNNNNNNNNN
6 SSSSSSSSSSSS
5 Snnnnnnnnnnn
4 Snnnnnnnnnnn
3 Snnnnnnnnnnn
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901
4
3
2   G G G GGG
1   G G G GGG
0   G G G GGG
9   G G G GGG
8   G G G GGG
7   GGG GGGGG
6   GGG GGGGG
5   G G G GGG
4   G G G GGG
3   G G G GGG
2  GG G G GGG
1     GGGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &+&+&+&+&+&+
3 ++++++++++++
2    & cCCCc+&
1  C +CCCCCC++
0  c &Cc oCc+&
9  C +  OOCC++
8  c & OOo c &
7  CCCCO  III
6  CCc O  iII
5  C -OOOOOO -
4  c _OoO_Oo-_
3  I -OO--OO--
2  i -  --  --
1 ------------
0 _-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | B_N | Internal1 | Y | A |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 |   | X |   | X |   |
| PMOS1 | X | X | X | X |   |
| PMOS2 | X |   |   |   |   |
| Poly1 |   | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 | N |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |

