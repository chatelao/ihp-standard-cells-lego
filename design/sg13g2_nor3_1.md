# Design Documentation for sg13g2_nor3_1

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
2
1
0
9
8
7
6  GG  G G
5
4
3
2
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3  +
2  &     c
1  +     O
0  &     o
9  +  OOOO
8  c     c
7
6  i   i i
5
4  _ cOOOo
3  -   - O
2  _ c _ c
1  -   -
0 _-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Input2 | Input3 | Output1 | Output2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |
| NMOS2 |   | X |   |   |   | X |   |
| PMOS1 | X |   |   |   |   |   | X |
| PMOS2 | X |   |   |   |   |   |   |
| Poly1 |   |   | X |   |   |   |   |
| Poly2 |   |   |   | X |   |   |   |
| Poly3 |   |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | N | N | N |
| PMOS1 |   |   |   |
| PMOS2 |   |   |   |
