# Design Documentation for sg13g2_slgcp_1

## Substrate
```
  012345678901234567890123456789
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789
4 pppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789
4
3 G G G G             G G
2 G G G G             G G
1 G G G G             G G
0 G G G G             G G
9 G G G G             G G
8 G G GGG             G G
7 G G G G             G G
6 GGG G G             GGG
5 G G G G             G G
4 G G G G             G G
3 G G G G             G G
2 G G G G             G G
1 G G G G             G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +     +        +         +
2  +     +        &         &
1  +   c +        & ccccc c & o
0  +   ccccccc c    c   c c & o
9       c    c c    ccc  cc & o
8    IIic  c   ccccccc   ccc  o
7  I    c CCCCCC    CC I C C  O
6  i  cCc C   CCCCC CC i C CCCO
5     c  CCCC C CCC CC     C  O
4  - cc     c c c cccc -  cc_ o
3  - cccccccccc c-c  c -  cc_ o
2  -   -    ccccc-cccc -    _
1  -   -         -     -    -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

