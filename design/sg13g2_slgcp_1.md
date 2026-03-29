# Design Documentation for sg13g2_slgcp_1

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
2 G GGGGG GGG G G     G G
1 G GGGGG GGG G G     G G
0 G GGGGGGGGG G G G   G G
9 GGGGGGGGGGG G G G   G G
8 GGGGGGGGGGG G G G   G G   G
7 GGGGGGGGGGG G G G   G G   G
6 GGGGGGGGGGG G G G   G G   G
5 GGGGGGGGGGG G G G   G G   G
4 G GGGGGGGGG G G G   G G
3 G GGGGGGGGG G G G   G G
2 G GGG GGGGG G G G   G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +     +        +         +
2  &     &        &         &
1  +   C +        + CCCCC C +OO
0  &   cCccCcC C    c c c c &Oo
9       C    C C    CCC C C +OO
8  i iIiCccC CcCcCcCcCc c cC Oo
7  I  I CCCCCCCC   C C IC  C  O
6  i cCcCci cCcCcCcC CiIcC CcCo
5    C   C CC C    C C     C  O
4  _ c c c  c cCcCcCcCc-  cC_ o
3  - CCCCCCCCCCC -C  C -  CC- O
2  _   _  c cCcC -cCcC -    _
1  -   -         -     -    -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | CLK | GATE | Input1 | SCE | Internal1 | GCLK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |
| NMOS2 |   | X | X |   |   |   |   | X | X |
| PMOS1 | X |   | X |   | X |   | X | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |
| Poly1 |   |   | X |   | X | X | X |   |   |
| Poly2 |   |   | X |   |   |   |   |   |   |
| Poly3 |   |   | X |   |   |   |   |   |   |
| Poly4 |   |   | X |   |   |   |   |   |   |
| Poly5 |   |   | X | X |   |   |   |   |   |
| Poly6 |   |   | X |   |   |   |   |   |   |
| Poly7 |   |   |   |   |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | O | N |
| PMOS1 | O | O | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |
