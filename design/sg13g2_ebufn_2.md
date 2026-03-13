# Design Documentation for sg13g2_ebufn_2

## Substrate
```
012345678901234567
NNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
012345678901234567

 ppppppXpppppXppp
 ppppppppppppXppp
 pppppppppppppppp
   X
   X

            X X
 nnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnn
 nnXnnnnnnnnnXnnn
 nnnnnnXnnnnnXnnn
 nnnnnnXnnnnnXnnn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901234567

       X   G X G
           G X G
           G G G
   X       G G G
   X       G G G
           G G G
           GXGXG
           GGGGG
           G G G
   X       G X G
       X   G X G
       X   G X G

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678901234567
++++++++++++++++++
       x     x
 CCCCCCCCC   x
 C   C         CC
 C x C   CCCCCCCC
   x C   CCC   CC
   O     CC     C
   OCCCCCCC x x C
   O      C I I C
   O CCCC CC    C
 C x C  C  C x CC
 CCCCC xC  C x CC
       x     x
------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678901234567














```
