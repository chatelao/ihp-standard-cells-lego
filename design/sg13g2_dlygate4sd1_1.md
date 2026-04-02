# Design Documentation for sg13g2_dlygate4sd1_1

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
1  pppppp pppppp
0  pppppp pppppp
9    pppp pppppp
8         pppppp
7
6
5
4         nnnnnn
3  nnnnnn    nnn
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
1   G
0   G
9   G
8   G
7   G G
6   G G   GG G
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
3    +       +
2    +       +c
1    +       + C
0  c & cC   c+cC
9  C    C      C
8     C C cCCCcC
7  II C C    C C
6  IIcCcCCc CCcC
5     C C CC OOO
4  CCCC C c   cC
3  C -  C    - C
2  c _ c    c-c
1    -       -
0 _-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Internal1 | Internal3 | Internal4 | Output1 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |
| NMOS3 |   |   | X |   |   | X |
| PMOS1 | X |   |   | X |   |   |
| PMOS2 | X |   | X |   | X |   |
| PMOS3 | X |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   |
| Poly2 |   |   |   |   |   |   |
| Poly3 |   |   | X |   |   |   |
| Poly4 |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |
| NMOS2 |   |   |   |   |
| NMOS3 |   |   |   |   |
| PMOS1 |   |   |   |   |
| PMOS2 | O |   |   |   |
| PMOS3 |   |   |   |   |
