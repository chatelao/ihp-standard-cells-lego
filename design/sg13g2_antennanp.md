# Design Documentation for sg13g2_antennanp

## Substrate
```
  01234
4 SSSSS
3 NNNNN
2 NNNNN
1 NNNNN
0 NNNNN
9 NNNNN
8 NNNNN
7 NNNNN
6 NNNNN
5 SSSSS
4 SSSSS
3 SSSSS
2 SSSSS
1 SSSSS
0 SSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234
4 ppppp
3 ppppp
2 ppppp
1 ppppp
0 ppppp
9 ppppp
8 ppppp
7 ppppp
6 ppppp
5 nnnnn
4 SnSSS
3 SSSSS
2 SSSSS
1 SSSSS
0 nnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  01234
4
3
2   G
1   G
0   G
9   G
8  GG
7   G
6   G
5   G
4   G
3   G
2   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234
4 &&&&&
3 +++++
2 +++++
1 +++++
0 +++++
9 +++++
8 +&+&+
7 +&+++
6 +&+++
5 +&+++
4  iIiI
3  III
2   II
1
0 _c_c_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A |
| --- | --- | --- | --- |
| NMOS1 |   | X |   |
| NMOS2 |   |   | X |
| PMOS1 | X |   | X |
| Poly1 | X |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
