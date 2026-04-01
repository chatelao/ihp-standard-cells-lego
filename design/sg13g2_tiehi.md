# Design Documentation for sg13g2_tiehi

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
7 NNNNNNN
6 SSSSSSS
5 nnnnnnn
4 nnnnnnn
3 nnnnnnn
2 nnnnnnn
1 nnnnnnn
0 nnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456
4
3     GG
2  G GGG
1 GG GGG
0 GGGGGG
9 GGGGGG
8 GGGGGG
7 GGGGGG
6 GGGGGG
5 GGGGGG
4 GGGGGG
3 GG GGG
2  G GGG
1    G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456
4 &&&&&&&
3 +++++++
2 +&+++++
1
0      oO
9 CCCC oO
8 CcCC oO
7 CCCC OO
6 CcCc oO
5 CCCC
4 CCCC c
3 -------
2 -------
1 -------
0 _______
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Internal1 | Internal2 | Internal3 | L_HI |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   | X |   |   |
| PMOS1 | X |   | X |   |   | X |
| Poly1 | X |   | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 | O |
| PMOS1 | O |
