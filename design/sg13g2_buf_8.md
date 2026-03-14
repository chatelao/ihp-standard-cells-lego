# Design Documentation for sg13g2_buf_8

## Substrate
```
  01234567890123456789012
4 NNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012
4
3  ppppppppppppppppppppp
2  ppppppppppppppppppppp
1  pppppppXpppXpppXpppXp
0
9
8
7
6     X
5  nnnnnnnnnnnnnnnnnnnXn
4  nnnnnnnXXXXXXXXXXXXXn
3  nnnnnnnXnnnXnnnXnnnXn
2  nnnnnnnXnnnXnnnXnnnXn
1  nnnnnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012
4
3     G
2     G
1     G   X   X   X   X
0     G
9     G
8     G
7     G
6     X
5     G               X
4     G   XXXXXXXXXXXXX
3     G   X   X   X   X
2     G   X   X   X   X
1     G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  01234567890123456789012
4 +++++++++++++++++++++++
3
2
1  C  C   x   x   x   x
0  C  C   O   O   O   O
9  C  C   O   O   O   O
8  CCCCCCCOOOOOOOOOOOOO
7        C            O
6   IIxI CCCCCCCCCCC  OO
5        C            x
4  CCCCCCCxxxxxxxxxxxxx
3  C  C   x   x   x   x
2  C  C   x   x   x   x
1
0 -----------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567890123456789012
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
