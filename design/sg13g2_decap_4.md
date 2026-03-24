# Design Documentation for sg13g2_decap_4

## Substrate
```
  0123456
4 NNNNNNN
3 NNNNNNN
2 NNNNNNN
1 NNNNNNN
0 NNNNNNN
9 NNNNNNN
8 NNNNNNN
7 SSSSSSS
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
3 NNNNNNN
2 NpppppN
1 NpppppN
0 NpppppN
9 NpppppN
8 NpppppN
7 SSSSSSS
6 SnSnSSS
5 SSSSSSS
4 SnnnnnS
3 SnnnnnS
2 SnnnnnS
1 SSSSSSS
0 nnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456
4
3
2 GGGGGGG
1  GGGGG
0 GGGGGGG
9  GGGGG
8 GGGGGGG
7  GGGGG
6   G GG
5  GGGGG
4   G GG
3  GGGGG
2   G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456
4 &+&+&+&
3 +++++++
2 &+ +&+&
1 ++ ++++
0 &+ +&+&
9 ++ ++++
8 &+ +&+&
7  ---++
6  _-_&+
5  ---++
4  _-_
3 ---- --
2 -_-_ _-
1 -------
0 -_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS |
| --- | --- | --- |
| NMOS1 |   | X |
| NMOS2 |   | X |
| NMOS3 |   | X |
| NMOS4 | X | X |
| PMOS1 | X |   |
| PMOS2 | X |   |
| Poly1 | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| NMOS3 | NSE |
| NMOS4 | NSEW |
| PMOS1 | O |
| PMOS2 |   |
