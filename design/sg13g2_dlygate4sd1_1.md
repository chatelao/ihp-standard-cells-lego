# Design Documentation for sg13g2_dlygate4sd1_1

## Substrate
```
012345678901234

NNNNNNNNNNNNNNN
NNNNNNNNNNNNNNN
NNNNNNNNNNNNNNN
NNNNNNNNNNNNNNN
NNNNNNNNNNNNNNN
NNNNNNNNNNNNNNN
NNNNNNNNNNNNNNN
NNNNNNNNNNNNNNN
SSSSSSSSSSSSSSS
SSSSSSSSSSSSSSS
SSSSSSSSSSSSSSS
SSSSSSSSSSSSSSS
SSSSSSSSSSSSSSS
SSSSSSSSSSSSSSS
SSSSSSSSSSSSSSS
SSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
012345678901234


pppXpppppppXpp
pppXpppppppXpp
pppXpppppppXpX
   X       X X
           X X


 X

nnnnnnnnnnnnnn
nnnnnnnnnnnnnn
nnnXnnnnnnnXnX
nnnXnnnnnnnXnn
nnnXnnnnnnnXnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901234


 G X       X
 G X       X
 G X       X X
 G X       X X
 G         X X
 G
 G
 X
 G
 G
 G
 G X       X X
 G X       X
 G X       X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678901234
+++++++++++++++
+++++++++++++++
   x       x
   x       x
   x       x xO
C  x CC    x xO
C     C    x xO
CCCCC C C    OO
    C C CCCCC O
IxI C CCC CCC O
III C C   CCC O
    C C CCC OOO
CCCCC C C    OO
C  x CC    x xO
   x       x
   x       x
---------------
---------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678901234


















```
