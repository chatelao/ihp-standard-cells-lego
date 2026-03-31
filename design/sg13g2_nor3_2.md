# Design Documentation for sg13g2_nor3_2

## Substrate
```
  0123456789012345
4 NNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345
4 pppppppppppppppp
3 NNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NppppppppppppppN
0 NppppppppppppppN
9 NppppppppppppppN
8 NppppppppppppppN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SnnnnnnnnnnnnnnS
4 SnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345
4
3
2   GG   GG    G
1   GG   GG    G
0   GG   GG    G
9   GG   GG    G
8   GG   GG    G
7   GG   GGG  GG
6   GG   GGG  GG
5   GG   GG    G
4   GG   GG    G
3   GG   GG    G
2   GG   GG    G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &+&+&+&+&+&+&+&+
3  +   +
2  +   +    c
1  + C + CCCCCCCC
0  + c + cc c o c
9  + C    C   O C
8    cCcCccCoOo c
7    I   I  O I
6   IiI IioOo iI
5    OOOOOOOOOO
4  - o    o   o -
3  - O ---O - O -
2  -   ---  -   -
1  -   ---  -   -
0 _-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | B | C | Internal1 | Y |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   | X |
| PMOS1 |   |   |   |   |   | X | X |
| PMOS2 | X |   |   |   |   |   |   |
| Poly1 |   |   | X |   |   | X | X |
| Poly2 |   |   |   | X |   | X | X |
| Poly3 |   |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | O | O |
| PMOS1 | O | O | O |
| PMOS2 |   |   |   |
