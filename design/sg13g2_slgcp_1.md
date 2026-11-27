# Design Documentation for sg13g2_slgcp_1

## Substrate
```
  012345678901234567890123456789
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSNNNNNNSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789
4 pppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNppNNNNNNN
2 NNNNNNNpNNNNNNNNNNNNNppNNNpppN
1 NpppppppppNppppppppppppppppppN
0 NppppppppppppppppppppppppppppN
9 NpppppppppppppNNpppppppppppppN
8 NNNNNNppppppppNNpppNpppppppppN
7 NNNNNNNNNNNNNNNNpppNNNNNNNNNNN
6 SSSSSSSSSSSSSSSNNNNNNSSSSSSSSS
5 SnnnnnnnSSSSSSSSnnSnnnnnnSSSSS
4 nnnnnnnnnnnnnnnnnnnnnnnnnSnnnS
3 nnnnnnnnnnnnnnnnnnnnnnnnnSnnnS
2 SSSSnnnnSnnnnnnnnnSnnnSSSSSSSS
1 SSSSnnSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789
4
3         GGGGGG
2   G G   GGGGGGGG G   G G GGG
1   G G   G  GGGGG G   G G GGG
0   G G   G  GGGGG G   G G GGG
9   G G   G  GG  G G   G G GGG
8  GG GG  G  GGGGG G   GGG GGG
7  GG GG  G GGGGG  G  GGG  GGG
6   G G GGGGGGGGGGGG  GGGGGGGG
5   G G GGGGG GGG GG  G GGG  G
4   G G G   G GGG G   G GG   G
3   G G G   G GGG G   G GG   G
2   G   G   G GGG G   G GG   G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3 ++++++++++++++++++++++++++++++
2 +&   c+&       ++        ++ o
1 ++  CC++   C C ++CCCCCC C++OO
0 +&  CcCCCCCcCc  &Cc   C c+&Oo
9       C  CCCCC   CCCC CCC++OO
8    IiIC Cc cCccCCCcCc CCcC Oo
7  I IIICCCCCCCC   CCC ICCCCCCO
6  i CCCCCCc cCCCCcCCC iCcCCCcO
5    CC  CCCCCC CCCCCC -  CC  O
4 -_CcC  c  CcCCCCCcCcC_  cC_ o
3 --CCCCCCCCCCCC--CC CC-  CC- O
2 --  -_    cCCC-_CCCcC-    _ o
1 ------------------------------
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | GCLK | CLK | GATE |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X |   |   |   |
| NMOS2 |   | X |   | X |   |   |
| PMOS1 | X |   | X | X |   |   |
| Poly1 |   |   |   |   |   |   |
| Poly2 |   |   | X |   |   |   |
| Poly3 | X |   | X |   | X |   |
| Poly4 |   |   |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 |
| --- | --- | --- | --- | --- |
| NMOS1 | O | O | O | O |
| NMOS2 |   |   | O |   |
| PMOS1 | O | O | O | O |

