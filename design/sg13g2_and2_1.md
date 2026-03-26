# Design Documentation for sg13g2_and2_1

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
2 G G G
1 G G G
0 G G G
9 G G G
8 G G G
7 G G G
6 G GGG  GG
5 G G G
4 G G G
3 GGG G
2 GGG G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3 +++++++++
2 &+  &+
1  + C++OOO
0  + c&+Ooo
9    C  OOO
8  cCcCcOoo
7  C IICCOO
6  c iIcCoo
5  C    OOO
4  c   cOoo
3 IiI   OOO
2 IiI  c
1
0  c c c c
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | VSS2 | VSS3 | VSS4 | VSS5 | VSS6 | A | B | X |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X | X | X | X |   |   |   |   |   |
| NMOS2 |   | X |   |   |   |   | X | X | X |   | X |
| PMOS1 | X | X |   |   |   |   |   |   |   |   | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |   |
| Poly1 | X |   |   |   |   |   |   |   | X | X |   |
| Poly2 |   |   |   |   |   |   |   |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| PMOS1 | O |   |
| PMOS2 |   |   |
