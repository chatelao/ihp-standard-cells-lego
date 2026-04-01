# Design Documentation for sg13g2_sdfrbpq_2

## Substrate
```
  0123456789012345678901234567890123456789012345678901234567890123
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
2 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
1 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
0 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
9 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
8 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSnnnnnnSSSSSnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SnnnnnnnnnnnnnnnnSnnnnnnnnSSSSnnnnnnSnnnnnnnSnnnnnSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnSnnnnnnnnSSSSSSSSSSnnnnnnnnSnnnnnnSSSSSSSSSSSSS
3 SnnnnnnnnnnnnnnnnSnnnnnnnnSSSSSSSSSSnnnnnnnnSnnnnnnSSSSSSSSSSSSS
2 SnnnnnnnnnnnnnnnnSSnnnnnnSSSSSSSSSSSnnnnnnnnSnnnnnnSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnnnnnnnnSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456789012345678901234567890123
4
3                       GGGGGGGGGGGGGGG
2   GGGG GG G GGGG  G GGGGGGGGGGGGGGGGGGGGG GGGGGGG   G GGGGGGGG
1   GGGG GGGG GGGG  G GGGGGGGGGGGGGGGGGGGGG GGGGGGG   GGGGGGGGGG
0   GGGG GGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGG
9   GGGG GGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGG
8   GGGG GGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGG
7   GGGG GGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGG
6   GGGGGGGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGG
5   GGGGGGGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGG
4   GGGGGGGG  GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGG
3   GGGGGGGG  GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGG
2   GGGGGGGG  GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGG G GGGGGGGGGGGGGG
1                       GGGGGGGGGGGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456789012345678901234567890123
4 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
3 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
2 ++++++++++++++++++&+++++++++&+++++++&+++++++++++++++++&+++++++++
1 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
0 +&+&++++&+++++&+&+++++++&+&+++++&+&+++&+++++++++++++++++++&+++&+
9 ++++++++++++++++++++++++++++++++++++++++++++++++++++------++++++
8 +&++++++++++++&+&+&+&+++++++++++++++&+&+++&+&+&+&++---_---&+++&+
7  IIIIIIIiIiIIII+++++++++++&&+++++++IIIIIIiiiIIIIIII-------OOOO
6  IiiIIIiiIiIiIi+++&+++++&+&&&+&+&+&IIIiIIiiiIIIIiII-_-----OOoO
5  IIIIIIIIIiIIII++++++++++++++++++++IIIIIIiiiIIIIIII-------OOoO
4 -_---_----_-----_-----_-_-_---_-----_-----_---_-_-----------_---
3 ----------------------------------------------------------------
2 -----_--------_---------------------------------------_-_---_---
1 ----------------------------------------------------------------
0 ________________________________________________________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | CLK | D | Internal1 | Internal2 | Internal3 | Q |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X |   |   |   |   |   |
| NMOS2 | X | X |   | X |   |   |   |   |
| NMOS3 | X | X | X |   |   |   |   |   |
| NMOS4 |   | X | X |   | X |   |   |   |
| NMOS5 | X |   | X |   |   | X |   |   |
| PMOS1 | X | X | X | X | X |   | X | X |
| Poly1 | X | X | X |   |   | X | X |   |
| Poly2 | X | X |   | X |   |   |   |   |
| Poly3 | X | X |   | X |   |   |   |   |
| Poly4 | X | X | X |   | X |   | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 | O |   |   | O |
| NMOS2 |   | O | O |   |
| NMOS3 | O |   |   |   |
| NMOS4 |   |   |   | O |
| NMOS5 | O |   |   |   |
| PMOS1 | O | O | O | O |
