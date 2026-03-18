# Design Documentation for sg13g2_dfrbp_2

## Substrate
```
  01234567890123456789012345678901234567890123456789012
4      NN          NN          NN          NN     NNNNN
3                                                 SSSSN
2                                                 SSSSN
1        NN              NN              NN        NN N
0        NN              NN              NN        NN N
9                                                     N
8                                                     N
7                                                     S
6                                                  SS S
5                                                  SS S
4        SS              SS              SS        SS S
3        SS              SS              SS        SS S
2                                                     S
1                                                     S
0                                                     S
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012
4      pp          pp          pp          pp     ppppp
3 N     NN          NN          NN          NN     NNNN
2 N     pp          pp          pp          pp     pppN
1 N                                                pppN
0 N     pp          pp          pp          pp     pppN
9 N     pp          pp          pp          pp     pppN
8 N                                                pppN
7 S     SS          SS          SS          SS     SSSS
6 S       SS              SS              SS        S S
5 S       SS              SS              SS        S S
4 S     nn          nn          nn          nn     nnnS
3 S       nn              nn              nn        n S
2 S       nn              nn              nn        n S
1      SS          SS          SS          SS     SSSSS
0      nn          nn          nn          nn     nnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012
4
3 G G     G G            G G
2
1
0
9
8
7 G G     G G            G G
6 GGG     GGG            GGG
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
  01234567890123456789012345678901234567890123456789012
4 c+c c+& c c+c c c+& c c c c c+& c c c c+c+& c & &+&+&
3  +         +                           +  +   +   +
2  + CcCcCcC + CcCc c c cCc c c cCcCcCcC +  &   &   &
1  + C      C+ C  C                      + O+   + OO+
0  + CcCc c cCcCc c   c c cCc c c        + O& cC& oO&
9  + CC   C     C C   C        CCC     C   O+ CC+ OO+
8    Cc cCcCcCcCc c  Cc cCcCcC CcCcCcCcCcC O& cC& oO&
7    CC C II C  C C  C  C      CC  CC    C O   C   O
6  i CC   Ii C CC CC C CC iI CCCCC C    CC OO  CCC OO
5    CCCCCCCCC CCCCC C  C    C  CCCCCCCCCC  O   C   OO
4    c  C   C      c    CcCc cCcCcCc     c  O   C - Oo
3  CCC-   - C CCCCCC         C      C-  CC- O - C - O -
2     -   - Cc c cCc c c c cCc c cC  _    -   -   -   -
1     -   -                          -    -   -   -   -
0  c c-_-c-c c c c _-c c c c c _-c c _ c c-_-c-c c-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

