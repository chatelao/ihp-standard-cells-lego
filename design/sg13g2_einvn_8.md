# Design Documentation for sg13g2_einvn_8

## Substrate
```
  012345678901234567890123456789012345678
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678
4
3  ppppppppppppppppppppppppppppppppppppp
2  ppppppppppppppppppppppppppppppppppppp
1  ppppppppppppppppppppppppppppppppppppp
0
9
8
7
6  X                              X
5  nnnnnnnnnnnnnnnnnnnnnnXXXnnnnnnnnnnnn
4  nnnnnnnnnnnnnnnnnnnnnnXXXXXXXXXXXXXnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnXnnnXnn
2  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0
```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234567890123456789012345678
4
3  G                              G
2  G                              G
1  G                              G
0  G                              G
9  G                              G
8  G                              G
7  G                              G
6  X                              X
5  G                     XXX      G
4  G                     XXXXXXXXXXXXX
3  G                             XG  X
2  G                              G
1  G                              G
0
```
Legend: G=Polysilicon, X=Connection (lower side)

## Metal 1
```
  012345678901234567890123456789012345678
4 +++++++++++++++++++++++++++++++++++++++
3
2
1    C C   C   C   C   CCCCCCCCCCCCCCCC
0    C C   C   C   C   C   C   C   C  C
9    C C   C   C   C   C O   O C O   OC
8    C C   C   C   CCCCC OOOOOOOOOOOOOC
7    C CCCCCCCCCCCCC     OOO
6  x C  CCCCCCCCCCCCCCCC OOO  IIIIxIII
5  I CCCC   C   C   C  C xxx
4    CCCC   C   C   C  C xxxxxxxxxxxxxC
3    CCCC   C   C   C  C         x   xC
2    CCCC   C   C   C  CCCCCCCCCCCCCCCC
1
0 ---------------------------------------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  012345678901234567890123456789012345678
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
