# Design Documentation for sg13g2_inv_8

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
2 NppppppppppppppppN
1 NppppppppppppppppN
0 NppppppppppppppppN
9 NppppppppppppppppN
8 NppppppppppppppppN
7 SSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567
4
3
2   G G
1   G G
0   G G
9   G G
8   G G
7   G G
6   GGGG GG G G G
5   G G
4   G G
3   G G
2   G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567
4 &+&+&+&+&+&+&+&+&+
3 ++++++++++++++++++
2 +&  +&  &+  &   &
1 ++OO++OO++O + O +
0 +&Oo+&Oo&+o & o &
9 ++OOOOOOOOO + O +
8 +&OoOoOooOo & o &
7    IIIIIIIOOOOO
6    iIiIiiIoOoOo
5           O   O
4  cOoOoOooOo c o c
3   OO  OO  O   O
2  c   cOoc o c o c
1
0 c c c c c c c c c
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS10 | VSS11 | VSS12 | VSS13 | VSS14 | VSS15 | VSS16 | VSS17 | VSS2 | VSS3 | VSS4 | VSS5 | VSS6 | VSS7 | VSS8 | VSS9 | A | Y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |   | X | X | X | X | X | X | X | X |   |   |
| NMOS2 |   |   | X | X | X | X | X | X | X | X |   |   |   |   |   |   |   |   |   | X |
| PMOS1 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| Poly2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| Poly3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| Poly4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |
| Poly5 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |
| NMOS2 | O |   |   |   |   |
| PMOS1 | O |   |   |   |   |
| PMOS2 |   |   |   |   |   |
