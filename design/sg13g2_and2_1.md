# Design Documentation for sg13g2_and2_1

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
2  ppppppXX
1
0
9
8
7
6     X
5  nnnnnnnX
4  nnnnnnXX
3  XnnnnnXX
2  nnnnnnnn
1  nnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789
5
4  G  G
3  G  G
2  G  G  XX
1  G  G
0  G  G
9  G  G
8  G  G
7  G  G
6  G  X
5  G  G   X
4  G  G  XX
3  X  G  XX
2  G  G
1  G  G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789
5 ++++++++++
4
3
2    C   xx
1    C   OO
0    C   OO
9    C   OO
8  CCCCCCOO
7  C    C O
6  C Ix C O
5  C      x
4  C     xx
3 IxI    xx
2 III
1
0 ----------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

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
