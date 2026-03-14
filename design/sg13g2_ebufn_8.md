# Design Documentation for sg13g2_ebufn_8

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
4                                         G   G
3                                         G   G
2                                         G   G
1                                         G   G
0                                         G   G
9                                         G   G
8                                         G   G
7                                         G   G
6                                         G   G
5                                         G   G
4                                         G   G
3                                         G   G
2                                         G   G
1                                         G   G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789012345678901234567
5 ++++++++++++++++++++++++++++++++++++++++++++++++
4
3
2  CCCCCCCCCCCCCCCCC   C   C   C   C          C
1  C   C   C   C   C   C   C   CCCCC          C
0  C O C O C O C O CCCCCCCCCCCCC     CCCCCCCCCC
9  C O   O   O   O CCCCCCCCCCCCCCCCCCC        CCC
8    OOOOOOOOOOOOO C                  CCCCC     C
7    O  CCCCCCCCCCCC                  C         C
6    O  CCCCCCCCCC CCCCCCCCCCCCCCCCC  C IIxI Ix C
5    xxxxxxxxxxxxx C   C   C   C   C  C         C
4  C x   x   x   x C   C   C   C   C  C   C   CCC
3  C   C   C   C   C   C   C   C   C CCCCCC   C
2  CCCCCCCCCCCCCCCCC
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
