# Design Documentation for sg13g2_nor3_2

## Substrate
```
  0123456789012345
4 SSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNN
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
0 NNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345
4 pppppppppppppppp
3
2
1  pppppppppppppp
0  pppppppppppppp
9  pppppppppppppp
8  pppppppppppppp
7
6
5  nnnnnnnnnnnnnn
4  nnnnnnnnnnnnnn
3  nnnnnnnnnnnnnn
2
1
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345
4
3
2   G          G
1   G          G
0   G          G
9   G          G
8   G          G
7   GG   GGG  GG
6   GG   GGG  GG
5   G          G
4   G          G
3   G          G
2   G          G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &+&+&+&+&+&+&+&+
3  +   +
2  & c & c  c   c
1  + C + CCCCCCCC
0  & c & cc c o c
9  + C    C   O C
8  c c    c OOo c
7        C  O
6   Ii  IiOOO iI
5         O OOO
4  _ o c co c o _
3  - O ---O - O -
2  -   ---  -   -
1  -   ---  -   -
0 _-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Input2 | Input3 | Internal2 | Internal3 | Output1 | Output2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |
| NMOS2 |   | X |   |   |   |   |   | X | X |
| PMOS1 | X |   |   |   |   | X | X |   | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |
| Poly1 |   |   | X |   |   |   |   |   |   |
| Poly2 |   |   |   |   | X |   |   |   |   |
| Poly3 |   |   |   | X |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | O | N |
| PMOS1 | O | O | S |
| PMOS2 |   |   |   |
