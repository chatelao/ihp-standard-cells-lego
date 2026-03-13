# Design Documentation for sg13g2_dllrq_1

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


ppXppppppXpppppppppXXXpppXppp
ppXppppppXpppppppppXXXpppXppp
ppXppppppppppppppppXXXpppXppX
  X                XXX   X  X
  X                         X


  X X
                        X
nnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnnnXnXX
nnnnnnnnnnnnnnnnnnnXnnnnnXnXX
nnXnnnnnnXXXnnnnnnnXnnnnnXnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123456789012345678


  X G    X         XXX  GX
  X G    X         XXX  GX
  X G              XXX  GX  X
  X G              XXX  GX  X
  X G                   G   X
  G G                   G
  G G                   G
  X X                   G
  G G                   X
  G G                   G
  G G                   G
  G G                   GX XX
  G G              X    GX XX
  X G    XXX       X    GX


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123456789012345678
+++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++
  x      x         xxx   x
  x      x         xxx   x
  x                xxx C x  x
C x CCCCCCCCCCCCC  xxx C x  x
C x CCC      CC C      C    x
C + CCCCC     C C CCCCCCCCC O
C     C CCCCC CCCCCC  C   C O
CIxIx C C   C       C C I C O
CIIII C C C CCCCC   C C x CCO
C   CCC C C CCCCC   C C I   O
C   CCCCC C    CCCCCCCC  - OO
CCCCCCCCCCC    C     CC  x xx
               C   x CC  x xx
  x      xxx       x     x
-----------------------------
-----------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123456789012345678


















```
