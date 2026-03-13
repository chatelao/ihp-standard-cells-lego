# Design Documentation for sg13g2_dlhrq_1

## Substrate
```
01234567890123456789012345678

NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890123456789012345678


pppXppppppXppppppppXppppXppp
pppXppppppXppppppppXppppXppp
pppXppppppXppppppppXppppXpXX
                        X XX
                        X XX


X   X                  X

nnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnXnnnnnnnnnnnnnnXnnnnnXnXX
nnnXnnnnnnXnnnnnnnXnnnnnXnnn
nnnXnnnnnnXnnnnnnnXnnnnnXnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123456789012345678


G  XG     X        X   GX
G  XG     X        X   GX
G  XG     X        X   GX XX
G   G                  GX XX
G   G                  GX XX
G   G                  G
G   G                  G
X   X                  X
G   G                  G
G   G                  G
G   G                  G
G  XG             X    GX XX
G  XG     X       X    GX
G  XG     X       X    GX


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123456789012345678
+++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++
   x      x        x    x
   x      x CCCCC  x    x
 C x      x C  CC  x  C x xx
 CCCCCCCCCCCC CCC     C x xx
 CC        CC CCC CCCCC x xx
  C  CC C  CCCC      CC + OO
  C   C C  C CCCCCCCCC     O
x C x CCC  C C C   CCC x   O
I C I C C    C CC    C   C O
CCC  CCCCCCCCC CC   CCCCCC O
C    CCCCCCCC CCC   C      O
   x C      C   C x C   x xx
   x C    x CCCCC x     x
   x      x       x     x
-----------------------------
-----------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123456789012345678


















```
