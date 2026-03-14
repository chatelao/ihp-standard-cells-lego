# Design Documentation for sg13g2_nand3_1

## Substrate
```
  0123456789
5 NNNNNNNNNN
4 NNNNNNNNNN
3 NNNNNNNNNN
2 NNNNNNNNNN
1 NNNNNNNNNN
0 NNNNNNNNNN
9 NNNNNNNNNN
8 NNNNNNNNNN
7 SSSSSSSSSS
6 SSSSSSSSSS
5 SSSSSSSSSS
4 SSSSSSSSSS
3 SSSSSSSSSS
2 SSSSSSSSSS
1 SSSSSSSSSS
0 SSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789
5
4  pppppppp
3  pppppppp
2  ppXpppXp
1
0
9
8
7   X X   X
6
5  nnnnnXnn
4  nnnnnXXn
3  nnnnnnXn
2  nnnnnnXn
1  nnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789
5
4   G G   G
3   G G   G
2   GXG  XG
1   G G   G
0   G G   G
9   G G   G
8   G G   G
7   X X   X
6   G G   G
5   G G X G
4   G G XXG
3   G G  XG
2   G G  XG
1   G G   G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789
5 ++++++++++
4
3
2    x   x
1    O   O
0    O   O
9    OOOOO
8       O
7  IxIx OIx
6  IIII OII
5       x
4       xx
3        x
2        x
1
0 ----------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789
5
4
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
