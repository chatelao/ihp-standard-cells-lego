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
1  pppppppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567
4
3       G
2       G
1       G
0       G
9       G
8       G
7       G
6       G
5       G
4       G
3       G
2       G
1       G
0
```
Legend: G=Polysilicon

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
