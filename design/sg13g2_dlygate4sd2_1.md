# Design Documentation for sg13g2_dlygate4sd2_1

## Substrate
```
  01234567890123
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
3
2  ppXpppppppXp
1  ppXpppppppXp
0  ppXpppppppXp
9            X
8
7
6   X
5  nnnnnnnnnnnn
4  nnnnnnnnnnnn
3  nnnnnnnnnnnn
2  nnXnnnnnnnXn
1  nnXnnnnnnnXn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123
3
2   GX       X
1   GX       X
0   GX       X
9   G        X
8   G
7   G
6   X
5   G
4   G
3   G
2   GX       X
1   GX       X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123
3 ++++++++++++++
2    x       x
1    x       x O
0  C x  C C  x O
9  C    C C  x O
8  CCCC C CCCC O
7     C C    C O
6  Ix C CCC CC O
5  II C C   C  O
4  CCCC C CCCOOO
3  C    C      O
2  C x  C    x O
1    x       x
0 --------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123
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
