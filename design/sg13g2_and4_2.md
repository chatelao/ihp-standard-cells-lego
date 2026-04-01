# Design Documentation for sg13g2_and4_2

## Substrate
```
  0123456789012345
4 SSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSS
9 SSSSSSSSSSSSSSSS
8 SSSSSSSSSSSSSSSS
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345
4 pppppppppppppppp
3 SSSSSSSSSSSSSSSS
2 SSnnnnnnnnnnnnnS
1 Snnnnnnnnnnnnnnn
0 Snnnnnnnnnnnnnnn
9 Snnnnnnnnnnnnnnn
8 Snnnnnnnnnnnnnnn
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSnnnnnnnnnnnnnS
4 Snnnnnnnnnnnnnnn
3 Snnnnnnnnnnnnnnn
2 SSnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  0123456789012345
4
3
2   GGGGGGGGGGGG
1   GGGGGGGGGGGG
0   GGGGGGGGGGGG
9   GGGGGGGGGGGG
8   GGGGGGGGGGGG
7   GGGGGGGGGGGG
6   GGGGGGGGGGGG
5   GGGGGGGGGGGG
4   GGGGGGGGGGGG
3   GGGGGGGGGGGG
2   GGGGGGGGGGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &&&&&&&&&&&&&&&&
3 ++++++++++++++++
2 +&++++++++&+&+++
1 ++++++++++++&&++
0 +&+&+++&++&+&&++
9 ++++++++++++&&++
8 ++++++++++++&+++
7  IIiIiIiiiIIOO
6  IIiIiIiiiiIOO
5  IIIIIIIIIIIOO
4 -_--------_-_---
3 ----------------
2 ----------_-_---
1 ----------------
0 ________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | C | X |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 |   | X | X | X |
| NMOS3 | X |   | X | X |
| PMOS1 | X |   |   |   |
| Poly1 | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| NMOS3 | O |
| PMOS1 |   |
