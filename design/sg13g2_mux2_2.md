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
2 NppppppppppppppppppN
1 NppppppppppppppppppN
0 NppppppppppppppppppN
9 NppppppppppppppppppN
8 NppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnS
2 Snnnnnnnnnnnnnnnnnnn
1 SSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789
4
3
2   G G  G G G
1   G G  G G G
0   G G  G G G
9   G G  G G G
8   G G  G G G
7   G G  G G G
6   GGG  GGGGG    G
5   G G  G G G
4   G G  GGGGG
3   G G  G G G
2   G G  G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789
4 &+&+&+&+&+&+&+&+&+&+
3 ++++++++++++++++++++
2    +&cCccCcCc+&OoO&
1    ++C  CC  C+ OOO+
0  c c c  cC  c+ OoO&
9  CCCCCCCCC  C+ OOO+
8  c   cCcc   c+ OoO&
7  CII C  II  CCCCOO
6  cIi cIiiIi cCcCoO
5  C   CI III   CCOO
4  c c cIiiIi cCcCoO
3      CCCCCCCC   OO
2    c cCccCcCcc  oO c
1
0  c c c c c c c c c c
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A0 | S | VDD2 | X | VDD | VSS | VSS10 | VSS11 | VSS12 | VSS13 | VSS14 | VSS2 | VSS3 | VSS4 | VSS5 | VSS6 | VSS7 | VSS8 | VSS9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   | X | X |   |   |   |   | X | X | X | X | X | X | X | X |
| NMOS2 | X |   | X | X |   |   |   | X | X | X | X |   |   |   |   |   |   |   |   |
| PMOS1 |   |   | X | X | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| PMOS2 |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   | X |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly2 | X |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly3 |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | O |   |
| PMOS1 | O | O |   |
| PMOS2 |   |   |   |
