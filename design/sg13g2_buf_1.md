# Design Documentation for sg13g2_buf_1

## Substrate
```
  0123456
4 NNNNNNN
3 NNNNNNN
2 NNNNNNN
1 NNNNNNN
0 NNNNNNN
9 NNNNNNN
8 NNNNNNN
7 SSSSSSS
6 SSSSSSS
5 SSSSSSS
4 SSSSSSS
3 SSSSSSS
2 SSSSSSS
1 SSSSSSS
0 SSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456
4 NNNNNNN
3 NNNNNNN
2 NpppppN
1 NpppppN
0 NpppppN
9 NpppppN
8 NpppppN
7 SSSSSSS
6 SSSSSSS
5 SSSSSSS
4 SnnnnnS
3 SnnnnnS
2 SnnnnnS
1 SSSSSSS
0 SSSSSSS
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456
4
3   G
2   G
1   G
0   G
9   G
8  GG
7   G
6   G
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
  0123456
4 &+&+&+&
3    +
2    &
1  C + O
0  xCx o
9    C O
8  i x o
7    C O
6    CCO
5  CCC O
4  C   O
3    - O
2    -
1    -
0 -_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

