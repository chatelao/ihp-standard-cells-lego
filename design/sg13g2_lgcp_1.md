# Design Documentation for sg13g2_lgcp_1

## Substrate
```
  012345678901234567890123456
4 NNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456
4 ppppppppppppppppppppppppppp
3 NNNNNNNNNNNppNNNNNNNNNNNNNN
2 NNNNNNNNNNNppNNNNNNNNNNNNNN
1 NppppppppppppppNpppppppppNN
0 NpppppppNNNNpppNpppppppppNN
9 NpppppppNNNNpppNpppppppppNN
8 NpppNNNNNNNNNNNNNNNNNNpppNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSnnnnnnnnnnSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnSSSSSSSnnnnnnnnnnnS
2 SSSnSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456
4
3
2   GG G G G  G       G GG
1   GG G G G  G       G GG
0   GG G G G  G       G GG
9   GG G G G GG       G GG
8   GG G G   GG       G GG
7   GG G G G GGG   GG G GG
6   GG G G G GG     G G GG
5   GG G G G GG       G G
4   GG G G G  G       G G
3   GG G G G  G       G G
2   GG G G   GG       G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&
3    +        +    +    +
2    +        +    +    +
1  C +  CCC       C+ C  + O
0  c   cCc  cCcCcCc  Cc + o
9  C CCCCCCCCC CC CI C  + O
8  c c i c   C  c cI CcC  o
7  C C I C C CCCC CII  C  O
6  cCi   c Cc c c c i  Cc o
5  C CCCCC CCCCCC C-  CC  O
4  cCcCcCcc _-- c  -  cC -o
3  C - C      -    -  CC -O
2    - cCccCcC-    -     -o
1    -        -    -     -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | CLK | GATE | Input1 | Internal1 | Internal2 | GCLK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |
| NMOS2 |   | X |   |   |   | X | X | X |
| PMOS1 | X |   |   |   |   | X |   |   |
| PMOS2 |   |   |   |   |   | X | X | X |
| Poly1 |   |   |   |   | X | X |   |   |
| Poly2 |   |   |   | X |   | X |   |   |
| Poly3 |   |   |   |   |   | X |   |   |
| Poly4 |   |   |   |   |   | X |   |   |
| Poly5 |   |   |   |   |   |   | X |   |
| Poly6 |   |   |   |   |   |   | X |   |
| Poly7 |   |   |   |   |   |   |   |   |
| Poly8 |   |   | X |   |   |   |   |   |
| Poly9 |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 | Poly9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | O | O | N |   |
| PMOS1 | O | O | O | O |   |   |   |   | O |
| PMOS2 |   |   |   |   | O | O |   |   |   |
