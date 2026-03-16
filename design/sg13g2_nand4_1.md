# Design Documentation for sg13g2_nand4_1

## Substrate
```
  01234567890
4 NNNNNNNNNNN
3 NNNNNNNNNNN
2 NNNNNNNNNNN
1 NNNNNNNNNNN
0 NNNNNNNNNNN
9 NNNNNNNNNNN
8 NNNNNNNNNNN
7 SSSSSSSSSSS
6 SSSSSSSSSSS
5 SSSSSSSSSSS
4 SSSSSSSSSSS
3 SSSSSSSSSSS
2 SSSSSSSSSSS
1 SSSSSSSSSSS
0 SSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890
4 ppppppppppp
3 NNNNNNNNNNN
2 NpppppppppN
1 NpppppppppN
0 NpppppppppN
9 NpppppppppN
8 NpppppppppN
7 SSSSSSSSSSS
6 SSSSSSSSSSS
5 SSSSSSSSSSS
4 SnnnnnnnnnS
3 SnnnnnnnnnS
2 SnnnnnnnnnS
1 SSSSSSSSSSS
0 nnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890
4
3 G G G G G
2 G G G G G
1 G G G G G
0 G G G G G
9 G G G G G
8 G G G G G
7 G G G G G
6 GGGGGGGGG
5 G G G G G
4 G G G G G
3 G G G G G
2 G G G G G
1 G G G G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
4 &+&+&+&+&+&
3  +   +   +
2  +   +   +
1  + o + o +
0  + o + o +
9  + ooooooo
8          o
7          O
6  i i i i O
5      I I O
4  -     I o
3  -     I o
2  -
1  -
0 -_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

