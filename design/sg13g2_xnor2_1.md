# Design Documentation for sg13g2_xnor2_1

## Substrate
```
  01234567890123
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 SSSSSSSSSSSSSS
9 SSSSSSSSSSSSSS
8 SSSSSSSSSSSSSS
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 SSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123
4 pppppppppppppp
3 SSSSSSSSSSSSSS
2 SnnnnnnnnnnnnS
1 SnnnnnnnnnnnnS
0 SnnnnnnnnnnnnS
9 SnnnnnnnnnnnnS
8 SnnnnnnnnnnnnS
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SnnnSSSnnnnnnS
4 SSSSSSnnnnnnnn
3 SSSSSSnnnnnnnn
2 SSSSSSnnnnnnnn
1 SSSSSSSSSSSSSS
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  01234567890123
4
3
2   GGGGGGGGGGG
1   GGGGGGGGGGG
0   GGGGGGGGGGG
9   GGGGGGGGGGG
8   GGGGGGGGGGG
7   GGGGGGGGGGG
6   GGGGGGGGGGG
5   GGGGGGGGGGG
4   GGGGGGGGGGG
3   GGGGGGGGGGG
2   GGGGGGGGGGG
1    GGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &&&&&&&&&&&&&&
3 ++++++++++++++
2 +++++++&++&+++
1 ++++++++++&+++
0 +++&+++&++&+++
9 ++++++++++&+++
8    OIIIIIIoOOO
7    OIiIiIIOOOO
6    OIiIiiIOOoO
5 --------------
4 ---_-_------_-
3 --------------
2 -------_------
1 --------------
0 ______________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | B | Y |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 |   | X |   | X |
| NMOS3 |   |   |   |   |
| NMOS4 | X |   |   | X |
| PMOS1 | X |   |   |   |
| Poly1 | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 | N |
| NMOS2 | O |
| NMOS3 | O |
| NMOS4 | O |
| PMOS1 |   |
