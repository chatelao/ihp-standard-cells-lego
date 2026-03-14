# Design Documentation for sg13g2_buf_16

## Substrate
```
  012345678901234567890123456789012345678901234567
5 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678901234567
5
4  pppppppppppppppppppppppppppppppppppppppppppppp
3  pppppppppppppppppppppppppppppppppppppppppppppp
2  pppppppppppppppppppppppppppppppppppppppppppppp
1
0
9
8
7
6
5  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456789012345678901234567
5
4                                           G
3                                           G
2                                           G
1                                           G
0                                           G
9                                           G
8                                           G
7                                           G
6                                           G
5                                           G
4                                           G
3                                           G
2                                           G
1                                           G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789012345678901234567
5 ++++++++++++++++++++++++++++++++++++++++++++++++
4
3
2    x   x   x   x   x   x   x   x   C    C   C
1    O   O   O   O   O   O   O   O   C    C   C
0    O   O   O   O   O   O   O   O   C    C   C
9    OOOOO   OOOOOOOOOOOOOOOOOOOOO CCCCCCCCCCCC
8    O   O   O   O   O   O         C
7    O   O   O   O   O   O         C
6    O   OOOOO   O   O   O CCCCCCCCC       IxII
5    x   x   x   x   x   x         C
4    x   x   x   x   x   xxxxxxxxx CCCCCCCCCCCC
3    x   x   x   x   x   x   x   x   C    C   C
2    x   x   x   x   x   x   x   x   C    C   C
1
0 ------------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234567890123456789012345678901234567
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
