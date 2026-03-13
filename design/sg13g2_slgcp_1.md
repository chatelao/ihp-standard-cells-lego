# Design Documentation for sg13g2_slgcp_1

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


XppppppXpppppppppXppppppppppXppp
XppppppXpppppppppXppppppppppXppp
XppppppXpppppppppXppppppppppXpXX
X                           X XX
                            X XX

   XX
 X                     X

nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
XnnnnnnnnnnnnnnnXnnnnnnXnnnnnXnX
XnnnnnnnnnnnnnnnXnnnnnnXnnnnnXnn
XnnnXnnnnnnnnnnnXnnnnnnXnnnnnXnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901234567890123456789012


XG G   X         X     G    X
XG G   X         X     G    X
XG G   X         X     G    X XX
XG G                   G    X XX
 G G                   G    X XX
 G G                   G
 G XX                  G
 X G                   X
 G G                   G
 G G                   G
 G G                   G
XG G            X      X     X X
XG G            X      X     X
XG GX           X      X     X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678901234567890123456789012
+++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++
x      x         x          x
x      x         x          x
x   C  x         x CCCCCC C x xx
x   CCCCCCCC C     C    C C x xx
      C    C C     C    C C x xx
      C  C C C CCCCC C  C C   OO
 IIxx C  C   C CCCCC C  C CC   O
 x    C CCCC C     C CIxC  CCC O
 I CCCC C    CCCCC C CIICC CCC O
   C   CCCC C CCCC C C     C   O
- CC      C C C  CCCCC -  CC - O
x CCCCCCCCC C C xC  CC x  CC x x
x         CCCCC xCCCCC x     x
x   x           x      x     x
---------------------------------
---------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678901234567890123456789012


















```
