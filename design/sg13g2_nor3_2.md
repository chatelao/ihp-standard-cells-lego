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
2 pppppppppppppppN
1 NppppppppppppppN
0 pppppppppppppppN
9 NppppppppppppppN
8 pppppppppppppppN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 Snnnnnnnnnnnnnnn
3 SnnnnnnnnnnnnnnS
2 Snnnnnnnnnnnnnnn
1 SSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345
4
3
2   G G G G  G G
1   G G G G  G G
0   G G G G  G G
9   G G G G  G G
8   G G G G  G G
7   G G G G  G G
6   GGGGGGG GGGG
5   G G G G  G G
4   G G G G  G G
3   G G G G  G G
2   G G G G  G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &+&+&+&+&+&+&+&+
3 ++++++++++++++++
2 &+Cc&+CccCcCcCcC
1 ++CC++CCCCCCCCCC
0 &+Cc&+CccCcCoOcC
9 ++CCCCCCCCOOOOCC
8 &+CcCcCccCoOoOcC
7   IIIIIIOOOIII
6   IIIiIIoOoIII
5 --OOOOOOOOOOOO--
4 -_Oo-_-_oO__oO-_
3 --OO----OO--OO--
2 -_  -_-_  -_  -_
1 ----------------
0 -_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | B | VSS2 | Y | VDD | VSS |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   | X |
| NMOS2 |   |   | X |   | X |
| PMOS1 |   | X | X | X |   |
| PMOS2 |   |   |   | X |   |
| Poly1 | X | X | X | X |   |
| Poly2 |   |   | X |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O | O |
| PMOS2 |   |   |
