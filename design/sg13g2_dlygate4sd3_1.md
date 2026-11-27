# Design Documentation for sg13g2_dlygate4sd3_1

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
2 NNNppppNNNNppppN
1 NppppppppppppppN
0 NppppppppppppppN
9 NNNppppppppppppN
8 NNNppppNpppppppN
7 NNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSnnnnnnnS
4 SSSSSSSSnnnnnnnS
3 SnnnnnnSnnnnnnnS
2 SSSSSSSSSSSSnnnS
1 SSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345
4
3
2   G GG   GG GG
1   G GG   GGGGG
0   G GG   GGGGG
9   G GG   GGGGG
8   G GG   GGGGG
7   G GG   GGGGG
6   GGGG  GGGGGG
5   G GG   GGGGG
4   G GG   GGGGG
3   G GG   GGGGG
2   G GG      GG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &+&+&+&+&+&+&+&+
3 ++++++++++++++++
2    +  c    +& o
1  C +  CCCC ++OO
0  c &  cCcC +&Oo
9  CCCCCCCCC   OO
8     CCcCcCCCCOo
7  II CCCCCCCCC O
6  Ii cCCCCccCc O
5     CCCC   CCOO
4  cCCCCcCcCCCCoO
3  C -  CC   --OO
2    _       -_oO
1 ----------------
0 _-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Internal1 | X | A |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 |   | X | X | X |   |
| NMOS3 |   |   |   |   |   |
| PMOS1 | X |   | X | X |   |
| PMOS2 | X |   |   |   |   |
| Poly1 |   |   | X |   | X |
| Poly2 | X | X | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 |   | O |
| NMOS3 | O |   |
| PMOS1 | O | O |
| PMOS2 |   |   |

