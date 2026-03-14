# Design Documentation for sg13g2_nand2b_2

## Substrate
```
  01234567890123
4 NNNNNNNNNNNNNN
3 NNNNNNNNNNNNNN
2 NNNNNNNNNNNNNN
1 NNNNNNNNNNNNNN
0 NNNNNNNNNNNNNN
9 NNNNNNNNNNNNNN
8 NNNNNNNNNNNNNN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 SSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123
4
3  pppppppppppp
2  pppppppppppp
1  pppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnn
4  nnnnnnnnnnnn
3  nnnnnnnnnnnn
2  nnnnnnnnnnnn
1  nnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123
4
3 G G    G G
2 G G    G G
1 G G    G G
0 G G    G G
9 G G    G G
8 G G    G G
7 G G    G G
6 GGG    GGG
5 G G    G G
4 G G    G G
3 G G    G G
2 G G    G G
1 G G    G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 ++++++++++++++
3 +   x   x   x
2 +   x   x   x
1 +   x x x x x
0 + C + O + O +
9 + C + OOOOO +
8    C+     O
7    C      O
6  x CC   xIO
5    C      x
4 - CCCCCCC x C
3 -   C x C   C
2 -     x CCCCC
1 -     x
0 --------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123
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
