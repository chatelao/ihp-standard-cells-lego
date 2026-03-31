# Design Documentation for sg13g2_einvn_8

## Substrate
```
  012345678901234567890123456789012345678
4 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456789012345678
4 ppppppppppppppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NpppNpppppppppppppppppppppppppppppppppN
0 NpppNpppppppppppppppppppppppppppppppppN
9 NpppNpppppppppppppppppppppppppppppppppN
8 NpppNpppppppppppppppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
4 SnnnSSnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
3 SnnnSSnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456789012345678
4
3
2   GG GGGG G G G G G     G G G G G G G
1   GG GGGG G G G G G     G G G G G G G
0   GG GGGG G G G G G     G G G G G G G
9   GG GGGG G G G G G     G G G G G G G
8   GG GGGG G G G G G     G G G G G G G
7  GGGGGGGGGGGGGGGGGGG    G G G G G G G
6  GGG G GG G G G G G    GGGGGGGGGGGGGG
5    G G GGGGGGGG G G     G G G G G G G
4    G G GGGGGGGG G G     G G G G G G G
3    G G GGGGGGGG G G     G G G G G G G
2    G G GGGGGGGG G G     G G G G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456789012345678
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&
3  +     +   +   +  +
2  +     +   +   +  +  CcCcCcCcCcCcCcCc
1  + C C + C + C +CC+  C   C   C   C  C
0  + c c +cC +cC +cC+  C O CoO C O CoOc
9  + C C + C + C +CC   C O   O   O   OC
8  + c c   C   C  cCcCcC OoOoOoOoOoOoO
7    C CCCCCCCCCCCC      OOO
6  i c  CccCcCcCcCcCcCcC OoO IiIiIiIiIi
5  I CCCC   C   C   C  C OOO
4  - cCcC - c - c - c- CcOoOoOoOoOoOoOc
3  - CCCC - C - C - C- CCCCCCCCC   C  C
2  -      -   -   -  -      c cCcCcCcCc
1  -      -   -   -  -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | TE_B | Internal1 | Z |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   |   |   |   | X |   |
| NMOS3 |   |   |   |   | X | X |
| PMOS1 |   |   |   |   | X |   |
| PMOS2 |   |   |   |   | X | X |
| PMOS3 | X |   |   |   |   |   |
| Poly1 |   |   |   | X | X |   |
| Poly2 |   |   | X |   | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O |   |
| NMOS3 | O | O |
| PMOS1 | O |   |
| PMOS2 | O | O |
| PMOS3 |   |   |
