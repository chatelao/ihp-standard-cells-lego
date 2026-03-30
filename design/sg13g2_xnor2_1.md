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
2 SSSSSSnnnnnnnS
1 SSSSSSSSSSSSSS
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123
4
3
2    GG   G G
1    GG   G G
0    GG   G G
9    GG G G G
8    GG G G G
7    GG G G G
6    GGGGGG G
5    GG G G G
4    GG G G G
3    GG G G G
2    GG G   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 ++++++++++++++
3  +    +     +
2  +&   + & & +
1  +  C +   O +
0  +  c +   o +
9  + CC     O
8    C IiIi oOo
7    C IIII   O
6    c iIiiIcCo
5  - CCCCCCCCCO
4  - Cc c c c o
3  - CCCCCCCC O
2  -_   _ - _
1  -      -
0 --------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD2 | VDD3 | VSS2 | VSS3 | B | Internal1 | Y |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS2 |   |   | X | X |   | X | X |
| PMOS1 |   |   |   |   | X | X | X |
| Poly1 | X |   | X |   | X | X |   |
| Poly2 |   | X |   | X |   | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O | O |
| PMOS2 |   |   |
