# Design Documentation for sg13g2_and4_2

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
2   G G GGGG
1   G G GGGG
0   G G GGGG
9   G G GGGG
8   G G GGGG
7   G G GGGG
6   GGGGGGGG
5   G G GGGG
4   G G GGGG
3   G G GGGG
2   G G GGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456789012345
4 &+&+&+&+&+&+&+&+
3  ++  +   +    +
2  &+  &   +    &
1  ++CC+ C +  OO+
0  &+cC& c +  oO&
9    CC  C    OO+
8  c   c    c oO
7  C I I IIICC O
6  c i i iiIcC O
5  C I I I     O
4  cC      -_ oO_
3  CC      -- OO-
2          -_   _
1          --   -
0 _-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A | B | D | Internal1 | Internal2 | Internal3 | Internal4 | Internal5 | X |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |   |   |   |   |   |   |
| NMOS2 |   | X |   |   |   | X |   |   |   |   | X |
| PMOS1 | X |   |   |   |   | X | X | X | X | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   | X | X | X |   |   |   |   | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |
