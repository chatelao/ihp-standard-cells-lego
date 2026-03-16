# Design Documentation for sg13g2_sdfbbp_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901
4 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
4
3  G G G G G   G G         G G G                    G G
2  G G G G G   G G         G G G                    G G
1  G G G G G   G G         G G G                    G G
0  G G G G G   G G         G G G                    G G
9  G G G G G   G G         GGG G                    G G
8  G G G G G   G G         G G G                    G G
7  G GGG G G   G G         G GGG                    G G
6  GGG GGG G   GGG         G G G                    GGG
5  G G G G G   G G         G G G                    G G
4  G G G GGG   G G         G G G                    G G
3  G G G G G   G G         G G G                    G G
2  G G G G G   G G         G G G                    G G
1  G G G G G   G G         G G G                    G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
4 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
3    +       +    ++        +      +      +++    +    +     +
2    + ccccc +    ++        + IIII +IIIIII+++    +    +     +
1  c + c   c + c c++c       + I  I +I    I    c  +    + ooc + o
0  ccccc c   ccc c++c  ccc  + Ic I +I cccIccccccccccccc ooc + o
9        cc  c   c  cc c  c & Ic IIII cccIcc  ccc      cooc   o
8   I I   c cc ccccc c cc ccc Icccccc   cIIIII  c  cc  cooc   o
7   I i IIC  C c   C C  C C C i     C C C    I  C  C   C OCC  O
6   i   iIC  C ciI CCCCCC CcC   C C C C CCCCCCCCC CC i C OCC  O
5      cCcCcCC cII  CCCCC CcCcCcC   C C CC      C  C     OC   O
4      c  _ cc cccccccc ccccccccccccc-c cc  - c c ccc - ooc - o
3  -      - c   c     c c            -c  c  - c   c   - ooc - o
2  -      - ccccc -         -  ccccc -cccc  - ccccc   -     -
1  -      -       -         -        -      -         -     -
0 --------------------------------------------------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

