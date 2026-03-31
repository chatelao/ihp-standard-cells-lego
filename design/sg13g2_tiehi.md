# Design Documentation for sg13g2_tiehi

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
3 ppppNNN
2 ppppppN
1 NNNpppN
0 ppppppN
9 ppppppN
8 ppppppN
7 SSSSSSS
6 SSSSSSS
5 SSSSSSS
4 nnnnnnS
3 SSSnnnS
2 SSSnnnS
1 SSSnSSS
0 nnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456
4
3
2  G GGG
1  G GGG
0  G GGG
9  G GGG
8  G GGG
7  G GGG
6 GG G G
5  G GGG
4  G GGG
3  G GGG
2  G GGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456
4 &+&+&+&
3 +
2 +
1
0      o
9 CC   O
8  c   o
7  CCC C
6 C  c c
5 C  C C
4 Cc   c
3
2    -
1    -
0 _-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Internal1 | Internal2 | Internal3 | L_HI |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X | X |   |   |
| PMOS1 | X |   |   |   | X | X |
| Poly1 |   |   | X |   | X |   |
| Poly2 |   |   |   | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 | O | O |
| PMOS1 | O | O |
