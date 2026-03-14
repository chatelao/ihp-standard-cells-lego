# Design Documentation for sg13g2_inv_2

## Substrate
```
  0123456
4 NNNNNNN
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
4
3  ppppp
2  ppppp
1  ppXpp
0
9
8
7
6  X
5  nnXnn
4  nnXnn
3  nnXnn
2  nnXnn
1  nnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456
4
3 G G
2 G G
1 G GX
0 G G
9 G G
8 G G
7 G G
6 GXG
5 G GX
4 G GX
3 G GX
2 G GX
1 G G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456
4 +++++++
3
2
1    x
0    O
9    O
8    O
7    O
6  x OOO
5    x
4    x
3    x
2    x
1
0 -------
```
Legend: +=VDD, -=VSS, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456
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
