# Design Documentation for sg13g2_buf_1

## Substrate
```
  01234567
5 NNNNNNNN
4 NNNNNNNN
3 NNNNNNNN
2 NNNNNNNN
1 NNNNNNNN
0 NNNNNNNN
9 NNNNNNNN
8 NNNNNNNN
7 SSSSSSSS
6 SSSSSSSS
5 SSSSSSSS
4 SSSSSSSS
3 SSSSSSSS
2 SSSSSSSS
1 SSSSSSSS
0 SSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567
5
4  pppppp
3  pppppp
2  ppppXX
1
0
9
8   X
7
6
5  nnnnnX
4  nnnnXX
3  nnnnXX
2  nnnnXX
1  nnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567
5
4   G
3   G
2   G  XX
1   G
0   G
9   G
8   X
7   G
6   G
5   G   X
4   G  XX
3   G  XX
2   G  XX
1   G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567
5 ++++++++
4
3
2  C   xx
1  C   OO
0  CCC OO
9     COO
8  Ix COO
7     C O
6     C O
5  CCCC x
4  C   xx
3      xx
2      xx
1
0 --------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567
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
