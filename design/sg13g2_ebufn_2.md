# Design Documentation for sg13g2_ebufn_2

## Substrate
```
  012345678901234567
3 NNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567
3
2  ppppppXpppppXppp
1  ppppppppppppXppp
0  pppppppppppppppp
9    X
8    X
7
6             X X
5  nnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnn
3  nnXnnnnnnnnnXnnn
2  nnnnnnXnnnnnXnnn
1  nnnnnnXnnnnnXnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567
3
2        X   G X G
1            G X G
0            G G G
9    X       G G G
8    X       G G G
7            G G G
6            GXGXG
5            GGGGG
4            G G G
3    X       G X G
2        X   G X G
1        X   G X G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234567
3 ++++++++++++++++++
2        x     x
1  CCCCCCCCC   x
0  C   C         CC
9  C x C   CCCCCCCC
8    x C   CCC   CC
7    O     CC     C
6    OCCCCCCC x x C
5    O      C I I C
4    O CCCC CC    C
3  C x C  C  C x CC
2  CCCCC xC  C x CC
1        x     x
0 ------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234567
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
