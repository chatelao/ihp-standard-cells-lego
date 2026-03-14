# Design Documentation for sg13g2_inv_8

## Substrate
```
  0123456789012345678
5 NNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678
5
4  ppppppppppppppppp
3  ppppppppppppppppp
2  ppXpppXpppXpppXpp
1
0
9
8
7
6       X
5  nnnnnnnnnnXnnnXnn
4  nnXXXXXXXXXnnnXnn
3  nnXnnnXnnnXnnnXnn
2  nnXnnnXnnnXnnnXnn
1  nnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678
5
4       G
3       G
2    X  GX   X   X
1       G
0       G
9       G
8       G
7       G
6       X
5       G    X   X
4    XXXXXXXXX   X
3    X  GX   X   X
2    X  GX   X   X
1       G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789012345678
5 +++++++++++++++++++
4
3
2    x   x   x   x
1    O   O   O   O
0    O   O   O   O
9    OOOOOOOOO   O
8            O   O
7            O   O
6    IIIxIII OOOOO
5            x   x
4    xxxxxxxxx   x
3    x   x   x   x
2    x   x   x   x
1
0 -------------------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345678
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
