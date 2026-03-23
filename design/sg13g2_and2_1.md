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
2 ppppppppp
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
2   G
1   G
0   G
9 G G G
8 G G G
7 G G G
6 GGGGGG
5 G G G
4 G G
3 GGG
2 G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3  +   +
2 &+Cc&+ oo
1  +CC + OO
0 &+Cc&+ oo
9   CC   OO
8 CcCcCc oo
7 CC   CC O
6 Cc i cC O
5 CC      O
4 Cc   _ oo
3 IiI  - OO
2 III  _
1      -
0 -_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | B | VSS | X | VDD |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |
| NMOS2 |   |   | X | X |   |
| PMOS1 |   |   | X | X | X |
| PMOS2 |   |   |   |   | X |
| Poly1 | X | X | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |
