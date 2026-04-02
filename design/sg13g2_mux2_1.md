# Design Documentation for sg13g2_mux2_1

## Substrate
```
  012345678901234567
4 SSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567
4 pppppppppppppppppp
3
2
1    pppppppppppppp
0  pppppppppppppppp
9  pppppppppppppppp
8  pppppppppppppppp
7
6
5
4  nnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnn
2
1
0 nnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567
4
3
2
1   G
0   G
9   G
8   G
7   GGG
6   GGG G G G  G G
5   G
4   G
3   G
2
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567
4 &+&+&+&+&+&+&+&+&+
3     +        +
2     +CCCCCCCC+
1     +C      C+ OO
0  c c C  c   C+cOo
9  C     CC   C+ OO
8  c   CC     C+cOo
7  C      I I C   O
6  CIi  Ici i cCcCO
5  C    I   I     O
4  c _  IIIII CCC o
3  C - CCCCCCC -  O
2    _   c     -c c
1    -         -
0 _-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | Input1 | Input2 | Internal1 | Internal6 | Output1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |   |   |   |
| NMOS2 |   |   | X |   |   | X |   | X |
| PMOS1 | X | X |   |   |   | X | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   | X |   |   |   |
| Poly2 |   |   |   |   |   |   |   |   |
| Poly3 |   |   |   | X |   |   |   |   |
| Poly4 |   |   |   | X |   |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |
| NMOS2 | O |   |   |   |   |   |
| PMOS1 | O |   |   |   |   |   |
| PMOS2 |   |   |   |   |   |   |
