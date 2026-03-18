# Design Documentation for sg13g2_dlhq_1

## Substrate
```
  012345678901234567890123456789
4      NN          NN     NNNNNN
3                             SS
2                             SS
1        NN             NN
0        NN             NN
9
8
7                   SS SS SS  SS
6                   SS SS SS  SS
5                             SS
4        SS
3        SS             SS
2                       SS
1
0
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789
4      pp          pp     pppppp
3 N     NN          NN     NNNNN
2 N     pp          pp     ppppN
1 N                            N
0 N     pp          pp      pp N
9 N     pp          pp      pp N
8 N                            N
7 S     SS          SS     SSSSS
6 S       SS            SS     S
5 S       SS            SS     S
4 S     nn          nn     nnnnS
3 S       nn            nn     S
2 S       nn            nn     S
1      SS          SS     SSSSSS
0      nn          nn     nnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789
4
3 G G                     G G
2
1
0
9
8
7 G G                     G G
6 GGG                     GGG
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
  012345678901234567890123456789
4 c+c c+&+c c c c c+&+c c &+&+&+
3  +     +           +      +
2  +     + Cc cCc    +      +
1  + CCCCCCC  C     CC    C + O
0  + cCc  cCcCc c       cCc + o
9  + CCC  C  CC CCCCCCCCCC  + O
8     C     cC CcC Cc  CcC    o
7  II C     CCC  C  C  CCCII  O
6  iI C CccCc   cC  c  CcCIicCo
5     C C  CCCCCCCC C  C C  C O
4    cC C- CcCcCc c c  C    c o
3  - CCCC-          CCCCCCCCC O
2  -     - Cc cCc c c
1  -     -            -     -
0  _ c _-_ c c c c _-c-c c-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

