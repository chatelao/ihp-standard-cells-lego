# Design Documentation for sg13g2_and4_2

## Substrate
```
  01234567890123456
5 NNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456
5
4  ppppppppppppppp
3  ppppppppppppppp
2  ppppppppppppXXp
1
0
9
8
7          X
6    X X X
5  nnnnnnnnnnnnnXn
4  nnnnnnnnnnnnXXn
3  nnnnnnnnnnnnXXn
2  nnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456
5
4   G G G G G
3   G G G G G
2   G G G G G  XX
1   G G G G G
0   G G G G G
9   G G G G G
8   G G G G G
7   G G G GXG
6   GXGXGXG G
5   G G G G G   X
4   G G G G G  XX
3   G G G G G  XX
2   G G G G G
1   G G G G G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456
5 +++++++++++++++++
4
3
2     C   C    xx
1     C   C    OO
0     C   C    OO
9  CCCCCCCCCCC OO
8  C         C  O
7  C I I I x C  O
6  C x x x I CC O
5  C I I I      x
4  CC          xx
3  CC          xx
2
1
0 -----------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456
5
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
