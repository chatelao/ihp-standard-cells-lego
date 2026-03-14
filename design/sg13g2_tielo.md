# Design Documentation for sg13g2_tielo

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
4  nnnnXn
3  nnnnXn
2  nnnXXn
1  nnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
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
4      X
3      X
2     XX
1
0
```
Legend: X=Connection (lower side)

## Metal 1
```
  01234567
5 ++++++++
4
3
2
1
0  C   C
9  C   C
8  C   C
7    C C
6    C C
5    C
4  CCC x
3      x
2     xx
1
0 --------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, x=Connection (upper side)

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
