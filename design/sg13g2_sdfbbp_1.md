# Design Documentation for sg13g2_sdfbbp_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
9 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
8 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
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
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSnnnnnnnnnnnnnnnnnnnnnnnnnnnnSSnnnnnSnnnnnS
1 SnnnnnnnnnSSSSSSSSSSnnnnnnnnnnnnnnnnnnnnnnnnnnnnnSnnnnnSnnnnnS
0 SnnnnnnnnnSSSSSSSSSSnnnnnnnnnnnnnnnnnnnnnnnnnnnnnSnnnnnSnnnnnS
9 SSSSSSSSSSSSSSSSSSSSnnnnnnnnnnnnnnnnnnnnnnnnnnnnnSnnnnnSnnnnnS
8 SSSSSSSSSSSSSSSSSSSSnnnnnnnnnnnnnnnnnnnnnnnnnnnnSSnnnnnSnnnnnS
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
4 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
1 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
4
3                  GGGGGGGGGGGGGGGGGGGG
2   GGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGG
1   GGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGG
0   GGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGG
9   GGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGG
8   GGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGG
7   GGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGG
6   GGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGG
5   GGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGG
4   GGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGG
3   GGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGG
2   GGGGGGGGGGG GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGG
1     GGGGGGGG         GGGGGGGGGGGGGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
4 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
3 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
2 +&++++++&+&+&+++&+++++++++++++++++++++++++++++++&+++++++&+++++
1 ++++++++++++++++++++++++++++++++++++++++++++++++++++++&+++++&+
0 +&+&+++&++++&+&+&+&+&+++&+++++&+&+++&+++&+&+&+++++++&+&+&+++&+
9 ++++++++++++++++++++++++++++++++++++++++++++++++++++++&+++++&+
8   iIiIIIII&+++iIIIiIIIIIIIIIIIiIIIIIiIIIiIIiiIIIIIiIIIoOCC  o
7   iIiIIIII++++IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIOOCC  c
6   iiIiIiII++++iiIIiIiIIIiIIIiIiIiIiIIIIIIIiIiIIIiIiiiIOOcC  c
5   IIIIIIII++++IiIIIIIIIIIIIIIIIIIII IIIIIIIIIIIIIIIIIIOOCC  c
4 -_---_-_----_-------_-_---_---_---_---_-_---_-_-_-_---_-_---_-
3 ------------------------------------------------------------_-
2 --------------_-----------------_-------_---_---_-------------
1 --------------------------------------------------------------
0 ______________________________________________________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | D | Internal1 | Internal2 | Internal3 | Internal4 | Internal5 | Q | Q_N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | X | X | X | X | X | X | X |   | X | X |
| NMOS2 | X |   | X |   |   |   | X |   |   |   |
| NMOS3 | X |   | X |   |   |   |   |   |   | X |
| NMOS4 | X |   |   |   |   | X |   |   | X |   |
| NMOS5 | X |   | X |   |   |   |   |   |   |   |
| PMOS1 | X |   |   |   |   |   |   |   |   |   |
| Poly1 | X | X | X |   |   |   |   |   |   |   |
| Poly2 | X | X | X | X | X |   | X | X |   |   |
| Poly3 | X | X | X |   |   | X |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 | O | O | O |
| NMOS2 |   | O |   |
| NMOS3 |   |   | O |
| NMOS4 |   |   | O |
| NMOS5 | O |   |   |
| PMOS1 |   | S |   |
