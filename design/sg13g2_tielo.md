# Design Documentation for sg13g2_tielo

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
8 NNNNNNN
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
3    G
2  G GGG
1  GGGGG
0  GGGGG
9  GGGGG
8  GGGGG
7  GGGGG
6  GG GG
5  GG GG
4  GG GG
3  GG GG
2  G  GG
1     GG
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
0  cCCCcC
9  CCCCCC
8  cCCCcC
7  CCCCCC
6  CCCCcC
5  CCCCCC
4  cCCOoC
3  CCCOoC
2 -_---_-
1 -------
0 _______
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Internal1 | L_LO |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X | X | X |
| PMOS1 | X |   | X |   |
| Poly1 | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 | O |
| PMOS1 | O |
