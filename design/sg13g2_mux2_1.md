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
1 NNNppppppppppppppN
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
2         G G
1   G     G G
0   G     G G
9   G     G G
8   G     G G
7   GGG   G G
6   GGG G G G  G G
5   G     G G
4   G     G G
3   G     G G
2         G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567
4 &+&+&+&+&+&+&+&+&+
3     +        +
2     +cCccCcCc+
1     +C      C+ OO
0  c   c  cC  c+ Oo
9  CCCCC CCC  C+ OO
8  c   cCcc   c+ Oo
7  CII C  I I CC  O
6  cIi cIii i cCcCo
5  C   CI   I   C O
4  c - cIiiIi cCc o
3  C - CCCCCCCC-  O
2    -    c    -
1    -         -
0 _-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A1 | S | Internal1 | X |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   |   | X |   | X | X |
| PMOS1 |   |   |   |   | X | X |
| PMOS2 | X |   |   |   |   |   |
| Poly1 |   |   | X |   | X |   |
| Poly2 |   |   | X |   | X |   |
| Poly3 |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |
| NMOS2 | O | O | O |   |   |   |
| PMOS1 | O | O | O |   |   |   |
| PMOS2 |   |   |   |   |   |   |
