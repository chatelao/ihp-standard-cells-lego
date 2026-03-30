# Design Documentation for sg13g2_mux2_2

## Substrate
```
  01234567890123456789
4 NNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789
4 pppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNN
1 NppppppppppppppppppN
0 NppppppppppppppppppN
9 NppppppppppppppppppN
8 NppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnS
2 SSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789
4
3
2  GG  GGGG G G G
1  GG  GGGG G G G
0  GG  GGGG G G G
9  GG  GGGG G G G
8  GG  GGGG G G G
7  GG  GGGG G G G
6  GGG GGGG G G G
5  GG  GGGG G G G
4  GG  GGGG G G G
3  GG  GGGG G G G
2  GG  GGGG G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789
4 ++++++++++++++++++++
3     +        +    +
2   & +CcCcC&Cc+& & +
1     +C      C+ OOO+
0  Cc  C  cC  c+ OoO+
9  CCCCC CCC  C+ OOO+
8  C   CcCc   c+ OoO+
7  CII C  I   CC   O
6  cIi cIii i cCcC O
5  C   CI   I   C  O
4  Cc- CiIiIi cCc oO-
3    - CCCCCCCC-  OO-
2    -_   c _  -_ _ -
1    -         -    -
0 --------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VDD3 | VSS | VSS2 | A1 | S | Internal1 | X |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS2 |   |   |   |   |   | X |   | X | X |
| PMOS1 |   |   |   |   |   |   |   | X | X |
| Poly1 |   | X |   |   |   |   | X | X |   |
| Poly2 |   |   |   |   |   | X |   | X |   |
| Poly3 |   |   | X |   | X | X |   | X |   |
| Poly4 |   |   |   |   |   |   |   | X |   |
| Poly5 | X |   |   | X |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |
| NMOS2 | O | O | O | O | O |
| PMOS1 | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |
