# Design Documentation for sg13g2_mux2_1

## Substrate
```
  012345678901234567
4 SSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSS
9 SSSSSSSSSSSSSSSSSS
8 SSSSSSSSSSSSSSSSSS
7 SSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567
4 pppppppppppppppppp
3 SSSSSSSSSSSSSSSSSS
2 SnnnnnnnnnnnnnnnnS
1 SnnnnnnnnnnnnnnnnS
0 SnnnnnnnnnnnnnnnnS
9 SnnnnnnnnnnnnnnnnS
8 SnnnnnnnnnnnnnnnnS
7 SSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSS
5 SnnnnnnnnnnnnnnnnS
4 SnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  012345678901234567
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
  012345678901234567
4 &&&&&&&&&&&&&&&&&&
3 ++++++++++++++++++
2 ++++++++++++++++++
1 +++++++++++++++&&+
0 +&+&++++&+++++&&&+
9 +++++++++++++++&&+
8 +&++++++++++++&&&+
7  IIIIIIIiIiIIIIIO
6  IiiIIIiiIiIiIiIO
5  IIIIIIIIIiIIIIIO
4 -_---_----_-----_-
3 ------------------
2 -----_--------_---
1 ------------------
0 __________________
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
