# Design Documentation for sg13g2_and3_1_from_lef

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
2 NppppppppppN
1 NppppppppppN
0 NppppppppppN
9 NppppppppppN
8 NppppppppppN
7 SSSSSSSSSSSS
6 SSSSSSSSSSSS
5 SSSSSSSSSSSS
4 SnnnnnnnnnnS
3 SnnnnnnnnnnS
2 SnnnnnnnnnnS
1 SSSSSSSSSSSS
0 nnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901
4
3     G G G
2     G G G
1     G G G
0     G G G
9     G G G
8     G G G
7     G G G
6     GGGGG
5     G G G
4     GGG G
3     G G G
2     G G G
1     G G G
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 cccccccccccc
3
2    c   cc
1      C
0    c c cc c
9      C
8   CcCcCcc  O
7   C      C O
6   C  c ccC O
5   C      OOO
4      c c O
3          O
2  IIIII c
1
0 cccccccccccc
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | Internal1 | Internal10 | Internal11 | Internal12 | Internal13 | Internal2 | Internal3 | Internal4 | Internal5 | Internal6 | Internal7 | Internal8 | Internal9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 | X |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   | X | X | X |   |   |   |   |   |
| PMOS1 |   | X | X | X |   |   |   |   | X |   |   | X | X |
| PMOS2 |   |   |   |   | X |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   | X |   |   | X |   | X | X | X |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 | N |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 | S |
