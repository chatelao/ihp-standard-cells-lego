# Design Documentation for sg13g2_nor4_1

## Substrate
```
  01234567890
4 SSSSSSSSSSS
3 NNNNNNNSSSS
2 NNNNNNNSSSS
1 NNNNNNNSSSS
0 SSSSSSSSSSS
9 SSSSSSSSSSS
8 SSSSSSSSSSS
7 SSSSSSSSSSS
6 SSSSSSSSSSS
5 SSSSSSSSSSS
4 SSSSSSSSSSS
3 SSSSSSSSSSS
2 SSSSSSSSSSS
1 SSSSSSSSSSS
0 SSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890
4 ppppppppppp
3 pppppppnnnn
2 pppppppnnnn
1 pppppppnnnn
0 SnnnnnnnSSS
9 SSSSSSSSSSS
8 SSSSSSSSSSS
7 SSSSSSSSSSS
6 SSSSSSSSSSS
5 SnnnnnnnnSS
4 SnnnnnnnnnS
3 SnnnnnnnnnS
2 SnnnnnnnnSS
1 SSSSSSSSSSS
0 nnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  01234567890
4
3
2  GGGGGGGG
1  GGGGGGGG
0  GGGGGGGG
9  GGGGGGGG
8  GGGGGGGG
7  GGGGGGGG
6  GGGGGGGG
5  GGGGGGGG
4  GGGGGGGG
3  GGGGGGGG
2  GGGGGGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
4 &&&&&&&&&&&
3 +++++++++++
2 +++++++++++
1 ++++++++&&+
0  ++&+++&&o
9  ++++++&&o
8  ++++&++&O
7  &+&+++++O
6  &+&+&++&O
5  ++++++++O
4  -+&+++&+O
3  -+++++++O
2  -+_++++_O
1
0 _c_c_c_c_c_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS3 | VSS4 | C | Y |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 | X |   | X | X | X | X |
| NMOS3 | X |   |   |   |   | X |
| PMOS1 | X |   |   |   |   |   |
| Poly1 | X |   | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| NMOS3 | O |
| PMOS1 | O |
