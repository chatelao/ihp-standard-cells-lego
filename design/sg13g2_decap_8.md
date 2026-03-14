# Design Documentation for sg13g2_decap_8

## Substrate
```
  012345678901
3 NNNNNNNNNNNN
2 NNNNNNNNNNNN
1 NNNNNNNNNNNN
0 NNNNNNNNNNNN
9 NNNNNNNNNNNN
8 NNNNNNNNNNNN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SSSSSSSSSSSS
3 SSSSSSSSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 SSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901
3
2  XppXXXXppp
1  XppXXXXppp
0  XppXXXXppp
9  X  XXXX
8  X  XXXX
7
6
5  nnnnnnnnnn
4  nnnnnnnnnn
3  XXnnnXnnnX
2  XXnnnXnnnX
1  XXnnnXnnnX
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901
3
2  X  XXXX
1  X  XXXX
0  X  XXXX
9  X  XXXX
8  X  XXXX
7
6
5
4
3  XX   X   X
2  XX   X   X
1  XX   X   X
0
```
Legend: X=Connection (lower side)

## Metal 1
```
  012345678901
3 ++++++++++++
2  x  xxxx   +
1  x  xxxx   +
0  x  xxxx   +
9  x  xxxx   +
8  x  xxxx   +
7     ++++
6   - ++++  -
5   - ++++  -
4   -       -
3  xx   x   x-
2  xx   x   x-
1  xx   x   x-
0 ------------
```
Legend: +=VDD, -=VSS, x=Connection (upper side)

## Metal 2
```
  012345678901
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
