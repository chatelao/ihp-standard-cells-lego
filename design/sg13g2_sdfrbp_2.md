# Design Documentation for sg13g2_sdfrbp_2

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4      NN          NN          NN          NN          NN         NN    N
3                                                                       N
2                                                                       N
1        NN              NN              NN              NN         NN  N
0        NN              NN              NN              NN         NN  N
9                                                                       N
8                                                                       N
7                                                                   SS  S
6                                                                   SS  S
5                                                                       S
4        SS              SS              SS              SS         SS  S
3        SS              SS              SS              SS         SS  S
2                                                                       S
1                                                                       S
0                                                                       S
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4      pp          pp          pp          pp          pp         pp    p
3 N     NN          NN          NN          NN          NN     NNNNNNNNNN
2 N     pp          pp          pp          pp          pp     pppppppppN
1 N                                                                    pN
0 N     pp          pp          pp          pp          pp        pp   pN
9 N     pp          pp          pp          pp          pp        pp   pN
8 N                                                                    pN
7 S     SS          SS          SS          SS          SS     SSSSSSSSSS
6 S       SS              SS              SS              SS       SSSSSS
5 S       SS              SS              SS              SS       SSSSSS
4 S     nn          nn          nn          nn          nn     nnnnnnnnnS
3 S       nn              nn              nn              nn       nnnnnS
2 S       nn              nn              nn              nn       nnnnnS
1      SS          SS          SS          SS          SS         SS    S
0      nn          nn          nn          nn          nn         nn    n
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901234567890
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
  01234567890123456789012345678901234567890123456789012345678901234567890
4 c c &+& c c c+c c+&+c c c c c+& c c c c c+& c c c c c+& & c & c &+c & &
3     +        +     +         +                          +   +   +   +
2     + CccCcCc+     + CcCcCcC + CcCc c c cCc c c cCcCcCcC+   +   +   +
1     + C     C+ CC  + C     C + C  C                     + O +   + OO+
0  cCcCcC cC  c+ Cc  + CcCc cCcCcCc c   c c cCc c c       + o + cC+ oO+
9  C     CCC  C+ CC  +CCC   C     C C   C       C CC    C   O + CC+ OO+
8  c   cCc    c+ Cc    Cc cCcCcCcCc c cCc cCcCcCc cCc cCcCcCo + cC+ oO+
7  C   C  I I C   C    CC C II C  C C  C  CIII  C C C C    CO    C   O
6  cIi cI i i cC CcCcC Cc   iI Cc c cC C Cc i cCc cCc    C CoOo  CcC Oo
5  C   CI   I    CC    CCCCCCCCCCCCCCC C  C I C  CCCCCCCCC C  O   C   OO
4  c - cIIIII cCcCc    C  c   c      C    cCcCc cCcCcC     C  o   c - oO
3  C - CCCCCCCC-  C  CCC-   - C CCCCCC        C      C -  CC- O - C - O-
2    -         -        -   - c c cCc c c c c cCc cC   -    -   -   -  -
1    -         -        -   -                          -    -   -   -  -
0  c _ _-c c c _ c _-c c-c c-c _-c c c c c _-c c c c c _-c c-c c-c-_-c _-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

