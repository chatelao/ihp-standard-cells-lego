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
2 ppppppppp
1 ppppppppp
0 ppppppppp
9 ppppppppp
8 ppppppppp
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 nnnnnnnnn
3 nnnnnnnnn
2 nnnnnnnnn
1 SSSSSSSSS
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678
4
3
2 G G G  G
1 G G G  G
0 G G G  G
9 G G GG G
8 G G GG G
7 G G GG G
6 GGGGGGGG
5 G G GG G
4 G G GG G
3 G G GG G
2 G G GG G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3  +   +
2  +   +&
1  + O + O
0  + o + Oo
9  + OOOOO
8    o O
7  I I OII
6  I I OIi
5      O
4  _   OOOo
3  -     O
2  _
1  -
0 -_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | Y | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS2 |   | X |   | X |
| PMOS1 |   | X | X |   |
| PMOS2 |   |   | X |   |
| Poly1 | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |
