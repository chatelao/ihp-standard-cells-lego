# Design Documentation for sg13g2_nand2b_1

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
2 pppppppNN
1 ppppppNNN
0 ppppppNpN
9 ppppppNNN
8 ppppppNpN
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 nnnnnnSnS
3 nnnnnnSSS
2 nnnnnnSSS
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
6 GGGGG
5 G G G
4 G G G
3 G G G
2 G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3    +  +
2    +  &
1    +O +
0  C +OoOo
9  CCCCC O
8      C o
7      C O
6  I I cCO
5  CCCCC O
4  C    Oo
3    -  OO
2    _
1    -
0 -_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | Y | VDD | VSS |
| --- | --- | --- | --- |
| NMOS1 |   |   | X |
| NMOS2 |   |   | X |
| NMOS3 | X |   |   |
| PMOS1 | X | X |   |
| PMOS2 | X |   |   |
| PMOS3 | X |   |   |
| PMOS4 |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| NMOS3 |   |
| PMOS1 | O |
| PMOS2 |   |
| PMOS3 |   |
| PMOS4 |   |
