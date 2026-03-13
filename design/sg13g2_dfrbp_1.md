# Design Documentation for sg13g2_dfrbp_1

## Substrate
```
012345678901234567890123456789012345678901234567890123456

NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
012345678901234567890123456789012345678901234567890123456


XppppppppppXppppppppppppppppppppppppppppppppXpppppppXppp
XppppppppppXppppppppppppppppppppppppppppppppXpppppppXppp
XppppppppppXppppppppppppppppppppppppppppppppXppXppppXpXX
X                                           X  X    X XX
X                                           X  X    X XX


         X                 X
X
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnnXnnnnXnXX
nnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnnXnnnnXnXX
nnnnXnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnXnnnnnnnXnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901234567890123456789012345678901234567890123456


X        G X               G                X       X
X        G X               G                X       X
X        G X               G                X  X    X XX
X        G                 G                X  X    X XX
X        G                 G                X  X    X XX
G        G                 G
G        G                 G
G        X                 X
X        G                 G
G        G                 G
G        G                 G
G   X   XG                 G           X    X  X    X XX
G   X   XG                 G           X    X  X    X XX
G   X   XG                 G           X    X       X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678901234567890123456789012345678901234567890123456
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
x          x                                x       x
x CCCCCCCCCx CCCCC CCCCCCCCCCCCCCCCCCCCCC   x       x
x C       Cx C   C                          x  x CC x xx
x C CCC C C  C C C    CCCCCCCCCCCC          x  x CC x xx
x C CCC C CCCC C C    C          C          x  x CC x xx
+ C C CCCCCCCCCC C CCCC CCCCCC C CCCC    C     O CC + OO
  C C C        C C  CC  C      C C  CCCCCCCCC  O CC    O
I C C C Ix C   C C  CC CC Ix   C C  CCC     C  O CC    O
x C C   II C C C CCCCC  C II CCC CC CCCCCCC C  O CCCCC O
I C CCCCCCCC CCCCC CCC  C    C  CCCCC       C OO CC    O
I C   C   C        CCCC CCCC CC            CC OO CC - OO
CCC x C x C CCCCCCCC         CCCCCCCCC x  CCx  x CC x xx
CCC x   x CCCCCCCCCCCCCCCCCCCCCCCCCC C x    x  x CC x xx
    x   x                              x    x       x
---------------------------------------------------------
---------------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678901234567890123456789012345678901234567890123456


















```
