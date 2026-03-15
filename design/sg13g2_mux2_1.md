# Design Documentation for sg13g2_mux2_1

## Substrate
```
  0123456789012345678
4 NNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678
4 ppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNN
2 NpppppppppppppppppN
1 NpppppppppppppppppN
0 NpppppppppppppppppN
9 NpppppppppppppppppN
8 NpppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678
4
3   G G GGGG
2   G G GGGG
1   G G GGGG
0   G G GGGG
9   G G GGGG
8   G G GGGG
7   G G GGGG
6   GGG GGGG
5   G G GGGG
4   G G GGGG
3   G G GGGG
2   G G GGGG
1   G G GGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678
4 &+&+&+&+&+&+&+&+&+&
3
2       cCcCcCcC
1       C      C  OO
0   cCcCc  C   C  oO
9   C    CCC   C  OO
8   c  CcC     C  oO
7   C  C  II I C   O
6   CiIC iiI I C C O
5   C  C I   I   C O
4   c  C IIIIIcCcCoO
3   C  CCCCCCCC   OO
2
1
0 _-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

