# Design Documentation for sg13g2_sdfbbp_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901
3                               X
2  ppXpppppppXppppXpppppppppppppXppXppXppppXpppppXppppXpppppppp
1  pppppppppppppppppppppppppXpppppppppppppppppppppppppppXXppXpX
0  ppppppppppppppppppppppppppppppXppXppppXppppppppppppppXXppppX
9                             X   X      X              XX    X
8                                                       XX    X
7   X X X                                  X X
6               X             X              X       X
5  nnnnnnnnnnnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXXnnnnX
2  XnnnnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnnnnXnnnnnnnnnXnXXnnXnX
1  nnnnnnnnnnnnnnnXnnnnnnnnnXnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0                               X
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
3                               X
2   GXG G    X  G X             X  X  X    X G   X   GX
1   G G G       G           X   G            G       G  XX  X X
0   G G G       G               GX  X    X   G       G  XX    X
9   G G G       G             X G X      X   G       G  XX    X
8   G G G       G               G            G       G  XX    X
7   X X X       G               G          X X       G
6   G G G       X             X G            X       X
5   G G G       X               G            G       G
4   G G G       G               G            G       G
3   G G G       G               G            G       G  XX    X
2  XG G G X     G               G    X      XG       GX XX  X X
1   G G G       G X         X   G            G       G
0                               X
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
3 ++++++++++++++++++++++++++++++x+++++++++++++++++++++++++++++++
2    x CCCCC x    x+        + IIxI xIIxIII+x+    x    x     +
1  C + C   C + C C++C       x I  I +I    I+++ C  +    + xx  x x
0  C   C C     C C++C  C    + IC x +x CCCxCCCCC         xxC + x
9  CCCCC C   CCC C  C  CCCC + xC IxII CCCxCC  CCCCCCCCCCxxC + x
8   I    CC CC CCCC CC CC C   IC        CICC ICCC  CC  CxxC   x
7   x x xIC  C C   C C  C CCC ICCCCCC C CIIxIx  C  CC  COOC   O
6   I I XIC  C CxI CCCCCC C C x C C C C CCCC x  C CC x C OCC  O
5   I  CCCCCCC CxI   CCCC CCCCCCC C C C C  CCCCCC CC I C OC   O
4      C    CC CII  CCC   CCCCCCCCCCC C CC      C  C     OC   O
3  -   C  - CC CCCCCCCC CCC      C   -C CC  - C C CCC - xxC - x
2  x      x CCCCC           -  CCCCC xCCCC  x CCCCC   x xx  x x
1  -      -       x         x        -      -         -     -
0 ------------------------------x-------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, X=Connection (lower side), x=Connection (upper side)

## Metal 2
```
  01234567890123456789012345678901234567890123456789012345678901
3
2
1
0
9
8
7
6       xM
5
4
3
2
1
0
```
Legend: M=Metal 2, x=Connection (upper side)
