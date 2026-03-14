# Design Documentation for sg13g2_sdfbbp_1

## Substrate
```
  0123456789012345678901234567890123456789012345678901234567890123456
5 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456789012345678901234567890123456
5    X        X     X        X     X X        X      X    X     X
4  ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3  ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
2  pppppppppppppppppppppppppppppppXpppppppXppppppppppppppppppppppppp
1                                  X   X    X
0                                           X
9                               X    X
8     X                                       X X
7   X    X                                      X
6                 X             X                       X
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXX
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXXnnnnXX
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXXnnnnXX
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXXnnnnXX
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0  X       X       X          X    X   X       X          X     X
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901234567890123456
5    X        X     X        X     X X        X      X    X     X
4   G G  G        G                G            G       G
3   G G  G        G                G            G       G
2   G G  G        G               XG      X     G       G
1   G G  G        G                X   X    X   G       G
0   G G  G        G                G        X   G       G
9   G G  G        G             X  G X          G       G
8   G X  G        G                G          X X       G
7   X G  X        G                G            X       G
6   G G  G        X             X  G            G       X
5   G G  G        G                G            G       G    X    XX
4   G G  G        G                G            G       G   XX    XX
3   G G  G        G                G            G       G   XX    XX
2   G G  G        G                G            G       G   XX    XX
1   G G  G        G                G            G       G
0  X       X       X          X    X   X       X          X     X
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789012345678901234567890123456789012345678901234567890123456
5 +++x++++++++x+++++x++++++++x+++++x+x++++++++x++++++x++++x+++++x++++
4
3
2      CCCCCC     C   C         IIxI   IIIxII
1  C   C    C   C C   C C       IC x   x CC xCCCCCC         OOC   OO
0  CCCCC C    CCC C   C C CCC   IC I   I CC xCC   CCCCCCCCC OOC   OO
9        CCC  C   C   CCC   C   xC IIxII CC ICC   CCC     C OOC   OO
8   I xI   C CC CCCCC  CCCC CCC ICCCCCCC  C IIxIx   C  CC C OOC   OO
7   x II x C  C C   C  C  C C C I     CC CC     x   C  C  C  OCC  OO
6   I    X C  C CIx CC CC C CCC x C C CC CCCCCC   C CCCCxICC OCC  OO
5   I  CCCCCCCC C I  CCCCCC CCCCCCC   C  CC   CCCCC C  C     xC   xx
4      C     CC C       C   CCCCCCCCCCC  CC C    C  CC CC   xxC   xx
3      C     C  C CCCCCCC CCC      C     C  C    C CCC      xxC   xx
2            CCCCCC              CCCCC   CCCC    CCCCC      xx    xx
1
0 -x-------x-------x----------x----x---x-------x----------x-----x----
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, X=Connection (lower side), x=Connection (upper side)

## Metal 2
```
  0123456789012345678901234567890123456789012345678901234567890123456
5
4
3
2
1
0
9
8
7
6        xM
5
4
3
2
1
0
```
Legend: M=Metal 2, x=Connection (upper side)
