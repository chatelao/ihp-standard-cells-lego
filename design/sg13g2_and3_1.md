# Design Documentation for sg13g2_and3_1

## Substrate
```
  012345678901
4 SSSSSSSSSSSS
3 NNNNNNNSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 SSSSSSSSSSSS
9 SSSSSSSSSSSS
8 SSSSSSSSSSSS
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SSSSSSSSSSSS
3 SSSSSSSSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 SSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901
4 pppppppppppp
3 pppppppnnnnn
2 nnnnnnnnnnnn
1 Snnnnnnnnnnn
0 Snnnnnnnnnnn
9 Snnnnnnnnnnn
8 SnnnnnnnnnnS
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SnnnnnnnnnSS
4 SnnnnnnnnnSS
3 SnnnnnnnnnSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  012345678901
4
3         GG
2  GGGGGGGGG
1  GGGGGGGGG
0  GGGGGGGGG
9  GGGGGGGGG
8  GGGGGGGGG
7  GGGGGGGGG
6  GGGGGGGGG
5  GGGGGGGGG
4  GGGGGGGGG
3  GGGGGGGGG
2  GGGGGGGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &&&&&&&&&&&&
3 ++++++++++++
2 +&+++&++++++
1 ++++++++++++
0 +&+++&++++&+
9  +++++++++OO
8  +++++++++oO
7  +++&&+&++OO
6  +++&&+&&+OO
5  ++++++++&oO
4 -_---_--_-_-
3 -----_------
2 -_-_-_------
1 ------------
0 ____________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | B | C | X |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 | X | X | X |   |   |   |
| NMOS3 | X |   |   |   |   | X |
| PMOS1 | X |   |   |   |   |   |
| Poly1 | X | X | X | X | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| NMOS3 | O |
| PMOS1 | S |
