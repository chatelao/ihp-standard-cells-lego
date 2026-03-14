# Design Documentation for sg13g2_dlhr_1

## Substrate
```
  01234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901
4
3  pppppppppppppppppppppppppppppp
2  pppppppppppppppppppppppppppppp
1  pppppppppppppppppppppppXXppppp
0
9
8
7
6    X X               X
5  nnnnnnnnnnnnnnnnnnnnnnnnXnnnnX
4  nnnnnnnnnnnnnnnnnnnnnnnXXnnnnX
3  nnnnnnnnnnnnnnnnnnnnnnnXnnnnnX
2  nnnnnnnnnnnnnnnnnnnnnnnXnnnnnX
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901
4
3    G G               G
2    G G               G
1    G G               G  XX
0    G G               G
9    G G               G
8    G G               G
7    G G               G
6    X X               X
5    G G               G   X    X
4    G G               G  XX    X
3    G G               G  X     X
2    G G               G  X     X
1    G G               G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456789012345678901
4 ++++++++++++++++++++++++++++++++
3
2
1             CCCC        xx
0  CCCCCCCCCC CCCC     C  OOC   O
9  C        C CCCC     C  OOC   O
8  C    CCCCC C CC CCCCCCC OC   O
7  C     C CC C CCCCC C  C OC   O
6  C x x C CCCC CCCCC Cx C OC   O
5  C I I C CCCCCC     CI   xCCCCx
4  C   CCCCC    C    CC   xxC   x
3      CCCCCCC CC    CC   x C   x
2      CCC    CCCC   CC   x C   x
1
0 --------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012345678901
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
