# Design Documentation for sg13g2_antennanp

## Substrate
```
  01234
4 NNNNN
3 SNNNN
2 NNNNN
1 NNNNN
0 NNNNN
9 NNNNN
8 NNNNN
7 NNNNN
6 SSSSS
5 SSSSS
4 SSSSS
3 SSSSS
2 SSSSS
1 SSSSS
0 SSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234
4 ppppp
3 NNNNN
2 Npppp
1 Npppp
0 Npppp
9 Npppp
8 Npppp
7 NNNNN
6 SSSSS
5 SSSSS
4 SnnnS
3 SnnnS
2 SnnnS
1 SSSSS
0 nnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  01234
4
3
2
1
0
9
8
7
6
5
4
3
2
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234
4 &+&+&
3
2
1
0
9  III
8  iIi
7  II
6  II
5  II
4  Iii
3  III
2   ii
1
0 _-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | A |
| --- | --- | --- | --- |
| NMOS1 |   | X |   |
| NMOS2 |   |   | X |
| PMOS1 |   |   | X |
| PMOS2 | X |   |   |

