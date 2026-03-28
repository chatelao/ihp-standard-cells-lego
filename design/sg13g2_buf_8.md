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
2 NpppppppppppppppppppppN
1 NpppppppppppppppppppppN
0 NpppppppppppppppppppppN
9 NpppppppppppppppppppppN
8 NpppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012
4
3
2     GG GG   G   G
1     GG GG   G   G
0     GG GG   G   G
9   G GG GG G G G G G
8   G GG GG G G G G G
7   G GG GG G G G G G
6   GGGG GG G G G G G
5   G GG GG G G G G G
4   G GG GG G G G G G
3     GG GG   G   G
2     GG GG   G   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&
3   +   +   +   +   +  +
2   +   +   &   &   &  +
1  C+ C + O + O + O +O +
0  c+ Cc+ o & o & o &O +
9  CCCCCC OOOOOOOOOOOOO+
8    c  C       o    O
7       C            O
6   IiIiCccCcCcCcCcCcOoO
5       C            O
4  cCcCcC oOoOoOoOoOoOo-
3  C- C - O - O - O -O -
2   -   -   _   _   _  -
1   -   -   -   -   -  -
0 _-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | A | X |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 |   | X | X |   | X |
| PMOS1 | X |   | X |   | X |
| PMOS2 | X |   |   |   |   |
| Poly1 |   |   | X | X |   |
| Poly2 |   |   | X |   | X |
| Poly3 |   |   | X |   | X |
| Poly4 |   |   | X |   | X |
| Poly5 |   |   | X |   | X |
| Poly6 |   |   | X |   | X |
| Poly7 |   |   | X |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | O | O |
| PMOS1 | O | O | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |   |   |
