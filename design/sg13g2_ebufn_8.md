# Design Documentation for sg13g2_ebufn_8

## Substrate
```
  01234567890123456789012345678901234567890123
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123
3
2  pppppppppppppppppXppXpppXpppXpppppppppXppp
1  pppppppppppppppppXppXpppXpppppppppppppXppp
0  pXpppXpppXpppXpppppppppppppppppppppppppppp
9   X   X   X   X
8   XXXXXXXXXXXXX
7
6                                      X  X
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nXnnnXnnnXnnnXnnnXnnnXnnXnnnXnnnnnnnnnXnnn
2  nnnnnnnnnnnnnnnnnXnnnXnnXnnnXnnnnnnnnnXnnn
1  nnnnnnnnnnnnnnnnnXnnnXnnXnnnXnnnnnnnnnXnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901234567890123
3
2                   X  X   X   X       G XG
1                   X  X   X           G XG
0   X   X   X   X                      G  G
9   X   X   X   X                      G  G
8   XXXXXXXXXXXXX                      G  G
7                                      G  G
6                                      X  X
5                                      G  G
4                                      G  G
3   X   X   X   X   X   X  X   X       G XG
2                   X   X  X   X       G XG
1                   X   X  X   X       G XG
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456789012345678901234567890123
3 ++++++++++++++++++++++++++++++++++++++++++++
2  CCCCCCCCCCCCCCCC x  x   x   x         x   +
1  C  C   C   C   C x Cx C x C   C       x C +
0  Cx C x C x C x CCCCCCCCCCCCCCCC CCCCCCCCC +
9  Cx   x   x   x                  C       C
8  Cxxxxxxxxxxxxx CCCCCCCCCCCCCCCCCCCCCC   CCC
7    O            C                 C        C
6    O  CCCCCCCCCCC CCCCCCCCCCCCCC  C IxI xI C
5    O            CCCCC   C  C   C  C        C
4  COOOOOOOOOOOOO C   C - C- C - C  C  C - CCC
3  Cx C x C x C x C x C x Cx C x C  C  C x C
2  CCCCCCCCCCCCCCCC x   x  x   x   CCCCC x C -
1                   x   x  x   x         x   -
0 --------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012345678901234567890123
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
