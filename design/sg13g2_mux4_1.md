# Design Documentation for sg13g2_mux4_1

## Substrate
```
  0123456789012345678901234567890123456
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345678901234567890123456
4 ppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNpppppppppppppppppppppNNNNNNNNpppppN
1 NpppppppppppppppppppppppNNNNNNppppppp
0 NpppppppppppppppppppppppNNNNNNppppppp
9 NpppppppppppppppppppppppNNNNNNppppppp
8 NpppppppppppppppppppppppNNNNNNppppppp
7 NNpppppppppppppppppppppNNNNNNNNNNNNNN
6 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
5 SSSSSSSSSSSSSSSSSSSSSSnnnnnnnSSnnnnnn
4 SSSSSSSSSSSSSSSSSSSSSSnnnnnnnSSnnnnnn
3 SSSSSSSSSSSSSSSSSSSSSSnnnnnnnSSnnnnnn
2 SSSSSSSSSSSSSSSSSSSSSSnnnnnnnSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345678901234567890123456
4
3    GGGGGGGGGGGGGGGG
2   GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGG
1   GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGG
0   GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGG
9   GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGG
8   GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGG
7   GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGG
6   GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGG
5   GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGG
4   GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGG
3   GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGG
2   GGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGGG
1                          GGGGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345678901234567890123456
4 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
3 +++++++++++++++++++++++++++++++++++++
2 ++++++++++++++&+++++++++&+&+++++&++++
1 +++++++++++++++++++++++++++++++++++++
0 +&+&++++++&+++++++&+++&+&+&+&+&+&+++&
9 +++++++++++++++++++++++++++++++++++++
8 +&+&++++++&+&+&+++&+++++&+&+&+&++++++
7  IIiIiIIIIIIiIiIIIIIIIiiI+++++++&++OO
6  IIiIiIiIIiIiIiIiIIIiIiiI+++++&+&+&OO
5 -----------------------------------__
4 -_------_-----------_-_-----------___
3 -----------------------------------__
2 -_-_--------_---------_--------------
1 -------------------------------------
0 _____________________________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A2 | X |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 |   | X | X |   |
| NMOS3 | X | X |   | X |
| PMOS1 | X |   | X |   |
| PMOS2 | X |   | X | X |
| PMOS3 | X |   |   |   |
| Poly1 | X | X | X |   |
| Poly2 | X | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 | N |   |
| NMOS2 | O | O |
| NMOS3 | O |   |
| PMOS1 |   | O |
| PMOS2 | O |   |
| PMOS3 |   | S |
