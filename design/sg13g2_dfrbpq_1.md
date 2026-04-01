# Design Documentation for sg13g2_dfrbpq_1

## Substrate
```
  012345678901234567890123456789012345678901234567
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678901234567
4 pppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNpppppppNpppppppppppppNNNNNNN
2 ppppppppNNNNNNNNNNNNpppppppNpppppppppppppNNNNNNN
1 ppppppppppppppppppNNpppppppNpppppppppppppNNNNNNN
0 ppppppppppppppppppNNpppppppNpppppppppppppNNNNNNN
9 ppppppppNNNNNNNNNNNNpppppppNpppppppppppppNNNNNNN
8 NppppppNNNNNNNNNNNNNpppppppNppppppppppppNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 NppppppNNNNNpppppppNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
5 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789012345678901234567
4
3     GGGGGGGGGGGGGGG
2  G GGGGGGGGGGGGGGGGGGGG GGGGGGG G G GGGGGGGG
1  G GGGGGGGGGGGGGGGGGGGG GGGGGGG G G GGGGGGGG
0  G GGGGGGGGGGGGGGGGGGGG GGGGGGGGG G GGGGGGGG
9  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGG GGGGGGGGGG
8  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGG GGGGGGGGGG
7  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGG GGGGGGGGGG
6  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGG GGGGGGGGGG
5  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGG GGGGGGGGGG
4  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGG GGGGGGGGGG
3  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGG GGGGGGGGGG
2  GGGGGGGGGGGGGGGGGGGGGG GGG G GGG GGGGGGGGGG
1     GGGGGGGGGGGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789012345678901234567
4 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
3 ++++++++++++++++++++++++++++++++++++++++++++++++
2 +++&++++++&+++++++&+++++++++++++++++&+++&+&+++++
1 ++++++++++++++++++++++++++++++++++++++++++++++&+
0 +++++++&&+++++&+&+++&+++++++++++++++++++&+&+++&+
9 ++++++++++++++++++++++++++++++++++++++++++++++&+
8 +&+&++++++++++++++&+&+++++&+&+++&+++++&+&+&+++&+
7 IiIIIIIIiiIIIIIIIIIIIIIIIIIIIIIIIC++++++ +++++O
6 IiIIIiIIiiiIiIiIIIIIIIiIiiIIIIiIIC&+++&+ +++&+O
5 IiIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIC++++++ +++++O
4 -_-----__---_-------_-----_-_-_---++++++-+&+++_-
3 ----------------------------------++++++-+++++--
2 -----_--------------------------_-++&+++--+++---
1 ------------------------------------------------
0 ________________________________________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | RESET_B | Internal1 | Internal2 | Internal3 | Q |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | X | X | X | X | X |   | X |
| PMOS1 |   |   | X |   |   |   |   |
| PMOS2 |   |   | X |   | X |   |   |
| PMOS3 | X |   | X |   |   |   |   |
| PMOS4 | X |   | X | X |   | X |   |
| Poly1 | X | X | X |   | X | X |   |
| Poly2 | X | X | X | X |   |   |   |
| Poly3 | X | X |   | X |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 | O | O | O |
| PMOS1 | O |   |   |
| PMOS2 | O |   |   |
| PMOS3 | O |   |   |
| PMOS4 | O | O | O |
