# Design Documentation for sg13g2_xor2_1

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
4   G     G
3   G     G
2   G     G
1   G     G
0   G     G
9   G     G
8   G     G
7   G     G
6   G     G
5   G     G
4   G     G
3   G     G
2   G     G
1   G     G
0   G     G
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 ++++++++++++++
3   x      x
2   x      x
1   x  C C x C O
0   +  C CCCCC O
9   + CCCCCCCC O
8     C       CO
7     C       CO
6  Ix C IIxII CO
5     C     xxxO
4  xx C  x  xx
3  xx    x  xxx
2  xx    x    x
1  xx    x    x
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
