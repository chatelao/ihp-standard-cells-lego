# Design Documentation for sg13g2_einvn_2

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
3 G G          G G
2
1
0
9
8
7 G G          G G
6 GGG          GGG
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
4 c & c+& & c &+&+
3   +     +
2   +     + cCcCc
1   + C C + C   C
0   + C C + c o c
9     C CCCCC O C
8  IIIC       o
7  IIIC       O
6  iIICc      o i
5  IIIC       O I
4     C CccCc o I
3   - C C - CCCCC
2   -     -
1   -     -
0  c-c _-c-c c-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

