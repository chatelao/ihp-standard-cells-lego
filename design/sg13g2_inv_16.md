# Design Documentation for sg13g2_inv_16

## Substrate
```
  0123456789012345678901234567890123
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123
3
2  XpppXpppXpppXppXpppXpppXpppXpppX
1  XpXpXpXpXpXpXXpXpXpXpXpXpXpXpXpX
0  XpXpXpXpXpXpXXpXpXpXpXpXpXpXpXpX
9  X X   X   X  X   X   X   X   X X
8  X XXXXXXXXXXXXXXXXXXXXXXXXXXXX X
7
6                                X
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  XnXnXnXnXnXnXXnXnXnXnXnXnXnnnXXn
2  XnXnXnXnXnXnXXnXnXnXnXnXnXnXnXXn
1  XnnnXnnnXnnnXnnXnnnXnnnXnnnXnnXn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123
3
2  X   X   X   X  X   X   X   X  GX
1  X X X X X X XX X X X X X X X XGX
0  X X X X X X XX X X X X X X X XGX
9  X X   X   X  X   X   X   X   XGX
8  X XXXXXXXXXXXXXXXXXXXXXXXXXXXXGX
7                                G
6                                X
5                                G
4                                G
3  X X X X X X XX X X X X X X   XX
2  X X X X X X XX X X X X X X X XX
1  X   X   X   X  X   X   X   X  X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789012345678901234567890123
3 ++++++++++++++++++++++++++++++++++
2  x   x   x   x  x   x   x   x   x
1  x x x x x x xx x x x x x x x x x
0  x x x x x x xx x x x x x x x x x
9  x x   x   x  x   x   x   x   x x
8  x xxxxxxxxxxxxxxxxxxxxxxxxxxxx x
7    OOOOOOOOOOOOOOOOOOOOOOOO
6    O   O   O  O   O   O   O   IxI
5    O   O   O  O   O   O   O
4    O   O   O  O   O   O   OOOO
3  x x x x x x xx x x x x x x   xx
2  x x x x x x xx x x x x x x x xx
1  x   x   x   x  x   x   x   x  x
0 ----------------------------------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345678901234567890123
3
2
1
0
9
8
7
6
5
4
3
2
1
0
```
