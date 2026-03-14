# Design Documentation for sg13g2_sdfbbp_1

## Substrate
```
01234567890123456789012345678901234567890123456789012345678901
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890123456789012345678901234567890123456789012345678901
                              X
 ppXpppppppXppppXpppppppppppppXppXppXppppXpppppXppppXpppppppp
 pppppppppppppppppppppppppXpppppppppppppppppppppppppppXXppXpX
 ppppppppppppppppppppppppppppppXppXppppXppppppppppppppXXppppX
                            X   X      X              XX    X
                                                      XX    X
  X X X                                  X X
              X             X              X       X
 nnnnnnnnnnnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXXnnnnX
 XnnnnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnnnXnnnnnnnnnXnXXnnXnX
 nnnnnnnnnnnnnnnXnnnnnnnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
                              X
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123456789012345678901234567890123456789012345678901
                              X
  GXG G    X  G X             X  X  X    X G   X   GX
  G G G       G           X   G            G       G  XX  X X
  G G G       G               GX  X    X   G       G  XX    X
  G G G       G             X G X      X   G       G  XX    X
  G G G       G               G            G       G  XX    X
  X X X       G               G          X X       G
  G G G       X             X G            X       X
  G G G       X               G            G       G
  G G G       G               G            G       G
  G G G       G               G            G       G  XX    X
 XG G G X     G               G    X      XG       GX XX  X X
  G G G       G X         X   G            G       G
                              X
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123456789012345678901234567890123456789012345678901
++++++++++++++++++++++++++++++x+++++++++++++++++++++++++++++++
   x CCCCC x    x+        + IIxI xIIxIII+x+    x    x     +
 C + C   C + C C++C       x I  I +I    I+++ C  +    + xx  x x
 C   C C     C C++C  C    + IC x +x CCCxCCCCC         xxC + x
 CCCCC C   CCC C  C  CCCC + xC IxII CCCxCC  CCCCCCCCCCxxC + x
  I    CC CC CCCC CC CC C   IC        CICC ICCC  CC  CxxC   x
  x x xIC  C C   C C  C CCC ICCCCCC C CIIxIx  C  CC  COOC   O
  I I XIC  C CxI CCCCCC C C x C C C C CCCC x  C CC x C OCC  O
  I  CCCCCCC CxI   CCCC CCCCCCC C C C C  CCCCCC CC I C OC   O
     C    CC CII  CCC   CCCCCCCCCCC C CC      C  C     OC   O
 -   C  - CC CCCCCCCC CCC      C   -C CC  - C C CCC - xxC - x
 x      x CCCCC           -  CCCCC xCCCC  x CCCCC   x xx  x x
 -      -       x         x        -      -         -     -
------------------------------x-------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, X=Connection (lower side), x=Connection (upper side)

## Metal 2
```
01234567890123456789012345678901234567890123456789012345678901







      xM






```
Legend: M=Metal 2, x=Connection (upper side)
