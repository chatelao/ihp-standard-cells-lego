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
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNpppNNNNNNNNpNppppppppNpppppNNpppppp
0 NNpppppppppppppppppppppNpppppNNpppppp
9 NNpppppppppppppppppppppNpppppNNpppppp
8 NNpppppppppppppppppppppNNNNNNNNpppppp
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSnnnnnSSnnnnnn
4 SnnnnnnnnnnnnnnnnnnnnnSnnnnnnSSnnnnnn
3 SnnnnnnnnnnnnnnnnnnnnnSnnnnnnSSnnnnnn
2 SSSSSSSSSSSSSSSSSSSSSSSnnSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456
4
3
2    G G G  G G G G G G G  G G  G G G
1    G G G  G G G G G G G  G G  G G G
0    G G G  G G G G G G G  G G  G G G
9    G G G  G G G G G G G  G G  G G G
8    G G G  G G G G G G G  G G  G G G
7    G G G  G G G G GGG GG G G GG G G
6    G GGG  G G G G G G GG G    G G G
5    G G G  G G G G G GGG  G    G G G
4    G G G  G G G G G G G  G    G G G
3    G G G  G G G G G G G  G    G G G
2    G G G  G G G G G G G  G    G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3     +        +        +           +
2     +        +&CcCcCcC+   cCcCcCc +
1  CC +        + C     C+ C C     C + O
0  cC +   cC    cC CcC CcCc c c cCc + o
9  CC +   CCCCCCCC CCC    C C C CCCCC O
8  cC +   cC  i i  CcCcC  c c c c   c o
7  C I I  C   I I   CCCCIIC C CCCII C O
6  c i iCcc c i i c c cCiIc c c iIi c o
5  C    C C C     C CCCCCCC C CCCC   OO
4  cCcCcC c cCcCcCcCcCc cCc   cCcC - Oo
3  C  - C   C  -   CCC - CCCCC CCC - OO
2     - CccCc  -    c  - CcCcCcC   -
1     -        -       -           -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A0 | A1 | A2 | A3 | S0 | S1 | Internal1 | X |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   |   | X |   |
| NMOS3 |   |   |   |   |   |   |   |   | X |   |
| NMOS4 |   |   |   |   |   |   |   |   |   | X |
| PMOS1 |   |   |   | X | X |   |   |   | X |   |
| PMOS2 |   |   |   |   |   |   |   |   | X | X |
| PMOS3 |   |   |   |   |   |   |   |   | X |   |
| PMOS4 | X |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   | X |   | X |   |
| Poly10 |   |   |   |   |   |   |   | X | X |   |
| Poly11 |   |   |   |   |   |   |   |   | X |   |
| Poly2 |   |   | X |   |   |   |   |   | X |   |
| Poly3 |   |   |   |   |   |   |   |   | X |   |
| Poly4 |   |   |   | X |   |   |   |   | X |   |
| Poly5 | X |   |   |   | X |   |   |   | X |   |
| Poly6 |   |   |   |   |   |   |   |   | X |   |
| Poly7 |   |   |   |   |   | X |   |   | X |   |
| Poly9 |   |   |   |   |   |   |   | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 | Poly10 | Poly11 | Poly12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   | W | O |   |   |   |   |
| NMOS3 | O | O | O | O | O | O | O |   |   |   |   |   |
| NMOS4 |   |   |   |   |   |   |   |   | W | O | O |   |
| PMOS1 | O | O | O | O | O | O | O |   |   |   |   |   |
| PMOS2 |   |   |   |   |   |   |   |   | W | O | O |   |
| PMOS3 |   |   |   |   |   |   |   | O |   |   |   | O |
| PMOS4 |   |   |   |   |   |   |   |   |   |   |   |   |
