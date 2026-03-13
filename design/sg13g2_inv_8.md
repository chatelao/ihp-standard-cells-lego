# Design Documentation for sg13g2_inv_8

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

 XpppXppXpppXpppX
 XpXpXXpXpXpXpXpX
 XpXpXXpXpXpXpXpX
 X X  X   X X X X
 X XXXXXXXX X X X

      X
 nnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnn
 XnXnnXnnnXnXnXnX
 XnXnXXnXnXnXnXnX
 XnnnXnnXnnnXnnnX

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678901234567

 X   XG X   X   X
 X X XX X X X X X
 X X XX X X X X X
 X X  X   X X X X
 X XXXXXXXX X X X
      G
      X
      G
      G
 X X  X   X X X X
 X X XX X X X X X
 X   XG X   X   X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
012345678901234567
++++++++++++++++++
 x   x  x   x   x
 x x xx x x x x x
 x x xx x x x x x
 x x  x   x x x x
 x xxxxxxxx x x x
          O   O
   IIIxII OOOOO
          O   O
   OOOOOOOO   O
 x x  x   x x x x
 x x xx x x x x x
 x   x  x   x   x
------------------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
012345678901234567














```
