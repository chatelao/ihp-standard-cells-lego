# Design Documentation for sg13g2_buf_4

## Substrate
```
  01234567890123
4 SSSSSSSSSSSSSS
3 NNNNNNNNNNNNNN
2 NNNNNNNNNNNNNN
1 NNNNNNNNNNNNNN
0 NNNNNNNNNNNNNN
9 NNNNNNNNNNNNNN
8 NNNNNNNNNNNNNN
7 NNNNNNNNNNNNNN
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 NNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123
4 pppppppppppppp
3
2
1  pppppppp
0  pppppppppppp
9  pppppppppppp
8  pppppppppppp
7
6
5
4  nnnnnnnnnnnn
3  nnnnnnnnnnnn
2
1
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123
4
3
2   G
1   G
0   G
9   G
8   G
7   G       GG
6   GGGGGGG GG
5   G
4   G
3   G
2   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &+&+&+&+&+&+&+
3  +   +  +   +
2  & c & c+   +
1  + O + O+   +
0  & o & o& c &
9  + O   O+ C
8  & oOOOo& cCC
7    O      II
6  OOO  CcC iI
5    O    C
4  _ oOOOoCCCCc
3  - O - O -- C
2  _ c _ cc-c c
1  -   -   -
0 _-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Internal1 | Internal2 | Output1 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X |   | X |   | X |
| PMOS1 | X |   |   |   | X | X |
| PMOS2 | X |   |   |   |   |   |
| Poly1 |   |   |   | X |   |   |
| Poly2 |   |   | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| PMOS1 | O | S |
| PMOS2 |   |   |
