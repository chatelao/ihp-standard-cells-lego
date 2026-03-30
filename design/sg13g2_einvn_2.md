# Design Documentation for sg13g2_einvn_2

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
2 NNNNNNNNNNNNNNNN
1 NNpppNpppppppppN
0 NNpppNpppppppppN
9 NNNNNNpppppppppN
8 NNNNNNpppppppppN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SSSSSSnnnnnnnnnS
3 SSnnnSnnnnnnnnnS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345
4
3
2  G  GGG   G G G
1  G  GGG   G G G
0  G  GGG   G G G
9  GG GGG G G G G
8  GG GGG G G G G
7  GG GGG G G G G
6  GGGGGG G G G G
5  GG GGG G G G G
4  GG GGG G G G G
3  G  GGG   G G G
2  G  GGG   G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 ++++++++++++++++
3   +     +
2   + & & + cCcCc
1   + C C + C   C
0   + c c + c o c
9     C CCCCC O C
8  IiIc   c   o
7  IIIC       O
6  iIiCc      o i
5  IIIC       O I
4     c cCcCc o i
3   - C C - CCCCC
2   - _ _ -   c
1   -     -
0 ----------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD2 | VDD3 | VSS2 | VSS3 | A | TE_B | Internal1 | Internal2 | Internal3 | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS3 |   |   |   |   | X |   |   | X |   | X |
| PMOS1 |   |   |   |   |   |   |   |   | X | X |
| PMOS2 |   |   |   |   |   |   | X |   |   |   |
| Poly1 | X | X | X | X |   | X | X | X | X |   |
| Poly2 |   |   |   |   |   |   |   | X | X |   |
| Poly3 |   |   |   |   |   |   |   | X | X | X |
| Poly4 |   |   |   |   | X |   |   |   | X |   |
| Poly5 |   |   |   |   |   |   |   | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |
| NMOS2 | O |   |   |   |   |
| NMOS3 | O | O | O | O | O |
| PMOS1 | O | O | O | O | O |
| PMOS2 | O |   |   |   |   |
| PMOS3 |   |   |   |   |   |
