# Design Documentation for sg13g2_buf_8

## Substrate
```
  01234567890123456789012
4 NNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012
4 ppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNN
1 ppppppppppppppppppppppN
0 ppppppppppppppppppppppN
9 ppppppppppppppppppppppN
8 ppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 nnnnnnnnnnnnnnnnnnnnnnS
3 nnnnnnnnnnnnnnnnnnnnnnS
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012
4
3
2    G G GGGGGGGG G G
1    G G GGGGGGGG G G
0    G G GGGGGGGG G G
9    G G GGGGGGGG G G
8    G G GGGGGGGG G G
7   GGGG GGGGGGGG G G
6   GGGG GGGGGGGGGGGGGG
5    G G GGGGGGGG G G
4    G G GGGGGGGG G G
3    G G GGGGGGGG G G
2    G G GGGGGGGG G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&
3   +   +   +   +   +  +
2   +   +   +   +   +  +
1  C+ C + O + O + O +O +
0  c+ Cc+ o + o + o +O +
9  CCCCCC OOOOOOOOOOOOO+
8    c  C       o    O
7       C            O
6   IiIiCccCcCcCcCcCcOoO
5       C            O
4  cCcCcC oOoOoOoOoOoOo-
3  C- C - O - O - O -O -
2   -   -   -   -   -  -
1   -   -   -   -   -  -
0 _-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | Internal1 | X |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 |   |   |   | X | X |
| PMOS1 |   |   |   | X | X |
| PMOS2 | X |   |   |   |   |
| Poly1 |   |   | X | X |   |
| Poly2 |   |   |   | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O | O |
| PMOS2 |   |   |
