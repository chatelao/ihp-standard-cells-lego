# Design Documentation for sg13g2_dllrq_1

## Substrate
```
  0123456789012345678901234567
4      NN          NN     NNNN
3
2
1        NN            NN
0        NN            NN
9
8
7                   SS SS SS
6                   SS SS SS
5
4        SS
3        SS            SS
2                      SS
1
0
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567
4      pp          pp     pppp
3 N     NN          NN     NNN
2 N     pp          pp     ppN
1 N                        ppN
0 N     pp          pp     ppN
9 N     pp          pp     ppN
8 N                        ppN
7 S     SS          SS     SSS
6 S       SS           SS    S
5 S       SS           SS    S
4 S     nn          nn     nnS
3 S       nn           nn    S
2 S       nn           nn    S
1      SS          SS     SSSS
0      nn          nn     nnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567
4
3   G G G               G G
2
1
0
9
8
7   G G G               G G
6   GGGGG               GGG
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
  0123456789012345678901234567
4 c c &+& c & c c c+&+& c &+&+
3     +     +       +++   +
2     +     +       +++   +
1     +             +++ C + O
0  c  + Ccc cCc c c +++ c + o
9  CC + CC     CC C CCCCCCCCO
8  c  + CccCcCcCc c cCcC   Co
7  C I I C C    CCCCCC C I C O
6  c i i c CcCcC     CcC i C O
5  C     C CCCCCCCC  C C I
4  cC   CccCcC   CcCcC C  - o
3  C   CC   CC   C     C  - O
2                    - C  - o
1     -      -       -    -
0  c c-_-c c _ c c _-_ c c-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

