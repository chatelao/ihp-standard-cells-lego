# Design Documentation for sg13g2_einvn_4

## Substrate
```
  01234567890123456789012
4 SSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012
4 ppppppppppppppppppppppp
3
2
1  ppp  pppppppppppppppp
0  ppp  pppppppppppppppp
9  ppp  pppppppppppppppp
8  ppp  pppppppppppppppp
7
6
5
4  nnn  nnnnnnnnnnnnnnnnn
3  nnn  nnnnnnnnnnnnnnnnn
2
1
0 nnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012
4
3
2               G G G G
1               G G G G
0               G G G G
9               G G G G
8               G G G G
7   GGGGGGGGGGG GGGGGGG
6                G G
5      G   G G G G G
4      G   G G G G G
3      G   G G G G G
2          G G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&
3  +      +  +
2  & c c  & c+cCcCcCCCcC
1  + C  C +C + C   C   C
0  & c cC &Cc+cCcIcCcIcC
9  + C  C +C + C I   I C
8  c c cC cCc cCcIiIiIc
7  IIC  CCCCCCCC   IIII
6  iIC             IiIi
5    C      C   C
4  _ cCc c_ c _ c i   i c
3  - CCC  - C - CCCCC
2  _ c c c_ c _ c   cCCCc
1  -      -   -
0 _-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | Input1 | Input2 | Input4 | Internal1 | Internal2 | Internal3 | Internal4 | Internal5 | Internal8 | Internal9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   | X |   |   |   |   | X |   |   |   |   |   |
| NMOS3 |   |   | X | X | X |   | X |   | X |   |   | X | X |
| PMOS1 | X |   |   |   |   |   |   | X |   |   |   |   |   |
| PMOS2 | X | X |   |   |   | X |   |   |   | X | X |   |   |
| PMOS3 | X |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly2 |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly3 |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly4 |   |   |   |   |   | X |   |   |   | X | X |   |   |
| Poly5 |   |   |   |   |   |   |   | X |   |   |   |   |   |
| Poly6 |   |   |   |   |   |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |
| NMOS3 | O | O | O | O | W |   |
| PMOS1 |   |   |   |   |   | S |
| PMOS2 |   |   |   | O |   | S |
| PMOS3 |   |   |   |   |   |   |
