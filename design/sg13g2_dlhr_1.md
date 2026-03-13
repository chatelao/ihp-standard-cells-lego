# Design Documentation for sg13g2_dlhr_1

## Substrate
```
0123456789012345678901234567890123

NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
0123456789012345678901234567890123


ppXppppppXppppppppXXpppXppppppXpp
ppXppppppXppppppppXXpppXppppppXpp
ppXppppppXppppppppXXpppXpXXpppXXX
                       X XX   XXX
                       X XX   XXX


  X X                 X

nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnXnnnnnnnnnnnnnnXnnnnnXnXnnnXXXX
nnXnnnnnnnnnnnnnnXnnnnnXnXnnnXXXX
nnXnnnnnnXnnnnnnnXnnnnnXnnnnnXXnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456789012345678901234567890123


  X G    X        XX  GX      X
  X G    X        XX  GX      X
  X G    X        XX  GX XX   XXX
  G G                 GX XX   XXX
  G G                 GX XX   XXX
  G G                 G
  G G                 G
  X X                 X
  G G                 G
  G G                 G
  G G                 G
  X G            X    GX X   XXXX
  X G            X    GX X   XXXX
  X G    X       X    GX     XX


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456789012345678901234567890123
++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++
  x      x        xx   x      x
  x      x CCCCC  xx   x      x
  x      x C   C  xx C x xx C xxx
CCCCCCCCCCCC C C     C x xx C xxx
C         CC C C     C x xx C xxx
C   CC CC CC C C CCCCCCCCCO C  OO
C    C  C C CC      C   CCO C  OO
CIxIxCC C C CCCCCCC CIx CCO C   O
CIIIICC C   C C   C CII CCO CCC O
C    C CCCCCC C     C     O C   O
C - CC CC    CC  - CC  - OO C-- O
  x CCCCCCCC     x CC  x x  Cxxxx
  x        CCCC  x CC  x x CCxxxx
  x      x       x     x     xx
----------------------------------
----------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456789012345678901234567890123


















```
