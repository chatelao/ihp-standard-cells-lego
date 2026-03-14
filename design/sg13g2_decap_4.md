# Design Documentation for sg13g2_decap_4

## Substrate
```
  0123456
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
3
2  XppXX
1  XppXX
0  XppXX
9  X  XX
8  X  XX
7
6
5  nnnnn
4  nnnnn
3  nXnnn
2  XXnnn
1  XXnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456
3
2  X  XX
1  X  XX
0  X  XX
9  X  XX
8  X  XX
7
6
5
4
3   X
2  XX
1  XX
0
```
Legend: X=Connection (lower side)

## Metal 1
```
  0123456
3 +++++++
2 +x  xx+
1 +x  xx+
0 +x  xx+
9 +x  xx+
8 +x  xx+
7     +
6   - +
5   - +
4   -
3   x
2 -xx   -
1 -xx   -
0 -------
```
Legend: +=VDD, -=VSS, x=Connection (upper side)

## Metal 2
```
  0123456
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
