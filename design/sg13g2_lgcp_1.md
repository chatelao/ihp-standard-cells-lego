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
3 ppppppppppppppppppppppppppp
2 ppppppppppppppppppppppppppp
1 ppppppppppppppppppppppppppp
0 ppppppppppppppppppppppppppp
9 ppppppppppppppppppppppppppp
8 ppppppppppppppppppppppppppp
7 SSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SnnnnnnnnnnnnnnnnnnnnnSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  012345678901234567890123456
4
3
2  GG GGGGG G   G G   G
1  GG GGGGG G G G G   G
0  GGGGGGGG G G G G   G
9  GGGGGGGG G G G G   G
8  GGGGGGGG G G G G   G G
7  GGGGGGGG G G G G   G G
6  GGGGGGGG G G G G G G G
5  GGGGGGGG G G G G   G G
4  GGGGGGGG G   G G   G
3  GG GGGGG G   G G   G
2  GG GGGGG G   G G   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 +++++++++++++++++++++++++++
3    +        +    +    +
2    +&     & + &  +&   + &
1  C +  CCC       C+ C  + O
0  Cc   c   cCcCcCc  Cc + o
9  C CCCCCCCCC CC CI C  + O
8  C C I C   C  c cI CcC  o
7  C C I C C CCCC CII  C  O
6  cCi i c Cc c c c i  Cc o
5  C CCCCC CCCCCC C-  CC  O
4  CcCcCcCc _-- c  -  cC -o
3  C - C      -    -  CC -O
2    -_CcCcCcC- _  -_   _-o
1    -        -    -     -
0 ---------------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VDD3 | VDD4 | VSS | VSS2 | CLK | GATE | Internal1 | Internal2 | GCLK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS2 |   |   |   |   | X | X |   |   | X | X | X |
| PMOS1 | X | X | X | X |   |   |   |   | X | X | X |
| Poly1 | X |   |   |   | X |   |   | X | X |   |   |
| Poly2 |   | X |   |   | X |   |   |   | X |   |   |
| Poly3 |   |   | X |   |   | X |   |   | X |   |   |
| Poly4 |   |   |   |   |   |   |   |   | X |   |   |
| Poly5 |   |   |   |   |   |   |   |   |   | X |   |
| Poly6 |   |   |   |   |   |   |   |   | X |   |   |
| Poly7 |   |   |   |   |   |   |   |   |   | X |   |
| Poly8 |   |   |   |   |   |   | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 | Poly8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | O | NE | N |
| PMOS1 | O | O | O | O | O | O | O |   |
