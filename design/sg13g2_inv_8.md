# Design Documentation for sg13g2_inv_8

## Substrate
```
  012345678901234567
4      NN     NNNNNN
3                 SS
2                 SS
1        NN       NN
0        NN       NN
9
8
7                 SS
6                 SS
5                 SS
4        SS       SS
3        SS       SS
2                 SS
1                 SS
0                 SS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567
4      pp     pppppp
3 N     NN     NNNNN
2 N     pp     ppppN
1 N                N
0 N     pp      pp N
9 N     pp      pp N
8 N                N
7 S     SS     SSSSS
6 S       SS       S
5 S       SS       S
4 S     nn     nnnnS
3 S       nn       S
2 S       nn       S
1      SS     SSSSSS
0      nn     nnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567
4
3   G G
2
1
0
9
8
7   G G
6   GGG
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
  012345678901234567
4 c+c c+& & c &+&+&+
3  +   +  +   +   +
2  +   +  +   +   +
1  + O +O + O + O +
0  + o +O + o + o +
9  + OOOOOOOO + O +
8           o   o
7           O   O
6    iIIIII oOoOo
5           O   O
4  - oOoOooOo - o -
3  - O -O - O - O -
2  -   -  -   -   -
1  -   -  -   -   -
0  _ c _-c-c c-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

