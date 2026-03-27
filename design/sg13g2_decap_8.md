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
2 NppppppppppN
1 NppppppppppN
0 NppppppppppN
9 NppppppppppN
8 NppppppppppN
7 SSSSSSSSSSSS
6 SSSSSSSSSSnS
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
3
2  GGGGGGGGGG
1  GGGGGGGGGG
0  GGGGGGGGGG
9  GGGGGGGGGG
8  GGGGGGGGGG
7  GGGGGGGGGG
6  GGGGGGGGG
5  GGGGGGGGGG
4  GGGGGGGGG
3  GGGGGGGGGG
2   GGGGGGGG
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901
4 &+&+&+&+&+&+
3  +  ++++   +
2  &  +&+&   +
1  +  ++++   +
0  &  +&+&   +
9  +  ++++   +
8     +&+&
7     ++++
6   - +&+&  _
5   -       -
4   -       _
3  --   -   --
2  _-   -   _-
1  --   -   --
0 _-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS |
| --- | --- | --- |
| NMOS1 |   | X |
| NMOS2 |   | X |
| NMOS3 |   | X |
| PMOS1 | X |   |
| PMOS2 | X |   |
| Poly1 | X |   |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 |   |
| NMOS2 | O |
| NMOS3 | NSW |
| PMOS1 | O |
| PMOS2 |   |
