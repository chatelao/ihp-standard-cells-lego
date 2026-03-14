# Design Documentation for sg13g2_and2_1

## Substrate
```
  012345678
3 NNNNNNNNN
2 NNNNNNNNN
1 NNNNNNNNN
0 NNNNNNNNN
9 NNNNNNNNN
8 NNNNNNNNN
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 SSSSSSSSS
3 SSSSSSSSS
2 SSSSSSSSS
1 SSSSSSSSS
0 SSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678
3
2  XpppXpp
1  XpppXpX
0  XpppXpX
9        X
8        X
7
6    X
5  nnnnnnn
4  nnnnnnn
3  XnnnXnX
2  nnnnXnn
1  nnnnXnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678
3
2  X G X
1  X G X X
0  X G X X
9  G G   X
8  G G   X
7  G G
6  G X
5  G G
4  G G
3  X G X X
2  G G X
1  G G X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678
3 +++++++++
2  x   x
1  x C x xO
0  x C x xO
9    C   xO
8  CCCCC xO
7  C   C  O
6  C x C  O
5  C I    O
4  C     OO
3 IxI  x xO
2 III  x
1      x
0 ---------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678
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
