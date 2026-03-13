# Design Documentation for sg13g2_ebufn_8

## Substrate
```
0123456789012345678901234567890123456789012345678

NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
0123456789012345678901234567890123456789012345678


pppppppppppppppppppXpppXpppXppppXppppppppppXpppX
pppppppppppppppppppXpppXpppXppppXppppppppppXpppX
pppppppppppppppppppXpppXpppXpppppppppppppppXpppX
  X   X   X    X                               X
  X   X   X    X


                                         X   X

nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnXnnnXnnnnXnnnXnnnnnnnnnnXnnnX
nnnnnnnnnnnnnnnnnnnXnnnXnnnnXnnnXnnnnnnnnnnXnnnX
nnnnnnnnnnnnnnnnnnnXnnnXnnnnXnnnXnnnnnnnnnnXnnnX


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456789012345678901234567890123456789012345678


                   X   X   X    X        G X G X
                   X   X   X    X        G X G X
                   X   X   X             G X G X
  X   X   X    X                         G   G X
  X   X   X    X                         G   G
                                         G   G
                                         G   G
                                         X   X
                                         G   G
                                         G   G
                                         G   G
                   X   X    X   X        G X G X
                   X   X    X   X        G X G X
                   X   X    X   X        G X G X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456789012345678901234567890123456789012345678
+++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++
                   x   x   x    x          x   x
CCCCCCCCCCCCCCCCCC x   x   x    x          x   x
C   C   C   C    C x C x C x CCCCCC        x C x
C x C x C x C  x CCCCCCCCCCCCCC     CCCCCCCCCC x
C x   x   x    x                    C        C
C OOOOOOOOOOOOOO CCCCCCCCCCCCCCCCCCCCCCCCC   CCC
  OO             C                   C         C
  OO  CCCCCCCCCCCC                   C IIxI Ix C
  OO             CCCCCCCCCCCCCCCCCC  C IIII II C
C OOOOOOOOOOOOOO C   C   CC   C   C  C         C
C O   O   O    O C - C - CC - C - C  C   C - CCC
C   C   C   C    C x C x CC x C x C CCCCCC x C x
CCCCCCCCCCCCCCCCCC x   x    x   x          x   x
                   x   x    x   x          x   x
-------------------------------------------------
-------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456789012345678901234567890123456789012345678


















```
