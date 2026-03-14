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
1  pppppppppppppppppppppppppppppppp
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345678901234567890123
4
3                                G
2                                G
1                                G
0                                G
9                                G
8                                G
7                                G
6                                G
5                                G
4                                G
3                                G
2                                G
1                                G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123
4 ++++++++++++++++++++++++++++++++++
3
2
1    o   o   o  o   o   o   o   o
0    O   O   O  O   O   O   O   O
9    O   O   O  O   O   O   O   O
8    OOOOOOOOOOOOOOOOOOOOOOOOOOOO
7    OOOOOOOOOOOOOOOOOOOOOOOO
6    O   O   O  O   O   O   O   IiI
5    o   o   o  o   o   o   o
4    o   o   o  o   o   o   oooo
3    o   o   o  o   o   o   o   o
2    o   o   o  o   o   o   o   o
1
0 ----------------------------------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, i=Metal 1 Input Connection, o=Metal 1 Output Connection

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
