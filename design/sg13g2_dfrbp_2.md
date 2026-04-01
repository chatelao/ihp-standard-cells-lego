# Design Documentation for sg13g2_dfrbp_2

## Substrate
```
  01234567890123456789012345678901234567890123456789012
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012
4 ppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 ppppppppppppppppppppppppppppppppppppppppppppppppppppp
2 ppppppppppppppppppppppppppppppppppppppppppppppppppppp
1 ppppppppppppppppppppppppppppppppppppppppppppppppppppp
0 ppppppppppppppppppppppppppppppppppppppppppppppppppppp
9 ppppppppppppppppppppppppppppppppppppppppppppppppppppp
8 ppppppppppppppppppppppppppppppppppppppppppppppppppppp
7 ppppppppppppppppppppppppppppppppppppppppppppppppppppp
6 NppppppNNNNNppppppNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
5 nnnnnnnnSSSSnnnnnnSnnnnnnnSSnnnnnSSSSSSSSnnnnnnSSSSSS
4 nnnnnnnnSSSSSSSSSSSnnnnnnnSnnnnnnSSSSSSSnnnnnnnSSSSSS
3 nnnnnnnnSSSSSSSSSSSnnnnnnnSnnnnnnSSSSSSSnnnnnnnSSSSSS
2 SnnnnnnSSSSSSSSSSSSnnnnnnnSnnnnnnSSSSSSSSnnnnnnSSSSSS
1 SSSSSSSSSSSSSSSSSSSnnnnnnnSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012
4
3     GGGGGGGGGGGGGGG
2  G GGGGGGGGGGGGGGGGGGGG GGGGGGG G G GGGGGGGGGG GGGGG
1  G GGGGGGGGGGGGGGGGGGGG GGGGGGG G G GGGGGGGGGG GGGGG
0  G GGGGGGGGGGGGGGGGGGGG GGGGGGGGGGG GGGGGGGGGG GGGGG
9  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGG GGGGG
8  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGG GGGGG
7  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGG GGGGG
6  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGG GGGGG
5  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGG GGGGG
4  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGG GGGGG
3  GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGG GGGGG
2  GGGGGGGGGGGGGGGGGGGGGG GGG G GGGGGGGGGGGGGGGG GGGGG
1     GGGGGGGGGGGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012
4 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
3 +++++++++++++++++++++++++++++++++++++++++++++++++++++
2 +++&++++++&+++++++&+++++++++++++++++&+++++++++++&+++&
1 +++++++++++++++++++++++++++++++++++++++++++++++++++++
0 +++++++&&+++++&+&+++&+++++++++++++++++&+++++&+++&+++&
9 +++++++++++++++++++++++++++++++++++++++++++++++++++++
8 +&+&++++++++++++++&+&+++++&+&+++&+++&+++++++&+++&+++&
7 ++++++++&&++++++++++++++&&+++++++++++++++++++++++++++
6 +&+++&++&&&+&+&+&IIIIIiIiiIIIIiII-_---_-OOoO++++OOOOO
5 +++++++++++++++++IIIIIIIiiIIIIIII-------OOoO++++OOooo
4 +++++++&&+++&++++---_-----_-_-_---------_-_-&+&+--___
3 +++++++++++++++++---------------------------++++-----
2 -----_--------------------------_---_-_------+&+-----
1 -----------------------------------------------------
0 _____________________________________________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | RESET_B | Internal1 | Internal2 | Internal3 | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X |   |   |   |   |   |
| NMOS2 | X | X | X |   |   |   |   |   |
| NMOS3 |   | X | X | X |   |   |   |   |
| NMOS4 | X | X |   |   |   |   |   | X |
| NMOS5 |   |   |   |   |   |   |   |   |
| PMOS1 | X | X | X | X | X | X | X |   |
| Poly1 | X | X | X |   | X | X |   |   |
| Poly2 | X | X | X | X |   | X |   | X |
| Poly3 | X | X |   |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 | O | O |   |
| NMOS2 | O |   |   |
| NMOS3 |   | O |   |
| NMOS4 |   | O | E |
| NMOS5 | O |   |   |
| PMOS1 | O | O | O |
