# Design Documentation for sg13g2_mux4_1

## Substrate
```
  0123456789012345678901234567890123456
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456
4 ppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NpppppppppppppppppppppppppppppppppppN
1 NpppppppppppppppppppppppppppppppppppN
0 NpppppppppppppppppppppppppppppppppppN
9 NpppppppppppppppppppppppppppppppppppN
8 NpppppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456
4
3
2  GG   GGG GGG GGG G GG GG G G GG G
1  GG   GGG GGG GGG G GG GG G G GG G
0  GG   GGG GGGGGGG G GG GG G G GG G
9  GG   GGG GGGGGGG G GG GG G G GG GG
8  GG   GGG GGGGGGG G GG GG G G GG GG
7  GG G GGG GGGGGGG G GG GG G G GG GG
6  GGGGGGGG GGGGGGG G GGGGG G G GGGGG
5  GG G GGG GGGGGGG G GG GG G G GG GG
4  GG G GGG GGGGGGG G GG GG G G GG
3  GG   GGG GGG GGG G    GG G G GG
2  GG   GGG GGG GGG G    GG G G GG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3     +        +        +           +
2     +        +&CcCcCcC&   cCcCcCc &
1  CC +        + C     C+ C C     C + O
0  cC +   cC    cC CcC CcCc c c cCc & o
9  CC +   CCCCCCCC CCC    C C C CCCCC O
8  cC +   cC  i i  CcCcC  c c c c   c o
7  C I I  C   I I   CCCCIIC C CCCII C O
6  c i iCcc c i i c c cCiIc c c cIi c o
5  C    C C C     C CCCCCCC C CCCC   OO
4  cCcCcC c cCcCcCcCcCc cCc   cCcC - Oo
3  C  - C   C  -   CCC - CCCCC CCC - OO
2     - CccCc  -    c  - CcCcCcC   -
1     -        -       -           -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | A0 | A1 | A2 | A3 | S0 | S1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |
| NMOS2 |   |   | X |   |   |   |   |   |   |
| PMOS1 | X |   | X |   | X | X |   |   |   |
| PMOS2 | X |   |   |   |   |   |   |   |   |
| Poly1 |   |   | X | X |   |   |   | X |   |
| Poly2 | X |   | X |   | X | X |   |   |   |
| Poly3 |   |   | X |   |   |   |   |   |   |
| Poly4 |   |   | X |   |   |   | X |   |   |
| Poly5 |   |   | X |   |   |   |   |   |   |
| Poly6 |   |   | X |   |   |   |   |   |   |
| Poly7 |   |   | X |   |   |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | O | O |
| PMOS1 | O | O | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |
