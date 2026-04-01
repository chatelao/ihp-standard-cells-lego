# Design Documentation for sg13g2_inv_16

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
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppp
3
2
1  pppppppppppppppppppppppppppppppp
0  pppppppppppppppppppppppppppppppp
9  pppppppppppppppppppppppppppppppp
8  pppppppppppppppppppppppppppppppp
7
6
5
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2
1
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123
4
3
2   G G G G          G G G G
1   G G G G          G G G G
0   G G G G          G G G G
9   G G G G          G G G G
8   G G G G          G G G G
7   GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
6   GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
5   G G G G          G G G G
4   G G G G          G G G G
3   G G G G          G G G G
2   G G G G          G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +   +   +   +  +   +   +   +   +
2  & c & cc+c c+c & c & c & c & c &
1  + O + O + O +O + O + O + O + O +
0  & o & oc+cOc+o & o & o & o & o &
9  + O   O   O  O   O   O   O   O +
8  c oOOOoOOoOOOoOOOoOOOoOOOoOOOo c
7    O   O   O  O   O   O   O
6    O   O   O  O   O   O   O   iIi
5    O   O   O  O   O   O   O
4  _ o _ oc-cOc-o _ o _ o _ oOOOo-c
3  - O - O - O -O - O - O - O - O-
2  _ c _ cc-c c-c _ c _ c _ c _ c-c
1  -   -   -   -  -   -   -   -  -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Output1 |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 |   | X |   | X |
| PMOS1 | X |   |   | X |
| PMOS2 | X |   |   |   |
| Poly1 | X | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |
