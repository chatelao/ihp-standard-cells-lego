# Design Documentation for sg13g2_mux2_2

## Substrate
```
012345678901234567890

NNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
012345678901234567890


pppXppppppppppXppppX
pppXppppppppppXppppX
pppXppppppppppXpXXXX
              X XXXX
              X XXXX


   X     X
      X
nnnnnnXnnnnXnnnnnnnn
nnnnnnnnnXnnnnnnnnnn
nnnXnnnnnnnnnnXnnXXX
nnnXnnnnnnnnnnXnnnnX
nnnXnnnnnnnnnnXnnnnX


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901234567890


  GXG   G G G X    X
  GXG   G G G X    X
  GXG   G G G X XXXX
  G G   G G G X XXXX
  G G   G G G X XXXX
  G G   G G G
  G G   G G G
  GXG   GXG G
  G G X GGG G
  G G X G GXG
  G G   GXG G
  GXG   G G G X  XXX
  GXG   G G G X    X
  GXG   G G G X    X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678901234567890
+++++++++++++++++++++
+++++++++++++++++++++
   x          x    x
   x CCCCCCCCCx    x
   x C       Cx xxxx
C    C   C   Cx xxxx
CCCCCC CCC   Cx xxxx
C   CCCC     C+ OOO+
C   C        C  OOO
C IxC   Ix   CCCC O
C IIC x IIII CCCC O
C   C x   IxCCCC  O
C  -C IIIxIIC    OO-
   xCCCCCCCCC x  xxx
   x          x    x
   x          x    x
---------------------
---------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678901234567890


















```
