# Design Documentation for sg13g2_and3_1

## Substrate
```
  012345678901
4 NNNNNNNNNNNN
3 NNNNNNNNNNNN
2 NNNNNNNNNNNN
1 NNNNNNNNNNNN
0 NNNNNNNNNNNN
9 NNNNNNNNNNNN
8 NNNNNNNNNNNN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SSSSSSSSSSSS
3 SSSSSSSSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 SSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901
4 pppppppppppp
3 NNNNNNNNNNNN
2 NppppppppppN
1 NppppppppppN
0 NppppppppppN
9 NppppppppppN
8 NppppppppppN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SnnnnnnnnnnS
3 SnnnnnnnnnnS
2 SnnnnnnnnnnS
1 SSSSSSSSSSSS
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901
4
3
2     G G G
1     G G G
0     G G G
9     G G G
8     G G G
7     G G G
6     GGGGG
5     G G G
4     GGG G
3     G G G
2  G GGGG G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &+&+&+&+&+&+
3    ++  +++
2    &+  &&+
1  CC++C +++OO
0  cC&+c &&+oO
9  CC  C    OO
8  cCcCcCcc  O
7  CC IIIICC O
6  cC IiIicC O
5  CC      OOO
4  cC Ii _ OoO
3  IIIII - O
2  iIiIi _
1        -
0 _-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | A | C | X |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X | X | X |   | X |
| PMOS1 | X |   | X |   |   | X |
| PMOS2 | X |   |   |   |   |   |
| Poly1 |   |   |   | X |   |   |
| Poly2 | X |   | X | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 |   | O |
| PMOS2 |   |   |
