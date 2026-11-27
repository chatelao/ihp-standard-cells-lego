# Design Documentation for sg13g2_nor3_2

## Substrate
```
  0123456789012345
4 NNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNN
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
7 NNNNNNNNNNNNNNNN
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
2   G G  GGGGG G
1   G G  GGGGG G
0   G G  GGGGG G
9   G G  GGGGG G
8   G G  GGGGG G
7   GGG GGGGGGGG
6   GGG GGGGGGGG
5   G G  GGGGG G
4   G G  GGGGG G
3   G G  GGGGG G
2   G G  GGGGG G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &+&+&+&+&+&+&+&+
3 ++++++++++++++++
2  & c+& cCCcCCCc
1  +CC++CCCCCCCCCC
0  &Cc+&CccCcCoOcC
9  +CCCCCCCCOOOOCC
8  & cCCCCc OOoOc
7   II   COOOOII
6   IiI IiOOOOiI
5  - OOOOOOOOOO -
4  _OoO_-_oO_OoO_-
3  -OO----OO--OO--
2  -  ----  --  --
1 ----------------
0 _-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | Y | B | C | A |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 |   | X |   | X |   |
| PMOS1 | X |   | X | X |   |
| PMOS2 | X |   |   |   |   |
| Poly1 |   |   |   |   | X |
| Poly2 |   | X | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O | O |
| PMOS2 |   |   |

