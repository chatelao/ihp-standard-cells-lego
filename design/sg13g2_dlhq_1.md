# Design Documentation for sg13g2_dlhq_1

## Substrate
```
012345678901234567890123456789
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
012345678901234567890123456789

 XpppppXpppppppppppXppppppXpp
 XppppppppppppppppppppppppXpX
 XppppppppppppppppppppppppXpX
 X                        X X
                          X X

  X                     X
 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnnnnnnnnn
 XnnnnnXnnnnnnnnnnnnnnnnnnnnX
 XnnnnnXnnnnnnnnnnnnnnnnnnnnX
 XnnnnnXnnnnnnnnnnnnXnnnnnXnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901234567890123456789

 XG    X           X    G X
 XG                     G X X
 XG                     G X X
 XG                     G X X
  G                     G X X
  G                     G
  X                     X
  G                     G
  G                     G
 XG    X                G   X
 XG    X                G   X
 XG    X            X   G X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678901234567890123456789
++++++++++++++++++++++++++++++
 x     x           x      x
 x CCC   CC CCC           x x
 x CCCCCCCCCC CCCCCCCCCCC x x
 x CCC  CCC   CCCCCCCCCCC x x
    CC  C CCC CC     CCCC x x
 II C     C  CCC CC  CCC    O
 Ix C CCC CCC CC  C  CCCxICCO
 II C C  CCCC     C  C C  C O
    C C- CC CCCCC C  C C  C O
 x CCCCx   CCCC   C    CCCC x
 x     x CCCCCCCCCCCCCCC    x
 x     x            x     x
------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678901234567890123456789














```
