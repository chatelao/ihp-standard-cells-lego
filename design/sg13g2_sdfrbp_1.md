# Design Documentation for sg13g2_sdfrbp_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901234567
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901234567
4 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNppppppppppppppppppppppppppppppppppppppppppppppppppp
2 Nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
1 Nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
0 Nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
9 Nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
8 Nppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
7 NNNNNNNNNNNNNNNNNNpppppppppppppppppppppppppppppppppppppppppppppppppN
6 NNNNNNNNNNNNNNNNNNNppppppNNNNNppppppNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
5 SnnnnnnnnnnnnnnnnSnnnnnnnnSSSSnnnnnnSnnnnnnnSnnnnnSSSSSSSSnnnnnSSSSS
4 SnnnnnnnnnnnnnnnnSnnnnnnnnSSSSSSSSSSnnnnnnnnSnnnnnnSSSSSSSnnnnnnSSSS
3 SnnnnnnnnnnnnnnnnSnnnnnnnnSSSSSSSSSSnnnnnnnnSnnnnnnSSSSSSSnnnnnnSSSS
2 SnnnnnnnnnnnnnnnnSSnnnnnnSSSSSSSSSSSnnnnnnnnSnnnnnnSSSSSSSnnnnnSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnnnnnnnnSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901234567
4
3                       GGGGGGGGGGGGGGG
2   GGGG GG G GGGG  G GGGGGGGGGGGGGGGGGGGGG GGGGGGG   G GGGGGGGGGGGG
1   GGGG GGGG GGGG  G GGGGGGGGGGGGGGGGGGGGG GGGGGGG   GGGGGGGGGGGGGG
0   GGGG GGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGG
9   GGGG GGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGG
8   GGGG GGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGG
7   GGGG GGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGG
6   GGGGGGGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGG
5   GGGGGGGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGG
4   GGGGGGGG  GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGG
3   GGGGGGGG  GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGG
2   GGGGGGGG  GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGG G GGGGGGGGGGGGGGGGGG
1                       GGGGGGGGGGGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901234567
4 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
3 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
2 ++++++++++++++++++&+++++++++&+++++++&+++++++++++++++++&+++++++++++&+
1 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
0 +&+&++++&+++++&+&+++++++&+&+++++&+&+++&+++++++++++++++++++&+++&+++&+
9 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
8 +&++++++++++++&+&+&+&+++++++++++++++&+&+++&+&+&+&+++++&+++&+++&+&+&+
7 ++++++++&+&+++++++++++++++&&+++++++++++++&&&+++++++++++++++++++++++
6  IiiIIIiiIiIiIi+++&+++++&+&&&+&+&+&IIIiIIiiiIIIIiII-_-----OOOOcC oo
5  IIIIIIIIIiIIII++++++++++++++++++++IIIIIIiiiIIIIIII-------oooOCC OO
4 -_---_----_----+&+++++&+&+&+++&++++-_-----_---_-_---------___-_---_-
3 ---------------++++++++++++++++++++---------------------------------
2 -----_--------_-+++-----------------------------------_-_---------_-
1 --------------------------------------------------------------------
0 ____________________________________________________________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | D | RESET_B | Internal1 | Internal2 | Internal3 | Internal4 | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   | X |   |   |   |   |   |   |
| NMOS2 | X | X | X |   |   |   |   |   |   |   |
| NMOS3 | X | X |   | X |   |   |   |   |   |   |
| NMOS4 |   | X |   | X | X |   |   |   |   |   |
| NMOS5 |   | X |   |   |   | X |   |   |   | X |
| NMOS6 |   |   |   |   |   |   |   |   |   |   |
| PMOS1 | X | X | X | X | X | X | X | X | X | X |
| Poly1 | X | X |   | X |   |   | X | X |   |   |
| Poly2 | X | X | X |   |   |   |   |   |   |   |
| Poly3 | X | X | X |   |   |   |   |   |   |   |
| Poly4 | X | X |   | X | X | X |   | X |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 | O |   |   | O |
| NMOS2 |   | O | O |   |
| NMOS3 | O |   |   |   |
| NMOS4 |   |   |   | O |
| NMOS5 |   |   |   | O |
| NMOS6 | O |   |   |   |
| PMOS1 | O | O | O | O |
