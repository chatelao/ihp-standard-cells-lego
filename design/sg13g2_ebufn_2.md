# Design Documentation for sg13g2_ebufn_2

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
3            G G G
2
1
0
9
8
7            G G G
6            GGGGG
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
4 c c c+&+c c &+&+&+
3        +     +
2  cCcCc +     +
1  C   CCCCC   + CC
0  c o c   CcCcCcCc
9    O C   C     CC
8    o     CcC   Cc
7    O     CC     C
6    oCcCccCc i i c
5    O      C     C
4  c o cCcc cC - Cc
3  C   C -C  C - CC
2  cCcCc -c    -
1        -     -
0  c c _-_ c c-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

