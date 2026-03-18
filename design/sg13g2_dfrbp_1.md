# Design Documentation for sg13g2_dfrbp_1

## Substrate
```
  0123456789012345678901234567890123456789012345678901
4      NN          NN          NN          NN     NNNN
3                                                 SSSS
2                                                 SSSS
1        NN              NN              NN        NN
0        NN              NN              NN        NN
9
8
7
6                                                  SS
5                                                  SS
4        SS              SS              SS        SS
3        SS              SS              SS        SS
2
1
0
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456789012345678901
4      pp          pp          pp          pp     pppp
3 N     NN          NN          NN          NN     NNN
2 N     pp          pp          pp          pp     ppN
1 N                                                ppN
0 N     pp          pp          pp          pp     ppN
9 N     pp          pp          pp          pp     ppN
8 N                                                ppN
7 S     SS          SS          SS          SS       S
6 S       SS              SS              SS       SSS
5 S       SS              SS              SS         S
4 S     nn          nn          nn          nn       S
3 S       nn              nn              nn       nnS
2 S       nn              nn              nn         S
1      SS          SS          SS          SS     SSSS
0      nn          nn          nn          nn     nnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901
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
  0123456789012345678901234567890123456789012345678901
4 c+c c+& c c+c c c+& c c c c c+& c c c c &+& c c+&+&+
3  +         +                            +      +
2  + cCcCccC +cCcCc c c cCc c c cCcCcCcC  +      +
1  + C      C+C   C                       + O  C + O
0  + cCcC c cCc c c    Cc cCc c c         + o  C + O
9  + CC   C     C C    C       CCCCC   C    O  C + O
8    cC CccCcCcCc c cCcCcCcCcC Cc  CcCcCcCc o  C + O
7  I CC C II C  C C  C  C      CC  CC     C O  C   O
6  i cC   Ii C Cc cCcC Cc iI CcCcC CcCcCc c o  CcCcO
5  I CCCCCCCCC CCCC CC  C    C  CCCC      C O  C   O
4  I c  C   c       cCcCcCcC CcCcCcC     Cc o  C - O
3  CCC-   - C CCCCCCC        C      C-  CC- O  C - O
2     -   - c c cCc c c c c cCc c c  -    -      -
1     -   -                          -    -      -
0  c c-_-c-c c c c _-c c c c c _-c c _ c c-_-c c _-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

