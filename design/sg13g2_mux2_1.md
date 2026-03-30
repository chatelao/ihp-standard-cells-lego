# Design Documentation for sg13g2_mux2_1

## Substrate
```
  012345678901234567
4 NNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567
4 pppppppppppppppppp
3 NNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNN
1 NppppppppppppppppN
0 NppppppppppppppppN
9 NppppppppppppppppN
8 NppppppppppppppppN
7 SSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnS
2 SSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567
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
  012345678901234567
4 ++++++++++++++++++
3     +        +
2   & +CcC&CcCc+&
1     +C      C+ OO
0  Cc  C  cC  c+ Oo
9  CCCCC CCC  C+ OO
8  C   CcCc   c+ Oo
7  CII C  I I CC  O
6  cIi cIii i cCcCo
5  C   CI   I   C O
4  Cc- CiIiIi cCc o
3  C - CCCCCCCC-  O
2    -_   _    -_
1    -         -
0 ------------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VDD3 | VSS | VSS2 | A1 | S | Internal1 | X |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS2 |   |   |   |   |   | X |   | X | X |
| PMOS1 |   |   |   |   |   |   |   | X | X |
| Poly1 |   | X |   |   |   |   | X | X |   |
| Poly2 |   |   | X |   | X | X |   | X |   |
| Poly3 |   |   |   |   |   | X |   | X |   |
| Poly4 |   |   |   |   |   |   |   | X |   |
| Poly5 | X |   |   | X |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |
| NMOS2 | O | O | O | O | O |
| PMOS1 | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |
