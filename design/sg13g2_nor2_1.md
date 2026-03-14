# Design Documentation for sg13g2_nor2_1

## Substrate
```
  01234567
5 NNNNNNNN
4 NNNNNNNN
3 NNNNNNNN
2 NNNNNNNN
1 NNNNNNNN
0 NNNNNNNN
9 NNNNNNNN
8 NNNNNNNN
7 SSSSSSSS
6 SSSSSSSS
5 SSSSSSSS
4 SSSSSSSS
3 SSSSSSSS
2 SSSSSSSS
1 SSSSSSSS
0 SSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567
5
4  pppppp
3  pppppp
2  pppppp
1
0
9
8
7
6
5  nnnnnn
4  nnnnnn
3  nnnnnn
2  nnnnnn
1  nnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567
5
4   G  G
3   G  G
2   G  G
1   G  G
0   G  G
9   G  G
8   G  G
7   G  G
6   G  G
5   G  G
4   G  G
3   G  G
2   G  G
1   G  G
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567
5 ++++++++
4
3
2      x
1      O
0      O
9    OOO
8    O
7    O
6  IxO x
5    x
4    xx
3    xx
2    xx
1
0 --------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

## Metal 2
```
  01234567
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
