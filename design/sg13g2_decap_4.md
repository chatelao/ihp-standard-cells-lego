# Design Documentation for sg13g2_decap_4

## Substrate
```
  0123456
4 SSSSSSS
3 NNNNNNN
2 NNNNNNN
1 NNNNNNN
0 NNNNNNN
9 NNNNNNN
8 NNNNNNN
7 NNNNNNN
6 SSSSSSS
5 SSSSSSS
4 SSSSSSS
3 SSSSSSS
2 SSSSSSS
1 SSSSSSS
0 SSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456
4 ppppppp
3 ppppppp
2 ppppppp
1 ppppppp
0 ppppppp
9 ppppppp
8 ppppppp
7 ppppppp
6 SSSSSSS
5 SSSSSSS
4 SSSSSSS
3 SSSSSSS
2 SSSSSSS
1 SSSSSSS
0 nnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  0123456
4
3
2  GGGGG
1  GGGGG
0  GGGGG
9  GGGGG
8  GGGGG
7  GGGGG
6  GGGGG
5  GGGGG
4  GGGGG
3  GGGGG
2  GGGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456
4 &&&&&&&
3 +++++++
2 +++++++
1 +++++++
0 +++++++
9 +++++++
8 +&+++&+
7 -------
6 ---_-_-
5 -------
4 -_-----
3 -------
2 -----_-
1 -------
0 _______
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS |
| --- | --- | --- |
| NMOS1 |   | X |
| PMOS1 | X |   |
| Poly1 | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| PMOS1 | O |
