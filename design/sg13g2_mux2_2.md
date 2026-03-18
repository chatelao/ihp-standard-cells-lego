# Design Documentation for sg13g2_mux2_2

## Substrate
```
  01234567890123456789
4      NN     NNNNNNNN
3                 SSSS
2                 SSSS
1        NN        NN
0        NN        NN
9
8
7
6                  SS
5                  SS
4        SS        SS
3        SS        SS
2
1
0
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789
4      pp     pppppppp
3 N     NN     NNNNNNN
2 N     pp     ppppppN
1 N                  N
0 N     pp       pp  N
9 N     pp       pp  N
8 N                  N
7 S     SS     SSSS  S
6 S       SS       SSS
5 S       SS         S
4 S     nn     nnnn  S
3 S       nn       nnS
2 S       nn         S
1      SS     SSSSSSSS
0      nn     nnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789
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
  01234567890123456789
4 c c &+& c c &+&+&+&+
3     +        +    +
2     & cCcCcCc+    &
1     + C     C+ OOO+
0  CcCcCc cC  c+ OoO&
9  C     CCC  C+ OOO+
8  C   CcC    c+ OoO&
7  CII C      C    O
6  CIi CI i i CC C O
5  C   CI   I CCCC O
4  c _ cIIIII C   Oo-
3    - CCCCCCCC-  OO-
2    _         _    -
1    -         -    -
0  c _ _-c c c-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

