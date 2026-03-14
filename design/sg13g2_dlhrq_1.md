# Design Documentation for sg13g2_dlhrq_1

## Substrate
```
012345678901234567890123456
NNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
012345678901234567890123456

 ppXppppppXpppppppXpppXppp
 ppXppppppXpppppppXpppXpXX
 pppppppppppppppppppppXpXX
                      X XX
                      X XX

 X  X                X
 nnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnnXnXX
 nnnXnnnnnXnnnnnnXnnnnXnnn
 nnnXnnnnnXnnnnnnXnnnnXnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901234567890123456

 G XG     X       X  GX
 G XG     X       X  GX XX
 G  G                GX XX
 G  G                GX XX
 G  G                GX XX
 G  G                G
 X  X                X
 G  G                G
 G  G                G
 G  G                GX XX
 G  X     X      X   GX
 G  X     X      X   GX

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678901234567890123456
+++++++++++++++++++++++++++
   x      x CCCC  x   x
 C x      x C  C  x C x xx
 CCCCCCCCCC CC C    C x xx
 CCC      C CC C CCCC x xx
   C CC C C CC C CCCC x xx
   C  C C CCCCCCCCC C    O
 x CxICCC CCC CC  C Cx C O
   C  C CCCCC CC    C  C O
 CCC  C       CC   CCCCC O
 C    CCCCCCCCCC   C  x xx
    x C   x CCCC x C  x
    x     x      x    x
---------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678901234567890123456














```
