# Design Documentation for sg13g2_and3_2

## Substrate
```
  012345678901
3 NNNNNNNNNNNN
2 NNNNNNNNNNNN
1 NNNNNNNNNNNN
0 NNNNNNNNNNNN
9 NNNNNNNNNNNN
8 NNNNNNNNNNNN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SSSSSSSSSSSS
3 SSSSSSSSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 SSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901
3
2  ppXpppXppp
1  ppXpppXpXp
0  ppXpppXpXp
9          XX
8           X
7
6     X X
5  nnnnnnnnnn
4  nnnnnnnnnn
3  nnnnXnXnXn
2  nnXnnnXnnn
1  nnnnnnXnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901
3
2    XGGGX
1    XGGGX X
0    XGGGX X
9    GGGGG XX
8    GGGGG  X
7    GGGGG
6    GXGXG
5    GGGGG
4    GGGGG
3    GGXGX X
2    XGGGX
1    GGGGX
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901
3 ++++++++++++
2    x   x   +
1   Cx C x x +
0   Cx C x x
9   C  C   xx
8   CCCCCCC x
7   C     C O
6   C xIxI  O
5   C IIII OO
4   C      O
3      x x x -
2  IIxII x   -
1        x   -
0 ------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901
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
