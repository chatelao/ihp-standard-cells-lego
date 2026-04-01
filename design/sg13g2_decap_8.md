# Design Documentation for sg13g2_decap_8

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
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  012345678901
4
3
2  GGGGG GGGG
1  GGGGG GGGG
0  GGGGG GGGG
9  GGGGG GGGG
8  GGGGG GGGG
7  GGGGGGGGGG
6  GGGGGGGGGG
5  GGGGGGGGGG
4  GGGGGGGGGG
3  GGGGGGGGGG
2  GGGGGGGGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &&&&&&&&&&&&
3 ++++++++++++
2 +++&++++++&+
1 ++++++++++++
0 ++++++++&+&+
9 ++++++++++++
8 +&++++++&+&+
7 ------------
6 -_-_----_---
5 ------------
4 -_---_--_---
3 ------------
2 ------------
1 ------------
0 ____________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS |
| --- | --- | --- |
| NMOS1 |   | X |
| NMOS2 | X |   |
| PMOS1 | X |   |
| Poly1 | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | S |
