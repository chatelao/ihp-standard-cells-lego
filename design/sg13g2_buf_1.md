# Design Documentation for sg13g2_buf_1

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
3 NNNNNNN
2 NppppNN
1 NpppNNN
0 NpppNpN
9 NpppNNN
8 NpppNpN
7 SSSSSSS
6 SSSSSSS
5 SSSSSSS
4 SnnnSnS
3 SnnnSSS
2 SnnnSSS
1 SSSSSSS
0 nnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456
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
  0123456
4 &+&+&+&
3    +
2    +&
1  C + O
0  CCC o
9    C O
8  I C o
7    C O
6  c cCO
5  CCC O
4  C   o
3    - O
2    _
1    -
0 -_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | X | VDD | VSS |
| --- | --- | --- | --- |
| NMOS1 |   |   | X |
| NMOS2 |   |   | X |
| NMOS3 | X |   |   |
| PMOS1 |   | X |   |
| PMOS2 | X |   |   |
| PMOS3 | X |   |   |
| PMOS4 |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| NMOS3 |   |
| PMOS1 | O |
| PMOS2 |   |
| PMOS3 |   |
| PMOS4 |   |
