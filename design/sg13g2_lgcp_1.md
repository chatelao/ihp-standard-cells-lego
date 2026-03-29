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
3 NNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NpppppppppppppppppppppppppN
1 NpppppppppppppppppppppppppN
0 NpppppppppppppppppppppppppN
9 NpppppppppppppppppppppppppN
8 NpppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456
4
3
2  G  G GG  G   G G
1  G  G GG  G G G G
0  G GG GG  G G G G G
9  G GG GG  G G G G G
8  G GGGGG  G G G G G   G
7  G GG GG  G G G G G   G
6  G GGGGG  G G G G G   G
5  G GG GG  G G G G G   G
4  G GG GG  G   G G G
3  G  G GG  G   G G G
2  G  G GG  G   G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&
3    +        +    +    +
2    &        &    +    &
1  C +  CCC       C+ C  + O
0  c   cCc  cCcCcCc  Cc & o
9  C CCCCCCCCC CC CI C  + O
8  c c i c   C  c cI CcC  o
7  C C I C C CCCC CII  C  O
6  cCc i c Cc c c c i  Cc o
5  C CCCCC CCCCCC C-  CC  O
4  cCcCcCcc  -_ c  -  cC -o
3  C - C      -    -  CC -O
2    _ cCccCcC_    -     -o
1    -        -    -     -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | CLK | GATE | Internal1 | Internal2 | GCLK |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |
| NMOS2 |   | X |   |   | X | X | X |
| PMOS1 | X |   |   | X | X | X | X |
| PMOS2 | X |   |   |   |   |   |   |
| Poly1 |   |   |   |   | X |   |   |
| Poly2 |   |   |   | X | X |   |   |
| Poly3 |   |   |   |   | X |   |   |
| Poly4 |   |   |   |   | X |   |   |
| Poly5 |   |   |   |   | X |   |   |
| Poly6 |   |   | X |   |   |   |   |
| Poly7 |   |   |   |   | X |   |   |
| Poly8 |   |   |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | O | N | N |
| PMOS1 | O | O | O | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |   |
