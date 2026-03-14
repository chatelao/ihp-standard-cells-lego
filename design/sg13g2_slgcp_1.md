# Design Documentation for sg13g2_slgcp_1

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
2  XpppppXppppppppXpppppppppXpp
1  XpppppXppppppppXpppppppppXpX
0  XppppppppppppppXpppppppppXpX
9  X                        X X
8                             X
7  X  X
6                      X
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  XnnnnnnnnnnnnnnnnnnnXnnnnXnX
2  XnnnnnnnnnnnnnXnnnnnXnnnnXnX
1  XnnnXnnnnnnnnnXnnnnnXnnnnXnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456789
3
2  X  G  X        X    G    X
1  X  G  X        X    G    X X
0  X  G           X    G    X X
9  X  G                G    X X
8  G  G                G      X
7  X  X                G
6  G  G                X
5  G  G                G
4  G  G                G
3  X  G                X    X X
2  X  G          X     X    X X
1  X  GX         X     X    X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234567890123456789
3 ++++++++++++++++++++++++++++++
2  x     x        x         x
1  x   C x        x CCCCC   x x
0  x   CCCCCCC C  x C   C C x x
9  x    C    C C    C   CCC x x
8       C  C C CCCCCCCC  CC   x
7  x IxIC CCCC C    CC   CCC  O
6  I  CCC C CCCCCCC CC x C CCCO
5     C   CCC C     CC   C C  O
4     C  CC C C CCC CC -  CC  O
3  x CCCCCCCCCC C CCCC x  CCx x
2  x       CCCCCCxCCCC x    x x
1  x   x         x     x    x
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
