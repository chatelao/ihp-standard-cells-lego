# Design Documentation for sg13g2_nor4_2

## Substrate
```
  012345678901234567890
4 SSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890
4 ppppppppppppppppppppp
3
2
1  pppppppppppppp ppppp
0  pppppppppppppp ppppp
9  pppppppppppppp ppppp
8  pppppppppppppp ppppp
7
6
5  nnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnn
2
1
0 nnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890
4
3
2   G          G   G G
1   G          G   G G
0   G          G   G G
9   G          G   G G
8   G          G   G G
7   GG    GG  GG  GGGG
6   GG    GG  GG  GGGG
5   G          G   G G
4   G          G   G G
3   G          G   G G
2   G          G   G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890
4 &+&+&+&+&+&+&+&+&+&+&
3  +   +
2  & c & c  c   c c   c
1  + C + C  C   C C   C
0  & c & cc c c c c c c
9  + C    C C C   C C C
8  c c    c c c   c c c
7   II    II  II II C
6   Ii    iIc iI Ii CO
5    CCCCCCCCCCCCCCCC
4  _ c c cc c c c c c _
3  - C ---C - C --- C -
2  -   ---  -   ---   -
1  -   ---  -   ---   -
0 _-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Input2 | Input3 | Input4 | Internal1 | Internal2 | Internal3 | Internal4 | Internal5 | Internal6 | Internal7 | Internal8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   | X |   |   |   |   | X |   |   |   |   |   |   |   |
| PMOS1 | X |   |   |   |   |   |   |   | X | X | X | X |   | X |
| PMOS2 |   |   |   |   |   |   | X | X |   |   |   |   | X |   |
| PMOS3 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   | X |   |   |   |   |   |   |   |   |   |   |   |
| Poly2 |   |   |   |   | X |   |   |   |   |   |   |   |   |   |
| Poly3 |   |   |   |   |   | X |   |   |   |   |   |   |   |   |
| Poly4 |   |   |   | X |   |   |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |
| NMOS2 | O | O | O | N |
| PMOS1 | O | O |   | S |
| PMOS2 |   |   | O |   |
| PMOS3 |   |   |   |   |
