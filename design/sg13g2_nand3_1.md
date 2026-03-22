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
2 G G GG G
1 G G GG G
0 G G GG G
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
2  +& &+
1  + O + O
0  + o + o
9  + OOOOO
8      o
7  I I OII
6  I I oIi
5      O
4  _   oOo
3  -     O
2  _
1  -
0 -_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | B | C | Y | VDD | VSS |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   | X |
| NMOS2 |   |   |   | X |   | X |
| PMOS1 |   |   |   |   | X |   |
| PMOS2 |   |   |   | X | X |   |
| Polysilicon | X |   |   | X | X |   |

## Silicon Neighbourhood

| Silicon | Overlaps With |
| --- | --- |
| NMOS | Polysilicon |
| PMOS | Polysilicon |
