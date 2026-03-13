# Design Documentation for sg13g2_and4_1

## Substrate
```
01234567890123

NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890123


XpppXppppXppp
XpppXppppXppp
XpppXppppXpXX
X   X    X XX
           XX


 X X  X X

nnnnnnnnnnnnn
nnnnnnnnnnnnn
nnnnnnnnnXnXX
nnnnnnnnnXnnn
nnnnnnnnnXnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123


XG GX G GX
XG GX G GX
XG GX G GX XX
XG GX G GX XX
 G G  G G  XX
 G G  G G
 G G  G G
 X X  X X
 G G  G G
 G G  G G
 G G  G G
 G G  G GX XX
 G G  G GX
 G G  G GX


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123
++++++++++++++
++++++++++++++
x   x    x
x   x    x
x C x C  x xxO
x C x C  x xxO
  C   C    xxO
CCCCCCCCCCCOOO
C         C  O
Cx x  x x C  O
CI I  I I C  O
C            O
C        - OOO
C        x xxO
         x
         x
--------------
--------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123


















```
