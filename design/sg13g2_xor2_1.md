# Design Documentation for sg13g2_xor2_1

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


pXpppppppXpppp
pXpppppppXpppp
pXpppppppXpppX
 X           X
 X           X


 X     X

nnnnnnnnnnnnnn
nnnnnnnnnnnnnn
XXnnnnnXnnnXnX
XXnnnnnXnnnnnX
XXnnnnnXnnnnnX


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901234


 X     G X
 X     G X
 X     G X   X
 X     G     X
 X     G     X
 G     G
 G     G
 X     X
 G     G
 G     G
 G     G
XX     X   X X
XX     X     X
XX     X     X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678901234
+++++++++++++++
+++++++++++++++
 x       x
 x       x
 x   C C x C xO
 x   C C   C xO
 x   C CCCCC xO
 + CCCCCCCCCCOO
   C        C O
Ix C IIxIII C O
II C IIIIII   O
   C       OOOO
-- CC  -   O
xx     x   x x
xx     x     x
xx     x     x
---------------
---------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678901234


















```
