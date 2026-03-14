# Design Documentation for sg13g2_buf_8

## Substrate
```
  01234567890123456789012
3 NNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012
3
2  pXpppXpppXpppXpppXppX
1  pXpppXpXpXpXpXpXpXpXX
0  pXpppXpXpXpXpXpXpXpXX
9         X   X   X   XX
8         XXXXXXXXXXXXXX
7
6     X
5  nnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnXnnnXnnnXnnnXX
2  nXnnnXnXnXnXnXnXnXnXX
1  nXnnnXnnnXnnnXnnnXnnX
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012
3
2   X G X   X   X   X  X
1   X G X X X X X X X XX
0   X G X X X X X X X XX
9     G   X   X   X   XX
8     G   XXXXXXXXXXXXXX
7     G
6     X
5     G
4     G
3     G   X   X   X   XX
2   X G X X X X X X X XX
1   X G X   X   X   X  X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456789012
3 +++++++++++++++++++++++
2   x   x   x   x   x  x
1  Cx C x x x x x x x xx
0  Cx C x x x x x x x xx
9  C  C   x   x   x   xx
8  CCCCCCCxxxxxxxxxxxxxx
7        C            O
6   IIxI CCCCCCCCCCC  OO
5        C            O
4  CCCCCCCOOOOOOOOOOOOO
3  C  C   x   x   x   xx
2  Cx C x x x x x x x xx
1   x   x   x   x   x  x
0 -----------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012
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
