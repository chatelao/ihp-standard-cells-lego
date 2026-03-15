# Design Documentation for sg13g2_nor4_1

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
4 NNNNNNNNNNN
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
0 SSSSSSSSSSS
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890
4
3   GG  GG
2   GG  GG
1   GG  GG
0   GG  GG
9   GG  GG
8   GG  GG
7   GG  GG
6  GGGGGGGG
5   GG  GG
4   GG  GG
3   GG  GG
2   GG  GG
1   GG  GG
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
4 &+&+&+&+&+&
3  +
2  &
1  +      OO
0  &     IOo
9  +     IOO
8      I I o
7  I I I IIO
6  i Iii IiO
5          O
4  - OoOoOoO
3  - O - O -
2  -   -   -
1  -   -   -
0 -_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

