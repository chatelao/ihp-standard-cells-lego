# Design Documentation for sg13g2_buf_16

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
3                                       G G
2
1
0
9
8
7                                       G G
6                                       GGG
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
4 c+c c+& c c & c &+& & c & c+c+&+c c+&+&+&+&+
3  +   +      +   +   +   +  +   +   +   +
2  +   +  &+  &   &   &   &  +   +   +   +  &+
1  + O + O++O + O + O + O + O+ O + C + C + C++
0  + O + Oc o & o & o & o & o+ O + C + C + Cc
9  + OOOOO  O   OOO O   OOOOOOOO   C CCC   C
8    O   O  o   o   o   o        C
7    O   O  O   O   O   O        C
6    O   OOOO   O   O   O CCCCCCCC      IiII
5    O   O  O   O   O   O        C
4  _ o _ o-_O - O - O - OoOoOoOo c c cCc c c--
3  - O - O--O - O - O - O - O- O - C - C - C--
2  _   _  -_  -   -   -   -  _   _   _   _  --
1  -   -  --  -   -   -   -  -   -   -   -  --
0  _ c _-c-_ c-c c-_-c-c c-c _ _-_ c _-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

