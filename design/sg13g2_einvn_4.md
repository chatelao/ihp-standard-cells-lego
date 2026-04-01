# Design Documentation for sg13g2_einvn_4

## Substrate
```
  01234567890123456789012
4 SSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSS
9 SSSSSSSSSSSSSSSSSSSSSSS
8 SSSSSSSSSSSSSSSSSSSSSSS
7 SSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012
4 ppppppppppppppppppppppp
3 SSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SnnnnnnnSSSSSSSSSSSSSSS
0 SnnnnnnnSSSSSSSSSSSSSSS
9 SnnnnnnnSSSSSSSSSSSSSSS
8 SnnnnnnnSSSSSSSSSSSSSSS
7 SnnnnnnnSSSSSSSSSSSSSSS
6 SnnnnnnnSSSSSSSSSSSSSSS
5 SnnnnnnnSSSSSSSSSSSSSSS
4 SnnnnnnnSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  01234567890123456789012
4
3
2  GGGGGGGGGGGG GGGGGGGG
1  GGGGGGGGGGGG GGGGGGGG
0  GGGGGGGGGGGG GGGGGGGG
9  GGGGGGGGGGGG GGGGGGGG
8  GGGGGGGGGGGG GGGGGGGG
7  GGGGGGGGGGGG GGGGGGGG
6  GGGGGGGGGGGG GGGGGGGG
5  GGGGGGGGGGGGGGGGGGGGG
4  GGGGGGGGGGGGGGGGGGGGG
3  GGGGGGGGGGGGGGGGGGGGG
2  GGGGGGGGGGGGGGGGGGGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012
4 &&&&&&&&&&&&&&&&&&&&&&&
3 +++++++++++++++++++++++
2 +++&+&+&++&+&+&+&+++&++
1 +++++++++++++++++++++++
0 +++&+&+&++&+&+&+&+&+&++
9 +++++++++++++++++++++++
8 +++&++++&+&+&+&+&+&+&++
7  iiII++++++++++++&&&&+
6  iiIII OOOOOOOOIIiiiiO
5  IIIIIOOOOOOOOOIIIIIIOO
4 ---_-_-_--_---_-_---_-_
3 -----------------------
2 ---_---_--_---_---_---_
1 -----------------------
0 _______________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | TE_B | Internal1 | Z |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 | X | X |   | X | X | X |
| PMOS1 | X |   |   |   |   |   |
| Poly1 | X | X | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 |   |
