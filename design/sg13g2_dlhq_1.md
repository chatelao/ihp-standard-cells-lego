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
2 ppppNNNNNNNNNNNNNNNNNNNpppppNN
1 ppppNNNNNNNNNNNNNNNNNNNpppppNN
0 ppppNNNNNNNNNNNNNNNNNNNppppppN
9 ppppNNNNNNNNNNNNNNNNNNNpppppNN
8 ppppNNNNNNNNNNNNNNNNNNNppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 nnnnSSSnSSSSSSSSSSSSSSSnnnnnnS
3 nnnnSSSSSSSSSSSSSSSSSSSnnnnnSS
2 nnnnSSSnSSSSSSSSSSSSSSSnnnnnSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789
4
3
2 G G                     G
1 G G                     G
0 G G                     G
9 G G                     G
8 G G                     G G
7 G G                     G G
6 GGG                     GGG
5 G G                     G G
4 G G                     G G
3 G G                     G G
2 G G                     G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +     +           +      +
2  +     +cCc cCc    +      +
1  + CCCCCCC  C CCCCCCCCCCC + O
0  + CCc ccCcCc c   c   cCC + o
9  + CCC  C  CC CCCCCCCCCCC + O
8     Cc    cCcCcCcCc  CcC    o
7  II C     CCC  C  C  CCCII  O
6  IIcC CccCc c cC  c cCcCiICCo
5     C C  CCCCCCCC C  C C  C O
4    CCcC_cCcCcCc c c  Cc   C o
3  - CCCC-          CCCCCCCCC O
2  _     _cCcCcCcCcCc c c
1  -     -            -     -
0 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | GATE | Q | VDD | VSS |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   | X |
| NMOS2 |   |   |   | X |
| NMOS3 |   |   |   | X |
| NMOS4 |   | X |   |   |
| NMOS5 |   |   |   | X |
| PMOS2 |   | X |   |   |
| PMOS3 |   |   | X |   |
| Poly2 | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| NMOS3 |   |   |
| NMOS4 |   | O |
| NMOS5 |   |   |
| PMOS1 | O |   |
| PMOS2 |   | O |
| PMOS3 |   |   |
