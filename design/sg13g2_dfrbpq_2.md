# Design Documentation for sg13g2_dfrbpq_2

## Substrate
```
  01234567890123456789012345678901234567890123456789
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789
4 pppppppppppppppppppppppppppppppppppppppppppppppppp
3 pppppppppppppppppppppppppppppppppppppppppppppppppp
2 pppppppppppppppppppppppppppppppppppppppppppppppppp
1 pppppppppppppppppppppppppppppppppppppppppppppppppp
0 pppppppppppppppppppppppppppppppppppppppppppppppppp
9 pppppppppppppppppppppppppppppppppppppppppppppppppp
8 pppppppppppppppppppppppppppppppppppppppppppppppppp
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 NppppppNNNNNppppppNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
5 nnnnnnnnSSSSnnnnnnSnnnnnnnSSnnnnnSSSSSSSSSSSSSSSSS
4 nnnnnnnnSSSSSSSSSSSnnnnnnnSnnnnnnSSSSSSSSSSSSSSSSS
3 nnnnnnnnSSSSSSSSSSSnnnnnnnSnnnnnnSSSSSSSSSSSSSSSSS
2 SnnnnnnSSSSSSSSSSSSnnnnnnnSnnnnnnSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSnnnnnnnSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789
4
3     GGGGGGGGGGGGGGG
2  G GGGGGGGGGGGGGGGGGGGG GGGGGGG G G GGGGGG GGGGG
1  G GGGGGGGGGGGGGGGGGGGG GGGGGGG G G GGGGGG GGGGG
0  G GGGGGGGGGGGGGGGGGGGG GGGGGGGGGGG GGGGGG GGGGG
9  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGG GGGGG
8  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGG GGGGG
7  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGG GGGGG
6  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGG GGGGG
5  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGG GGGGG
4  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGG GGGGG
3  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGG GGGGG
2  GGGGGGGGGGGGGGGGGGGGGG GGG G GGGGGGGGGGGG GGGGG
1     GGGGGGGGGGGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789
4 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
3 ++++++++++++++++++++++++++++++++++++++++++++++++++
2 +++&++++++&+++++++&+++++++++++++++++&+&+++++++&+++
1 ++++++++++++++++++++++++++++++++++++++++++++++++++
0 +++++++&&+++++&+&+++&+++++++++++++++++&+++++++&+++
9 ++++++++++++++++++++++++++++++++++++++++++++++++++
8 +&+&++++++++++++++&+&+++++&+&+++&+++&+++++++++&+++
7 ++++++++&&+++++++IIIIIIIiiIIIIIII-----------  OOO
6 +&+++&++&&&+&+&+&IIIIIiIiiIIIIiII-_---_-----  ooo
5 +++++++++++++++++IIIIIIIiiIIIIIII-----------  OOO
4 +++++++&&+++&++++---_-----_-_-_-----------_---_---
3 +++++++++++++++++---------------------------------
2 -----_--------------------------_---_-_---_-------
1 --------------------------------------------------
0 __________________________________________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | RESET_B | Internal1 | Internal2 | Internal3 | Q |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X |   |   |   |   |
| NMOS2 | X | X | X |   |   |   |   |
| NMOS3 |   | X | X | X |   |   |   |
| NMOS4 |   |   |   |   |   |   |   |
| PMOS1 | X |   | X |   |   |   |   |
| PMOS2 | X |   | X |   | X |   |   |
| PMOS3 | X | X | X | X |   | X | X |
| Poly1 | X | X | X |   | X | X |   |
| Poly2 | X | X | X | X |   | X |   |
| Poly3 | X | X |   |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 | O | O |   |
| NMOS2 | O |   |   |
| NMOS3 |   | O |   |
| NMOS4 | O |   |   |
| PMOS1 | O |   |   |
| PMOS2 | O |   |   |
| PMOS3 | O | O | O |
