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
4  G  GG  G
3  G  GG  G
2  G  GG  G
1  G  GG  G
0  G  GG  G
9  G  GG  G
8  G  GG  G
7  G  GG  G
6  G  GG  G
5  G  GG  G
4  G  GG  G
3  G  GG  G
2  G  GG  G
1  G  GG  G
0  G  GG  G
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
4 +++++++++++
3  x
2  x
1  x      xx
0  +     xOO
9  +     IOO
8      x x O
7  x x x IxO
6  I Ixx IIO
5          x
4  x xxxxxxx
3  x x x x x
2  x   x   x
1  x   x   x
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
