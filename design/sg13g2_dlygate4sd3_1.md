# Design Documentation for sg13g2_dlygate4sd3_1

## Substrate
```
  0123456789012345
4 SSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSS
9 SSSSSSSSSSSSSSSS
8 SSSSSSSSSSSSSSSS
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
3 SSSSSSSSSSSSSSSS
2 SnnnnnnSnnnnnnSS
1 SnnnnnnnnnnnnnnS
0 SnnnnnnnnnnnnnnS
9 SnnnnnnnnnnnnnnS
8 SnnnnnnSnnnnnnnS
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSnnnnnnSS
4 SSSSSSSSnnnnnnnS
3 SSSSSSSSnnnnnnnS
2 SSSSSSSSnnnnnnSS
1 SSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  0123456789012345
4
3
2   G     GGG GG
1   GG    GGGGGG
0   GG    GGGGGG
9   GG    GGGGGG
8   GG    GGGGGG
7   GG    GGGGGG
6   GG    GGGGGG
5   GG    GGGGGG
4   GG    GGGGGG
3   GG    GGGGGG
2   GG    G G GG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &&&&&&&&&&&&&&&&
3 ++++++++++++++++
2 ++++++++++&+++++
1 ++++++++++++++&+
0 +&+++++&&+&+++&+
9  IIIIICC+++++Oo
8  IIIIICc&++++Oo
7  iiIIICC+++++OO
6  iiiIICC&+&+&OO
5  IIIIICC+++++OO
4  IIIIICC&++++Oo
3 ----------------
2 ----------------
1 ----------------
0 ________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | Internal1 | X |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 | X |   |   | X | X |
| NMOS3 | X |   | X | X | X |
| PMOS1 | X |   |   |   |   |
| Poly1 |   |   | X |   |   |
| Poly2 | X |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 |   | O |
| NMOS3 | O | O |
| PMOS1 |   |   |
