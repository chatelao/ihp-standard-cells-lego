# Design Documentation for sg13g2_nor4_1

## Substrate
```
01234567890
NNNNNNNNNNN
NNNNNNNNNNN
NNNNNNNNNNN
NNNNNNNNNNN
NNNNNNNNNNN
NNNNNNNNNNN
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
SSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890

 Xpppppppp
 XppppppXX
 XppppppXX
 X     XXX
 X   X  XX
     X X
 X X    X
 nnnXXnnnn
 nnnnnnnnn
 XnXnnnXnn
 XnXnXnXnX
 XnnnXnnnX

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890

 X  GG  G
 X  GG  XX
 X  GG  XX
 X  GG XXX
 X  GX  XX
 G  GX XG
 X XGG  X
 G  XX  G
 G  GG  G
 X XGG XG
 X XGX XGX
 X  GX  GX

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890
+++++++++++
 x
 x      xx
 x      xx
 x     xxx
 x   x Ixx
     x x O
 x x I IxO
 I Ixx IIO
   OOOOOOO
 x x   x
 x x x x x
 x   x   x
-----------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890














```
