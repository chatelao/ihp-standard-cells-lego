# Design Documentation for sg13g2_buf_8

## Substrate
```
  01234567890123456789012
4 NNNNNNNNNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012
4 ppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNN
1 ppppppppppppppppppppppN
0 ppppppppppppppppppppppN
9 ppppppppppppppppppppppN
8 ppppppppppppppppppppppN
7 NNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 nnnnnnnnnnnnnnnnnnnnnnS
3 nnnnnnnnnnnnnnnnnnnnnnS
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012
4
3
2  GGGGG G G G G GGGGGGG
1  GGGGG G G G G GGGGGGG
0  GGGGG G G G G GGGGGGG
9  GGGGG G G G G GGGGGGG
8  GGGGG G G G G GGGGGGG
7  GGGGG GGGGGGGGGGGGGGG
6  GGGGG GGGGGGGGGGGGGGG
5  GGGGG G G G G GGGGGGG
4  GGGGG G G G G GGGGGGG
3  GGGGG G G G G GGGGGGG
2  GGGGG G G G G GGGGGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&
3 +++++++++++++++++++++++
2  c&+c &+o & o+& o+&o &+
1 CC++CC++OO+ O++OO++OO++
0 Cc&+cC&+oO& o+&Oo+&oO&+
9 CCCCCCC OOOOOOOOOOOOO++
8  cCCcCCCoOOOoOOOoOOoO&
7       CCCCCCCCCCCC OOO
6   iiIiCccCcccCccccCOOO
5       CC           OO
4 CcCCcCCCoOOOoOOOoOOoO_-
3 CC--CC--OO- O--OO--OO--
2  c_-c _-o _ o-_ o-_o _-
1 -----------------------
0 _-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | X | A |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |
| NMOS2 |   | X | X | X |   |
| PMOS1 | X | X |   | X |   |
| PMOS2 | X |   |   |   |   |
| Poly1 | X | X | X |   | X |
| Poly2 | X | X | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O | O |
| PMOS2 |   |   |

