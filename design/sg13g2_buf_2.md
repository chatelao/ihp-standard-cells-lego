# Design Documentation for sg13g2_buf_2

## Substrate
```
  012345678
4 NNNNNNNNN
3 NNNNNNNNN
2 NNNNNNNNN
1 NNNNNNNNN
0 NNNNNNNNN
9 NNNNNNNNN
8 NNNNNNNNN
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 SSSSSSSSS
3 SSSSSSSSS
2 SSSSSSSSS
1 SSSSSSSSS
0 SSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678
4 ppppppppp
3 NNNNNNNNN
2 NpppppppN
1 NpppppppN
0 NpppppppN
9 NpppppppN
8 NpppppppN
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 SnnnnnnnS
3 SnnnnnnnS
2 SnnnnnnnS
1 SSSSSSSSS
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678
4
3       G G
2       G G
1       G G
0       G G
9       G G
8       G G
7       G G
6       GGG
5       G G
4       G G
3       G G
2       G G
1       G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &+&+&+&+&
3  +    +
2  +    &
1  +    +C
0  +cCcCcC
9  CC  C C
8  C  oC
7  C  OC
6  COOOCIi
5     OCCC
4   - O  c
3   - O -C
2   -   -
1   -   -
0 -_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

