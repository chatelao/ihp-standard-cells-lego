# Design Documentation for sg13g2_and3_2

## Substrate
```
012345678901
NNNNNNNNNNNN
NNNNNNNNNNNN
NNNNNNNNNNNN
NNNNNNNNNNNN
NNNNNNNNNNNN
NNNNNNNNNNNN
SSSSSSSSSSSS
SSSSSSSSSSSS
SSSSSSSSSSSS
SSSSSSSSSSSS
SSSSSSSSSSSS
SSSSSSSSSSSS
SSSSSSSSSSSS
SSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
012345678901

 ppXpppXppp
 ppXpppXpXp
 ppXpppXpXp
         XX
          X

    X X
 nnnnnnnnnn
 nnnnnnnnnn
 nnnnXnXnXn
 nnXnnnXnnn
 nnnnnnXnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901

   XGGGX
   XGGGX X
   XGGGX X
   GGGGG XX
   GGGGG  X
   GGGGG
   GXGXG
   GGGGG
   GGGGG
   GGXGX X
   XGGGX
   GGGGX

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678901
++++++++++++
   x   x   +
  Cx C x x +
  Cx C x x
  C  C   xx
  CCCCCCC x
  C     C O
  C xIxI  O
  C IIII OO
  C      O
     x x x -
 IIxII x   -
       x   -
------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678901














```
