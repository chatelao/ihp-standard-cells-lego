# Design Documentation for sg13g2_nor2b_1

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
5 SSSSSSSSS
4 SnnnnnnnS
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
2 G G   G G
1 G G   G G
0 G G   G G
9 G G   G G
8 G G   G G
7 G G   G G
6 GGGG  GGG
5 G G   G
4 G G   G
3 G G   G
2 G G   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3    +
2    +&  o
1 CC +  OO
0 Cc +& Oo
9 CC   OOO
8 CcCcCo o
7    CCO
6  i cCOIi
5 CCCCCO
4 CcCcCo _
3    - O -
2    _ o _
1    -   -
0 -_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | B_N | VSS | Y | VDD |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |
| NMOS2 |   |   | X | X |   |
| PMOS1 |   |   | X | X | X |
| PMOS2 |   |   |   |   | X |
| Poly1 |   | X | X |   |   |
| Poly2 | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O | O |
| PMOS2 |   |   |
