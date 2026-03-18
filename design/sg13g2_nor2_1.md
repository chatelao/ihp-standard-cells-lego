# Design Documentation for sg13g2_nor2_1

## Substrate
```
  0123456
4 NNNNNNN
3       N
2       N
1   NN  N
0   NN  N
9       N
8       N
7   SS  S
6   SS  S
5       S
4   SS  S
3   SS  S
2       S
1       S
0       S
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456
4 ppppppp
3 NNNNNNN
2 NpppppN
1 N    pN
0 N pp pN
9 N pp pN
8 N    pN
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
```
  0123456
4
3   G   G
2
1
0
9
8
7   G   G
6  GG  GG
5
4
3
2
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456
4 &+&+&+&
3   +
2   +
1   +  O
0   +  o
9   +OOO
8    o
7    O
6  i o i
5    O
4   -o -
3   -O -
2   -  -
1   -  -
0 -_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

