# Design Documentation for sg13g2_nand4_1

## Substrate
```
  01234567890
4     NN    N
3       SSSSN
2       SSSSN
1     NN    N
0     NN    N
9           N
8           N
7   SSSS    S
6   SSSS SS S
5        SS S
4           S
3     SS    S
2     SS    S
1           S
0           S
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890
4     pp    p
3 NNNNNNNNNNN
2 NpppppppppN
1 N        pN
0 N   pp   pN
9 N   pp   pN
8 N        pN
7 SSSSSSSSSSS
6 SSSSSSSSSSS
5 SSSSSSSSSSS
4 SnnnnnnnnnS
3 SnnnnnnnnnS
2 SnnnnnnnnnS
1     SS    S
0     nn    n
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890
4
3 G G G G G
2
1
0
9
8
7 G G G G G
6 GGGGGGGGG
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
  01234567890
4 c+c &+c c+&
3  +   +   +
2  +   +   +
1  + O + O +
0  + O + O +
9  + OOOOOOO
8          O
7          O
6  i i i i O
5      I I O
4  _     I o
3  -     I O
2  _
1  -
0  _ c-_ c c-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

