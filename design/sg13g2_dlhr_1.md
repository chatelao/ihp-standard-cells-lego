# Design Documentation for sg13g2_dlhr_1

## Substrate
```
  01234567890123456789012345678901
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
3
2  pppXpppppXppppppXXXpppXppppXpp
1  pppXpppppXppppppXXXpppXXXppXpp
0  ppppppppppppppppXXXpppXXXppXpX
9                        XXX  X X
8                          X    X
7
6    X X               X
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnXXnnnnnnnnnnnnXnnnnXnXnnnXnX
2  nnXXnnnnnnnnnnnnXnnnnXnXnnnXnX
1  nnXXnnnnnXnnnnnnXnnnnXnnnnnXnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901
3
2    GXG    X      XXX G X    X
1    GXG    X      XXX G XXX  X
0    G G           XXX G XXX  X X
9    G G               G XXX  X X
8    G G               G   X    X
7    G G               G
6    X X               X
5    G G               G
4    G G               G
3    XXG           X   GX X   X X
2    XXG           X   GX X   X X
1    XXG    X      X   GX     X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456789012345678901
3 ++++++++++++++++++++++++++++++++
2     x     x      xxx   x    x
1     x     x CCCC xxx   xxx  x
0  CCCCCCCCCC CCCC xxx C xxxC x x
9  C        C CCCC     C xxxC x x
8  C    CCCCC C CC CCCCCCC xC   x
7  C     C CC C CCCCC C  C OC   O
6  C x x C CCCC CCCCC Cx C OC   O
5  C I I C CCCCCC     CI   OCCCCO
4  C --CCCCC    C    CC   OOC   O
3    xxCCCCCCC CC  x CC x x C x x
2    xxCCC    CCCC x CC x x C x x
1    xx     x      x    x     x
0 --------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012345678901
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
