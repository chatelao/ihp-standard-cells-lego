# Design Documentation for sg13g2_nor4_2

## Substrate
```
  012345678901234567890
4 NNNNNNNNNNNNNNNNNNNNN
3 SNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890
4 ppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNN
1 NppppppppppppppNppppp
0 NppppppppppppppNppppp
9 NppppppppppppppNppppp
8 NppppppppppppppNppppp
7 NNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSS
5 Snnnnnnnnnnnnnnnnnnnn
4 Snnnnnnnnnnnnnnnnnnnn
3 Snnnnnnnnnnnnnnnnnnnn
2 SSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890
4
3
2   G G  GGGGG G   G G
1   G G  GGGGG G   G G
0   G G  GGGGG G   G G
9   G G  GGGGG G   G G
8   G G  GGGGG G   G G
7   GGG  GGGGGGG  GGGG
6   GGG  GGGGGGG  GGGG
5   G G  GGGGG G   G G
4   G G  GGGGG G   G G
3   G G  GGGGG G   G G
2   G G  GGGGG G   G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890
4 &+&+&+&+&+&+&+&+&+&+&
3 +++++++++++++++++++++
2  & c+& cCCcCCCc cCCCc
1  +CC++CCCCCCCCCCCCCCC
0  &Cc+&CccCcCcCcCc cCc
9  +CCCCCCCCCCCCCCC CCC
8  & cCCCCc c cCCCc cCc
7   II    II  II II C
6   ii    ii  ii Ii CO
5  - CCCCCCCCCCCCCCCC -
4  _CcC_-_cC_CcC_-_Cc-_
3  -CC----CC--CC--- C--
2  -  ----  --  ---  --
1 ---------------------
0 _-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | Y | A | B | C | D |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X |   |   |   |   |
| PMOS1 | X | X |   |   |   |   |
| PMOS2 |   | X |   |   |   |   |
| PMOS3 | X |   |   |   |   |   |
| Poly1 |   |   | X |   |   |   |
| Poly2 |   | X |   | X | X |   |
| Poly3 |   |   |   |   |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | O | O |
| PMOS1 | O | O |   |
| PMOS2 |   |   | O |
| PMOS3 |   |   |   |

