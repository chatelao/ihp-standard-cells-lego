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
3
2 G GG    G G G G   G G GG G
1 G GG   GG G G G   G G GG G
0 G GG   GG G G G   G G GG G
9 G GG   GG G G G   G G GG G
8 G GG   GG G G G   G G GG GG
7 G GG   GG G G G   G G GG GG
6 GGGG   GG G G G   G G GGGGG
5 G GG   GG G G G   G G GG GG
4 G GG    G G G G   G G GG GG
3 G GG    G G G G   G G GG GG
2 G GG    G G G G   G G GG GG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +     +           +      +
2  &     &cCc cCcC   +      &
1  + C CCCCC  C             + O
0  & c c ccCcCc cCcCcCcCcCc & o
9  + C C  C  CC CCCCCCCCCCC + O
8    c      cCc cCcCc  CcC    o
7  IICC     CCCCCC  C  CCCIICCO
6  iIcC CccCc c cC  c cCcCiIcCo
5    CC C  CCCCCCCC C  C CC COO
4    c cC_ Cc     c c  Cc c cOo
3  - C CC-  CCCCC   CCCCCCCCCOO
2  _     _cCcCcCcCcCc     c
1  -     -            -    -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | D | GATE | Internal1 | Q |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |
| NMOS2 |   | X | X |   |   | X | X |
| PMOS1 | X |   | X |   |   | X | X |
| PMOS2 | X |   |   |   |   |   |   |
| Poly1 |   |   |   | X |   | X |   |
| Poly2 |   |   | X |   |   |   |   |
| Poly3 |   |   | X |   |   |   |   |
| Poly4 |   |   | X |   |   |   |   |
| Poly5 |   |   | X |   |   |   |   |
| Poly6 |   |   | X |   |   |   |   |
| Poly7 |   |   | X |   |   |   |   |
| Poly8 |   |   | X |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | O | O | O |
| PMOS1 | O | O | O | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |
