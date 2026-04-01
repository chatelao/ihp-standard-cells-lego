# Design Documentation for sg13g2_mux2_2

## Substrate
```
  01234567890123456789
4 SSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSS
9 SSSSSSSSSSSSSSSSSSSS
8 SSSSSSSSSSSSSSSSSSSS
7 SSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789
4 pppppppppppppppppppp
3 SSSSSSSSSSSSSSSSSSSS
2 SnnnnnnnnnnnnnnnnnnS
1 SnnnnnnnnnnnnnnnnnnS
0 SnnnnnnnnnnnnnnnnnnS
9 SnnnnnnnnnnnnnnnnnnS
8 SnnnnnnnnnnnnnnnnnnS
7 SSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSS
5 SnnnnnnnnnnnnnnnnnnS
4 SnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  01234567890123456789
4
3
2   GGGG GG G GGGG
1   GGGG GGGG GGGG
0   GGGG GGGG GGGG
9   GGGG GGGG GGGG
8   GGGG GGGG GGGG
7   GGGG GGGG GGGG
6   GGGGGGGGG GGGG
5   GGGGGGGGG GGGG
4   GGGGGGGG  GGGG
3   GGGGGGGG  GGGG
2   GGGGGGGG  GGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789
4 &&&&&&&&&&&&&&&&&&&&
3 ++++++++++++++++++++
2 ++++++++++++++++++++
1 +++++++++++++++&&+++
0 +&+&++++&+++++&&&+++
9 +++++++++++++++&&+++
8 +&++++++++++++&&&+++
7  IiiIIIIIIIIIIIIOO
6  IiiIIIiiIiIiIiIOO
5  IIIIIIIIIiIIIIIOO
4 -_---_----_-----_---
3 --------------------
2 -----_--------_-----
1 --------------------
0 ____________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A0 | X |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 |   | X | X | X |
| NMOS3 | X |   | X | X |
| PMOS1 | X |   |   |   |
| Poly1 | X | X | X |   |
| Poly2 | X | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| NMOS3 | O | O |
| PMOS1 |   |   |
