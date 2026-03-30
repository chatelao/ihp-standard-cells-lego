# Design Documentation for sg13g2_nand3b_1

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
2 NNNNNNNNNNNN
1 NNpppppppppN
0 NNpppppppppN
9 NNpppppppppN
8 NNpppppppppN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSnnnnnnnnnS
4 SSnnnnnnnnnS
3 SSnnnnnnnnnS
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
2  GG   G   G
1  GG   G   G
0  GG   G   G
9  GG   G G G
8  GG G G G G
7  GG G G G G
6  GGGGGGGG G
5  GG G G G G
4  GG G G G G
3  GG   G G G
2  GG   G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 ++++++++++++
3     +   +
2     + & +
1     + O + OO
0  Cc + o + oO
9  CC + OOOOOO
8  C      o  O
7  C I I I   O
6  c i i icCcO
5  C       C O
4  CcCcCcCcCoO
3     -     OO
2   _ - _
1     -
0 ------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD2 | VSS2 | VSS3 | A_N | B | C | Internal1 | Y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS2 |   |   |   |   |   |   | X | X |
| PMOS1 |   |   |   |   |   |   | X | X |
| Poly1 | X | X | X | X | X | X | X | X |
| Poly2 |   |   |   |   |   |   | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O | O |
| PMOS2 |   |   |
