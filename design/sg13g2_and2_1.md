# Design Documentation for sg13g2_and2_1

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
1  ppppppp
0  ppppppp
9  ppppppp
8      ppp
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
2   G
1   G
0   G
9   G
8   G
7   G
6   GG GG
5   G
4   G
3   G
2 GGG
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
1  + C + O
0  & c & o
9    C   O
8  CCCCC o
7  C   C
6  C i c
5  C
4  c   _ o
3 III  - O
2 IiI  -
1      -
0 _-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Input2 | Internal1 | Output1 | Output2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |
| NMOS2 |   | X |   |   | X | X |   |
| PMOS1 | X |   |   |   | X |   | X |
| PMOS2 | X |   |   |   |   |   |   |
| Poly1 |   |   | X | X |   |   |   |
| Poly2 |   |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | N |
| PMOS1 | O |   |
| PMOS2 |   |   |
