# Design Documentation for sg13g2_inv_1

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
3
2  ppp
1  ppp
0  ppp
9  ppp
8  ppp
7
6
5
4  nnn
3  nnn
2  nnn
1
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234
4
3   G
2   G
1   G
0   G
9   G
8   G
7   G
6  GG
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
  01234
4 &+&+&
3  +
2  +
1  + o
0  + o
9  + o
8    o
7    O
6  i O
5    O
4  - o
3  - o
2  -
1  -
0 -_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

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
Legend: M=Metal 2
