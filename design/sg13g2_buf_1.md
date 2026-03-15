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
GOLDEN STANDARD

```
  0123456
4 ppppppp
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
0 nnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
GOLDEN STANDARD

```
  0123456
4
3   G G
2   G G
1   G G
0   G G
9   G G
8  GG G
7   G G
6   G G
5   G G
4   G G
3   G G
2   G G
1   G G
0
```
Legend: G=Polysilicon
GOLDEN STANDARD

## Metal 1
```
  0123456
4 &+&+&+&
3    +
2    &
1  C + O
0  cCc o
9    C O
8  i c o
7    C O
6    CCO
5  CCC O
4  C   O
3    - O
2    -
1    -
0 -_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

