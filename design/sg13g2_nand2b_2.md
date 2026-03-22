# Design Documentation for sg13g2_nand2b_2

## Substrate
GOLDEN STANDARD

```
  012345678901234
4 NNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
GOLDEN STANDARD

```
  012345678901234
4 ppppppppppppppp
3 NNNNNNNNNNNNNNN
2 pppNppppppppppN
1 pppNppppppppppN
0 pppNppppppppppN
9 pppNppppppppppN
8 pppNppppppppppN
7 SSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSS
4 SnnnSnnnnnnnnnS
3 SnnnSnnnnnnnnnS
2 SnnnSnnnnnnnnnS
1 SSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
GOLDEN STANDARD

```
  012345678901234
4
3       G G G G
2  G    G G G G
1  G    G G G G
0  G    G G G G
9  G    G G G G
8  G    G G G G
7  G    G G G G
6  G   GGGG GGG
5  G    G G G G
4  G    G G G G
3  G    G G G G
2  G    G G G G
1       G G G G
0
```
Legend: G=Polysilicon

## Metal 1
GOLDEN STANDARD

```
  012345678901234
4 &+&+&+&+&+&+&+&
3 +    +   +   +
2 +    & o & o &
1 & c  + O + O +
0 + C  & o & o &
9 & C  + OOOOO +
8   C  &     o &
7   C        O
6 IiCCCc   IiO
5   C        O
4 _ c  cCCCc o c
3 -    C   C   C
2 -    c _ cCCCc
1 -      -
0 _-_-_-_-_-_-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Connection (upper side)

## Connectivity Matrix

| Silicon | A_N | B | Internal1 | Internal2 | Y | VDD | VSS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   |   | X |
| NMOS2 |   |   |   | X |   |   |   |
| NMOS3 |   |   | X |   | X |   | X |
| PMOS1 |   |   |   | X |   | X |   |
| PMOS2 |   |   |   |   | X | X |   |
| PMOS3 |   |   |   |   |   | X |   |
| Poly1 |   |   |   | X |   |   |   |
| Poly2 |   | X |   |   |   |   |   |
| Poly3 | X |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Overlaps With |
| --- | --- |
| NMOS2 | Poly3 |
| NMOS3 | Poly1 |
| NMOS3 | Poly2 |
| PMOS1 | Poly3 |
| PMOS2 | Poly1 |
| PMOS2 | Poly2 |
