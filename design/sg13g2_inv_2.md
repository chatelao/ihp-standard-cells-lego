# Design Documentation for sg13g2_inv_2

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
6  X
5  nnnnn
4  nnnnn
3  XnXnX
2  XnXnX
1  XnnnX
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456
3
2 GXG  X
1 GXGX X
0 GXGX X
9 GXGX X
8 GXGX X
7 G G
6 GXG
5 G G
4 G G
3 GXGX X
2 GXGX X
1 GXG  X
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
6  x OOO
5    O
4    O
3  x x x
2  x x x
1  x   x
0 -------
```
Legend: +=VDD, -=VSS, O=Metal 1 Output, x=Connection (upper side)

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
