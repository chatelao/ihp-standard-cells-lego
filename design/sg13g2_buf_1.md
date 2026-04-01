# Design Documentation for sg13g2_buf_1

## Substrate
```
  0123456
4 SSSSSSS
3 NNNNNNN
2 NNNNNNN
1 NNNNNNN
0 NNNNNNN
9 NNNNNNN
8 NNNNNNN
7 NNNNNNN
6 SSSSSSS
5 SSSSSSS
4 SSSSSSS
3 SSSSSSS
2 SSSSSSS
1 SSSSSSS
0 SSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456
4 ppppppp
3 ppppppp
2 ppppppp
1 ppppppp
0 ppppppp
9 ppppppp
8 ppppppp
7 ppppppp
6 SSSSSSS
5 SnnnnnS
4 nnnnnnS
3 nnnnnnS
2 SnnnnnS
1 SSSSSSS
0 nnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  0123456
4
3
2  GGGG
1  GGGG
0  GGGG
9  GGGG
8  GGGG
7  GGGG
6  GGGG
5  GGGG
4  GGGG
3  GGGG
2  G GG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456
4 &&&&&&&
3 +++++++
2 +++++++
1 +++++++
0 IiIIIo
9 IIIIIo
8 IiiIIiI
7 IIIIIII
6 IIIiIII
5 IIIIIII
4 -_---_-
3 -------
2 -----_-
1 -------
0 _______
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | X |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 |   | X | X | X |
| PMOS1 | X |   | X | X |
| Poly1 |   | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
