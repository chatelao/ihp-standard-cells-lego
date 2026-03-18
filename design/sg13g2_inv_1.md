# Design Documentation for sg13g2_inv_1

## Substrate
```
  01234
4 NNNNN
3 SSSSN
2 SSSSN
1  NN N
0  NN N
9     N
8     N
7     S
6  SS S
5  SS S
4  SS S
3  SS S
2     S
1     S
0     S
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234
4 ppppp
3 NNNNN
2 NpppN
1 NpppN
0 NpppN
9 NpppN
8 NpppN
7 SSSSS
6 S S S
5 S S S
4 SnnnS
3 S n S
2 S n S
1 SSSSS
0 nnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234
4
3   G
2
1
0
9
8
7   G
6  GG
5
4
3
2
1
0
```
Legend: G=Polysilicon

## Metal 1
GOLDEN STANDARD

```
  01234
4 &&&&&
3  +
2  & o
1  + O
0  & o
9  + O
8  & o
7    O
6  i O
5    O
4  _ o
3  - O
2  _ o
1  -
0 _____
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

