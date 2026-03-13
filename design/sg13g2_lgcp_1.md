# Design Documentation for sg13g2_lgcp_1

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

 ppXppppppppXpppppXpppXppp
 ppXppppppppXpppppXpppXpXp
 pppppppppppppppppXpppXpXp
                      X X
                      X X
     X           X
                  X
 nnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnXXnnnnXnnnnnXXn
 nnXnnnnnnnnXnnnnXnnnnnXXn
 nnXnnnnnnnnXnnnnXnnnnnXnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901234567890123456

   X G      X     X   X
   X G      X     X   X X
     G            X   X X
     G            G   X X
     G            G   X X
     X           XG
     G            X
     G            G
     G            G
     G     XX    XG    XX
   X G      X    XG    XX
   X G      X    XG    X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678901234567890123456
+++++++++++++++++++++++++++
   x        x     x   x
 C x        x     x   x x
 C    CCC   CCCCC xC  x x
 C CCCCCCCCCC   C  C  x x
 C C   C    C C CI CCCx x
 C C x C C  CCC Cx   C  O
 CCC I C C  CCC CIx  CC O
 C CCCCC CCCCCC C    C  O
 CCCC C       C  -  CC -O
 C   CCCC  xx C  x  CC xx
 C x CCCCCCCx    x     xx
   x        x    x     x
---------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678901234567890123456














```
