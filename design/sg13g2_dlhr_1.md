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
2  pppppppppppppppppppppppppppppppp
1
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123
5
4    G G                G
3    G G                G
2    G G                G
1    G G                G
0    G G                G
9    G G                G
8    G G                G
7    G G                G
6    G G                G
5    G G                G
4    G G                G
3    G G                G
2    G G                G
1    G G                G
0
```
Legend: G=Polysilicon

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
