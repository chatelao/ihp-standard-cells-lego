# Design Documentation for sg13g2_inv_8

## Substrate
```
  012345678901234567
3 NNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567
3
2  XpppXppXpppXpppX
1  XpXpXXpXpXpXpXpX
0  XpXpXXpXpXpXpXpX
9  X X  X   X X X X
8  X XXXXXXXX X X X
7
6       X
5  nnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnn
3  XnXnnXnnnXnXnXnX
2  XnXnXXnXnXnXnXnX
1  XnnnXnnXnnnXnnnX
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567
3
2  X   XG X   X   X
1  X X XX X X X X X
0  X X XX X X X X X
9  X X  X   X X X X
8  X XXXXXXXX X X X
7       G
6       X
5       G
4       G
3  X X  X   X X X X
2  X X XX X X X X X
1  X   XG X   X   X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234567
3 ++++++++++++++++++
2  x   x  x   x   x
1  x x xx x x x x x
0  x x xx x x x x x
9  x x  x   x x x x
8  x xxxxxxxx x x x
7           O   O
6    IIIxII OOOOO
5           O   O
4    OOOOOOOO   O
3  x x  x   x x x x
2  x x xx x x x x x
1  x   x  x   x   x
0 ------------------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234567
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
