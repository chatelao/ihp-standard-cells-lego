# Design Documentation for sg13g2_sdfbbp_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901
4      NN          NN          NN          NN          NN     NN
3                                                             SS
2
1        NN              NN              NN             NN
0        NN              NN              NN             NN
9
8
7                                                   SS SS SS  SS
6                                                   SS SS SS  SS
5                                                             SS
4        SS              SS              SS
3        SS              SS              SS             SS
2                                                       SS
1
0
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901
4      pp          pp          pp          pp          pp     pp
3 N     NN          NN          NN          NN          NN     N
2 N     pp          pp          pp          pp          pp     N
1 N                                                            N
0 N     pp          pp          pp          pp          pp     N
9 N     pp          pp          pp          pp          pp     N
8 N                                                            N
7 S     SS          SS          SS          SS          SS     S
6 S       SS              SS              SS            SS     S
5 S       SS              SS              SS            SS     S
4 S     nn          nn          nn          nn          nn     S
3 S       nn              nn              nn            nn     S
2 S       nn              nn              nn            nn     S
1      SS          SS          SS          SS          SS     SS
0      nn          nn          nn          nn          nn     nn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
4
3  G G G G G   G G         G G G                    G G
2
1
0
9                          GGG
8
7  G GGG G G   G G         G GGG                    G G
6  GGG GGG G   GGG         G G G                    GGG
5
4        GGG
3
2
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
4    + ++    +    +++       +  ++  +      +++    +    +++   + ++
3    +       +    ++        +      +       +     +    +     +
2    + cCccC +    ++        + IIII +IIIIII +     +    +     +
1  C + C   C + C C++C       + I  I +I    I    C  +    + OOC + O
0  cCcCc c   CcC C++c  CcC  + IC I +I cCcIcCcCcCcCcCcCc oOc + o
9        CC  C   C  CC C  C & IC IIII CCCICC  CCC      COOC   O
8   I I   c cC CcCcC C Cc cCc ICcCcCc   cIIIII  c  Cc  CoOc   o
7   I i IiC  C C   C C  C C C i     C C C    I  C  C   C OCC  O
6   i   iIc  C CiI CcCcCc cCc   c c c c cCcCcCcCc cC i C OcC  o
5      CCCCCCC CII  CCCCC CCCCCCC   C C CC      C  C     OC   O
4      c  _ cC CcCcCcCc cCcCcCcCcCcCc-c cC  - c c cCc - oOc - o
3  -      - C   C     C C            -C  C  - C   C   - OOC - O
2  -      - cCcCc -         -  CcCcC -cCcC  - cCcCc   -     -
1  -      -       -         -        -      -         -     -
0  -   -- -       ---       -  --    -     --         ---   - --
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

