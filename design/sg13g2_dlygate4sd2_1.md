# Design Documentation for sg13g2_dlygate4sd2_1

## Substrate
```
  01234567890123
4 NNNNNNNNNNNNNN
3 NNNNNNNNNNNNNN
2 NNNNNNNNNNNNNN
1 NNNNNNNNNNNNNN
0 NNNNNNNNNNNNNN
9 NNNNNNNNNNNNNN
8 NNNNNNNNNNNNNN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 SSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123
4 NNNNNNNNNNNNNN
3 NNNNNNNNNNNNNN
2 NppppppppppppN
1 NppppppppppppN
0 NppppppppppppN
9 NppppppppppppN
8 NppppppppppppN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SnnnnnnnnnnnnS
3 SnnnnnnnnnnnnS
2 SnnnnnnnnnnnnS
1 SSSSSSSSSSSSSS
0 SSSSSSSSSSSSSS
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123
4
3   G
2   G
1   G
0   G
9   G
8   G
7   G
6  GG
5   G
4   G
3   G
2   G
1   G
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &+&+&+&+&+&+&+
3    +       +
2    &       &
1    +    C  + O
0  x &  C C  & O
9  CCCC C C    O
8     C C CxCx O
7  II C C    C O
6  iI C CCC CC O
5     C C CCCOOO
4  CxCx x x    O
3  C -  C    - O
2    -       -
1    -       -
0 -_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

