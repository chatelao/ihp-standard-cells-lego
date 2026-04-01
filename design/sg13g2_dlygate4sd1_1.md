# Design Documentation for sg13g2_dlygate4sd1_1

## Substrate
```
  01234567890123
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 SSSSSSSSSSSSSS
9 SSSSSSSSSSSSSS
8 SSSSSSSSSSSSSS
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 SSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123
4 pppppppppppppp
3 SSSSSSSSSSSSSS
2 SnnnnnnSnnnnnS
1 nnnnnnnSnnnnnn
0 nnnnnnnSnnnnnn
9 nnnnnnnSnnnnnn
8 SnnnnnnSnnnnnn
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSnnnnnS
4 SSSSSSSSnnnnnn
3 SSSSSSSSnnnnnn
2 SSSSSSSSnnnnnS
1 SSSSSSSSSSSSSS
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  01234567890123
4
3
2   G GG  GGGGG
1   G GG  GGGGG
0   G GG  GGGGG
9   G GG  GGGGG
8   G GG  GGGGG
7   G GG  GGGGG
6   GGGG  GGGGG
5   G GG  GGGGG
4   G GG  GGGGG
3   G GG  GGGGG
2   G GG  G GGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &&&&&&&&&&&&&&
3 ++++++++++++++
2 ++++++++++++++
1 ++++++++++++++
0 +&+++&++++&+++
9 ++++++++++++++
8 IIIIICCCoOOOOO
7 IiiIIICCOOOOOO
6 IiiiIICCoOOOoO
5 IIIIIICCOOOooo
4 IIIIIICCoOOOoO
3 --------------
2 ----------_---
1 --------------
0 ______________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | Internal1 | X |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 |   | X |   | X | X |
| NMOS3 | X |   | X | X |   |
| NMOS4 | X |   |   | X | X |
| PMOS1 | X |   |   |   |   |
| Poly1 | X |   | X | X |   |
| Poly2 | X | X |   | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 |   | O |
| NMOS3 | O |   |
| NMOS4 |   | O |
| PMOS1 |   |   |
