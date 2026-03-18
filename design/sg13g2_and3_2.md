# Design Documentation for sg13g2_and3_2

## Substrate
```
  012345678901
4      NN
3
2
1      NN
0      NN
9
8
7   SS SS SS
6   SS SS SS
5
4
3      SS
2      SS
1
0
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901
4      pp
3 N    NN    N
2 N    pp    N
1 N          N
0 N    pp    N
9 N    pp    N
8 N          N
7 S    SS    S
6 S    SS    S
5 S    SS    S
4 S    nn    S
3 S    nn    S
2 S    nn    S
1      SS
0      nn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901
4
3     GGGG
2
1
0
9
8
7     GGGG
6     GGGG
5
4     GGG
3
2
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 c c+c+&+c c+
3    +   +   +
2    +   +   +
1   C+ C + O +
0   C+ c + Oo
9   C  C    O
8   CcCcCcc o
7   C IIIIC O
6   C IiiI  o
5   C      OO
4      i - O -
3      I - O -
2  IIIII -   -
1        -   -
0  c c _-_ c _
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

