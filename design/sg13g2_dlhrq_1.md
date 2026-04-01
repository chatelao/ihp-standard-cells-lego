# Design Documentation for sg13g2_dlhrq_1

## Substrate
```
  012345678901234567890123456
4 SSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234567890123456
4 ppppppppppppppppppppppppppp
3 NNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNppppNNpppppppppppppppppNN
1 NpppppppppppppppppppppppppN
0 NpppppppppppppppppppppppppN
9 NpppppppppppppppppppppppppN
8 NpppppppppppppppppppppppppN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SnnnnnSnnnnnnnnnnnSSSSSSSSS
4 nnnnnnnnnnnnnnnnnnSSSSSSSSS
3 nnnnnnnnnnnnnnnnnnSSSSSSSSS
2 SnnnnnSSnnnnnnnnnnSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSS
0 nnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  012345678901234567890123456
4
3
2  GGGGG GG GGGGGGGGGGGGGGG
1  GGGGGGGGGGGGGGGGGGGGGGGG
0  GGGGGGGGGGGGGGGGGGGGGGGG
9  GGGGGGGGGGGGGGGGGGGGGGGG
8  GGGGGGGGGGGGGGGGGGGGGGGG
7  GGGGGGGGGGGGGGGGGGGGGGGG
6  GGGGGGGGGGGGGGGGGGGGGGGG
5  GGGGGGGGGGGGGGGGGGGGGGGG
4  GGGGGGGGGGGGGGGGGGGGGGGG
3  GGGGGGGGGGGGGGGGGGGGGGGG
2  GGGGGGGGGGGGGGGGGGGGGGGG
1        GG    GGGGG
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678901234567890123456
4 &&&&&&&&&&&&&&&&&&&&&&&&&&&
3 +++++++++++++++++++++++++++
2 ++++++++++++++++++++&+++&++
1 +++++++++++++------+++++&&+
0 +&+&++++++&++-_-_-_-&+++&&+
9 ++++++--------------++++&&+
8 +++++_--_-----------&+&+&&
7  iIIi_--------------+&+++O
6  iIIi_-_--_-_-_---_-+&&++O
5  IIII---------------+++++O
4  iIII_----_---_---_-++++&O
3 ---------------------------
2 ---_-_----------_----------
1 ---------------------------
0 ___________________________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | GATE | RESET_B | Q |
| --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |   |
| NMOS2 |   | X | X |   |   |
| PMOS1 | X | X | X |   | X |
| PMOS2 | X |   |   |   |   |
| Poly1 | X | X | X | X | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 | N |
| NMOS2 | O |
| PMOS1 | O |
| PMOS2 |   |
