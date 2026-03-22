# Design Documentation for sg13g2_antennanp

## Substrate
```
  01234
4 NNNNN
3 NNNNN
2 NNNNN
1 NNNNN
0 NNNNN
9 NNNNN
8 NNNNN
7 SSSSS
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
2 NpppN
1 NpppN
0 NpppN
9 NpppN
8 NpppN
7 SSSSS
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
2   G
1   G
0   G
9   G
8   G
7   G
6  GG
5   G
4   G
3   G
2   G
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
7  I
6  I
5  I
4  iIi
3   II
2
1
0 -_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | Input | VDD | VSS |
| --- | --- | --- | --- |
| NMOS | X |   | X |
| PMOS | X | X |   |
