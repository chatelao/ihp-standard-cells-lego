# Design Documentation for sg13g2_nand4_1

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
3  G G GGG
2  G G GGG
1  G G GGG
0  G G GGG
9  G G GGG
8  G G GGG
7  G G GGG
6  G G GGG
5  G G GGG
4  G G GGG
3  G G GGG
2  G G GGG
1  G G GGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
4 +++++++++++
3
2
1    x   x
0    O   O
9    O   O
8    OOOOOOO
7          O
6  x x x x O
5      x I x
4      x x x
3        x x
2          x
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
