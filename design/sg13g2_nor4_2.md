# Design Documentation for sg13g2_nor4_2

## Substrate
```
  012345678901234567890
4 NNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890
4 ppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNN
2 ppppppppppppppppppppN
1 NpppppppppppppppppppN
0 Npppppppppppppppppppp
9 NpppppppppppppppppppN
8 Npppppppppppppppppppp
7 SSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890
4
3
2   G G   G GG G G G
1   G G   G GG G G G
0   G G   G GG G G G
9   G G   G GG G G G
8   G G   G GG G G G
7   G G   G GG G G G
6   GGG   GGGGGG GGGG G
5   G G   G GG G G G
4   G G   G GG G G G
3   G G   G GG G G G
2   G G   G GG G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890
4 &+&+&+&+&+&+&+&+&+&+&
3 +++++++++++++++++++++
2 &+  &+CccCcCcCc   c
1  + C++CCCCCCCCC CCCCC
0  + c&+CccCcCc c c o c
9  + CCCCCCCCCCCCCC O C
8  + cCcCccCcCcCcCc o c
7   III   II III II OOO
6   IiI   ii IiI Ii oOo
5    OOOOOOOOOOOOOOOO
4  c o    oOo o     o
3    O    OO  O     O
2  c   c c   c   c   c
1
0  c c c c c c c c c c
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS10 | VSS11 | VSS12 | VSS13 | VSS14 | VSS15 | VSS16 | VSS17 | VSS2 | VSS3 | VSS4 | VSS5 | VSS6 | VSS7 | VSS8 | VSS9 | A | B | C | D | Y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X |   |   |   |   |   |   |   | X | X | X | X | X | X | X | X |   |   |   |   |   |
| NMOS2 |   |   |   | X | X | X | X | X | X | X |   |   |   |   |   |   |   |   |   |   |   |   | X |
| PMOS1 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |
| Poly2 |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X | X | X |
| Poly3 |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X |
| Poly4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |
| NMOS2 | O | O | O |   |
| PMOS1 | O | O | O |   |
| PMOS2 |   |   |   |   |
