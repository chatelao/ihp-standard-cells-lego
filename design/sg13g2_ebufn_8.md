# Design Documentation for sg13g2_ebufn_8

## Substrate
```
  01234567890123456789012345678901234567890123
4      NN          NN          NN     NNNNNNNN
3
2
1        NN              NN            NN
0        NN              NN            NN
9
8
7                                   SS SS SS
6                                   SS SS SS
5
4        SS              SS
3        SS              SS            SS
2                                      SS
1
0
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123
4      pp          pp          pp     pppppppp
3 N     NN          NN          NN     NNNNNNN
2 N     pp          pp          pp     ppppppN
1 N                                          N
0 N     pp          pp          pp       pp  N
9 N     pp          pp          pp       pp  N
8 N                                          N
7 S     SS          SS          SS     SSSSSSS
6 S       SS              SS           SS    S
5 S       SS              SS           SS    S
4 S     nn          nn          nn     nnnnnnS
3 S       nn              nn           nn    S
2 S       nn              nn           nn    S
1      SS          SS          SS     SSSSSSSS
0      nn          nn          nn     nnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123
4
3                                     G G G G
2
1
0
9
8
7                                     G G G G
6                                     GGG GGG
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
  01234567890123456789012345678901234567890123
4 c c c+& c c c c c+& c+c c+c c+& c c &+&+&+&+
3                   +  +   +   +         +   +
2  c cCcCcc c cCcCc +  +   +   +         +   +
1  C  C   C   C   C   C+ C + CCCCC       + C +
0  cO C O c o c o cCcCcCcCc cC     CcCcCcCcC +
9  CO   O   O   O      CC     CCCCCC       CCC
8  cOoOoOooOo c o c                 cCcC     C
7    O  CCCCCCCCC C                 C        C
6    o  CccCcCcCc cCcCc cCc cCc cC  c IiI Ii C
5   OO  OOO O   O C   C   C  C   C  C        C
4  cO   O   o   o c - c - c- C - C  c  C - CcC
3  C  C   C   C   C - C - C- C - C CCCCC - C -
2  c cCcCcc c cCcCc -   -  -   -         -   -
1                   -   -  -   -         -   -
0  c c _-c c c c c _-c c-c _ c _-c c c-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

