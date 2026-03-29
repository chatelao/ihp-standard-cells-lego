# Design Documentation for sg13g2_dlygate4sd3_1

## Substrate
```
  0123456789012345
4 NNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSS
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
2 NppppppppppppppN
1 NppppppppppppppN
0 NppppppppppppppN
9 NppppppppppppppN
8 NppppppppppppppN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345
4
3
2 G G  G GG G
1 G G  G GG G
0 G G  G GG G
9 G G  G GG G G
8 G G  G GG G G
7 G G  G GG G G
6 GGG  G GG G G
5 G G  G GG G G
4 G G  G GG G G
3 G G  G GG G
2 G G  G GG G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &+&+&+&+&+&+&+&+
3    +        +
2    &        &
1    +  C C   +OO
0  c &  Ccc   &Oo
9  CCCC C C    OO
8    cC C cCcCcOo
7  II C C     C O
6  iI CcCccCc c o
5     C C     COO
4  cCcC C cCcCcOo
3  C -  C     -OO
2    _        _
1    -        -
0 _-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | X |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 |   | X | X | X |
| PMOS1 | X |   | X | X |
| PMOS2 | X |   |   |   |
| Poly1 |   |   | X |   |
| Poly2 |   |   | X |   |
| Poly3 |   |   | X |   |
| Poly4 |   |   | X |   |
| Poly5 |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |
| NMOS2 | O | O | O | O | O |
| PMOS1 | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |
