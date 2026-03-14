# Design Documentation for sg13g2_einvn_2

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
7   X
6
5  nnnnnnnnnnnnXnX
4  nnnnnnnnnnnnXnn
3  nnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456
5
4  G G          G G
3  G G          G G
2  G G          G G
1  G G          G G
0  G G          G G
9  G G          G G
8  G G          G G
7  GXG          G G
6  G G          G G
5  G G         XGXG
4  G G         XG G
3  G G          G G
2  G G          G G
1  G G          G G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456
5 +++++++++++++++++
4
3           CCCCCC
2     CCCC  CC   C
1     CCCC  CC   C
0     CCCC  CC O C
9      CCCCCCC O C
8  III C       O
7  IxI C       O
6  III CC      O I
5  III C       x x
4      C CCCCC x I
3     CC C  CC
2        C  CCCCCC
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
