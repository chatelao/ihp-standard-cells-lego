# Design Documentation for sg13g2_einvn_2

## Substrate
```
  0123456789012345
4 NNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012345
4 pppppppppppppppp
3 NNNNNNNNNNNNNNNN
2 NppppppppppppppN
1 NppppppppppppppN
0 NppppppppppppppN
9 NppppppppppppppN
8 NppppppppppppppN
7 SSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnS
2 SnnnnnnnnnnnnnnS
1 SSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456789012345
4
3
2 GG G G       GGG
1 GG G G       GGG
0 GG G G       GGG
9 GGGG G       GGG
8 GGGG G       GGG
7 GGGG G       GGG
6 GGGG G       GGG
5 GGGG G       GGG
4 GGGG G       GGG
3 GG G G       GGG
2 GG G G       GGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &+&+&+&+&+&+&+&+
3   +     +
2   +     & cCcCc
1   + C C + C   C
0   + CcCc& c o c
9     C CCCCC O C
8  iIiC   c   o
7  IIIC       O
6  iIiCc      o i
5  IIIC       O I
4     C CccCc o i
3   - C C - CCCCC
2   -  c  _   c
1   -     -
0 _-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | A | TE_B | Internal1 | Internal2 | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |   |   |   |
| NMOS2 |   |   | X | X |   | X | X | X |
| PMOS1 | X | X |   |   | X |   |   | X |
| PMOS2 |   | X |   |   |   |   |   |   |
| Poly1 |   |   |   |   | X |   |   |   |
| Poly2 | X |   |   |   |   | X |   |   |
| Poly3 | X |   |   | X |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | O | O |
| PMOS1 | O | O | O |
| PMOS2 |   |   |   |
