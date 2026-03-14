# Design Documentation for sg13g2_xnor2_1

## Substrate
```
  012345678901234
5 NNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234
5
4  ppppppppppppp
3  ppppppppppppp
2  ppppppppppXpp
1
0
9
8         X
7      XXX X
6          X
5  nnnnnnnnnnnnn
4  nnnnnnnnnnnnX
3  nnnnnnnnnnnnX
2  nnnnnnnnnnnnX
1  nnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234
5
4        G G
3        G G
2        G G X
1        G G
0        G G
9        G G
8        GXG
7      XXX X
6        G X
5        G G
4        G G   X
3        G G   X
2        G G   X
1        G G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234
5 +++++++++++++++
4
3
2            x
1     C      O
0     C      O
9    CC      O
8    C  IIxI OOOO
7    C xxx x    O
6    C III x  C O
5    C CCCCCCCC O
4    C C       xO
3    CCC CCCCC xO
2              xO
1
0 ---------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234
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
