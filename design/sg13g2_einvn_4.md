# Design Documentation for sg13g2_einvn_4

## Substrate
```
  01234567890123456789012
4 NNNNNNNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012
4 ppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNN
2 NpppppppppppppppppppppN
1 NpppppppppppppppppppppN
0 NpppppppppppppppppppppN
9 NpppppppppppppppppppppN
8 NpppppppppppppppppppppN
7 SSSSSSSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234567890123456789012
4
3
2 G GG      G G G  G GG
1 G GG      G G G  G GG
0 G GG      G G G  G GG
9 G GG      G G G  G GG
8 G GG   GG G G G  G GG
7 G GG   GG G G G  G GG
6 GGGG   GG G G G  GGGG
5 G GG   GG G G G  G GG
4 G GG   G  G   G  G GG
3 G GG   G  G   G  G GG
2 G GG   G  G   G  G GG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012
4 &+&+&+&+&+&+&+&+&+&+&+&
3  +      +  +
2  &      &  + CcCcCcCcC
1  + C  C +C + C   C   C
0  & c cC &Cc+ C OcCoO C
9  + C  C +C + C O   O C
8    c  C  Cc  C OoOoO
7  IIC  CCCCCCCC  OIIII
6  iIc  CccCcCcCc oIiIi
5    C  C   C   COOOOOO
4  _ cCcC _ c _ cOo o o c
3  - CCCC - C - CCCCC   C
2  _      _   _   c cCcCc
1  -      -   -
0 _-_-_-_-_-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | A | TE_B | Z |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |
| NMOS2 |   | X | X |   |   | X |
| PMOS1 | X |   | X |   |   | X |
| PMOS2 | X |   |   |   |   |   |
| Poly1 |   |   | X |   | X |   |
| Poly2 |   |   | X |   |   |   |
| Poly3 |   |   | X |   |   |   |
| Poly4 |   |   | X |   |   |   |
| Poly5 |   |   | X | X |   | X |
| Poly6 |   |   | X |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 | Poly4 | Poly5 | Poly6 |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   |
| NMOS2 | O | O | O | O | O | N |
| PMOS1 | O | O | O | O | O | O |
| PMOS2 |   |   |   |   |   |   |
