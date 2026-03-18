# Design Documentation for sg13g2_ebufn_4

## Substrate
```
  012345678901234567890123456
4      NN          NN     NNN
3                       SSSSN
2                       SSSSN
1        NN           NN    N
0        NN           NN    N
9                           N
8                           N
7                   SSSS    S
6                   SSSS SS S
5                        SS S
4        SS                 S
3        SS           SS    S
2                     SS    S
1                           S
0                           S
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456
4      pp          pp     ppp
3 N     NN          NN     NN
2 N     pp          pp     pN
1 N                        pN
0 N     pp          pp     pN
9 N     pp          pp     pN
8 N                        pN
7 S     SS          SS     SS
6 S       SS       SSSSSSSSSS
5 S       SS       SSSSSSSSSS
4 S     nn          nn     nS
3 S       nn       nnnnnnnnnS
2 S       nn       nnnnnnnnnS
1      SS          SS     SSS
0      nn          nn     nnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456
4
3   G G G
2
1
0
9
8   GGG
7   G G G
6   G GGG
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
  012345678901234567890123456
4 c c+c+& c c+c c+c+& c c &+&
3    +       +   +
2    +       +   + CcCcCcCcC
1  C +      C+ C + C   C   C
0  cCcCcCc  cCcC + C O C O C
9  C     CCCCC C   C O   O C
8  cIi cCcc  C CcCcC OoOoO
7  CI     C  C   CC    C O
6  cI  iI c         cCcC O
5  C   I  C CCCCCCCC OOOOO
4  c - I  c c- C - C O   O C
3  C - CCCC C- C - C   C   C
2    -    c  -   - CcCcCcCcC
1    -       -   -
0  c _ _-c c _ c _ _-c c c-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

