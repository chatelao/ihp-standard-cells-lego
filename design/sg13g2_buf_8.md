# Design Documentation for sg13g2_buf_8

## Substrate
```
  0123456789012345678901234
5 NNNNNNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234
5
4  ppppppppppppppppppppppp
3  ppppppppppppppppppppppp
2  ppppppppXpppXpppXpppXpp
1
0
9
8
7
6     X
5  nnnnnnnnnnnnnnnnnnnnXnn
4  nnnnnnnnXXXXXXXXXXXXXnn
3  nnnnnnnnXnnnXnnnXnnnXnn
2  nnnnnnnnXnnnXnnnXnnnXnn
1  nnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234
5
4     G
3     G
2     G    X   X   X   X
1     G
0     G
9     G
8     G
7     G
6     X
5     G                X
4     G    XXXXXXXXXXXXX
3     G    X   X   X   X
2     G    X   X   X   X
1     G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  0123456789012345678901234
5 +++++++++++++++++++++++++
4
3
2  C   C   x   x   x   x
1  C   C   O   O   O   O
0  C   C   O   O   O   O
9  CCCCCCC OOOOOOOOOOOOO
8        C             O
7        C             O
6   IIxI CCCCCCCCCCCCC OOO
5        C             x
4  CCCCCCC xxxxxxxxxxxxx
3  C   C   x   x   x   x
2  C   C   x   x   x   x
1
0 -------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  0123456789012345678901234
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
