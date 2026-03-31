# Design Documentation for sg13g2_inv_8

## Substrate
```
  012345678901234567
4 NNNNNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567
4 pppppppppppppppppp
3 NNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNN
1 NppppppppppppppppN
0 NppppppppppppppppN
9 NppppppppppppppppN
8 NppppppppppppppppN
7 SSSSSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSS
4 SnnnnnnnnnnnnnnnnS
3 SnnnnnnnnnnnnnnnnS
2 SSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567
4
3
2      G GG  G G G
1      G GG  G G G
0      G GG  G G G
9      G GG  G G G
8      G GG  G G G
7   GGGGGGGGGGGGGG
6   GGGGGGGGGGGGGG
5      G GG  G G G
4      G GG  G G G
3      G GG  G G G
2      G GG  G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567
4 &+&+&+&+&+&+&+&+&+
3  +   +  +   +   +
2  +   +  +   +   +
1  + O +O + O + O +
0  + o +Oo+ o + o +
9  + OOOOOOOO + O +
8           o   o
7           O   O
6    iIiIii oOoOo
5           O   O
4  - oOoOooOo - o -
3  - O -O - O - O -
2  -   -  -   -   -
1  -   -  -   -   -
0 _-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | Y |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 |   |   |   | X |
| PMOS1 |   |   |   | X |
| PMOS2 | X |   |   |   |
| Poly1 |   |   | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |
