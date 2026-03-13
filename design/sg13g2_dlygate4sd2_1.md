# Design Documentation for sg13g2_dlygate4sd2_1

## Substrate
```
01234567890123
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
NNNNNNNNNNNNNN
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
SSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
01234567890123

 ppXpppppppXp
 ppXpppppppXp
 ppXpppppppXp
           X


  X
 nnnnnnnnnnnn
 nnnnnnnnnnnn
 nnnnnnnnnnnn
 nnXnnnnnnnXn
 nnXnnnnnnnXn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
01234567890123

  GX       X
  GX       X
  GX       X
  G        X
  G
  G
  X
  G
  G
  G
  GX       X
  GX       X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890123
++++++++++++++
   x       x
   x       x O
 C x  C C  x O
 C    C C  x O
 CCCC C CCCC O
    C C    C O
 Ix C CCC CC O
 II C C   C  O
 CCCC C CCCOOO
 C    C      O
 C x  C    x O
   x       x
--------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
01234567890123














```
