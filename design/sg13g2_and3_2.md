# Design Documentation for sg13g2_and3_2

## Substrate
```
  0123456789012
4 NNNNNNNNNNNN
3 NNNNNNNNNNNN
2 NNNNNNNNNNNN
1 NNNNNNNNNNNN
0 NNNNNNNNNNNN
9 NNNNNNNNNNNN
8 NNNNNNNNNNNN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SSSSSSSSSSSS
3 SSSSSSSSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 SSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012
4
3
2  pppppppppp
1  pppppppppp
0  pppppppppp
9  pppppppppp
8  pppppppppp
7
6
5
4  nnnnnnnnnn
3  nnnnnnnnnn
2  nnnnnnnnnn
1
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012
4
3   G G G G G G
2   G G G G G G
1   G G G G G G
0   G G G G G G
9   G G G G G G
8   G G G G G G
7   G G G G G G
6   GGG GGG GGG
5   G G G G G G
4   G G G G G G
3   G G G G G G
2   G G G G G G
1   G G G G G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012
4 &+&+&+&+&+&+
3    +   +   +
2    +   +   +
1   C+ C + o +
0   C+ C + oo
9   C  C    o
8   CCCCCCC o
7   C     C O
6   Ci   i  Oi
5   C      OO
4        - o -
3        - o -
2        -   -
1        -   -
0 -_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

## Metal 2
```
  0123456789012
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
