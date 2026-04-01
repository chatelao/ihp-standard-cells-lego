# Design Documentation for sg13g2_sdfrbp_2

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4 ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
2 ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
1 ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
0 ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
9 ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
8 ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
7 ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
6 NNNNNNNNNNNNNNNNNNNppppppNNNNNppppppNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
5 SnnnnnnnnnnnnnnnnSnnnnnnnnSSSSnnnnnnSnnnnnnnSnnnnnSSSSSSSSnnnnnnnSSSSSS
4 SnnnnnnnnnnnnnnnnSnnnnnnnnSSSSSSSSSSnnnnnnnnSnnnnnnSSSSSSSnnnnnnnSSSSSS
3 SnnnnnnnnnnnnnnnnSnnnnnnnnSSSSSSSSSSnnnnnnnnSnnnnnnSSSSSSSnnnnnnnSSSSSS
2 SnnnnnnnnnnnnnnnnSSnnnnnnSSSSSSSSSSSnnnnnnnnSnnnnnnSSSSSSSnnnnnnnSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSnnnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4
3                       GGGGGGGGGGGGGGG
2   GGGG GG G GGGG  G GGGGGGGGGGGGGGGGGGGGG GGGGGGG   G GGGGGGGGGGGGGGGG
1   GGGG GGGG GGGG  G GGGGGGGGGGGGGGGGGGGGG GGGGGGG   GGGGGGGGGGGGGGGGGG
0   GGGG GGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGG
9   GGGG GGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGG
8   GGGG GGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGG
7   GGGG GGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGG
6   GGGGGGGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGG
5   GGGGGGGGG GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGG
4   GGGGGGGG  GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGG
3   GGGGGGGG  GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGG
2   GGGGGGGG  GGGG  GGGGGGGGGGGGGGGGGGGGGGG GGG G GGGGGGGGGGGGGGGGGGGGGG
1                       GGGGGGGGGGGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901234567890
4 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
3 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
2 ++++++++++++++++++&+++++++++&+++++++&+++++++++++++++++&+++++++++++&+++&
1 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
0 +&+&++++&+++++&+&+++++++&+&+++++&+&+++&+++++++++++++++++++&+++&+++&+++&
9 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
8 +&++++++++++++&+&+&+&+++++++++++++++&+&+++&+&+&+&+++++&+++&+++&+++&+++&
7 ++++++++&+&+++++++++++++++&&+++++++++++++&&&+++++++++++++++++++++++++++
6  IiiIIIiiIiIiIi+++&+++++&+&&&+&+&+&IIIiIIiiiIIIIiII-_-----OOoO++&+OOOOO
5  IIIIIIIIIiIIII++++++++++++++++++++IIIIIIiiiIIIIIII-------OOoO++++OOooO
4 -_---_----_----+&+++++&+&+&+++&++++-_-----_---_-_---------_-_-&+&+--__-
3 ---------------++++++++++++++++++++---------------------------++++-----
2 -----_--------_-+++-----------------------------------_-_-----++++----_
1 -----------------------------------------------------------------------
0 _______________________________________________________________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | D | RESET_B | Internal1 | Internal2 | Internal3 | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   | X |   |   |   |   |   |
| NMOS2 | X | X | X |   |   |   |   |   |   |
| NMOS3 | X | X |   | X |   |   |   |   |   |
| NMOS4 |   | X |   | X | X |   |   |   |   |
| NMOS5 | X | X |   |   |   |   |   |   | X |
| NMOS6 |   |   |   |   |   |   |   |   |   |
| PMOS1 | X | X | X | X | X | X | X | X | X |
| Poly1 | X | X |   | X |   | X | X |   |   |
| Poly2 | X | X | X |   |   |   |   |   |   |
| Poly3 | X | X | X |   |   |   |   |   |   |
| Poly4 | X | X |   | X | X |   | X | X | X |

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
