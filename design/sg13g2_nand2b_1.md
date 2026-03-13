# Design Documentation for sg13g2_nand2b_1

## Substrate
```
012345678

NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
012345678


ppXpppXp
ppXpppXp
ppXpXpXp
  X XXXX
       X


X  X

nnnnnnnn
nnnnnnnn
nnXnnnXX
nnXnnnnn
nnXnnnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678


G XG  X
G XG  X
G XGX X
G XGXXXX
G  G   X
G  G
G  G
X  X
G  G
G  G
G  G
G XG  XX
G XG
G XG


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678
+++++++++
+++++++++
  x   x
  x   x
  x x x
C x xxxx
C      x
CCCCCC O
     C O
x  x CCO
I  I CCO
CCCCCCOO
C     OO
  x   xx
  x
  x
---------
---------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678


















```
