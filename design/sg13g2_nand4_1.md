# Design Documentation for sg13g2_nand4_1

## Substrate
```
  01234567890
5 NNNNNNNNNNN
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
5
4  ppppppppp
3  ppppppppp
2  ppppppppp
1
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
5
4  G  G G G
3  G  G G G
2  G  G G G
1  G  G G G
0  G  G G G
9  G  G G G
8  G  G G G
7  G  G G G
6  G  G G G
5  G  G G G
4  G  G G G
3  G  G G G
2  G  G G G
1  G  G G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
5 +++++++++++
4
3
2    x   x
1    O   O
0    O   O
9    OOOOOOOO
8           O
7           O
6  x Ix x x O
5      xxII O
4      IIx xO
3        x xO
2          xO
1
0 -----------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890
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
