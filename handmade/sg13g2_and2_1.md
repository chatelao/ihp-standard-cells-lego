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
3 G G G
2 G G G
1 G G G
0 G G G
9 G G G
8 G G G
7 G G G
6 G GGG
5 G G G
4 G G G
3 GGG G
2 G G G
1 G G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3  +   +
2  & c & oO
1  + C + OO
0  & c & oO
9    C   OO
8  CCCCC oO
7  C   C  O
6  C i c  O
5  c      O
4      - oO
3 III  - OO
2 iIi  - oO
1      -
0 -_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)
