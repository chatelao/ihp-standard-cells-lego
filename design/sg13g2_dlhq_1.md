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
2 G G                    G G
1 G G                    G G
0 G G                    G G
9 G G                    G G
8 G G                    G G
7 G G                    G G
6 GGG                    GGG  G
5 G G                    G G
4 G G                    G G
3 G G                    G G
2 G G                    G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +     +           +      +
2  &     &c c cCcC   +      &
1  + C CCCC   C             + O
0  & c c cc cCc c c c c cCc & o
9  + C C  C  CC CCCCCCCCCCC + O
8    c      cCc cCcCc  CcC    o
7  IICC     CCC  C  C  CCCIICCO
6  iIcC Ccc c c cC  c cCcCiIcCo
5    CC     CCC     C  C CC COO
4    c c _ Cc     c c  Cc c cOo
3  - C C -  CCCCC   C    CCCCOO
2  _     _cCcCcCcCcCc     c
1  -     -           --    --
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | VSS3 | VSS4 | VSS5 | VSS7 | VSS8 | D | GATE | Q |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |   |   |
| NMOS2 |   | X | X | X | X | X |   |   |   |   | X |
| PMOS1 | X |   | X | X |   |   | X | X |   |   | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   | X |   |   |
| Poly2 |   |   |   |   |   |   |   |   |   | X |   |
| Poly3 |   |   |   |   |   |   |   |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | O |   |
| PMOS1 | O | O |   |
| PMOS2 |   |   |   |
