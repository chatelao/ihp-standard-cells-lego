# Design Documentation for sg13g2_nor2b_1

## Substrate
```
  012345678
4 SSSSSSSSS
3 NNNNNNNNN
2 NNNNNNNNN
1 NNNNNNNNN
0 NNNNNNNNN
9 NNNNNNNNN
8 NNNNNNNNN
7 NNNNNNNNN
6 SSSSSSSSS
5 SSSSSSSSS
4 SSSSSSSSS
3 SSSSSSSSS
2 SSSSSSSSS
1 SSSSSSSSS
0 NNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678
4 ppppppppp
3
2
1    pppp
0  pppppp
9  pppppp
8  pppppp
7
6
5
4  nnnnnnn
3  nnnnnnn
2
1
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678
4
3
2     G
1   G G
0   G G
9   G G
8   G G
7   G G
6  GGGG GG
5   G G G
4   G G G
3   G G G
2     G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3    +
2    &   c
1    +  OO
0  c &  Oo
9  C   OOO
8  cCC O c
7    C O
6  i c OIi
5    C O
4  cCC o _
3    - O -
2    _ c _
1    -   -
0 _-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Input2 | Internal1 | Output1 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X |   |   | X | X |
| PMOS1 | X |   |   |   | X |   |
| PMOS2 | X |   |   |   |   |   |
| Poly1 |   |   | X |   | X |   |
| Poly2 |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O |   |
| PMOS2 |   |   |
