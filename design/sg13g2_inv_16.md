# Design Documentation for sg13g2_inv_16

## Substrate
```
  012345678901234567890123456789012345
5 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345
5
4  pppppppppppppppppppppppppppppppppp
3  pppppppppppppppppppppppppppppppppp
2  pppppppppppppppppppppppppppppppppp
1
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456789012345
5
4                                  G
3                                  G
2                                  G
1                                  G
0                                  G
9                                  G
8                                  G
7                                  G
6                                  G
5                                  G
4                                  G
3                                  G
2                                  G
1                                  G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789012345
5 ++++++++++++++++++++++++++++++++++++
4
3
2    x   x   x   x    x   x   x   x
1    O   O   O   O    O   O   O   O
0    O   O   O   O    O   O   O   O
9    O   O   O   O    O   O   O   O
8    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
7    O   O   O   O    O   O   O
6    O   O   O   O    O   O   O   IxI
5    x   x   x   x    x   x   x
4    x   x   x   x    x   x   xxxxx
3    x   x   x   x    x   x   x   x
2    x   x   x   x    x   x   x   x
1
0 ------------------------------------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234567890123456789012345
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
