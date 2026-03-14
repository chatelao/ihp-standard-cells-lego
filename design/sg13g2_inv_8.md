# Design Documentation for sg13g2_inv_8

## Substrate
```
  012345678901234567
4 NNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567
4
3  pppppppppppppppp
2  pppppppppppppppp
1  ppXppXpppXpppXpp
0
9
8
7
6       X
5  nnnnnnnnnXnnnXnn
4  nnXXXXXXXXnnnXnn
3  nnXnnXnnnXnnnXnn
2  nnXnnXnnnXnnnXnn
1  nnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567
4
3       G
2       G
1    X  X   X   X
0       G
9       G
8       G
7       G
6       X
5       G   X   X
4    XXXXXXXX   X
3    X  X   X   X
2    X  X   X   X
1       G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234567
4 ++++++++++++++++++
3
2
1    x  x   x   x
0    O  O   O   O
9    O  O   O   O
8    OOOOOOOO   O
7           O   O
6    IIIxII OOOOO
5           x   x
4    xxxxxxxx   x
3    x  x   x   x
2    x  x   x   x
1
0 ------------------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234567
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
