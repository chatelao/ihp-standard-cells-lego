# Design Documentation for sg13g2_buf_1

## Substrate
```
  0123456
3 NNNNNNN
2 NNNNNNN
1 NNNNNNN
0 NNNNNNN
9 NNNNNNN
8 NNNNNNN
7 SSSSSSS
6 SSSSSSS
5 SSSSSSS
4 SSSSSSS
3 SSSSSSS
2 SSSSSSS
1 SSSSSSS
0 SSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456
3
2  ppXpp
1  ppXpX
0  ppppX
9      X
8      X
7  X
6
5  nnnnn
4  nnnnn
3  nnXnX
2  nnXnX
1  nnXnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456
3
2  G X
1  G X X
0  G   X
9  G   X
8  G   X
7  X
6  G
5  G
4  G
3  G X X
2  G X X
1  G X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456
3 +++++++
2    x
1  C x x
0  C   x
9  CCC x
8    C x
7  x C O
6    CCO
5  CCC O
4  C   O
3    x x
2    x x
1    x
0 -------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456
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
