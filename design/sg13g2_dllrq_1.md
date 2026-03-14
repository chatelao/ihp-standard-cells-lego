# Design Documentation for sg13g2_dllrq_1

## Substrate
```
  012345678901234567890123456789
5 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
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
5
4  pppppppppppppppppppppppppppp
3  pppppppppppppppppppppppppppp
2  pppppppppppppppppppppppppppp
1
0
9
8
7    X X
6                         X
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnX
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnX
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnX
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456789
5
4    G G                  G
3    G G                  G
2    G G                  G
1    G G                  G
0    G G                  G
9    G G                  G
8    G G                  G
7    X X                  G
6    G G                  X
5    G G                  G
4    G G                  G   X
3    G G                  G   X
2    G G                  G   X
1    G G                  G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234567890123456789
5 ++++++++++++++++++++++++++++++
4
3
2
1       CCCCCCCCCCCC     C    OO
0   C   CC         C     C    OO
9   C   CC      CC C CCCCCCCC OO
8   C   CC CCCCCCC C CCCCC   COO
7   Cx x C C   CCCCCCCCC CII C O
6   CI I CCC CCCC      C CxI C O
5   C    C C CCCCCCC   C CII   O
4   C   CCCC CC   CCCCCCCC    xO
3   CCCCCCCCCCC   C     CC    xO
2                 C     CC    xO
1
0 ------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234567890123456789
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
