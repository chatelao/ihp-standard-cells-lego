# Design Documentation for sg13g2_nand3_1

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
2  ppppppp
1  ppppppp
0  ppppppp
9  ppppppp
8  ppppppp
7
6
5  nnnnnnn
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
2   G G
1   G G
0   G G
9   G G
8   G G
7  GGGG GG
6  GGGG GG
5   G G
4   G G
3   G G
2   G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3  +   +
2  & c & c
1  + O + O
0  & o & o
9  + OOOOO
8  c c O c
7  I IIOII
6  i iIOIi
5      O
4  _   OOo
3  -     O
2  _     c
1  -
0 _-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Input2 | Input3 | Output1 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X |   |   |   | X |
| PMOS1 | X |   |   |   |   | X |
| PMOS2 | X |   |   |   |   |   |
| Poly1 |   |   | X | X |   |   |
| Poly2 |   |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | N |
| PMOS1 | O | S |
| PMOS2 |   |   |
