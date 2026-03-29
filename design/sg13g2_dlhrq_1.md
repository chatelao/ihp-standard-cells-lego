# Design Documentation for sg13g2_dlhrq_1

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
2 G G G GGGG  G G G   G   G
1 G G G GGGG  G G G   G   G
0 G GGG GGGGG G G G   G   G
9 G GGG GGGGG G G G   G   G
8 G GGG GGGGG G G G   G G G
7 G GGG GGGGG G G G   G G G
6 GGGGGGGGGGG G G G   G G G
5 G GGG GGGGG G G G   G G G
4 G GGG GGGGG G G G   G G G
3 G GG  GGGGG G G G   G   G
2 G GG  GGGG  G G G   G   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&
3    +      +       +   +
2    &      & cCcC  &   &
1  C +      + C  C  + C + OO
0  cCcCcCccCc cCcC    c & oO
9  CCC CC C C CC C CCCC + OO
8    c cCcc c cCcCcCc c   oO
7  I CIICCC CCC C   C CI   O
6  i cIiCci c c cCc   cIiCcO
5  CCC  CCCCCCC CC   CCCCC O
4  c   cCccCcC CcC  cCc   oO
3     - C    C   C - C  - OO
2     -     _CcCcC -    _
1     -     -      -    -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | D | GATE | Input1 | RESET_B | Q |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |
| NMOS2 |   | X |   |   |   |   | X |
| PMOS1 | X |   |   |   |   |   | X |
| PMOS2 | X |   |   |   |   |   |   |
| Poly1 |   |   | X | X | X |   | X |
| Poly2 |   |   |   |   |   |   | X |
| Poly3 |   |   |   |   |   |   | X |
| Poly4 |   |   |   |   |   |   | X |
| Poly5 |   |   |   |   |   |   | X |
| Poly6 |   |   |   |   |   |   | X |
| Poly7 |   |   |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | O | O |
| PMOS1 | O | O | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |
