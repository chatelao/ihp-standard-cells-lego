# Design Documentation for sg13g2_dlhq_1

## Substrate
```
  012345678901234567890123456789
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789
4 pppppppppppppppppppppppppppppp
3 pppppppppppppppppppppppppppppp
2 pppppppppppppppppppppppppppppp
1 pppppppppppppppppppppppppppppp
0 pppppppppppppppppppppppppppppp
9 pppppppppppppppppppppppppppppp
8 pppppppppppppppppppppppppppppp
7 pppppppppppppppppppppppppppppp
6 NppppppppNNNNNNNNNNNNNNNNNNNNN
5 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789
4
3
2  GGGGGG G  GGGG GGG G G G GG
1  GGGGGG G  GGGGGGGGGGGG GGGG
0  GGGGGGGGGGGGGGGGGGGGGGGGGGG
9  GGGGGGGGGGGGGGGGGGGGGGGGGGG
8  GGGGGGGGGGGGGGGGGGGGGGGGGGG
7  GGGGGGGGGGGGGGGGGGGGGGGGGGG
6  GGGGGGGGGGGGGGGGGGGGGGGGGGG
5  GGGGGGGGGGGGGGGGGGGGGGGGGGG
4  GGGGGGGGGGGGGGGGGGGGGGGGGGG
3  GGGGGGGGGGGGGGGGGGGGGGGGGGG
2  GGGGGG GG  GGGGGGGGGGGGGGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789
4 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
3 ++++++++++++++++++++++++++++++
2 +++&+&++&+&+++&+++&+++++++++++
1 ++++++++++++++++++++++++++++&+
0 +++&+&++++++++++++++++++&+++&+
9 ++++++++++++++++++++++++++++&+
8 ++++++++++++&+++&+++&+++&+++&+
7  iiIII   IIIIIIIIIIIIIIIiiIIO
6  iiiI-------_-_IIIIIIIiIiiiIO
5 ------------------------------
4 -_-_-_--_---_-_-_-_-----_---_-
3 ------------------------------
2 ------------------_-_-----_---
1 ------------------------------
0 ______________________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | D | GATE | Internal1 | Internal2 | Q |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X | X | X | X | X |
| PMOS1 | X |   | X | X | X | X | X |
| Poly1 | X | X | X | X | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 | O |
| PMOS1 | O |
