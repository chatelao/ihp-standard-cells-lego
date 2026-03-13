# Design Documentation for sg13g2_ebufn_4

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


pppXppppppppXpppXppppppppppp
pppXppppppppXpppXppppppppppp
pppXppppppppXpppXppppppppppp
                X   X    X
                    X    X

   X
  X
     X
nnnnnXnnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnnnnnnnnnnnn
nnXnnnnnnnnnXnnnXnnnnnnnnnnn
nnXnnnnnnnnnXnnnXnnnnnnnnnnn
nnXnnnnnnnnnXnnnXnnnnnnnnnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123456789012345678


   X G      X   X
   X G      X   X
   X G      X   X
   G G          X   X    X
   G G              X    X
   G G
   X G
  XG G
   G X
   G X
   G G
  XG G      X   X
  XG G      X   X
  XG G      X   X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123456789012345678
+++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++
   x        x   x
   x        x   x CCCCCCCCCC
CC x      C x C x C    C   C
CCCCCCCC  CCCCC x C x  C x C
C      C      C   C x    x C
C    C CCCCCC CCCCC OOOOOO C
C Ix CCCC   C            O
C x     C   CCCCCCCCCCCC O
C I IxI C CCCCCCCCC      O
C   Ix  C C   C   C OOOOOO
C - II  C C - C - C O    O C
C x  CCCC C x C x C    C   C
C x  CCCC C x C x CCCCCCCCCC
  x         x   x
-----------------------------
-----------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123456789012345678


















```
