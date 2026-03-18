# Design Documentation for sg13g2_sdfrbpq_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901
4      NN          NN          NN          NN          NN     NN
3                                                             SS
2
1        NN              NN              NN             NN
0        NN              NN              NN             NN
9
8
7                                                   SS SS SS  SS
6                                                   SS SS SS  SS
5                                                             SS
4        SS              SS              SS
3        SS              SS              SS             SS
2                                                       SS
1
0
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901
4      pp          pp          pp          pp          pp     pp
3 N     NN          NN          NN          NN          NN     N
2 N     pp          pp          pp          pp          pp     N
1 N                                                            N
0 N     pp          pp          pp          pp          pp     N
9 N     pp          pp          pp          pp          pp     N
8 N                                                            N
7 S     SS          SS          SS          SS          SS     S
6 S       SS              SS              SS            SS     S
5 S       SS              SS              SS            SS     S
4 S     nn          nn          nn          nn          nn     S
3 S       nn              nn              nn            nn     S
2 S       nn              nn              nn            nn     S
1      SS          SS          SS          SS          SS     SS
0      nn          nn          nn          nn          nn     nn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
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
  01234567890123456789012345678901234567890123456789012345678901
4 c c &+& c c c+c c+&+c c c c c+& c c c c c+& c c c c c+& & & &+
3     +        +     +         +                          + +
2     & cCcCcCc+     + CcCcCcC + CcCc c c cCc c c cCcCcCcC& &
1     + C     C+ CC  + C     C + C  C                     + + O
0  CcCcCc cC  c+ Cc  + CcCc cCcCcCc c   c c cCc c c       & & o
9  C     CCC  C+ CC  +CCC   C     C C   C       C CC    C   + O
8  C   CcC    c+ Cc    Cc cCcCcCcCc c cCc cCcCcCc cCc cCcCcC& o
7  C   C  I I C   C    CC C II C  C C  C  CIII  C C C C    C  O
6  CIi CI i i CC CCCCC CC   iI CC C CC C CC i CCC CCC    C CC O
5  C   CI   I    CC    CCCCCCCCCCCCCCC C  C I C  CCCCCCCCC C OO
4  c _ cIIIII CcCcC    c  C   C      c    CcCcC CcCcCc     c oO
3  C - CCCCCCCC-  C  CCC-   - C CCCCCC        C      C -  CC- O
2    _         _        -   - Cc c cCc c c c cCc c c   _    -
1    -         -        -   -                          -    -
0  c _ _-c c c _ c _-c c-c c-c _-c c c c c _-c c c c c _-c c-c-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

