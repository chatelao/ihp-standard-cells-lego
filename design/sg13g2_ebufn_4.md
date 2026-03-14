# Design Documentation for sg13g2_ebufn_4

## Substrate
```
  01234567890123456789012345678
5 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678
5
4  ppppppppppppppppppppppppppp
3  ppppppppppppppppppppppppppp
2  ppppppppppppppppppppppppppp
1
0
9
8     X
7    X
6       X
5  nnnnXnnnnnnnnnnnnnnXXXXXXnn
4  nnnnnnnnnnnnnnnnnnnXnnnXXnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678
5
4     G G
3     G G
2     G G
1     G G
0     G G
9     G G
8     X G
7    XG G
6     G X
5     GXG             XXXXXX
4     G G             X   XX
3     G G
2     G G
1     G G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456789012345678
5 +++++++++++++++++++++++++++++
4
3                   CCCCCCCCC
2  CC       C   C   C   C   C
1  CC       C   C   C   C   C
0  CCCCCCCC CCCCC   C O C OOC
9  C    C CCCCC C   C O   OOC
8  C Ix CCC   C CCCCC OOOOOO
7  C x    C   CCCCCCCCCCCC O
6  C I Ix C           CCCC O
5  C   x  C CCCCCCCCC xxxxxx
4  C   I  C C   C   C x   xxC
3  C      C C   C   C       C
2  C   CCCC C   C   CCCCCCCCC
1
0 -----------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012345678
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
