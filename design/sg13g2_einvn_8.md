# Design Documentation for sg13g2_einvn_8

## Substrate
```
  012345678901234567890123456789012345678901
5 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678901
5
4  pppppppppppppppppppppppppppppppppppppppp
3  pppppppppppppppppppppppppppppppppppppppp
2  pppppppppppppppppppppppppppppppppppppppp
1
0
9
8
7
6  X                                X
5  nnnnnnnnnnnnnnnnnnnnnnnnXXXnnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnnnXXXXXXXXXXXXXnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456789012345678901
5
4  G                                G
3  G                                G
2  G                                G
1  G                                G
0  G                                G
9  G                                G
8  G                                G
7  G                                G
6  X                                X
5  G                       XXX      G
4  G                       XXXXXXXXXXXXX
3  G                                G
2  G                                G
1  G                                G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234567890123456789012345678901
5 ++++++++++++++++++++++++++++++++++++++++++
4
3
2                        CCCCCCCCCCCCCCCCC
1    C  C   C   C   C    C   C   C   C   C
0    C  C   C   C   C    C O C O C O C O C
9    C  C   C   C   CCCCCC O   O   O   O C
8    C  CCCCCCCCCCCCC      OOOOOOOOOOOOO
7    C                     OOO
6  x C   CCCCCCCCCCCCCCCCC OOO  IIIIxIIII
5  I CCC C   C   C   C   C xxx
4     CC C   C   C   C   C xxxxxxxxxxxxx C
3     CC C   C   C   C   C       C   C   C
2     CC C               CCCCCCCCCCCCCCCCC
1
0 ------------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234567890123456789012345678901
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
