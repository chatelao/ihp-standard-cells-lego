# Design Documentation for sg13g2_dlhrq_1

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
3 G G G G             G G
2
1
0
9
8
7 G G G G             G G
6 GGG GGG             GGG
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
4 c c+c+& c & c c c+& c & &+&
3    +      +       +   +
2    +      + cCcC  +   +
1  C +      + C  C  + C + OO
0  cCc cCcc c cC C    c + oO
9  CCC CC C C CC C CCCC + OO
8    c  C c c cCcCcCc c   oO
7  I CIICCC CCC C   C CI   O
6  i cIiC c   c cC    ci C O
5  CCC  C CCCCC CC   CCCCC O
4  c    CccCcC CcC   C     O
3     - C     C  C - C  - OO
2     -     - cCcC -    -
1     -     -      -    -
0  c c-_-c c-c c c _-c c-c-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

