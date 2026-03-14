# Design Documentation for sg13g2_sdfbbp_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901
4    X       X    X         X   X  X       X     X    X     X
3  pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
2  pppppppppppppppppppppppppppppXpppppXpppppppppppppppppppppppp
1  pppppppppppppppppppppppppppppppppppppppppppppppppppppXXppppX
0                                X  X    X
9                             X   X      X
8
7   X X X                                  X X
6               X             X              X       X
5  nnnnnnnnnnnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnX
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnX
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXXnnnnX
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXXnnnnX
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0  X      X       X         X   X    X      X         X     X
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
4    X       X    X         X   X  X       X     X    X     X
3   G G G       G               G            G       G
2   G G G       G               X     X      G       G
1   G G G       G               G            G       G  XX    X
0   G G G       G               GX  X    X   G       G
9   G G G       G             X G X      X   G       G
8   G G G       G               G            G       G
7   X X X       G               G          X X       G
6   G G G       X             X G            X       X
5   G G G       X               G            G       G   X    X
4   G G G       G               G            G       G   X    X
3   G G G       G               G            G       G  XX    X
2   G G G       G               G            G       G  XX    X
1   G G G       G               G            G       G
0  X      X       X         X   X    X      X         X     X
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
4 +++x+++++++x++++x+++++++++x+++x++x+++++++x+++++x++++x+++++x+++
3
2      CCCCC                  IIxI  IIxIII
1  C   C   C   C C  C         I  I  I    I    C         xx    x
0  C   C C     C C  C  C      IC x  x CCCxCCCCC         OOC   O
9  CCCCC C   CCC C  C  CCCC   xC IxII CCCxCC  CCCCCCCCCCOOC   O
8   I    CC CC CCCC CC CC C   IC        CICC ICCC  CC  COOC   O
7   x x xIC  C C   C C  C CCC ICCCCCC C CIIxIx  C  CC  COOC   O
6   I I XIC  C CxI CCCCCC C C x C C C C CCCC x  C CC x C OCC  O
5   I  CCCCCCC CxI   CCCC CCCCCCC C C C C  CCCCCC CC I C xC   x
4      C    CC CII  CCC   CCCCCCCCCCC C CC      C  C     xC   x
3      C    CC CCCCCCCC CCC      C    C CC    C C CCC   xxC   x
2           CCCCC              CCCCC  CCCC    CCCCC     xx    x
1
0 -x------x-------x---------x---x----x------x---------x-----x---
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, X=Connection (lower side), x=Connection (upper side)

## Metal 2
```
  01234567890123456789012345678901234567890123456789012345678901
4
3
2
1
0
9
8
7
6       xM
5
4
3
2
1
0
```
Legend: M=Metal 2, x=Connection (upper side)
