# Design Documentation for sg13g2_nor4_1

## Substrate
```
  01234567890
4 NNNNNNNNNNN
3 NNNNNNNNNNN
2 NNNNNNNNNNN
1 NNNNNNNNNNN
0 NNNNNNNNNNN
9 NNNNNNNNNNN
8 NNNNNNNNNNN
7 SSSSSSSSSSS
6 SSSSSSSSSSS
5 SSSSSSSSSSS
4 SSSSSSSSSSS
3 SSSSSSSSSSS
2 SSSSSSSSSSS
1 SSSSSSSSSSS
0 SSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890
4
3  ppppppppp
2  ppppppppp
1  ppppppppp
0
9
8
7
6
5  nnnnnnnnn
4  nnnnnnnnn
3  nnnnnnnnn
2  nnnnnnnnn
1  nnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890
4
3  G GGG GG
2  G GGG GG
1  G GGG GG
0  G GGG GG
9  G GGG GG
8  G GGG GG
7  G GGG GG
6  G GGG GG
5  G GGG GG
4  G GGG GG
3  G GGG GG
2  G GGG GG
1  G GGG GG
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
4 +++++++++++
3
2
1         xx
0         OO
9        xOO
8      x IOO
7      x x O
6  x x I IxO
5  I Ixx IIx
4    xxxxxxx
3    x   x
2    x   x
1
0 -----------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890
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
