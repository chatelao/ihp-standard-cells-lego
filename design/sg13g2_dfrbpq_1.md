# Design Documentation for sg13g2_dfrbpq_1

## Substrate
```
01234567890123456789012345678901234567890123456789012

NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890123456789012345678901234567890123456789012


XppppppppppXpppppppppppppppppppppppppppppppXppppXppp
XppppppppppXpppppppppppppppppppppppppppppppXppppXppp
XppppppppppXpppppppppppppppppppppppppppppppXppppXpXX
X                                          X    X XX
X                                          X    X XX


         X                 X
X
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnnnnnXnXX
nnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnnnnnXnXX
nnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnnnnnXnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123456789012345678901234567890123456789012


X        G X               G               X    X
X        G X               G               X    X
X        G X               G               X    X XX
X        G                 G               X    X XX
X        G                 G               X    X XX
G        G                 G
G        G                 G
G        X                 X
X        G                 G
G        G                 G
G        G                 G
G   X   XG                 G           X        X XX
G   X   XG                 G           X        X XX
G   X   XG                 G           X        X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123456789012345678901234567890123456789012
+++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++
x          x                               x    x
x CCCCCCCCCx CCCCC CCCCCCCCCCCCCCCCCCCCCC  x    x
x C       Cx C   C                         x  C x xx
x C CCC C C  C C C    CCCCCCCCCCCC         x  C x xx
x C CCC C CCCC C C    C          C         x  C x xx
+ C C CCCCCCCCCC C CCCC CCCCCC C CCCC    C +  C + OO
  C C C        C C  CC  C      C C  CCCCCCCC  C    O
I C C C Ix C   C C  CC CC Ix   C C  CCC    C  C    O
x C C   II C C C CCCCC  C II CCC CC CCCCCCCC  CCCC O
I C CCCCCCCC CCCCC CCC  C    C  CCCCC      C  C    O
I C   C   C        CCCC CCCC CC            C  C - OO
CCC x C x C CCCCCCCC         CCCCCCCCC x  CC  C x xx
CCC x   x CCCCCCCCCCCCCCCCCCCCCCCCCC C x      C x xx
    x   x                              x        x
-----------------------------------------------------
-----------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123456789012345678901234567890123456789012


















```
