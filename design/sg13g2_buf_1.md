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
2  pppppp
1
0
9
8
7
6
5  nnnnnn
4  nnnnnn
3  nnnnnn
2  nnnnnn
1  nnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567
5
4   G
3   G
2   G
1   G
0   G
9   G
8   G
7   G
6   G
5   G
4   G
3   G
2   G
1   G
0
```
Legend: G=Polysilicon

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
