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
1  ppppppppXp
0
9
8
7
6     X X
5  nnnnnnnnXX
4  nnnnnnnnXn
3  nnnnXnnnXn
2  nnXnnnnnnn
1  nnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901
4
3    GGGGG
2    GGGGG
1    GGGGG X
0    GGGGG
9    GGGGG
8    GGGGG
7    GGGGG
6    GXGXG
5    GGGGG XX
4    GGGGG X
3    GGXGG X
2    XGGGG
1    GGGGG
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901
4 ++++++++++++
3
2
1   C  C   x
0   C  C   O
9   C  C   OO
8   CCCCCCC O
7   C     C O
6   C xIxI  O
5   C IIII xx
4   C      x
3      x   x
2  IIxII
1
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
