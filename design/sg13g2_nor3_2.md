# Design Documentation for sg13g2_nor3_2

## Substrate
```
  0123456789012345
4      NN     NNNN
3
2
1        NN
0        NN
9
8
7
6
5
4        SS
3        SS
2
1
0
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345
4      pp     pppp
3 N     NN     NNN
2 N     pp     ppN
1 N            ppN
0 N     pp     ppN
9 N     pp     ppN
8 N            ppN
7 S     SS       S
6 S     SS     SSS
5 S     SS       S
4 S     nn       S
3 S     nn     nnS
2 S     nn       S
1      SS     SSSS
0      nn     nnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345
4
3   G G G G  G G
2
1
0
9
8
7   G G G G  G G
6   GGG GGG  GGG
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
  0123456789012345
4 c+c c+& c c &+&+
3  +   +
2  +   +
1  + C + CCCCCCCC
0  + C + Cc c o c
9  + C    C   O C
8    CcCcCc oOo c
7           O
6   Ii  IiOOO iI
5    OOOOOO OOO
4  _ o    O   O -
3  - O ---O - O -
2  _   _-_  -   -
1  -   ---  -   -
0  _ c _-_ c-c-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

