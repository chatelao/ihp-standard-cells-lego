# Design Documentation for sg13g2_and3_2

## Substrate
```
  012345678901
4 NNNNNNNNNNNN
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
4
3  pppppppppp
2  pppppppppp
1  pppppppppp
0
9
8
7
6
5  nnnnnnnnnn
4  nnnnnnnnnn
3  nnnnnnnnnn
2  nnnnnnnnnn
1  nnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901
4
3    GGGGG
2    GGGGG
1    GGGGG
0    GGGGG
9    GGGGG
8    GGGGG
7    GGGGG
6    GGGGG
5    GGGGG
4    GGGGG
3    GGGGG
2    GGGGG
1    GGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 ++++++++++++
3    x   x   +
2    x   x   +
1   Cx C x x +
0   C+ C + OO
9   C  C    O
8   CCCCCCC O
7   C xIxIC O
6   C IIII  O
5   C      xx
4      I x x -
3      x x x -
2  IIxII x   -
1        x   -
0 ------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901
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
