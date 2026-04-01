# Design Documentation for sg13g2_nand3b_1

## Substrate
```
  012345678901
4 SSSSSSSSSSSS
3 NNNNNNNSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 SSSSSSSSSSSS
9 SSSSSSSSSSSS
8 SSSSSSSSSSSS
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
3 pppppppnnnnn
2 nnnnnnnnnnnn
1 SSnnnnnnnnnS
0 SSnnnnnnnnnS
9 SSnnnnnnnnnS
8 SSnnnnnnnnnS
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSnnnnnnnnnS
4 Snnnnnnnnnnn
3 Snnnnnnnnnnn
2 SSnnnnnnnnnS
1 SSSSSSSSSSSS
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  012345678901
4
3
2    G GGG GG
1   GG GGG GG
0   GG GGG GG
9   GG GGG GG
8   GG GGG GG
7   GG GGG GG
6   GG GGG GG
5   GG GGG GG
4   GG GGG GG
3   GG GGG GG
2    G GGG GG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &&&&&&&&&&&&
3 ++++++++++++
2 +++++&++++++
1 ++++++++++&&
0 +++&+&+&++&&
9 ++++++++++&&
8 +++&+++&++&+
7  OOiIiOoOOOO
6  OOiIiOiOOoO
5  OOIIIOOOOOO
4  OOIIIOOOOoO
3 ------------
2 ---_--------
1 ------------
0 ____________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | B | C | Y |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 |   | X |   |   | X |
| NMOS3 | X |   |   |   | X |
| PMOS1 | X |   |   |   |   |
| Poly1 | X | X |   | X | X |
| Poly2 | X |   | X | X | X |
| Poly3 | X |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | O | O |
| NMOS3 | O | O | O |
| PMOS1 | S | S |   |
