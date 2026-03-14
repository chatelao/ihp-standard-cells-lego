# Design Documentation for sg13g2_mux2_2

## Substrate
```
  01234567890123456789
4 NNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789
4
3  pppppppppppppppppp
2  pppppppppppppppppp
1  ppppppppppppppXXXp
0
9
8
7
6   X     X
5  nnnnnXnnnXnnnnnnXn
4  nnnnnnnXnnnnnnnnXn
3  nnnnnnnnnnnnnnnXXn
2  nnnnnnnnnnnnnnnXXn
1  nnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789
4
3  G G   G G G
2  G G   G G G
1  G G   G G G   XXX
0  G G   G G G
9  G G   G G G
8  G G   G G G
7  G G   G G G
6  GXG   GXG G
5  G G  XG GXG     X
4  G G   GXG G     X
3  G G   G G G    XX
2  G G   G G G    XX
1  G G   G G G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456789
4 ++++++++++++++++++++
3
2       CCCCCCC
1       C     C  xxx
0  C    C CC  C  OOO
9  CCCCCCCCC  C  OOO
8  C   CCC    C  OOO
7  C   C      C    O
6  CxI C  x I CC C O
5  C   Cx I x    C x
4  C   CIIxII CCCC x
3  C   C      C   xx
2      CCCCCCCC   xx
1
0 --------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789
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
