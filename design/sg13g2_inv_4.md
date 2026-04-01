# Design Documentation for sg13g2_inv_4

## Substrate
```
  01234567890
4 SSSSSSSSSSS
3 NNNNNNNSSSS
2 NNNNNNNSSSS
1 NNNNNNNSSSS
0 SSSSSSSSSSS
9 SSSSSSSSSSS
8 SSSSSSSSSSS
7 SSSSSSSSSSS
6 SSSSSSSSSSS
5 SSSSSSSSSSS
4 SSSSSSSSSSS
3 SSSSSSSSSSS
2 SSSSSSSSSSS
1 SSSSSSSSSSS
0 SSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890
4 ppppppppppp
3 pppppppnnnn
2 pppppppnnnn
1 pppppppnnnn
0 SnnnnnnnSSS
9 SSSSSSSSSSS
8 SSSSSSSSSSS
7 SSSSSSSSSSS
6 SSSSSSSSSSS
5 SSSSSSSSSSS
4 SSSSSSSSSSS
3 SSSSSSSSSSS
2 SSSSSSSSSSS
1 SSSSSSSSSSS
0 nnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  01234567890
4
3
2   GGGGGGG
1   GGGGGGG
0   GGGGGGG
9   GGGGGGG
8   GGGGGGG
7   GGGGGGG
6   GGGGGGG
5   GGGGGGG
4   GGGGGGG
3   GGGGGGG
2   GGGGGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890
4 &&&&&&&&&&&
3 +++++++++++
2 +++&++++&++
1 +++++++++++
0 +++&+++&&++
9 +++++++++++
8 +++&+++&&+
7   iiiiiIiI
6   ciiiiiiI
5    IIIIIiI
4 ---_-_-__--
3 -----------
2 ---_----_--
1 -----------
0 ___________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A |
| --- | --- | --- | --- |
| NMOS1 |   | X |   |
| NMOS2 | X |   | X |
| PMOS1 | X |   | X |
| Poly1 | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
