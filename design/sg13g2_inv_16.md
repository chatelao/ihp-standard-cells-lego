# Design Documentation for sg13g2_inv_16

## Substrate
```
  0123456789012345678901234567890123
4      NN          NN         NN
3                                 SS
2                                 SS
1        NN              NN       NN
0        NN              NN       NN
9
8
7                                 SS
6                                 SS
5                                 SS
4        SS              SS       SS
3        SS              SS       SS
2                                 SS
1                                 SS
0                                 SS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123
4      pp          pp         pp
3 N     NN          NN     NNNNNNNNN
2 N     pp          pp     ppppppppN
1 N                                N
0 N     pp          pp        pp   N
9 N     pp          pp        pp   N
8 N                                N
7 S     SS          SS     SSSSSSSSS
6 S       SS              SS       S
5 S       SS              SS       S
4 S     nn          nn     nnnnnnnnS
3 S       nn              nn       S
2 S       nn              nn       S
1      SS          SS         SS
0      nn          nn         nn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123
4
3                               G G
2
1
0
9
8
7                               G G
6                               GGG
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
  0123456789012345678901234567890123
4 c+c c+& c+c c+c &+& & c & c &+&+&
3  +   +   +   +  +   +   +   +   +
2  +   +   +   +  +   +   +   +   +
1  + O + O + O +O + O + O + O + O +
0  + o + o + O +o + o + o + o + o +
9  + O   O   O  O   O   O   O   O +
8    o c ooOcOc o c o oOo c oOoOo
7    O   O   O  O   O   O   O
6    o   o   O  o   o   o   o   IiI
5    O   O   O  O   O   O   O
4  - o - o - O -o - o - o - oOoOo-
3  - O - O - O -O - O - O - O - O-
2  -   -   -   -  -   -   -   -  -
1  -   -   -   -  -   -   -   -  -
0  _ c _-c _ c _ c-_-c-c c-c c-_ _ c
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

