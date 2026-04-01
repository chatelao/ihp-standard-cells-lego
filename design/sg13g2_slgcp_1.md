# Design Documentation for sg13g2_slgcp_1

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
3 NNNNNNNNNNNNNNNNNNNppppppppppN
2 NNNNNNNpppNNNNNNNNNppppppppppN
1 NppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppN
7 NppppppppNNppppppppNNNNNNNNNNN
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
3       GGGGGGGG
2  GG G GGGGGGGGGGGG  GGGGGGGG
1  GG G GGGGGGGGGGGG  GGGGGGGG
0  GG G GGGGGGGGGGGG  GGGGGGGG
9  GG G GGGGGGGGGGGG  GGGGGGGG
8  GG GGGGGGGGGGGGGG  GGGGGGGG
7  GG G GGGGGGGGGGGG  GGGGGGGG
6  GG G GGGGGGGGGGGG  GGGGGGGG
5  GG G GGGGGGGGGGGG  GGGGGGGG
4  GG G GGGGGGGGGGGG  GGGGGGGG
3  GG G GGGGGGGGGGGG  GGGGGGGG
2  G  G GGGGGGGGGGGG  GGGGGGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789
4 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
3 ++++++++++++++++++++++++++++++
2 +++&++++++++++++++++++++++++++
1 ++++++++++++++++++++++++++++&+
0 +++++&+&++&+&+++&+&+++++&+++&+
9 +++++++++------------+++++++&+
8   IiiiIIi-_-_-_---_-_III&+&+o
7  iIIIIIII------------iII++++O
6  iIIIIIII-_-----_---_iII++&+O
5 ------------------------------
4 ---_--------_-----_-_---_---_-
3 ------------------------------
2 ---_----------_-----_-------_-
1 ------------------------------
0 ______________________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | CLK | GATE | Internal1 | GCLK |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | X | X | X | X |   | X |
| PMOS1 | X | X | X | X | X | X |
| Poly1 |   |   |   | X |   |   |
| Poly2 | X | X | X | X | X |   |
| Poly3 | X | X | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 | O | O | O |
| PMOS1 | O | O | O |
