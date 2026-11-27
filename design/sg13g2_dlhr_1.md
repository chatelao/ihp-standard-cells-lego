# Design Documentation for sg13g2_dlhr_1

## Substrate
```
  01234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901
4 pppppppppppppppppppppppppppppppp
3 NNNppNNNNppNNNNNNNNNNNNNNNNNNNNN
2 NNNppNNNNppppppppppppppppNpppppN
1 NppppppppppppppppppppppppppppppN
0 NppppppppppppppppppppppppppppppN
9 NpppppppppppppNNNNNppppppppppppN
8 NppppppNppppppNNNNNpppppppNNpppN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SnnnnnnnnnnSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnSnnnnnnSnnnnnS
3 SnnnnnnnnnnnnnnnnnSnnnnnnnnnnnnS
2 SSSSSSSSnnnnnnSSSSSnnnnnnnnnnnnS
1 SSSSSSSSSnnSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901
4
3
2          G GG G GG GGGGGG  G G
1   GG G   G GG G GG GGGGGG  G G
0   GG G   G GG G GG GGGGGG  G G
9   GG G   G GG GGGG GGGGGG  G G
8   GG G   G GG GGGG GGGGGG  G G
7   GGGG GGGGGGGGGGGGGGGGGG  G G
6   GGGGGGGGGGGGGGGGGGGGGGGGGGGG
5   G GG   G GGGGGGG  GGGG   G G
4   G GG   G GG GGG   GG G   G G
3   G GG   G GG GGG   GG G   G G
2     GG   G GG GGG   GG G   G G
1            GG       GG G   G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3 ++++++++++++++++++++++++++++++++
2    +&    +& CCCC &+&  &+oO  &
1  C ++    ++CCCCC +++CC++OOC +OO
0  cCCCCCCCCCCCcCC    Cc&+oOc &Oo
9  CC   C C CCCCCCCCCCCC  OOC +OO
8  C    cCcCCCCC cCcCCCcCCCOC  Oo
7  C I ICCCCCCCCCCCCCCC  CCOC   O
6  C i iCcCCcCCcC   cCCi cCOCCCcO
5  C --CCCCCCCCCC    CCI   OC   O
4  cC_-cCCcC   cC -_CcC-_OoOC _Oo
3    --CCCCCCCCCC --CCC--OO C -OO
2    _-     _CCCcC--CcC-_Oo c _Oo
1 --------------------------------
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | D | GATE | Internal1 | Q | Q_N | RESET_B |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X |   |   |   |   |
| NMOS2 |   | X | X | X | X | X |   |
| PMOS1 | X |   | X | X | X | X |   |
| Poly1 | X | X | X | X | X |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 | O |
| NMOS2 | O |
| PMOS1 | O |

