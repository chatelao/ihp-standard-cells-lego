# Design Documentation for sg13g2_sighold

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
2  pppppppp
1
0
9
8
7
6
5  nnnnnnXn
4  nnnnnnXn
3  nnnnnnnn
2  nnnnnnnn
1  nnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
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
5        X
4        X
3
2
1
0
```
Legend: X=Connection (lower side)

## Metal 1
```
  0123456789
5 ++++++++++
4
3
2
1
0
9  C     C
8  C     C
7  CCCCCCC
6  C     C
5  CCCC  x
4  C     x
3
2
1
0 ----------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, x=Connection (upper side)

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
