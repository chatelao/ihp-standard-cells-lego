# Design Documentation for sg13g2_nor2b_2

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
8 Nppppppppppp
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 Snnnnnnnnnnn
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
2  GG GGGGG
1  GG GGGGG
0  GG GGGGG
9  GG GGGGG
8  GG GGGGG
7  GGGGGGGG
6  GG GGGGG
5  GG GGGGG
4  GG GGGGG
3  GG GGGGG
2  GG GG GG
1     GGGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &+&+&+&+&+&+
3    +       +
2  & +   c   +
1  C + CCCCC +
0  c + c ocC +
9  C +   O C +
8  c   oOo
7  CCC O  III
6  c   o  iIi
5  C - OOOOO -
4    - o ooO -
3  I - O - O -
2  _ -   -   -
1    -   -   -
0 _-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD2 | VSS | VSS2 | A | B_N | Internal1 | Internal2 | Y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   | X |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   |   |   |   | X |
| PMOS1 |   |   |   |   |   |   | X | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |
| Poly1 |   | X |   | X | X | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 | N |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |
