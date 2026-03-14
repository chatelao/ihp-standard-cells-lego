# Design Documentation for sg13g2_inv_16

## Substrate
```
0123456789012345678901234567890123
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
0123456789012345678901234567890123

 XpppXpppXpppXppXpppXpppXpppXpppX
 XpXpXpXpXpXpXXpXpXpXpXpXpXpXpXpX
 XpXpXpXpXpXpXXpXpXpXpXpXpXpXpXpX
 X X   X   X  X   X   X   X   X X
 X XXXXXXXXXXXXXXXXXXXXXXXXXXXX X

                               X
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
 XnXnXnXnXnXnXXnXnXnXnXnXnXnnnXXn
 XnXnXnXnXnXnXXnXnXnXnXnXnXnXnXXn
 XnnnXnnnXnnnXnnXnnnXnnnXnnnXnnXn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
0123456789012345678901234567890123

 X   X   X   X  X   X   X   X  GX
 X X X X X X XX X X X X X X X XGX
 X X X X X X XX X X X X X X X XGX
 X X   X   X  X   X   X   X   XGX
 X XXXXXXXXXXXXXXXXXXXXXXXXXXXXGX
                               G
                               X
                               G
                               G
 X X X X X X XX X X X X X X   XX
 X X X X X X XX X X X X X X X XX
 X   X   X   X  X   X   X   X  X

```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
0123456789012345678901234567890123
++++++++++++++++++++++++++++++++++
 x   x   x   x  x   x   x   x   x
 x x x x x x xx x x x x x x x x x
 x x x x x x xx x x x x x x x x x
 x x   x   x  x   x   x   x   x x
 x xxxxxxxxxxxxxxxxxxxxxxxxxxxx x
   OOOOOOOOOOOOOOOOOOOOOOOO
   O   O   O  O   O   O   O   IxI
   O   O   O  O   O   O   O
   O   O   O  O   O   O   OOOO
 x x x x x x xx x x x x x x   xx
 x x x x x x xx x x x x x x x xx
 x   x   x   x  x   x   x   x  x
----------------------------------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
0123456789012345678901234567890123














```
