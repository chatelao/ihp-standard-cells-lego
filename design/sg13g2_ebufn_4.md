# Design Documentation for sg13g2_ebufn_4

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
2  ppXpppppppXpppXpppppppppp
1  ppXpppppppXpppXpppppppppp
0  ppppppppppppppXpppppppppp
9                    X   X
8                    XXXXX
7   X
6
5  nnnnXXnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnn
3  nnXnnnnnnnXnnnXnnnXnnnXnn
2  nnXnnnnnnnXnnnXnnnnnnnnnn
1  nnXnnnnnnnXnnnXnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456
3
2   GX  G    X   X
1   GX  G    X   X
0   G   G        X
9   G   G            X   X
8   G   G            XXXXX
7   X   G
6   G   G
5   G  XX
4   G   G
3   GX  G    X   X   X   X
2   GX  G    X   X
1   GX  G    X   X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234567890123456
3 +++++++++++++++++++++++++++
2    x       x   x CCCCCCCCC
1  C x      Cx C x C   C   C
0  CCCCCCC  CCCC x C   C   C
9  C     C     C   C x   x C
8  C   C CCCCC CCCCC xxxxx C
7  CxI CCCC  C           O
6  CI     C  CCCCCCCCCCC O
5  C   xx C CCCCCCCC     O
4  C   I  C C  C   C OOOOO
3  C x    C Cx C x C x   x C
2  C x CCCC Cx C x CCCCCCCCC
1    x       x   x
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
