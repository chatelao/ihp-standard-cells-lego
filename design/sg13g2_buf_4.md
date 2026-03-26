# Design Documentation for sg13g2_buf_4

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
2           G G
1           G G
0           G G
9           G G
8           G G
7           G G
6  G G      GGG
5           G G
4           G G
3           G G
2           G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &+&+&+&+&+&+&+
3 ++++++++++++++
2  &  +&  &+  &
1  +OO++OO++  +
0  &Oo+&Oo&+cC&
9  +OO++OO++CCCC
8  &OoOoOo&+cCcC
7  OOO      IICC
6  oOo  Ccc iicC
5   OO    C   CC
4  cOoOoOocCcCcC
3   OO  OO    CC
2  cOo c    c
1
0 c c c c c c c
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | VSS10 | VSS11 | VSS2 | VSS3 | VSS4 | VSS5 | VSS6 | VSS7 | VSS8 | VSS9 | A | X |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   | X | X | X | X | X | X |   |   |   |   |
| NMOS2 |   | X |   | X | X |   |   |   |   |   |   | X | X |   | X |
| PMOS1 | X | X |   |   |   |   |   |   |   |   |   |   |   |   | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 | X | X |   |   |   |   |   |   |   |   |   | X |   | X |   |
| Poly2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| Poly3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O |   |   |
| PMOS1 | O |   |   |
| PMOS2 |   |   |   |
