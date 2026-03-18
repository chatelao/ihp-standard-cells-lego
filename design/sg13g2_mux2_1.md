# Design Documentation for sg13g2_mux2_1

## Substrate
```
  012345678901234567
4      NN     NNNNNN
3                 SS
2                 SS
1        NN       NN
0        NN       NN
9
8
7                 SS
6                 SS
5                 SS
4        SS       SS
3        SS       SS
2                 SS
1                 SS
0                 SS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567
4      pp     pppppp
3 N     NN     NNNNN
2 N     pp     ppppN
1 N                N
0 N     pp      pp N
9 N     pp      pp N
8 N                N
7 S     SS     SSSSS
6 S       SS       S
5 S       SS       S
4 S     nn     nnnnS
3 S       nn       S
2 S       nn       S
1      SS     SSSSSS
0      nn     nnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567
4
3   G G  G G G
2
1
0
9
8
7   G G  G G G
6   GGG  GGGGG
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
  012345678901234567
4 c c &+& c c &+&+&+
3     +        +
2     & cCcCcCc+
1     + C     C+ OO
0  CcCcCc cC  c+ Oo
9  C     CCC  C+ OO
8  C   CcC    c+ Oo
7  C   C  I I C   O
6  CIi CI i i CC CO
5  C   CI   I    CO
4  c _ cIIIII CcCcO
3  C - CCCCCCCC-  O
2    _         _
1    -         -
0  c _ _-c c c-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

