# Design Documentation for sg13g2_and4_2

## Substrate
```
01234567890123456

NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890123456


pXpppXppppXppppX
pXpppXppppXppppX
pXpppXppppXpXXXX
 X   X    X XXXX
            XXXX


  X X  X X

nnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnn
nnnnnnnnnnXnXXXX
nnnnnnnnnnXnnnnX
nnnnnnnnnnXnnnnX


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123456


 X G XG G X    X
 X G XG G X    X
 X G XG G X XXXX
 X G XG G X XXXX
 G G GG G G XXXX
 G G GG G G
 G G GG G G
 GXGXGGXGXG
 G G GG G G
 G G GG G G
 G G GG G G
 G G GG G X XXXX
 G G GG G X    X
 G G GG G X    X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123456
+++++++++++++++++
+++++++++++++++++
 x   x    x    x
 x   x    x    x
 x C x C  x xxxx
 x C x C  x xxxx
   C   C    xxxx
CCCCCCCCCCCCOOO+
C          C  O
C x x  x x C  O
C I I  I I C  O
C             O
CC        - OOO-
CC        x xxxx
          x    x
          x    x
-----------------
-----------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123456


















```
