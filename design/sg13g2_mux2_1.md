# Design Documentation for sg13g2_mux2_1

## Substrate
```
  0123456789012345678
5 NNNNNNNNNNNNNNNNNNN
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
5
4  ppppppppppppppppp
3  ppppppppppppppppp
2  ppppppppppppppppp
1
0
9
8
7
6
5  nnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678
5
4   G     G  G
3   G     G  G
2   G     G  G
1   G     G  G
0   G     G  G
9   G     G  G
8   G     G  G
7   G     G  G
6   G     G  G
5   G     G  G
4   G     G  G
3   G     G  G
2   G     G  G
1   G     G  G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678
5 +++++++++++++++++++
4
3
2       CCCCCCCC  xx
1       C  C   C  OO
0  CCCCCC  C   C  OO
9  C     CCC   C  OO
8  C   CCC     C  OO
7  C   C  xI I C   O
6  CxI CxIII x CC CO
5  C   C x   I    Cx
4  C   C IIxII CCCCx
3  C   C       C   x
2      CCCCCCCCC   x
1
0 -------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345678
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
