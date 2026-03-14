# Design Documentation for sg13g2_nor2_1

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
2  pXppp
1  pXppX
0  pXppX
9   X  X
8   XXXX
7
6  X   X
5  nnnnn
4  nnnnn
3  nXXnX
2  nXXnX
1  nXnnX
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456
3
2  GX  G
1  GX  X
0  GX  X
9  GX  X
8  GXXXX
7  G   G
6  X   X
5  G   G
4  G   G
3  GXX X
2  GXX X
1  GX  X
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456
3 +++++++
2   x
1   x  x
0   x  x
9   x  x
8   xxxx
7    O
6  x O x
5    O
4    O
3   xx x
2   xx x
1   x  x
0 -------
```
Legend: +=VDD, -=VSS, O=Metal 1 Output, x=Connection (upper side)

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
