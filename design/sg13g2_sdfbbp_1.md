# Design Documentation for sg13g2_sdfbbp_1

## Substrate
```
  01234567890123456789012345678901234567890123456789012345678901
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123456789012345678901
4 pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNpppppppppppppNNNNpppNpppppN
1 NpppppppppNpppNpppppNppNNNpppppppppppppppppppppppNNNpppNpppppN
0 NpppppppppNpppNppppppppppppppppppppppppppppppppppNpppppNpppppN
9 NNNNNNNNNNNNNNNpppppppppppppppppppppppNNNNpppppppNpppppNpppppN
8 NNNNNNNNNNNNNNNpppppNNNNNNppppppppppNNNNNNpppppppNpppppNNNpppN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSnnnnnnSSSSSnnnnnnnnnnSnnnnSSSnnnnnnnSnnnnnSSSnnnS
4 SnnnnnnnnnnnSnnnnnnSnnnnnnnnnnnnnnnnnnnnnnnnnnnnnSnnnnnSnnnnnS
3 SnnnnnnnnnnnSnnnnnnSnnnnnnnnnnnnnnnnnnnnnnnnnnnnnSnnnnnSnnnnnS
2 SSSSSSSSSSSSSSSnnSSSSSSSSnnnnnSSnnSSSSnnnnnnnnnnnSSSnnnSnnnnnS
1 SSSSSSSSSSSSSSSnnSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012345678901234567890123456789012345678901
4
3                     GGGGGGGGGGGGGGGG
2   G G G G   G  GGGGGGGGGGGGGGGGGGGGGGGGG   G GG      G   G G
1   G G G G   G  GGGGGGGGGG  G  G GGGGGGGG   G GG    G G   G G
0   G G G G   G  GGGGGGGGGGG G  G GGGGGGGG   G GG    G G   G G
9   G G G GGG G  GGGGGGGGGGG G  G GGGGGGGGGG G GG    G G   G G
8  GGGG GG GG G  GGGGGGGGGGG G  G GGGGG G GG G GG    G G GGG G
7  GGGG GG G  G GGGGGGGGG GG GG G GGGGGGG  GGG GGG   G G G G G
6  GGGG GGGGGGG GGGGGGGGGGGG GGGGGGGGG GG  G GGGGGG GGGGGGGGGG
5  GGGG GGGGG   G  G G G GGG G GGGG GGGGGGGG G G GG  G GGGGG G
4   G G GG  G   G  G G G GGG G GGGG  GGG GGG G G G   G G   G G
3   G G GG  G   G  G G G GGG G GGGG  GGG G G G G G   G G   G G
2   G GGGGGGG   G  G GGG GGGGGGGGGGGGGGG G G G G G     G   G G
1     GGGGGGG            GGGGGGGGGGGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123456789012345678901
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
2  c &+CCCCc+& c c&+c      ++ IIII++IIIIII&+& c  &+   & o   &
1  CC++C  CC++CCCC++CC     ++ IC I++IICC I+++CCC ++   + OOC + O
0  cCCCC c   CCcCc&+cCCccC +& IcCI+&IICcCICCCCcCCCCCCCC oOc & o
9  CCCCC CCCCCCCCC  CCCCCCC++ ICCIIIIICCCICC ICCCCCCCCCCOOC + O
8   i i  CCCcC CCcCCcCCCCCCCC IcCCCCC cCCICcIIcCC  Cc CCoOC   o
7   I I IICC C CIICCCCCCCCCCCCI C  CC CCCIIIII  C CCC CCOOCC  O
6   i   IiCC C CiICcCCCcCCCcCCiCc cCc CCCCCCCiCcCCcC iCcOOCc  O
5   I  CCCCCCC CII  CCCCCCCCCCCCC  CC CCCCCCCCCCC CC   COOC   O
4  _   c  _CCc c ICCcCcCcCCCCCCCCcCC-_CCccC _CcCcCcCcC_OoOc _ o
3  --  C  -CCC CCCCCCCCCCC  -  C C C--C  CC -CC CCC   -OOOC - O
2  --     -CCCCCC-_         _ CcCCCc--CCCCC _CcCCCc   - o   _
1 --------------------------------------------------------------
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | CLK | Internal1 | RESET_B | SCD | Q | Q_N | D | SCE | SET_B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X |   |   |   |   |   |   |   |   |
| NMOS2 |   | X | X |   | X |   |   |   |   |   |   |
| NMOS3 |   | X |   |   | X |   |   | X |   |   |   |
| NMOS4 |   | X |   | X |   |   | X |   |   |   |   |
| NMOS5 |   | X | X |   |   |   |   |   |   |   |   |
| PMOS1 | X |   | X |   | X |   |   |   |   |   |   |
| PMOS2 | X |   |   |   | X |   |   | X |   |   |   |
| PMOS3 | X |   |   | X |   |   | X |   |   |   |   |
| PMOS4 |   |   | X |   |   | X |   |   |   |   |   |
| PMOS5 |   |   | X |   |   |   |   |   |   |   |   |
| PMOS6 | X |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   | X |   |   | X |   |   | X | X |   |
| Poly2 | X | X | X |   | X |   |   |   |   |   | X |
| Poly3 |   |   |   | X | X |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 | N | O |   |
| NMOS2 |   | O |   |
| NMOS3 |   |   | O |
| NMOS4 |   |   | O |
| NMOS5 | O |   |   |
| PMOS1 |   | O |   |
| PMOS2 |   |   | O |
| PMOS3 |   |   | O |
| PMOS4 | O |   |   |
| PMOS5 | O |   |   |
| PMOS6 |   | S |   |

