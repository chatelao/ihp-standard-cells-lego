# Design Documentation for sg13g2_tielo

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
2 NpppppN
1 NpppppN
0 NpppppN
9 NpppppN
8 NNNpppN
7 NNNNNNN
6 SSSSSSS
5 SnnnnnS
4 SnnnnnS
3 SnnnnnS
2 SnnnnnS
1 nnnnSSS
0 nnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456
4
3     G
2     G
1   G G
0   G G
9  GG G
8  GGGG
7   GGG
6   G GG
5   G GG
4   G G
3   G G
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
2  +&
1
0  c   c
9  C   C
8  c c c
7    CCC
6    CCc
5  CCCC
4  cCCOo
3     OO
2  -_ Oo
1 -------
0 _-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Internal1 | L_LO |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   | X |
| PMOS1 | X |   | X | X |
| Poly1 |   |   | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 | O |
| PMOS1 | O |

