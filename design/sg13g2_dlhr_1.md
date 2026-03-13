# Design Documentation for sg13g2_dlhr_1

## Substrate
```
01234567890123456789012345678901
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890123456789012345678901

 pppXpppppXppppppXXXpppXppppXpp
 pppXpppppXppppppXXXpppXXXppXpp
 ppppppppppppppppXXXpppXXXppXpX
                       XXX  X X
                         X    X

   X X               X
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nnXXnnnnnnnnnnnnXnnnnXnXnnnXnX
 nnXXnnnnnnnnnnnnXnnnnXnXnnnXnX
 nnXXnnnnnXnnnnnnXnnnnXnnnnnXnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123456789012345678901

   GXG    X      XXX G X    X
   GXG    X      XXX G XXX  X
   G G           XXX G XXX  X X
   G G               G XXX  X X
   G G               G   X    X
   G G               G
   X X               X
   G G               G
   G G               G
   XXG           X   GX X   X X
   XXG           X   GX X   X X
   XXG    X      X   GX     X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123456789012345678901
++++++++++++++++++++++++++++++++
    x     x      xxx   x    x
    x     x CCCC xxx   xxx  x
 CCCCCCCCCC CCCC xxx C xxxC x x
 C        C CCCC     C xxxC x x
 C    CCCCC C CC CCCCCCC xC   x
 C     C CC C CCCCC C  C OC   O
 C x x C CCCC CCCCC Cx C OC   O
 C I I C CCCCCC     CI   OCCCCO
 C --CCCCC    C    CC   OOC   O
   xxCCCCCCC CC  x CC x x C x x
   xxCCC    CCCC x CC x x C x x
   xx     x      x    x     x
--------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123456789012345678901














```
