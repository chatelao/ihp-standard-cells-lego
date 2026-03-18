# Design Documentation for sg13g2_einvn_8

## Substrate
```
  012345678901234567890123456789012345678
4      NN          NN          NN     NNN
3                                       N
2                                       N
1        NN              NN         NN  N
0        NN              NN         NN  N
9                                       N
8                                       N
7                                   SS  S
6                                   SS  S
5                                       S
4        SS              SS         SS  S
3        SS              SS         SS  S
2                                       S
1                                       S
0                                       S
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678
4      pp          pp          pp     ppp
3 N     NN          NN          NN     NN
2 N     pp          pp          pp     pN
1 N                                    pN
0 N     pp          pp          pp     pN
9 N     pp          pp          pp     pN
8 N                                    pN
7 S     SS          SS          SS     SS
6 S       SS              SS       SSSSSS
5 S       SS              SS       SSSSSS
4 S     nn          nn          nn     nS
3 S       nn              nn       nnnnnS
2 S       nn              nn       nnnnnS
1      SS          SS          SS     SSS
0      nn          nn          nn     nnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789012345678
4
3 G G                       G G
2
1
0
9
8
7 G G                       G G
6 GGG                       GGG
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
  012345678901234567890123456789012345678
4 c+c c+&+c c+c c+c+& c c c c c+& c c &+&
3  +     +   +   +  +
2  +     +   +   +  +  Cc cCcCcCc cCcCc
1  + C C + C + C + C+  C   C   C   C  C
0  + c c + C + C + C+  C O C O C O C Oc
9  + C C + C + C + CCCCC O   O   O   OC
8  + c c ccCcCcCc cC     OoOcOoOcOc cO
7    C                   OOO
6  i c  Ccc cCc c c cCcC OoO cIIIIIIII
5    CCCC   C   C   C  C OOO  OO     O
4  - cCcC - c - c - c- C O   O   O   Oc
3  -  C C - C - C - C- CCCCCCCCC   C  C
2  -      -   -   -  -         CcCcCcCc
1  -      -   -   -  -
0  _ c _-c-c c-c c-_-_ c c c c _-c c c-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

