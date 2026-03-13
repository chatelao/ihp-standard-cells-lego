# Design Documentation for sg13g2_ebufn_2

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


pppppppXppppppXppp
pppppppXppppppXppp
ppppppppppppppXppp
   X
   X


             X X

nnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnXnnn
nnnnnnXnnnnnnnXnnn
nnnnnnXnnnnnnnXnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456789012345678


       X    G X G
       X    G X G
            G X G
   X        G G G
   X        G G G
            G G G
            G G G
            GXGXG
            GGGGG
            G G G
            G G G
            G X G
      X     G X G
      X     G X G


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456789012345678
+++++++++++++++++++
+++++++++++++++++++
       x      x
CCCCCC x      x
C    CCCCC    x CC
C  x C   CCCCCCCCC
C  x C   C      CC
  OO C   CCC    CC
  O      CC      C
  O CCCCCCC IxIx C
  O C     C IIII C
  O       C      C
C O CCCCCCCCC - CC
C   C    C  C x CC
CCCCC x  C  C x CC
      x       x
-------------------
-------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456789012345678


















```
