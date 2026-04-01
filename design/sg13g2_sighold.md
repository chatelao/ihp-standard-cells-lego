# Design Documentation for sg13g2_sighold

## Substrate
```
  012345678
4 SSSSSSSSS
3 NNNNNNNSS
2 NNNNNNNSS
1 NNNNNNNSS
0 NNNNNNNSS
9 NNNNNNNSS
8 SSSSSSSSS
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 SSSSSSSSS
3 SSSSSSSSS
2 SSSSSSSSS
1 SSSSSSSSS
0 SSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678
4 ppppppppp
3 pppppppnn
2 pppppppnn
1 pppppppnn
0 pppppppnn
9 pppppppnn
8 nnnnnnnnn
7 SSSSSSSSS
6 SSSSSSSSS
5 SSSSSSSSS
4 nnnnnnnnn
3 nnnnnnnnn
2 nnnnnnnnn
1 nnnnnnnnn
0 nnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P)

## Polysilicon
```
  012345678
4
3
2  G
1  G
0  GG
9  GG
8  GG
7  GG
6  GG
5  GG
4  GG
3  GG
2  G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  012345678
4 &&&&&&&&&
3 +++++++++
2 +&+++++&+
1
0
9  CCCCCC
8 CcCCCCCc
7 CCCCCCCc
6 CCCcCCCc
5 CCCCCCCc
4 CcCCCCCc
3
2 ---------
1 ---------
0 _________
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | SH |
| --- | --- | --- | --- |
| NMOS1 |   | X | X |
| NMOS2 | X |   | X |
| PMOS1 | X |   |   |
| Poly1 | X |   | X |

## Silicon Neighbourhood

| Silicon | Poly1 |
| --- | --- |
| NMOS1 | O |
| NMOS2 | O |
| PMOS1 | O |
