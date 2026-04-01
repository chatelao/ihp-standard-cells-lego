# Design Documentation for sg13g2_and4_2

## Substrate
```
  0123456789012345
4 SSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345
4 pppppppppppppppp
3
2
1   ppppppppppppp
0   ppppppppppppp
9   ppppppppppppp
8           ppppp
7
6
5
4   nnnnnnnnnnnnn
3   nnnnnnnnnnnnn
2
1
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012345
4
3
2              G
1              G
0              G
9              G
8              G
7    G G G G GGG
6          G GGG
5              G
4              G
3              G
2              G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &+&+&+&+&+&+&+&+
3   +  +   +    +
2  c+c & c +c c &
1   +C + C +  OO+
0  c+c & c +c oO&
9    C   C    OO+
8  C          cOc
7  C I I III   O
6  C i i iiIcC O
5  C I I I     O
4  cC      -c oO_
3  CC      -  OO-
2  c       -c c _
1          -    -
0 _-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Internal3 | Internal4 | Output1 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 |   | X |   |   | X |
| PMOS1 | X |   | X | X | X |
| PMOS2 | X |   |   |   |   |
| Poly1 |   |   |   |   |   |
| Poly2 |   |   |   |   |   |
| Poly3 |   |   |   |   |   |
| Poly4 |   |   |   |   |   |
| Poly5 |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |
| NMOS2 | O |   |   |   |   |
| PMOS1 | O |   |   |   |   |
| PMOS2 |   |   |   |   |   |
