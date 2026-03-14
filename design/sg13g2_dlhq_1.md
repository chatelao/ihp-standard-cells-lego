# Design Documentation for sg13g2_dlhq_1

## Substrate
```
  012345678901234567890123456789
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789
3
2  XpppppXpppppppppppXppppppXpp
1  XppppppppppppppppppppppppXpX
0  XppppppppppppppppppppppppXpX
9  X                        X X
8                           X X
7
6   X                     X
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  XnnnnnXnnnnnnnnnnnnnnnnnnnnX
2  XnnnnnXnnnnnnnnnnnnnnnnnnnnX
1  XnnnnnXnnnnnnnnnnnnXnnnnnXnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456789
3
2  XG    X           X    G X
1  XG                     G X X
0  XG                     G X X
9  XG                     G X X
8   G                     G X X
7   G                     G
6   X                     X
5   G                     G
4   G                     G
3  XG    X                G   X
2  XG    X                G   X
1  XG    X            X   G X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234567890123456789
3 ++++++++++++++++++++++++++++++
2  x     x           x      x
1  x CCC   CC CCC           x x
0  x CCCCCCCCCC CCCCCCCCCCC x x
9  x CCC  CCC   CCCCCCCCCCC x x
8     CC  C CCC CC     CCCC x x
7  II C     C  CCC CC  CCC    O
6  Ix C CCC CCC CC  C  CCCxICCO
5  II C C  CCCC     C  C C  C O
4     C C- CC CCCCC C  C C  C O
3  x CCCCx   CCCC   C    CCCC x
2  x     x CCCCCCCCCCCCCCC    x
1  x     x            x     x
0 ------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234567890123456789
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
