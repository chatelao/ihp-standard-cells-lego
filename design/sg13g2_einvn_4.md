# Design Documentation for sg13g2_einvn_4

## Substrate
```
  01234567890123456789012
3 NNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012
3
2  XppppppXppXpppppppppp
1  XppppppXppXpppppppppp
0  XppppppXppXpppppppppp
9  X      X  X   X   X
8  X      X  X   XXXXX
7
6   X               X
5  nnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnn
3  XnnnnnnXnnnXnnnnnnnXn
2  XnnnnnnXnnnXnnnnnnnnn
1  XnnnnnnXnnnXnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012
3
2  XG     X  X      G
1  XG     X  X      G
0  XG     X  X      G
9  XG     X  X   X  GX
8  XG     X  X   XXXXX
7   G               G
6   X               X
5   G               G
4   G               G
3  XG     X   X     G X
2  XG     X   X     G
1  XG     X   X     G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456789012
3 +++++++++++++++++++++++
2  x      x  x CCCCCCCCC
1  x C  C xC x C   C   C
0  x C  C xC x C   C   C
9  x C  C xC x C x C x C
8  x C  C xC x C xxxxx C
7    C  CCCCCCCC OO
6  IxC            OIxII
5  IIC   CCCCCCCC O
4    C   C  C   C OOOOO
3  x CCC Cx C x C     x C
2  x CCC Cx C x CCCCCCCCC
1  x      x   x
0 -----------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012
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
