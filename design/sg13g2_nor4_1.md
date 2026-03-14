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
4
3
2  ppppppppp
1  ppppppppp
0  ppppppppp
9  ppppppppp
8  ppppppppp
7
6
5
4  nnnnnnnnn
3  nnnnnnnnn
2  nnnnnnnnn
1
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890
4
3   G G G G
2   G G G G
1   G G G G
0   G G G G
9   G G G G
8   G G G G
7   G G G G
6  GG GGG GG
5   G G G G
4   G G G G
3   G G G G
2   G G G G
1   G G G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
4 &+&+&+&+&+&
3  +
2  +
1  +      oo
0  +      oo
9  +      oo
8          o
7          O
6  i   i   i
5          O
4  - ooooooo
3  - o - o -
2  -   -   -
1  -   -   -
0 -_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

## Metal 2
```
  01234567890
4
3
2
1
0
9
8
7
6
5
4
3
2
1
0
```
Legend: M=Metal 2
