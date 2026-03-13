# Design Documentation for sg13g2_dlhq_1

## Substrate
```
012345678901234567890123456789012

NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
012345678901234567890123456789012


XppppppXppppppppppppXpppppppXppp
XppppppXppppppppppppXpppppppXppp
XpppppppppppppppppppppppppppXpXX
X                           X XX
X                           X XX


 X                         X

nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
XnnnnnnXnnnnnnnnnnnnnnnnnnnnnnXX
XnnnnnnXnnnnnnnnnnnnnnnnnnnnnnnn
XnnnnnnXnnnnnnnnnnnnnXnnnnnnXnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901234567890123456789012


XG     X            X      GX
XG     X            X      GX
XG                         GX XX
XG                         GX XX
XG                         GX XX
 G                         G
 G                         G
 X                         X
 G                         G
 G                         G
 G                         G
XG     X                   G  XX
XG     X                   G
XG     X             X     GX


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678901234567890123456789012
+++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++
x      x            x       x
x      x CCC CCC    x       x
x CC CCCCC   C              x xx
x CC C    CCCC CCCCCCCCCCCC x xx
x CC C  CCC CC CCCCCCCC CCC x xx
   C C  C CC   CC     C CCC + OO
II C      C  CCCC CC  C CC     O
Ix CCCCCC C CC  C  C  C CCIx C O
II CCC   CCCCC CC  C  C  C   C O
   C C   C  CCCCCC C  C  CC  COO
  CC C - CCC     C C  CC     COO
x CC C x   CCCCC   CCCCCCCCCCCxx
x      x CCCCCCCCCCC
x      x             x      x
---------------------------------
---------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678901234567890123456789012


















```
