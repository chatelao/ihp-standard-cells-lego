# Design Documentation for sg13g2_and4_2

## Substrate
```
  0123456789012345
4 NNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345
4
3  pppppppppppppp
2  pppppppppppppp
1  pppppppppppXXp
0
9
8
7
6    X X XX
5  nnnnnnnnnnnnXn
4  nnnnnnnnnnnXXn
3  nnnnnnnnnnnXXn
2  nnnnnnnnnnnXXn
1  nnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345
4
3   G G GGGG
2   G G GGGG
1   G G GGGG  XX
0   G G GGGG
9   G G GGGG
8   G G GGGG
7   G G GGGG
6   GXGXGXXG
5   G G GGGG   X
4   G G GGGG  XX
3   G G GGGG  XX
2   G G GGGG  XX
1   G G GGGG
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789012345
4 ++++++++++++++++
3
2
1    C   C    xx
0    C   C    OO
9    C   C    OO
8  CCCCCCCCCCCOO
7  C         C O
6  C x x xxI C O
5  C I I III   x
4  C          xx
3  CC         xx
2  CC         xx
1
0 ----------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345
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
