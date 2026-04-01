# Design Documentation for sg13g2_antennanp

## Substrate
```
  01234
4 SSSSS
3 NNNNN
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
0 NNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234
4 ppppp
3
2  pppp
1  pppp
0  pppp
9  pppp
8  pppp
7
6
5
4  nnn
3  nnn
2  nnn
1
0 nnnnn
```
Legend: n=NMOS Active, p=PMOS Active

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
0  c c
9  III
8  iIi
7  I
6  I
5  I
4  cIi
3   II
2  c c
1
0 _-_-_
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | Input1 | Input2 |
| --- | --- | --- | --- | --- |
| NMOS1 |   | X |   |   |
| NMOS2 |   |   | X | X |
| PMOS1 |   |   | X |   |
| PMOS2 | X |   |   |   |

