# Design Documentation for sg13g2_sdfrbp_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901234567
4      NN          NN          NN          NN          NN     NNNNNNNN
3                                                                 SSSS
2                                                                 SSSS
1        NN              NN              NN              NN        NN
0        NN              NN              NN              NN        NN
9
8
7
6                                                                  SS
5                                                                  SS
4        SS              SS              SS              SS        SS
3        SS              SS              SS              SS        SS
2
1
0
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901234567
4      pp          pp          pp          pp          pp     pppppppp
3 N     NN          NN          NN          NN          NN     NNNNNNN
2 N     pp          pp          pp          pp          pp     ppppppN
1 N                                                                  N
0 N     pp          pp          pp          pp          pp       pp  N
9 N     pp          pp          pp          pp          pp       pp  N
8 N                                                                  N
7 S     SS          SS          SS          SS          SS     SSSS  S
6 S       SS              SS              SS              SS       SSS
5 S       SS              SS              SS              SS         S
4 S     nn          nn          nn          nn          nn     nnnn  S
3 S       nn              nn              nn              nn       nnS
2 S       nn              nn              nn              nn         S
1      SS          SS          SS          SS          SS     SSSSSSSS
0      nn          nn          nn          nn          nn     nnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901234567
4
3   G G  G G G             G G             G G
2
1
0
9
8
7   G G  G G G             G G             G G
6   GGG  GGGGG             GGG             GGG
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
  01234567890123456789012345678901234567890123456789012345678901234567
4 c c &+& c c c+c c+&+c c c c c+& c c c c c+& c c c c c+& & c &+&+&+&+
3     +        +     +         +                          +   +   +
2     & cCcCcCc+     + CcCcCcC + CcCc c c cCc c c cCcCcCcC&   &   &
1     + C     C+ CC  + C     C + C  C                     + O +   + O
0  CcCcCc cC  c+ Cc  + CcCc cCcCcCc c   c c cCc c c       & o & c & o
9  C     CCC  C+ CC  +CCC   C     C C   C       C CC    C   O + C + O
8  C   CcC    c+ Cc    Cc cCcCcCcCc c cCc cCcCcCc cCc cCcCcCo & c   o
7  C   C  I I C   C    CC C II C  C C  C  CIII  C C C C    CO   C   O
6  CIi CI i i CC CCCCC CC   iI CC C CC C CC i CCC CCC    C CO   CC OO
5  C   CI   I    CC    CCCCCCCCCCCCCCC C  C I C  CCCCCCCCC COO  C   O
4  c _ cIIIII CcCcC    c  C   C      c    CcCcC CcCcCc     cOo  C - O
3  C - CCCCCCCC-  C  CCC-   - C CCCCCC        C      C -  CCO - C - O
2    _         _        -   - Cc c cCc c c c cCc c c   _      -   -
1    -         -        -   -                          -      -   -
0  c _ _-c c c _ c _-c c-c c-c _-c c c c c _-c c c c c _-c c c-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

