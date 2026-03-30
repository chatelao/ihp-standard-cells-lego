# Design Documentation for sg13g2_nand3_1

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
0 NpppppppN
9 NpppppppN
8 NpppppppN
7 SSSSSSSSS
6 SSSSSSSSS
5 SnnnnnnnS
4 SnnnnnnnS
3 SnnnnnnnS
2 SSSSSSSSS
1 SSSSSSSSS
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678
4
3
2
1
0
9
8
7
6  G G   G
5
4
3
2
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 +++++++++
3  +   +
2  +&O&+ O
1  + O + O
0  +oO +oO
9  + OOOOO
8     oO
7  I IIOII
6  i iIoIi
5      O
4  -   OoO
3  -     O
2  -_ _
1  -
0 ---------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | A | B | C | Y |
| --- | --- | --- | --- | --- | --- |
| NMOS2 |   |   |   |   | X |
| PMOS1 | X |   |   |   | X |
| Poly1 |   |   |   | X |   |
| Poly2 |   |   | X |   |   |
| Poly3 |   | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | N | N | N |
| PMOS1 |   |   |   |
| PMOS2 |   |   |   |
