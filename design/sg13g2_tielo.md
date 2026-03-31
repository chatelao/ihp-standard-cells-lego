# Design Documentation for sg13g2_tielo

## Substrate
```
  0123456
4 NNNNNNN
3 NNNNNNN
2 NNNNNNN
1 NNNNNNN
0 NNNNNNN
9 NNNNNNN
8 NNNNNNN
7 SSSSSSS
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
8 NNNNNNN
7 SSSSSSS
6 SSSSSSS
5 nnnnnnn
4 nnnnnnn
3 nnnnnnn
2 nnnnnnn
1 nnnnnnn
0 nnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456
4
3
2  G G G
1  GGG G
0  GGG G
9  GGG G
8  GGG G
7  GGG G
6  GGG G
5  GGG G
4  GGG G
3  GGG G
2  G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456
4 +++++++
3   +
2  &+&
1
0  c   c
9  C   C
8  c   c
7    C C
6    c c
5    C
4  CcCoO
3      O
2 _ - _O
1   -
0 -------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS2 | VSS3 | Internal1 | Internal2 | Internal3 | L_LO |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X | X |   |   | X |
| PMOS1 | X |   |   |   | X | X |   |
| Poly1 | X |   |   | X |   | X |   |
| Poly2 |   |   |   |   | X |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 | O | O |
| PMOS1 | O | O |
