# Design Documentation for sg13g2_nor2b_2

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
8 Snnnnnnnnnnn
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 Snnnnnnnnnnn
4 Snnnnnnnnnnn
3 Snnnnnnnnnnn
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  012345678901
4
3
2  GGGGGGGGGG
1  GGGGGGGGGG
0  GGGGGGGGGG
9  GGGGGGGGGG
8  GGGGGGGGGG
7  GGGGGGGGGG
6  GGGGGGGGGG
5  GGGGGGGGGG
4  GGGGGGGGGG
3  GGGGGGGGGG
2  GGGGGGGGGG
1    GGGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &&&&&&&&&&&&
3 ++++++++++++
2 +&++++++++&+
1 ++++++++++++
0 +&+++&+&&+&+
9 ++++++++++++
8 +&+&+++&&+++
7  ++++OOOooc
6  ++++OOOioc
5 -----_------
4 -_---_-__-_-
3 -_---_------
2 -_----------
1 ------------
0 ____________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | B_N | Y |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 | X | X |   |   | X |
| NMOS3 | X |   |   |   | X |
| PMOS1 | X |   |   |   |   |
| Poly1 | X | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 | N |
| NMOS2 | O |
| NMOS3 | O |
| PMOS1 | S |
