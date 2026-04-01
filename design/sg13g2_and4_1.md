# Design Documentation for sg13g2_and4_1

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
2 SSnnnnnnnnnnnS
1 SnnnnnnnnnnnnS
0 SnnnnnnnnnnnnS
9 SnnnnnnnnnnnnS
8 SnnnnnnnnnnnnS
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSnnnnnnnnnnnS
4 SnnnnnnnnnnnnS
3 SnnnnnnnnnnnnS
2 SSnnnnnnnnnnnS
1 SSSSSSSSSSSSSS
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  01234567890123
4
3
2   GGGGGGGGGG
1   GGGGGGGGGG
0   GGGGGGGGGG
9   GGGGGGGGGG
8   GGGGGGGGGG
7   GGGGGGGGGG
6   GGGGGGGGGG
5   GGGGGGGGGG
4   GGGGGGGGGG
3   GGGGGGGGGG
2   GGGGGGGGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &&&&&&&&&&&&&&
3 ++++++++++++++
2 +&+++++&++&+++
1 ++++++++++++&&
0 +&+&+++&++&+&&
9  IIIIIIIIIIIoo
8  IIIIIIIIIIIoo
7  IIiIiIiIiIIOO
6  IIiIiIiiiiIOO
5  IIIIIIIIIIIOO
4 -_--------_-_-
3 --------------
2 ----------_---
1 --------------
0 ______________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | C | X |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 |   | X | X | X |
| NMOS3 | X |   | X | X |
| PMOS1 | X |   |   |   |
| Poly1 | X | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| NMOS3 | O |
| PMOS1 |   |
