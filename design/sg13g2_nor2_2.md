# Design Documentation for sg13g2_nor2_2

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

 ppXpppppp
 ppXpppppp
 ppXpppppp
       X
       XXX

   X   X
 nnnnnnnnn
 nnnnnnnnn
 XnXnnnXnn
 XnXnXnXnX
 XnnnXnnnX

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890

  GXG G G
  GXG G G
  GXG G G
  G G GXG
  G G GXXX
  G G G G
  GXG GXG
  G G G G
  G G G G
 XGXG GXG
 XGXGXGXGX
 XG GXG GX

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890
+++++++++++
   x
 C x CCCCC
 C x C   C
 C   C x
 CCCCC xxx
         O
   x   x O
         O
   OOOOOOO
 x x   x
 x x x x x
 x   x   x
-----------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890














```
