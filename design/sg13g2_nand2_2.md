# Design Documentation for sg13g2_nand2_2

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
2  ppXpppXpp
1
0
9
8        X
7    X    X
6
5  nnnnnnXnn
4  nnnnnnXnn
3  nnnnnnnnn
2  nnnnnnnnn
1  nnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890
5
4   G G  G G
3   G G  G G
2   GXG  X G
1   G G  G G
0   G G  G G
9   G G  G G
8   G G  X G
7   GXG  GXG
6   G G  G G
5   G G  X G
4   G G  X G
3   G G  G G
2   G G  G G
1   G G  G G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890
5 +++++++++++
4
3
2    x   x
1    O   O
0    OOOOO
9      O
8      O x
7    x O Ix
6    I OOO
5        x
4  CCCCC x C
3  C   C   C
2  C   CCCCC
1
0 -----------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

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
