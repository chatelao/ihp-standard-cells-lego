# Design Documentation for sg13g2_and4_1

## Substrate
```
  01234567890123
4 SSSSSSSSSSSSSS
3 NNNNNNNNNNNNNN
2 NNNNNNNNNNNNNN
1 NNNNNNNNNNNNNN
0 NNNNNNNNNNNNNN
9 NNNNNNNNNNNNNN
8 NNNNNNNNNNNNNN
7 NNNNNNNNNNNNNN
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 NNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123
4 pppppppppppppp
3
2
1   ppppppppppp
0   ppppppppppp
9   ppppppppppp
8           ppp
7
6
5
4   nnnnnnnnnnn
3   nnnnnnnnnnn
2
1
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123
4
3
2
1
0
9
8
7            G
6    G G G G G
5
4
3
2
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &+&+&+&+&+&+&+
3   +  +   +
2  c+c & c +c c
1   +C + C +  OO
0  c+c & c +c oO
9    C   C    OO
8  C          oO
7  C I I I I   O
6  C i i icIcC O
5  C           O
4  cC      -c oO
3  CC      -  OO
2  c       -c c
1          -
0 _-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Input2 | Input3 | Internal3 | Internal4 | Output1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |
| NMOS2 |   | X |   |   |   |   |   | X |
| PMOS1 | X |   |   |   |   | X | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |
| Poly1 |   |   | X |   |   |   |   |   |
| Poly2 |   |   |   | X |   |   |   |   |
| Poly3 |   |   |   |   | X |   |   |   |
| Poly4 |   |   |   |   |   |   |   |   |
| Poly5 |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |
| PMOS1 |   |   |   |   | S |
| PMOS2 |   |   |   |   |   |
