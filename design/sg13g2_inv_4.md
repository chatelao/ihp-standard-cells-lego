# Design Documentation for sg13g2_inv_4

## Substrate
```
  01234567890
3 NNNNNNNNNNN
2 NNNNNNNNNNN
1 NNNNNNNNNNN
0 NNNNNNNNNNN
9 NNNNNNNNNNN
8 NNNNNNNNNNN
7 SSSSSSSSSSS
6 SSSSSSSSSSS
5 SSSSSSSSSSS
4 SSSSSSSSSSS
3 SSSSSSSSSSS
2 SSSSSSSSSSS
1 SSSSSSSSSSS
0 SSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890
3
2  XpppXpppX
1  XpXpXpXpX
0  XpXpXpXpX
9  X X X X X
8  X XXXXXX
7
6     X
5  nnnnnnnnn
4  nnnnnnnnn
3  XnXnnnXnn
2  XnXnXnXnX
1  XnnnXnnnX
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890
3
2  X  GX   X
1  X XGX X X
0  X XGX X X
9  X XGX X X
8  X XXXXXX
7     G
6     X
5     G
4     G
3  X XG  X
2  X XGX X X
1  X  GX   X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890
3 +++++++++++
2  x   x   x
1  x x x x x
0  x x x x x
9  x x x x x
8  x xxxxxx
7         O
6   IIxII O
5         O
4    OOOOOO
3  x x   x
2  x x x x x
1  x   x   x
0 -----------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890
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
