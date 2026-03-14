# Design Documentation for sg13g2_nor2b_1

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
2  ppppppXp
1
0
9
8
7
6  X     X
5  nnnnXnnn
4  nnnnXnnn
3  nnnnXnnn
2  nnnnXnnn
1  nnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789
5
4  G     G
3  G     G
2  G     X
1  G     G
0  G     G
9  G     G
8  G     G
7  G     G
6  X     X
5  G   X G
4  G   X G
3  G   X G
2  G   X G
1  G     G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789
5 ++++++++++
4
3
2        x
1        O
0  C     O
9  C   OOO
8  CCCCO
7     CO
6  x  CO x
5     Cx
4  CCCCx
3      x
2      x
1
0 ----------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, O=Metal 1 Output, x=Connection (upper side)

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
