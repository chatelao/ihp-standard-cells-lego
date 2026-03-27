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
2 NpppppppN
1 NpppppppN
0 Npppppppp
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
2       G G
1       G G
0       G G
9       G G
8       G G
7       G G
6    G  GGG
5       G G
4       G G
3       G G
2       G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3 +++++++++
2 +&   &+
1 ++   ++ C
0 +& cC  cc
9   C  C CC
8  c oO   c
7   OOO II
6    oO Ii
5  -- O   C
4  _- O  cc
3  --  -- C
2  _-  _-
1 ---------
0 _-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | X |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 |   | X |   | X |
| PMOS1 | X |   |   | X |
| PMOS2 | X |   |   |   |
| Poly1 |   |   | X | X |
| Poly2 |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| PMOS1 | O |   |
| PMOS2 |   |   |
