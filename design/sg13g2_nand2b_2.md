# Design Documentation for sg13g2_nand2b_2

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
2 pppNppppppppppN
1 NpppppppppppppN
0 ppppppppppppppN
9 NpppppppppppppN
8 NpppppppppppppN
7 SSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSS
4 SnnnSnnnnnnnnnS
3 SnnnnnnnnnnnnnS
2 SnnnSnnnnnnnnnS
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
6 GGG GGG G G
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
3 +   +   +   +
2 &   &   &   &
1 +   + O + O +
0 & Cc& Oo& o &
9 + C + OOOOO +
8    c&   o o
7    C      O
6  I cCIIIiIo
5    C      O
4 - CcCcCcc o c
3 -   C - C   C
2 -_    -_cCcCc
1 -     -
0 -_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)
