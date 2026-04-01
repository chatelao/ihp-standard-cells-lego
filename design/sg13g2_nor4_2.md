# Design Documentation for sg13g2_nor4_2

## Substrate
```
  012345678901234567890
4 SSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSS
9 SSSSSSSSSSSSSSSSSSSSS
8 SSSSSSSSSSSSSSSSSSSSS
7 SSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890
4 ppppppppppppppppppppp
3 SSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSS
1 SnnnnnnnSSSSSSSSSSSSS
0 SnnnnnnnSSSSSSSSSSSSS
9 SnnnnnnnSSSSSSSSSSSSS
8 SnnnnnnnSSSSSSSSSSSSS
7 SnnnnnnnSSSSSSSSSSSSS
6 SnnnnnnnSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  012345678901234567890
4
3
2   GGG  GGG GGG  GGGG
1   GGG  GGG GGG  GGGG
0   GGG  GGG GGG  GGGG
9   GGG  GGG GGG  GGGG
8   GGG  GGG GGG  GGGG
7   GGG  GGG GGG  GGGG
6   GGG  GGG GGG  GGGG
5   GGG  GGG GGG  GGGG
4   GGG  GGG GGG  GGGG
3   GGG  GGG GGG  GGGG
2   GGG  GGG  GG  GGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890
4 &&&&&&&&&&&&&&&&&&&&&
3 +++++++++++++++++++++
2 +++&+++++++++++++++++
1 +++++++++++++++++++++
0 +++&+++&&+&+&+&+&+&+&
9 +++++++++++++++++++++
8 ++++++++++++&+++&+&+&
7   IIIIOOOOOOOOOOOOO
6   iiIIOOioOOioOoiOOc
5 ---------------------
4 ---_-_-__-_-_-_-_-_--
3 ---------------------
2 ---------------------
1 ---------------------
0 _____________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | B | C | D | Internal1 | Y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |
| NMOS2 | X |   | X |   |   |   | X | X |
| PMOS1 | X |   |   |   |   |   |   |   |
| Poly1 | X | X | X |   |   |   |   | X |
| Poly2 | X | X |   | X |   |   | X | X |
| Poly3 | X | X |   |   | X |   | X | X |
| Poly4 | X | X |   |   |   | X |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |
| NMOS2 | O | O |   |   |
| PMOS1 |   |   |   |   |
