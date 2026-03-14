# Design Documentation for sg13g2_dlhr_1

## Substrate
```
  0123456789012345678901234567890123
5 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123
5
4  pppppppppppppppppppppppppppppppp
3  pppppppppppppppppppppppppppppppp
2  pppppppppppppppppppppppppXXppppp
1
0
9
8
7    X X
6                       X
5  nnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnXXnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnXnnnnnX
2  nnnnnnnnnnnnnnnnnnnnnnnnnXnnnnnX
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123
5
4    G G                G
3    G G                G
2    G G                G   XX
1    G G                G
0    G G                G
9    G G                G
8    G G                G
7    X X                G
6    G G                X
5    G G                G    X
4    G G                G   XX
3    G G                G   X     X
2    G G                G   X     X
1    G G                G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789012345678901234567890123
5 ++++++++++++++++++++++++++++++++++
4
3
2             CCCCC         xx
1   C         C   C     C   OOC   OO
0   CCCCCCCCCCC C C     C   OOC   OO
9   C   CCCC CC C C CCCCC    OC   OO
8   C    CCC CCCC   CCCCCCCC OC   OO
7   Cx x C C C CCCCCCC C   C OC    O
6   CI I C C C C C   C CxI C OCCCC O
5   C    C CCCCCCC     CII   xC    O
4   C   CCCC     C    CC    xxC    O
3       CCCCCCC CC    CC    x C   xO
2             CCCCC   CC    x C   xO
1
0 ----------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345678901234567890123
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
