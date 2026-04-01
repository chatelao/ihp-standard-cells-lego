# Design Documentation for sg13g2_lgcp_1

## Substrate
```
  012345678901234567890123456
4 SSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456
4 ppppppppppppppppppppppppppp
3 ppppppppppppppppppppppppppp
2 ppppppppppppppppppppppppppp
1 ppppppppppppppppppppppppppp
0 ppppppppppppppppppppppppppp
9 ppppppppppppppppppppppppppp
8 ppppppppppppppppppppppppppp
7 NNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SnnnnnnnnnnnnnSSnnnnnSSSSSS
5 SnnnnnnnnnnnnnnnnnnnnnSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnSSSSS
3 SnnnnnnnnnnnnnnnnnnnnnSSSSS
2 SnnnnnnnnnnnnnnSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456
4
3
2   GGGGGGGGGGGGGGGGGGG GGG
1   GGGGGGGGGGGGGGGGGGG GGG
0   GGGGGGGGGGGGGGGGGGG GGG
9   GGGGGGGGGGGGGGGGGGG GGG
8   GGGGGGGGGGGGGGGGGGG GGG
7   GGGGGGGGGGGGGGGGGGG GGG
6   GGGGGGGGGGGGGGGGGGG GGG
5   GGGGGGGGGGGGGGGGGGG GGG
4   GGGGGGGGGGGGGGGGGGG GGG
3   GGGGGGGGGGGGGGGGGGG GGG
2   GGGGGGG GGGGGGGGGGG GGG
1            GGGGGGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 &&&&&&&&&&&&&&&&&&&&&&&&&&&
3 +++++++++++++++++++++++++++
2 ++++++++++&+++++++++++++&++
1 ++++++++++++++++++++++++&++
0 +&+&++++&+++++++&+&+&+++&++
9 +++++++++------+++++++++&++
8 +&+++&++&-----_++&++++&+&+
7  IIIIiIII------CCiI+++++oO
6  IIiIiIiI-_-_-_Cc i+++&+OO
5 ---------------------------
4 -_-_----_-_---_---_-_-_-_--
3 ---------------------------
2 -_--------_-----------_----
1 ---------------------------
0 ___________________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | CLK | GATE | Internal1 | GCLK |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 | X | X | X | X | X |   |
| PMOS1 | X | X |   | X | X | X |
| Poly1 | X | X | X | X | X |   |
| Poly2 | X | X |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 | N |   |
| NMOS2 | O | E |
| PMOS1 | O | O |
