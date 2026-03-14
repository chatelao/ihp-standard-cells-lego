# Design Documentation for sg13g2_lgcp_1

## Substrate
```
  012345678901234567890123456
3 NNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456
3
2  ppXppppppppXpppppXpppXppp
1  ppXppppppppXpppppXpppXpXp
0  pppppppppppppppppXpppXpXp
9                       X X
8                       X X
7      X           X
6                   X
5  nnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnXXnnnnXnnnnnXXn
2  nnXnnnnnnnnXnnnnXnnnnnXXn
1  nnXnnnnnnnnXnnnnXnnnnnXnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456
3
2    X G      X     X   X
1    X G      X     X   X X
0      G            X   X X
9      G            G   X X
8      G            G   X X
7      X           XG
6      G            X
5      G            G
4      G            G
3      G     XX    XG    XX
2    X G      X    XG    XX
1    X G      X    XG    X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234567890123456
3 +++++++++++++++++++++++++++
2    x        x     x   x
1  C x        x     x   x x
0  C    CCC   CCCCC xC  x x
9  C CCCCCCCCCC   C  C  x x
8  C C   C    C C CI CCCx x
7  C C x C C  CCC Cx   C  O
6  CCC I C C  CCC CIx  CC O
5  C CCCCC CCCCCC C    C  O
4  CCCC C       C  -  CC -O
3  C   CCCC  xx C  x  CC xx
2  C x CCCCCCCx    x     xx
1    x        x    x     x
0 ---------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234567890123456
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
