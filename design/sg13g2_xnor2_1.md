# Design Documentation for sg13g2_xnor2_1

## Substrate
```
  01234567890123
4 NNNNNNNNNNNNNN
3 NNNNNNNNNNNNNN
2 NNNNNNNNNNNNNN
1 NNNNNNNNNNNNNN
0 NNNNNNNNNNNNNN
9 NNNNNNNNNNNNNN
8 NNNNNNNNNNNNNN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 SSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123
4 pppppppppppppp
3 NNNNNNNNNNNNNN
2 NNNNNNNNNNNNNN
1 NppppppppppppN
0 NppppppppppppN
9 NppppppppppppN
8 NppppppppppppN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SnnnnnSSSSSSSS
4 SnnnnnnnnnnnnS
3 SnnnnnnnnnnnnS
2 SSSSSSSSnSSSSS
1 SSSSSSSSSSSSSS
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123
4
3
2    G G G   G
1    G G G   G
0    G G G   G
9    G G G   G
8    G G G   G
7   GG G G   G
6   GGGG G G G
5   GG G G
4   GG G G
3   GG G G
2   GG G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &+&+&+&+&+&+&+
3  +    +     +
2  +    +     +
1  +  C +   O +
0  + cC +   o +
9  + CC     O
8    c iIii oOo
7    C IIII   O
6    c iIiiIcCo
5  - CCCCCCCCCO
4  - cCc c  c o
3  - CCCCCCCC O
2  -      -
1  -      -
0 _-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | Internal1 | Y |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 |   |   |   | X | X |
| PMOS1 |   |   | X | X | X |
| PMOS2 | X |   |   |   |   |
| Poly1 |   |   | X | X |   |
| Poly2 |   |   | X | X |   |
| Poly3 |   |   |   |   |   |
| Poly4 |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |
| NMOS2 | O | O |   |   |
| PMOS1 | O | O |   | O |
| PMOS2 |   |   |   |   |
