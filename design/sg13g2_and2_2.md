# Design Documentation for sg13g2_and2_2

## Substrate
```
  01234567890
5 NNNNNNNNNNN
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
5
4  ppppppppp
3  ppppppppp
2  ppppppXXp
1
0
9
8
7
6     X
5  nnnnnnnXn
4  nnnnnnXXn
3  XnnnnnXXn
2  nnnnnnnnn
1  nnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890
5
4 G GG G
3 G GG G
2 G GG G XX
1 G GG G
0 G GG G
9 G GG G
8 G GG G
7 G GG G
6 G GGXG
5 G GG G  X
4 G GG G XX
3 GXGG G XX
2 G GG G
1 G GG G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890
5 +++++++++++
4
3
2    C   xx
1    C   OO
0    C   OO
9    C   OO
8  CCCCCC O
7  C    C O
6  C Ix C O
5  C      x
4  C     xx
3 IxI    xx
2 III
1
0 -----------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890
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
