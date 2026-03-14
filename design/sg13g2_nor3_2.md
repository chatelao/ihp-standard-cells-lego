# Design Documentation for sg13g2_nor3_2

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
2  ppppppppppppppp
1
0
9
8
7
6    X  XX     XX
5  nnXXXXXXXnXXXnn
4  nnXnnnnnXnnnXnn
3  nnXnnnnnXnnnXnn
2  nnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456
5
4   G GG G     G G
3   G GG G     G G
2   G GG G     G G
1   G GG G     G G
0   G GG G     G G
9   G GG G     G G
8   G GG G     G G
7   G GG G     G G
6   GXGGXX     XXG
5   GXXXXXXX XXX G
4   GXGG G X   X G
3   GXGG G X   X G
2   G GG G     G G
1   G GG G     G G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456
5 +++++++++++++++++
4
3
2    C   CCCCCCCCC
1    C   C   C   C
0    C   C C C O C
9    CCCCCCC   O C
8            OOO
7            O
6   IxI xx OOO xx
5    xxxxxxx xxx
4    x     x   x
3    x     x   x
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
