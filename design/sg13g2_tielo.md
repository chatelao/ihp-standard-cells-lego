# Design Documentation for sg13g2_tielo

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
3 NpppNNN
2 NpppppN
1 NNNpppN
0 NpppppN
9 NNNpppN
8 NNNNNNN
7 SSSSSSS
6 SSSSSSS
5 SnnnnnS
4 SnnnnnS
3 SSSnnnS
2 SnnnnnS
1 SnnnSSS
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
0  GGGGG
9  GGGGG
8  GGGGG
7  GGG G
6  GGG G
5  GGGGG
4  GGGGG
3  GGGGG
2  G GGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456
4 &+&+&+&
3   +
2   +
1
0  c   c
9  C   C
8  c   c
7    C C
6    c c
5    C
4  cCc o
3      O
2   - Oo
1   -
0 _-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Internal1 | Internal2 | Internal3 | L_LO |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X |   |   | X |
| PMOS1 | X |   |   | X | X |   |
| Poly1 |   |   | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 | O |
| PMOS1 | O |
