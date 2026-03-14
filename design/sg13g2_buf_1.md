# Design Documentation for sg13g2_buf_1

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
1  ppppX
0
9
8
7  X
6
5  nnnnX
4  nnnnX
3  nnnnX
2  nnnnX
1  nnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456
4
3  G
2  G
1  G   X
0  G
9  G
8  G
7  X
6  G
5  G   X
4  G   X
3  G   X
2  G   X
1  G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456
4 +++++++
3
2
1  C   x
0  C   O
9  CCC O
8    C O
7  x C O
6    CCO
5  CCC x
4  C   x
3      x
2      x
1
0 -------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, O=Metal 1 Output, x=Connection (upper side)

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
