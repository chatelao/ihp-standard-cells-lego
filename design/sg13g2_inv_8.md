# Design Documentation for sg13g2_inv_8

## Substrate
```
  012345678901234567
4 SSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567
4 pppppppppppppppppp
3
2
1  pppppppppppppppp
0  pppppppppppppppp
9  pppppppppppppppp
8  pppppppppppppppp
7
6
5
4  nnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnn
2
1
0 nnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567
4
3
2            G G G
1            G G G
0            G G G
9            G G G
8            G G G
7   GGGGGGGGGGGGGG
6   GGGGGGGGGGGGGG
5            G G G
4            G G G
3            G G G
2            G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567
4 &+&+&+&+&+&+&+&+&+
3  +   +  +   +   +
2  & c & c& c & c &
1  + O +O + O + O +
0  & o &Oc& o & o &
9  + O  O   O + O +
8  c c   c  o c o c
7           O   O
6    iIiIii OOOOO
5           O   O
4  _ oOOOoOOo _ o _
3  - O -O - O - O -
2  _ c _ c_ c _ c _
1  -   -  -   -   -
0 _-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Output1 | Output2 | Output3 | Output6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |
| NMOS2 |   | X |   | X |   |   |   |
| PMOS1 | X |   |   | X | X | X | X |
| PMOS2 | X |   |   |   |   |   |   |
| Poly1 |   |   | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |
