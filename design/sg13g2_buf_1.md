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
2 NNNNNNN
1 NpppppN
0 NpppppN
9 NpppppN
8 NpppppN
7 SSSSSSS
6 SSSSSSS
5 SSSSSSS
4 SnnnnnS
3 SnnnnnS
2 SSSSSSS
1 SSSSSSS
0 nnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456
4
3
2 GGG
1 GGG
0 GGGG
9 GGGG
8 GGGG
7 GGGG
6 GGGG
5 GGGG
4 GGG
3 GGG
2 GGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456
4 +++++++
3    +
2  & + &
1  C + O
0  c   o
9  CCC O
8  iIc o
7    C O
6    iCo
5  CCC O
4 cCc-oO
3    - O
2   _-_O
1    -
0 -------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD2 | VSS | A | Internal1 | X |
| --- | --- | --- | --- | --- | --- |
| NMOS2 |   |   |   | X | X |
| PMOS1 |   |   | X | X | X |
| Poly1 | X | X | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |
