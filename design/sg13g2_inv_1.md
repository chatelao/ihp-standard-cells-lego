# Design Documentation for sg13g2_inv_1

## Substrate
```
  01234
3 NNNNN
2 NNNNN
1 NNNNN
0 NNNNN
9 NNNNN
8 NNNNN
7 SSSSS
6 SSSSS
5 SSSSS
4 SSSSS
3 SSSSS
2 SSSSS
1 SSSSS
0 SSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234
3
2  Xpp
1  XpX
0  XpX
9  X X
8  X X
7
6  X
5  nnn
4  nnn
3  XnX
2  XnX
1  Xnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234
3
2  X
1  X X
0  X X
9  X X
8  X X
7  G
6  X
5  G
4  G
3  X X
2  X X
1  X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234
3 +++++
2  x
1  x x
0  x x
9  x x
8  x x
7    O
6  x O
5    O
4    O
3  x x
2  x x
1  x
0 -----
```
Legend: +=VDD, -=VSS, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234
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
