# Design Documentation for sg13g2_buf_4

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
1 nnnnnnnnnnnnnn
0 nnnnnnnnnnnnnn
9 nnnnnnnnnnnnnn
8 nnnnnnnnnnnnnn
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  01234567890123
4
3
2   GGGGGGG G
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
2 +++&++++++++++
1 ++++++++++++++
0 +++&+++&++&+++
9 ++++++++++++++
8 +++&+++&++&+++
7  OOOOOOOOOOOOO
6  oooOOOoOOioOO
5  OOOOOOOOOOOOO
4 ---_-_-_----_-
3 --------------
2 ---_----_-_---
1 --------------
0 ______________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | X |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 | X |   |   | X |
| PMOS1 | X |   |   |   |
| Poly1 | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 |   |
