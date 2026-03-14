# Design Documentation for sg13g2_inv_4

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
7     X
6
5  nnnnnnnnX
4  nnXXXXXXX
3  nnXnnnXnn
2  nnXnnnXnn
1  nnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890
5
4     G
3     G
2     G
1     G
0     G
9     G
8     G
7     X
6     G
5     G    X
4    XXXXXXX
3    XG  X
2    XG  X
1     G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890
5 +++++++++++
4
3
2
1    O   O
0    O   O
9    OOOOOOO
8          O
7   IIxIII O
6   IIIIII O
5          x
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
