# Design Documentation for sg13g2_decap_8

## Substrate
```
  012345678901
4 NNNNNNNNNNNN
3 NNNNNNNNNNNN
2 NNNNNNNNNNNN
1 NNNNNNNNNNNN
0 NNNNNNNNNNNN
9 NNNNNNNNNNNN
8 NNNNNNNNNNNN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SSSSSSSSSSSS
3 SSSSSSSSSSSS
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 SSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901
4 pppppppppppp
3 NNNNNNNNNNNN
2 NNNNNNNNNNNN
1 Nppppppppppp
0 Nppppppppppp
9 Nppppppppppp
8 NNNNNNNNNNNN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 Snnnnnnnnnnn
3 Snnnnnnnnnnn
2 SSSSSSSSSSSS
1 SSSSSSSSSSSS
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901
4
3
2   GGGG GGGG
1   GGGG GGGG
0   GGGG GGGG
9   GGGG GGGG
8   GGGG GGGG
7   G      GG
6   G  GGG GG
5      G G
4   GGGG GGGG
3   GGGG GGGG
2   GGGG GGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &+&+&+&+&+&+
3  +  ++++   +
2  +  ++++   +
1  +  ++++   +
0  +  ++++   +
9  +  ++++   +
8     ++++
7     ++++
6   - ++++  -
5   -       -
4   -       -
3  --   -  ---
2  --   -  ---
1  --   -  ---
0 _-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS |
| --- | --- | --- |
| NMOS1 |   | X |
| NMOS2 |   |   |
| PMOS1 |   |   |
| PMOS2 | X |   |
| Poly1 |   |   |
| Poly2 |   |   |
| Poly3 |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O |   |   |
| PMOS1 |   | O | O |
| PMOS2 |   |   |   |
