# Design Documentation for sg13g2_tiehi

## Substrate
```
  0123456
4 NNNNNNN
3 SNNNNNN
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
3 ppppNNN
2 ppppppN
1 ppppppN
0 ppppppN
9 ppppppN
8 ppppppN
7 NNNNNNN
6 SSSSSSS
5 nnnnnnS
4 nnnnnnS
3 SSnnnnS
2 SSnnnnS
1 SSnnSSS
0 nnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456
4
3     G
2     G
1  GG G
0  GG G
9  GG G
8  GG G
7  GG GG
6 GGGGGG
5 GGGGG
4  GG G
3  GG G
2     G
1     G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456
4 &+&+&+&
3 +++++++
2 &+
1
0      o
9 CC   O
8 cC   o
7 CCCCCC
6 c  cCc
5 C  C C
4 c    c
3    -
2   -_
1 -------
0 _-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Internal1 | L_HI |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X | X |   |
| PMOS1 | X |   | X | X |
| Poly1 |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 | O |
| PMOS1 | O |

