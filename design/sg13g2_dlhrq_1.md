# Design Documentation for sg13g2_dlhrq_1

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
2  ppXppppppXpppppppXpppXppp
1  ppXppppppXpppppppXpppXpXX
0  pppppppppppppppppppppXpXX
9                       X XX
8                       X XX
7
6  X  X                X
5  nnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnXnXX
2  nnnXnnnnnXnnnnnnXnnnnXnnn
1  nnnXnnnnnXnnnnnnXnnnnXnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456
3
2  G XG     X       X  GX
1  G XG     X       X  GX XX
0  G  G                GX XX
9  G  G                GX XX
8  G  G                GX XX
7  G  G                G
6  X  X                X
5  G  G                G
4  G  G                G
3  G  G                GX XX
2  G  X     X      X   GX
1  G  X     X      X   GX
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234567890123456
3 +++++++++++++++++++++++++++
2    x      x CCCC  x   x
1  C x      x C  C  x C x xx
0  CCCCCCCCCC CC C    C x xx
9  CCC      C CC C CCCC x xx
8    C CC C C CC C CCCC x xx
7    C  C C CCCCCCCCC C    O
6  x CxICCC CCC CC  C Cx C O
5    C  C CCCCC CC    C  C O
4  CCC  C       CC   CCCCC O
3  C    CCCCCCCCCC   C  x xx
2     x C   x CCCC x C  x
1     x     x      x    x
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
