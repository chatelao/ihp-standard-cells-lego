# Design Documentation for sg13g2_dllr_1

## Substrate
```
  0123456789012345678901234567890123
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppp
3 pppppppppppppppppppppppppppppppppp
2 pppppppppppppppppppppppppppppppppp
1 pppppppppppppppppppppppppppppppppp
0 pppppppppppppppppppppppppppppppppp
9 pppppppppppppppppppppppppppppppppp
8 pppppppppppppppppppppppppppppppppp
7 pppppppppppppppppppppppppppppppppp
6 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
5 SSnnnnSSnnnnnnnnnnnSSSSSSSSSnnnnnS
4 SnnnnnnnnnnnnnnnnnnnSSSSSSSSnnnnnS
3 SnnnnnnnnnnnnnnnnnnnSSSSSSSSnnnnnS
2 SSnnnnSSnnnnnnnnnnnSSSSSSSSSnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123
4
3
2   GGGG   GGGGGGGGGGGGGGGGGGGGGGG
1   GGGG   GGGGGGGGGGGGGGGGGGGGGGG
0   GGGG   GGGGGGGGGGGGGGGGGGGGGGG
9   GGGG   GGGGGGGGGGGGGGGGGGGGGGG
8   GGGG   GGGGGGGGGGGGGGGGGGGGGGG
7   GGGG   GGGGGGGGGGGGGGGGGGGGGGG
6   GGGG   GGGGGGGGGGGGGGGGGGGGGGG
5   GGGG   GGGGGGGGGGGGGGGGGGGGGGG
4   GGGG   GGGGGGGGGGGGGGGGGGGGGGG
3   GGGG   GGGGGGGGGGGGGGGGGGGGGGG
2    GGG   GGGGGGGG GGGGGGGGGGGGGG
1                    GGG G GGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123
4 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
3 ++++++++++++++++++++++++++++++++++
2 ++++++++++++&+++++++++++++++++++&+
1 ++++++++++++++------++++++&+++++&+
0 +&+&+++&++++++_-_-_-&+&+++&+&+++&+
9 ++++++++++++++------++++++&+++++&+
8 +++&++++_---------_-++&+&+&+++++&+
7  IIiIiII------------++++++OO++++OO
6  IIiIiII--_---_-_---++&&++OO++&+OO
5  IIIIIII------------++++++OO++++OO
4 -_-_----_-_---------_-_---_-_---_-
3 ----------------------------------
2 ---_----_-----_-------_---_-_---_-
1 ----------------------------------
0 __________________________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | D | RESET_B | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X | X |   |   |   |
| NMOS3 | X | X |   |   |   | X |
| PMOS1 | X | X | X |   | X | X |
| Poly1 | X | X | X | X | X |   |
| Poly2 | X | X | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 | N |   |
| NMOS2 | O | O |
| NMOS3 | O |   |
| PMOS1 | O | O |
