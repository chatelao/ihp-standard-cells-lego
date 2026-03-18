# Design Documentation for sg13g2_nor2b_2

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
3 G G     G G
2
1
0
9
8
7 G G     G G
6 G G     GGG
5
4
3 GGG
2
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 c c+c+& c c+
3    +       +
2    +       +
1  C + CCCCC +
0  c + c   C +
9  C +   O C +
8  c   oOo
7  CCC O   I
6  c   o   i
5  C   OOOOO
4    - o   O -
3  i - O - O -
2  I -   -   -
1    -   -   -
0  c _ _-_ c _
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

