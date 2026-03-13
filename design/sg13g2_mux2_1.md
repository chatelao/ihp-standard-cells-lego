# Design Documentation for sg13g2_mux2_1

## Substrate
```
0123456789012345678

NNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
0123456789012345678


pppXppppppppppXppp
pppXppppppppppXppp
pppXppppppppppXpXX
              X XX
              X XX


   X     X
      X    X
nnnnnnXnnnnnnnnnnn
nnnnnnnnnXnnnnnnnn
nnnXnnnnnnnnnnXnnX
nnnXnnnnnnnnnnXnnX
nnnXnnnnnnnnnnXnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456789012345678


   X     G G  X
   X     G G  X
   X     G G  X XX
   G     G G  X XX
   G     G G  X XX
   G     G G
   G     G G
   X     X G
   G  X  G X
   G  X  G G
   G     X G
   X     G G  X  X
   X     G G  X  X
   X     G G  X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456789012345678
+++++++++++++++++++
+++++++++++++++++++
   x          x
   x CCCCCCCCCx
   x C       Cx xx
C    C   C   Cx xx
CCCCCC CCC   Cx xx
C   CCCC     C+ OO
C   C        C  OO
C IxC   IxII CCCCO
C IIC x IIIx CCCCO
C   C x   II   C O
C  -C IIIxIICCCC O
C  xCCCCCCCCC x  x
   x          x  x
   x          x
-------------------
-------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456789012345678


















```
