# Design Documentation for sg13g2_ebufn_2

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
3 nnnnnnnnnnnnnnnnnn
2 nnnnnnnnnnnnnnnnnn
1 nnnnnnnnnnnnnnnnnn
0 nnnnnnnnnnnnnnnnnn
9 nnnnnnnnnnnnnnnnnn
8 nnnnnnnnnnnnnnnnnn
7 SSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  012345678901234567
4
3
2   GGG GGGGGGG G
1   GGG GGGGGGGGG
0   GGG GGGGGGGGG
9   GGG GGGGGGGGG
8   GGG GGGGGGGGG
7   GGG GGGGGGGGG
6   GGGGGGGGGGGGG
5   GGG GGGGGGGGG
4   GGG GGGGGGGGG
3   GGG GGGGGGGGG
2   GGG GGGGGGGGG
1   GGG GGGGGGG G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567
4 &&&&&&&&&&&&&&&&&&
3 ++++++++++++++++++
2 +&+++&++&+++++&+++
1 ++++++++++++++++++
0  oOoIiIIIIIIIIIII
9  OOoIIIIIIIIIIIII
8  OOoIiIIIIiIIIIII
7   OOIIIIIIIIIIIII
6   OOIiIIIIiIiIiII
5   OOIIIIIIIIIIIII
4 -_-_-_-__---_-_---
3 ------------------
2 -_---_--_-----_---
1 ------------------
0 __________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | Z |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 | X |   | X | X |
| PMOS1 | X |   |   |   |
| Poly1 | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 | N |
| NMOS2 | O |
| PMOS1 |   |
