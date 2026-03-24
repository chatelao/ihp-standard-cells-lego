# Design Documentation for sg13g2_nor2b_2

## Substrate
```
  012345678901
4 NNNNNNNNNNNN
3 NNNNNNNNNNNN
2 NNNNNNNNNNNN
1 NNNNNNNNNNNN
0 NNNNNNNNNNNN
9 NNNNNNNNNNNN
8 NNNNNNNNNNNN
7 SSSSSSSSSSSS
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
2 NppppppppppN
1 NppppppppppN
0 NppppppppppN
9 NppppppppppN
8 NppppppppppN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 Snnnnnnnnnnn
3 SnnnnnnnnnnS
2 Snnnnnnnnnnn
1 SSSSSSSSSSSS
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901
4
3
2 G G     G G
1 G G     G G
0 G G     G G
9 G G     G G
8 G G     G G
7 G G     G G
6 G G  G  GGG
5 G G     G G
4 GGG     G G
3 GGG     G G
2 GGG     G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &+&+&+&+&+&+
3 ++++++++++++
2   &+CcCccC&+
1  C +CCCCCC++
0  c +CcOocC&+
9  C +  OOCC++
8  c + oOocC&+
7  CCCCO  IIII
6  cCcCo  iIiI
5  C -OOOOOO--
4  iI_Oo-_oO-_
3  II-OO--OO--
2  iI_  -_  -_
1 ------------
0 -_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | B_N | VSS2 | VSS3 | Y | VDD | VSS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   | X |
| NMOS2 |   | X | X |   | X |   | X |
| PMOS1 |   |   | X | X | X | X |   |
| PMOS2 |   |   |   |   |   | X |   |
| Poly1 |   | X | X |   |   | X |   |
| Poly2 | X |   |   | X | X | X |   |
| Poly3 |   |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | O |   |
| PMOS1 | O | O |   |
| PMOS2 |   |   |   |
