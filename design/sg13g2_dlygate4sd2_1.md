# Design Documentation for sg13g2_dlygate4sd2_1

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
2 NppppppppppppN
1 NppppppppppppN
0 NppppppppppppN
9 NppppppppppppN
8 NppppppppppppN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SnnnnnnnnnnnnS
3 SnnnnnnnnnnnnS
2 SnnnnnnnnnnnnS
1 SSSSSSSSSSSSSS
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123
4
3
2 G G  G GG G G
1 G G  G GG G G
0 G G  G GG G G
9 G G  G GG G G
8 G G  G GG G G
7 G G  G GG G G
6 GGG  G GG G G
5 G G  G GG G G
4 G G  G GG G G
3 G G  G GG G G
2 G G  G GG G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &+&+&+&+&+&+&+
3    +       +
2    &       +
1    +    C  + O
0  c & cC c  +oO
9  CCCC C C    O
8    cC C cCcC O
7  II C C    C O
6  iI CcCccCcCcO
5     C C CC OOO
4  cCcC C c   oO
3  C -  C    - O
2    _ c     -
1    -       -
0 _-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | VSS3 | A | X |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X | X | X |   | X |
| PMOS1 | X |   |   | X |   | X |
| PMOS2 | X |   |   |   |   |   |
| Poly1 |   |   |   |   | X |   |
| Poly2 |   |   | X | X |   |   |
| Poly3 |   |   |   | X |   |   |
| Poly4 |   |   |   | X |   |   |
| Poly5 |   |   |   | X |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |
| NMOS2 | O | O | O | O | O |
| PMOS1 | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |
