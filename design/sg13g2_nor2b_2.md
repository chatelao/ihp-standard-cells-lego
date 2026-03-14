# Design Documentation for sg13g2_nor2b_2

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
4 G G     G G
3 G G     G G
2 G G     G G
1 G G     G G
0 G G     G G
9 G G     G G
8 G G     G G
7 G G     GGG
6 G G     G G
5 G G     G G
4 G G     G G
3 GGG     G G
2 G G     G G
1 G G     G G
0 G G     G G
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 ++++++++++++
3    x       +
2    x       +
1  C x CCCCC +
0  C + C   C +
9  C +   O C +
8  C   OOO
7  CCC O  IxI
6  C   O  III
5  C   xxxxx
4    x x   x -
3  x x x x x -
2  I x   x   -
1    x   x   -
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
