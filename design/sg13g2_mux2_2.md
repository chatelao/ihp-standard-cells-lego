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
2 SnnnnnnnnnnnnnnnnnnS
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
4   G G  G GGG
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
2    &+        +&   &
1    ++   CC   + OO +
0  c   c  cC   + Oo &
9  CCCCCCCCC   + OO +
8  c   cCc     + Oo &
7   II C  II  C C OO
6   Ii  I iI  cCc oO
5  C    I II    C OO
4  c _  Ii  i c   o _
3    - C  CC C -- O -
2    _         -_   _
1 --------------------
0 _-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A0 | A1 | S | X |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X |   | X |   | X |
| PMOS1 | X |   |   |   |   | X |
| PMOS2 | X |   |   |   |   |   |
| Poly1 |   |   |   |   | X |   |
| Poly2 |   |   | X | X |   | X |
| Poly3 |   |   |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | O |   |
| PMOS1 | O | O |   |
| PMOS2 |   |   |   |
