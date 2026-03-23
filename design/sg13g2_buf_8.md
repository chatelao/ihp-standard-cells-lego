# Design Documentation for sg13g2_buf_8

## Substrate
```
  01234567890123456789012
4 NNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSS
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
2 Npppppppppppppppppppppp
1 NpppppppppppppppppppppN
0 Npppppppppppppppppppppp
9 NpppppppppppppppppppppN
8 Npppppppppppppppppppppp
7 SSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012
4
3
2     G
1     G
0     G
9   G G
8   G G
7   G G
6   GGGG GG G G G G G
5   G G
4   G G
3     G
2     G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&
3   +   +   +   +   +  +
2 Cc& Cc& o & o & o & o+&
1 CC+ CC+ O + O + O + O+
0 Cc& Cc& o & o & o & o+&
9 CCCCCCCCOOOOOOOOOOOOO+
8 CcCcCcCco o o o o o o &
7       CCCCCCCCCCCCC O
6   IiIiCccCcCcCcCcCc OO
5       CC            O
4 CcCcCcCcoOoOoOoOoOoOo_
3 CC- CC- O - O - O - O-
2 Cc-_Cc-_o -_o_- o_- o_
1   -   -   -   -   -  -
0 -_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | A | VSS | X | VDD |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 |   | X | X |   |
| PMOS1 |   | X | X | X |
| PMOS2 |   |   |   | X |
| Poly1 | X |   |   |   |
| Poly2 |   | X |   |   |
| Poly3 |   | X |   |   |
| Poly4 |   | X |   |   |
| Poly5 |   | X |   |   |
| Poly6 |   | X |   |   |
| Poly7 |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 | Poly7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |   |
| NMOS2 | O |   |   |   |   |   |   |
| PMOS1 | O |   |   |   |   |   |   |
| PMOS2 |   |   |   |   |   |   |   |
