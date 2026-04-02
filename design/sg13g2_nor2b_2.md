# Design Documentation for sg13g2_nor2b_2

## Substrate
```
  012345678901
4 SSSSSSSSSSSS
3 NNNNNNNNNNNN
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
0 NNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901
4 pppppppppppp
3
2
1  ppppppppppp
0  ppppppppppp
9  ppppppppppp
8  ppppppppppp
7
6
5  nnnnnnnnnnn
4  nnnnnnnnnnn
3  nnnnnnnnnnn
2
1
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901
4
3
2   G G G
1   G G G
0   G G G
9   G G G
8   G G G
7   GGG GGG
6   G G G G
5   G G G
4   G G G
3   G G G
2  GG G
1     GGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &+&+&+&+&+&+
3    +       +
2    & c  c c+
1  C + CCCCC +
0  c & c ccCc+
9  C +   O C +
8  c c OOoc c
7  CCC O  III
6  C c O  iII
5  C   OOOOO
4  c _ o ccOc-
3  I - O - O -
2  i -   -   -
1    -   -   -
0 _-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | Input1 | Input2 | Internal1 | Internal2 | Internal3 | Output1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |   |   |   |   |
| NMOS2 |   |   | X |   |   | X |   |   | X |
| PMOS1 | X | X |   |   |   | X | X | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   | X |   |   |   |   |   |
| Poly2 |   |   |   |   | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 | N |   |
| NMOS2 | O | O |
| PMOS1 | O | O |
| PMOS2 |   |   |
