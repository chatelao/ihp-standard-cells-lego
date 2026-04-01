# Design Documentation for sg13g2_buf_8

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
1 pppppppppppppppppppppp
0 pppppppppppppppppppppp
9 pppppppppppppppppppppp
8 pppppppppppppppppppppp
7
6
5
4 nnnnnnnnnnnnnnnnnnnnnn
3 nnnnnnnnnnnnnnnnnnnnnn
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
2        G G G G
1        G G G G
0        G G G G
9        G G G G
8        G G G G
7   GGGG G G G G
6   GGGG GGGGGGGGGGGGGG
5        G G G G
4        G G G G
3        G G G G
2        G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&
3   +   +   +   +   +  +
2  c+c c+cc & c & c & c+c
1  C+ C + O + O + O +O +
0  c+cCc+co & o & o &Oc+c
9  C  C   O   O   O  O +
8  c   c  c   c   c  Oc c
7                    O
6   IiIi ccCcCcCcCcCcOOO
5                    O
4  cCCCcC oOOOoOOOoOOOc-c
3  C- C - O - O - O -O -
2  c-c c-cc _ c _ c _ c-c
1   -   -   -   -   -  -
0 _-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Internal1 | Internal2 | Internal3 | Internal4 | Internal6 | Output1 | Output2 | Output3 | Output4 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   | X |   |   |   |   | X |   |   |   |
| PMOS1 | X |   |   |   |   | X | X | X | X | X | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 | X | X |   |   | X |   |   |   |   |   |   |   |
| Poly2 |   |   | X |   |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| PMOS1 | O | S |
| PMOS2 |   |   |
