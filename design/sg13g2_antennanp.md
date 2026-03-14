# Design Documentation for sg13g2_antennanp

## Substrate
```
  01234
4 NNNNN
3 NNNNN
2 NNNNN
1 NNNNN
0 NNNNN
9 NNNNN
8 NNNNN
7 SSSSS
6 SSSSS
5 SSSSS
4 SSSSS
3 SSSSS
2 SSSSS
1 SSSSS
0 SSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234
4
3  ppp
2  ppp
1  ppp
0
9
8
7
6
5  nnn
4  nnn
3  nnn
2  nnn
1  nnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234
4
3  GG
2  GG
1  GG
0  GG
9  GG
8  GG
7  GG
6  GG
5  GG
4  GG
3  GG
2  GG
1  GG
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234
4 +++++
3
2
1
0
9  IxI
8  III
7  x
6  I
5  I
4  I
3   xI
2   II
1
0 -----
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, x=Connection (upper side)

## Metal 2
```
  01234
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
