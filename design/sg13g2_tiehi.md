# Design Documentation for sg13g2_tiehi

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
8 ppppppp
7 SSSSSSS
6 SSSSSSS
5 SSSSSSS
4 nnnnnnn
3 nnnnnnn
2 nnnnnnn
1 nnnnnnn
0 nnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  0123456
4
3
2    G G
1 GG G G
0 GG G G
9 GG G G
8 GG G G
7 GG G G
6 GG G G
5 GG G G
4 GG G G
3 GG G G
2 GG   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456
4 +++++++
3 +
2 +& &
1
0      o
9 CC   O
8  c   o
7  CCC C
6 C  c c
5 C  C C
4 c    C
3
2   _-_
1    -
0 -------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | Internal1 | Internal2 | Internal3 | L_HI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X | X |   |   |   |
| PMOS1 | X | X |   |   |   | X | X |
| Poly1 |   |   |   | X |   | X |   |
| Poly2 |   |   |   |   | X |   | X |
| Poly3 |   | X |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 | O | O | O |
| PMOS1 | O | O | O |
