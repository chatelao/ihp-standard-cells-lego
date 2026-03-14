# Design Documentation for sg13g2_einvn_8

## Substrate
```
  012345678901234567890123456789012345678
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678
3
2  XpppppXpppXpppXppXppppppppppppppppppp
1  XpppppXpppXpppXppXppppppppppppppppppp
0  XpppppXpppXpppXppXppppppppppppppppppp
9  X     X   X   X       X   X   X   X
8  X     X   X   X       XXXXXXXXXXXXX
7
6  X                              X
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  XnnnnnnXnnnXnnnXnnXnnnnnnnnnnnXnnnXnn
2  XnnnnnnXnnnXnnnXnnXnnnnnnnnnnnnnnnnnn
1  XnnnnnnXnnnXnnnXnnXnnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456789012345678
3
2  X     X   X   X  X             G
1  X     X   X   X  X             G
0  X     X   X   X  X             G
9  X     X   X   X       X   X   XG  X
8  X     X   X   X       XXXXXXXXXXXXX
7  G                              G
6  X                              X
5  G                              G
4  G                              G
3  X      X   X   X  X           XG  X
2  X      X   X   X  X            G
1  X      X   X   X  X            G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234567890123456789012345678
3 +++++++++++++++++++++++++++++++++++++++
2  x     x   x   x  x
1  x C C x C x C x Cx  CCCCCCCCCCCCCCCC
0  x C C x C x C x Cx  C   C   C   C  C
9  x C C x C x C x C   C x   x C x   xC
8  x C C x C x C x CCCCC xxxxxxxxxxxxxC
7    C CCCCCCCCCCCCC     OOO
6  x C  CCCCCCCCCCCCCCCC OOO  IIIIxIII
5  I CCCC   C   C   C  C OOO
4    CCCC - C - C - C  C OOOOOOOOOOOOOC
3  x CCCC x C x C x Cx C         x   xC
2  x CCCC x C x C x Cx CCCCCCCCCCCCCCCC
1  x      x   x   x  x
0 ---------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234567890123456789012345678
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
