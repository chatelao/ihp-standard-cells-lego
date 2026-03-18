# Design Documentation for sg13g2_dlhq_1

## Substrate
```
  012345678901234567890123456789
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789
4 pppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NppppppppppppppppppppppppppppN
1 NppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppN
9 NppppppppppppppppppppppppppppN
8 NppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789
4
3 G G                     G G
2 G G                     G G
1 G G                     G G
0 G G                     G G
9 G G                     G G
8 G G                     G G
7 G G                     G G
6 GGG                     GGG
5 G G                     G G
4 G G                     G G
3 G G                     G G
2 G G                     G G
1 G G                     G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +     +           +      +
2  +     + Cc cCc    +      &
1  + CCCCCCC  C CCCCCCCCCCC + O
0  + CcC  cCcCc c       cCc & o
9  + CCC  C  CC CCCCCCCCCCC + O
8     c     cC CcC Cc  CcC    o
7  II C     CCC  C  C  CCCII  O
6  iI C CCCCC   CC  C  CCCIiCCO
5     C C  CCCCCCCC C  C C  C O
4    cC C_ cCcCcC C C  c    C O
3  - CCCC-          CCCCCCCCC O
2  _     _ cCcCcCcCcC
1  -     -            -     -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

