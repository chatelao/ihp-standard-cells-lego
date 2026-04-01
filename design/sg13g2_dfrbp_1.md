# Design Documentation for sg13g2_dfrbp_1

## Substrate
```
  0123456789012345678901234567890123456789012345678901
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456789012345678901
4 pppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNpppppppNppppppppppppppppNNNNNNNN
2 ppppppppNNNNNNNNNNNNpppppppNppppppppppppppppNNNNNNNN
1 ppppppppppppppppppNNpppppppNppppppppppppppppNNNNNNNN
0 ppppppppppppppppppNNpppppppNppppppppppppppppNNNNNNNN
9 ppppppppNNNNNNNNNNNNpppppppNppppppppppppppppNNNNNNNN
8 NppppppNNNNNNNNNNNNNpppppppNppppppppppppppppNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 NppppppNNNNNpppppppNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
5 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901
4
3     GGGGGGGGGGGGGGG
2  G GGGGGGGGGGGGGGGGGGGG GGGGGGG G G GGGGGGGGGGG
1  G GGGGGGGGGGGGGGGGGGGG GGGGGGG G G GGGGGGGGGGG
0  G GGGGGGGGGGGGGGGGGGGG GGGGGGGGG G GGGGGGGGGGG
9  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGG GGGGGGGGGGGGG
8  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGG GGGGGGGGGGGGG
7  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGG GGGGGGGGGGGGG
6  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGG GGGGGGGGGGGGG
5  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGG GGGGGGGGGGGGG
4  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGG GGGGGGGGGGGGG
3  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGG GGGGGGGGGGGGG
2  GGGGGGGGGGGGGGGGGGGGGG GGG G GGG GGGGGGGGGGGGG
1     GGGGGGGGGGGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456789012345678901
4 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
3 ++++++++++++++++++++++++++++++++++++++++++++++++++++
2 +++&++++++&+++++++&+++++++++++++++++&+++++&+&+&+++++
1 +++++++++++++++++++++++++++++++++++++++++++++++++&++
0 +++++++&&+++++&+&+++&+++++++++++++++++++++&+&+&++&++
9 +++++++++++++++++++++++++++++++++++++++++++++++++&++
8 +&+&++++++++++++++&+&+++++&+&+++&+++++&+++&+&+&++&++
7 IiIIIIIIiiIIIIIIIIIIIIIIIIIIIIIIIC------- OO ++++OO
6 IiIIIiIIiiiIiIiIIIIIIIiIiiIIIIiIIC_---_-- OO +++&OO
5 IiIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIC------- oO ++++OO
4 -_-----__---_-------_-----_-_-_---------_-_--+&++---
3 ---------------------------------------------++++---
2 -----_--------------------------_---_-_------+&++---
1 ----------------------------------------------------
0 ____________________________________________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | RESET_B | Internal1 | Internal2 | Internal3 | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | X | X | X | X | X |   | X |
| PMOS1 |   |   | X |   |   |   |   |
| PMOS2 |   |   | X |   | X |   |   |
| PMOS3 | X |   | X |   |   |   |   |
| PMOS4 | X | X | X | X |   | X | X |
| Poly1 | X | X | X |   | X | X |   |
| Poly2 | X | X | X | X |   |   |   |
| Poly3 | X | X |   | X |   | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 | O | O | O |
| PMOS1 | O |   |   |
| PMOS2 | O |   |   |
| PMOS3 | O |   |   |
| PMOS4 | O | O | O |
