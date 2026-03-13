# Design Documentation for sg13g2_dlygate4sd3_1

## Substrate
```
01234567890123456

NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSS

```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890123456


ppXpppppppppXppp
ppXpppppppppXppp
ppXpppppppppXpXX
  X         X XX
              XX


 X

nnnnnnnnnnnnnnnn
nnnnnnnnnnnnnnnn
nnXnnnnnnnnnXnXX
nnXnnnnnnnnnXnXX
nnXnnnnnnnnnXnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123456


 GX         X
 GX         X
 GX         X XX
 GX         X XX
 G            XX
 G
 G
 X
 G
 G
 G
 GX         X XX
 GX         X XX
 GX         X


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123456
+++++++++++++++++
+++++++++++++++++
  x         x
  x         x
  x   C C   x xx
C x   C C   x xx
CCCCC C C     xx
    C C C     OO
III C C CCCCC  O
IxI C CCCCC CC O
III C CCCCC CC O
    C C     C OO
CCCCC C CCCCC OO
C x   C     x xx
  x         x xx
  x         x
-----------------
-----------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123456


















```
