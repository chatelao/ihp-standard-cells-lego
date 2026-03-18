# Design Documentation for sg13g2_dfrbpq_2

## Substrate
```
  01234567890123456789012345678901234567890123456789
4      NN          NN          NN          NN     NN
3                                                 SS
2
1        NN              NN              NN       NN
0        NN              NN              NN       NN
9
8
7                                                 SS
6                                                 SS
5                                                 SS
4        SS              SS              SS       SS
3        SS              SS              SS       SS
2                                                 SS
1                                                 SS
0                                                 SS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789
4      pp          pp          pp          pp     pp
3 N     NN          NN          NN          NN     N
2 N     pp          pp          pp          pp     N
1 N                                                N
0 N     pp          pp          pp          pp     N
9 N     pp          pp          pp          pp     N
8 N                                                N
7 S     SS          SS          SS          SS     S
6 S       SS              SS              SS       S
5 S       SS              SS              SS       S
4 S     nn          nn          nn          nn     S
3 S       nn              nn              nn       S
2 S       nn              nn              nn       S
1      SS          SS          SS          SS     SS
0      nn          nn          nn          nn     nn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789
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
  01234567890123456789012345678901234567890123456789
4 c+c c+& c c+c c c+& c c c c c+& c c c c+c+& & c &+
3  +         +                           +    +   +
2  + CcCcCcC + CcCc c c cCc c c cCcCcCcC +    &   &
1  + C      C+ C  C                      + C  + O +
0  + CcCc c cCcCc c   c c cCc c c        + C  & o &
9  + CC   C     C C   C        CCC     C   C  + O +
8    Cc cCcCcCcCc c  Cc cCcCcC CcCcCcCcCcC C    o
7    CC C II C  C C  C  C      CC  CC    C C    O
6  i CC   Ii C CC CC C CC iI CCCCC C    CC CCC  OOO
5    CCCCCCCCC CCCCC C  C    C  CCCCCCCCCC  C   O
4    c  C   C      c    CcCc cCcCcCc     c- C - O -
3  CCC-   - C CCCCCC         C      C-  CC- C - O -
2     -   - Cc c cCc c c c cCc c cC  _    -   -   -
1     -   -                          -    -   -   -
0  c c-_-c-c c c c _-c c c c c _-c c _ c c-_-c-c c-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

