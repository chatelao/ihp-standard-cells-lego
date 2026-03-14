# Design Documentation for sg13g2_nor2b_1

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
2  ppXpppp
1  ppXppXX
0  ppXppXX
9    X  XX
8      XXX
7
6  X    X
5  nnnnnnn
4  nnnnnnn
3  nnnnXnX
2  nnXnXnX
1  nnXnnnX
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678
3
2  G X  G
1  G X  XX
0  G X  XX
9  G X  XX
8  G   XXX
7  G    G
6  X    X
5  G    G
4  G    G
3  G   XGX
2  G X XGX
1  G X  GX
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678
3 +++++++++
2    x
1    x  xx
0  C x  xx
9  C x  xx
8  CCC xxx
7    C O
6  x C OxI
5    C O
4  CCC O -
3      x x
2    x x x
1    x   x
0 ---------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

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
