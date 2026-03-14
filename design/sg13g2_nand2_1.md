# Design Documentation for sg13g2_nand2_1

## Substrate
```
  0123456
3 NNNNNNN
2 NNNNNNN
1 NNNNNNN
0 NNNNNNN
9 NNNNNNN
8 NNNNNNN
7 SSSSSSS
6 SSSSSSS
5 SSSSSSS
4 SSSSSSS
3 SSSSSSS
2 SSSSSSS
1 SSSSSSS
0 SSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456
3
2  XpppX
1  XpXpX
0  XpXpX
9  X X X
8  X X X
7
6  X   X
5  nnnnn
4  nnnnn
3  XnnnX
2  XnnnX
1  Xnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456
3
2  X   X
1  X X X
0  X X X
9  X X X
8  X X X
7  G   G
6  X   X
5  G   G
4  G   G
3  X   X
2  X   X
1  X   G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456
3 +++++++
2  x   x
1  x x x
0  x x x
9  x x x
8  x x x
7    O
6  x O x
5  I O I
4  - OOO
3  x   x
2  x   x
1  x
0 -------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456
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
