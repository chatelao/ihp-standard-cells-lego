# Design Documentation for sg13g2_nand2b_1

## Substrate
```
  012345678
3 NNNNNNNNN
2 NNNNNNNNN
1 NNNNNNNNN
0 NNNNNNNNN
9 NNNNNNNNN
8 NNNNNNNNN
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 SSSSSSSSS
3 SSSSSSSSS
2 SSSSSSSSS
1 SSSSSSSSS
0 SSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678
3
2  ppXppXp
1  ppXXpXp
0  ppXXppp
9    XXXXX
8        X
7
6  X X
5  nnnnnnn
4  nnnnnnn
3  nnXnnXX
2  nnXnnXX
1  nnXnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678
3
2  G X  X
1  G XX X
0  G XX
9  G XXXXX
8  G G   X
7  G G
6  X X
5  G G
4  G G
3  G X  XX
2  G X  XX
1  G X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678
3 +++++++++
2    x  x
1    xx x
0  C xx
9  C xxxxx
8  CCCCC x
7      C O
6  x x CCO
5      C O
4  CCCCCOO
3  C x  xx
2    x  xx
1    x
0 ---------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678
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
