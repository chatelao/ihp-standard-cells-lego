# Design Documentation for sg13g2_and2_2

## Substrate
```
  01234567890
4 SSSSSSSSSSS
3 NNNNNNNSSSS
2 NNNNNNNSSSS
1 NNNNNNNSSSS
0 SSSSSSSSSSS
9 SSSSSSSSSSS
8 SSSSSSSSSSS
7 SSSSSSSSSSS
6 SSSSSSSSSSS
5 SSSSSSSSSSS
4 SSSSSSSSSSS
3 SSSSSSSSSSS
2 SSSSSSSSSSS
1 SSSSSSSSSSS
0 SSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890
4 ppppppppppp
3 pppppppnnnn
2 pppppppnnnn
1 pppppppnnnn
0 nnnnnnnnnnS
9 nnnnnnnnnnS
8 nnnnnnnnnnS
7 SSSSSSSSSSS
6 SSSSSSSSSSS
5 nnnnnnnnnnS
4 nnnnnnnnnnS
3 nnnnnnnnnnS
2 SSSSSSSSSSS
1 SSSSSSSSSSS
0 nnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  01234567890
4
3
2 GGGGGGGGG
1 GGGGGGGGG
0 GGGGGGGGG
9 GGGGGGGGG
8 GGGGGGGGG
7 GGGGGGGGG
6 GGGGGGGGG
5 GGGGGGGGG
4 GGGGGGGGG
3 GGGGGGGGG
2 GGGG GGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
4 &&&&&&&&&&&
3 +++++++++++
2 +++&+++++++
1 +++++++&+++
0 +++&+++&+++
9 +++++++&+++
8 +++++++&++
7  IIIIIIO
6  IIiIiIO
5 ----------
4 ---_---_---
3 ___--------
2 ___--------
1 -----------
0 ___________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | B | X |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 |   | X | X | X |
| NMOS3 | X |   | X | X |
| PMOS1 | X |   | X |   |
| Poly1 | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| NMOS3 | O |
| PMOS1 | O |
