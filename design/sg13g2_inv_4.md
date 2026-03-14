# Design Documentation for sg13g2_inv_4

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

 XpppXpppX
 XpXpXpXpX
 XpXpXpXpX
 X X X X X
 X XXXXXX

    X
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

 X  GX   X
 X XGX X X
 X XGX X X
 X XGX X X
 X XXXXXX
    G
    X
    G
    G
 X XG  X
 X XGX X X
 X  GX   X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
01234567890
+++++++++++
 x   x   x
 x x x x x
 x x x x x
 x x x x x
 x xxxxxx
        O
  IIxII O
        O
   OOOOOO
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
