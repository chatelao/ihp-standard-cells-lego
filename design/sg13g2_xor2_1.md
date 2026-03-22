# Design Documentation for sg13g2_xor2_1

## Substrate
```
  012345678901234
4 NNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234
4 ppppppppppppppp
3 NNNNNNNNNNNNNNN
2 NpppppppppppppN
1 NpppppppppppppN
0 NpppppppppppppN
9 NpppppppppppppN
8 NpppppppppppppN
7 SSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234
4
3 G G G G
2 G G G G
1 G G G G
0 G G G G
9 G G G G
8 G G G G
7 G G G G
6 GGG GGGGG G
5 G G G G
4 G G G G
3 G G G G
2 G G G G
1 G G G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234
4 &+&+&+&+&+&+&+
3   +      +
2   &     &+
1   +  C C + C O
0   &  c ccCcCoO
9   + CCCCCCCC O
8     C  c    oO
7     C       CO
6  IIcCIIiiIi cO
5     C     OOOO
4  _-cC  _  oOo
3  --    -  OO-
2  _-    _    -_
1  --    -    -
0 -_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)
