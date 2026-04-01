# Design Documentation for sg13g2_sdfrbpq_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901
4 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNppppppppppppppppppppppppppppppppppppppppppppp
2 Nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
1 Nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
0 Nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
9 Nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
8 NppppppppppppppppNpppppppppppppppppppppppppppppppppppppppppppp
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSnnnnnnSSSSSnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SnnnnnnnnnnnnnnnnSnnnnnnnnSSSSnnnnnnSnnnnnnnSnnnnnSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnSnnnnnnnnSSSSSSSSSSnnnnnnnnSnnnnnnSSSSSSSSSSS
3 SnnnnnnnnnnnnnnnnSnnnnnnnnSSSSSSSSSSnnnnnnnnSnnnnnnSSSSSSSSSSS
2 SnnnnnnnnnnnnnnnnSSnnnnnnSSSSSSSSSSSnnnnnnnnSnnnnnnSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnnnnnnnnSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
4
3                       GGGGGGGGGGGGGGG
2   GGGG GG G GGGG  G GGGGGGGGGGGGGGGGGGGGG GGGGGGG   G GGG GG
1   GGGG GGGG GGGG  G GGGGGGGGGGGGGGGGGGGGG GGGGGGG   GGGGG GG
0   GGGG GGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGG GG
9   GGGG GGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGG GG
8   GGGG GGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGG GG
7   GGGG GGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGG GG
6   GGGGGGGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGG GG
5   GGGGGGGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGG GG
4   GGGGGGGG  GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGG GG
3   GGGGGGGG  GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGG GG
2   GGGGGGGG  GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGG G GGGGGGGGG GG
1                       GGGGGGGGGGGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
4 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
3 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
2 ++++++++++++++++++&+++++++++&+++++++&+++++++++++++++++&+++++++
1 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
0 +&+&++++&+++++&+&+++++++&+&+++++&+&+++&+++++++++++++++&+++++&+
9 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
8 +&++++++++++++&+&+&+&+++++++++++++++&+&+++&+&+&+&+++++&+&+++&+
7  IIIIIIIiIiIIII+++++++++++&&+++++++IIIIIIiiiIIIIIII--------OOO
6  IiiIIIiiIiIiIi+++&+++++&+&&&+&+&+&IIIiIIiiiIIIIiII-_-----_OOO
5  IIIIIIIIIiIIII++++++++++++++++++++IIIIIIiiiIIIIIII--------ooO
4 -_---_----_----+&+++++&+&+&+++&++++-_-----_---_-_---------___-
3 ---------------++++++++++++++++++++---------------------------
2 -----_--------_-+++-----------------------------------_-_-----
1 --------------------------------------------------------------
0 ______________________________________________________________
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
| Poly4 | X | X | X |   | X |   | X |   |
| Poly5 |   | X |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 |
| --- | --- | --- | --- | --- | --- |
| NMOS1 | O |   |   | O |   |
| NMOS2 |   | O | O |   |   |
| NMOS3 | O |   |   |   |   |
| NMOS4 |   |   |   | O |   |
| NMOS5 | O |   |   |   |   |
| PMOS1 | O | O | O | O | O |
