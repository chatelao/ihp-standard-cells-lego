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
2 G       G G
1 G       G G
0 G       G G
9 G       G G
8 G       G G
7 G       G G
6 G       G G
5 G       G G
4 G       G G
3 G       G G
2           G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 ++++++++++++
3  +  ++++   +
2 &+  ++++& &+
1  +  ++++   +
0  +  ++++&  +
9  +  ++++   +
8     ++++
7     ++++
6   - ++++  -
5   -       -
4   -       -
3  --   -  ---
2 _-- _ - _---
1  --   -  ---
0 ------------
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD |
| --- | --- |
| PMOS1 | X |
| Poly1 | X |
| Poly2 | X |
| Poly3 | X |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 | Poly3 |
| --- | --- | --- | --- |
| NMOS1 |   |   |   |
| NMOS2 | O | W | O |
| PMOS1 | O | W | O |
| PMOS2 |   |   |   |
