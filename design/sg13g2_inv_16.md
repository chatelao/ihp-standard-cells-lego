# Design Documentation for sg13g2_inv_16

## Substrate
```
  0123456789012345678901234567890123
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123
4
3  pppppppppppppppppppppppppppppppp
2  pppppppppppppppppppppppppppppppp
1  ppXpppXpppXppXpppXpppXpppXpppXpp
0
9
8
7
6                                X
5  nnXnnnXnnnXnnXnnnXnnnXnnnXnnnnnn
4  nnXnnnXnnnXnnXnnnXnnnXnnnXXXXnnn
3  nnXnnnXnnnXnnXnnnXnnnXnnnXnnnXnn
2  nnXnnnXnnnXnnXnnnXnnnXnnnXnnnXnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123
4
3                                G
2                                G
1    X   X   X  X   X   X   X   XG
0                                G
9                                G
8                                G
7                                G
6                                X
5    X   X   X  X   X   X   X    G
4    X   X   X  X   X   X   XXXX G
3    X   X   X  X   X   X   X   XG
2    X   X   X  X   X   X   X   XG
1                                G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789012345678901234567890123
4 ++++++++++++++++++++++++++++++++++
3
2
1    x   x   x  x   x   x   x   x
0    O   O   O  O   O   O   O   O
9    O   O   O  O   O   O   O   O
8    OOOOOOOOOOOOOOOOOOOOOOOOOOOO
7    OOOOOOOOOOOOOOOOOOOOOOOO
6    O   O   O  O   O   O   O   IxI
5    x   x   x  x   x   x   x
4    x   x   x  x   x   x   xxxx
3    x   x   x  x   x   x   x   x
2    x   x   x  x   x   x   x   x
1
0 ----------------------------------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345678901234567890123
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
