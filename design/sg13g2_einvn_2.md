# Design Documentation for sg13g2_einvn_2

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


pXXpppppXppppppp
pXXpppppXppppppp
pXXpppppXppppppp
 XX     X   XX
            XX

 X


nnnnnnnnnnnnnnnX
nnnnnnnnnnnnnnnn
nXXnnnnnXnnnnnnn
nXXnnnnnXnnnnnnn
nXXnnnnnXnnnnnnn


```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123456


GXX     X     G G
GXX     X     G G
GXX     X     G G
GXX     X   XXG G
G G         XXG G
G G           G G
GXG           G G
GGG           G G
G G           G G
G G           GXG
G G           G G
GXX     X     G G
GXX     X     G G
GXX     X     G G


```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123456
+++++++++++++++++
+++++++++++++++++
 xx     x
 xx     x CCCCC
 xxCC C x C   C
 xxCC C x C xxC
    C C   C xxC
III C CCCCC OOC
IxI C       OO
III CC      OO
III CC      OOII
    C       OOIx
    C CCCCC OOII
 xx C C x C
 xx   C x CCCCC
 xx     x
-----------------
-----------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123456


















```
