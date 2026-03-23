# Design Documentation for sg13g2_buf_2

## Substrate
```
  012345678
4 NNNNNNNNN
3 NNNNNNNNN
2 NNNNNNNNN
1 NNNNNNNNN
0 NNNNNNNNN
9 NNNNNNNNN
8 NNNNNNNNN
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 SSSSSSSSS
3 SSSSSSSSS
2 SSSSSSSSS
1 SSSSSSSSS
0 SSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678
4 ppppppppp
3 NNNNNNNNN
2 ppppppppN
1 NpppppppN
0 ppppppppp
9 NpppppppN
8 Npppppppp
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 Snnnnnnnn
3 SnnnnnnnS
2 SnnnnnnnS
1 SSSSSSSSS
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678
4
3
2         G
1         G
0       G
9       G G
8       G
7       G G
6  G   GGGG
5       G G
4
3         G
2         G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3  +    +
2 &+    &
1  +    +CC
0 &+CcCcCcc
9 CCCCCCCCC
8 CcCoOc cc
7 CC  OC
6 CcOOOcIi
5     OCCCC
4  _-oO_Ccc
3   - O -CC
2  _-o _-
1   -   -
0 -_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | VSS | X | VDD |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 |   | X | X |   |
| PMOS1 |   | X | X | X |
| PMOS2 |   |   |   | X |
| Poly2 | X | X |   |   |
| Poly3 |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |
| NMOS2 | SE | N |   |   |   |
| PMOS1 |   | O |   | NSE | NE |
| PMOS2 |   |   |   |   |   |
