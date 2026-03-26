# Design Documentation for sg13g2_tiehi

## Substrate
```
  0123456
4 NNNNNNN
3 NNNNNNN
2 NNNNNNN
1 NNNNNNN
0 NNNNNNN
9 NNNNNNN
8 NNNNNNN
7 SSSSSSS
6 SSSSSSS
5 SSSSSSS
4 SSSSSSS
3 SSSSSSS
2 SSSSSSS
1 SSSSSSS
0 SSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456
4 ppppppp
3 NNNNNNN
2 ppppppN
1 NpppppN
0 NpppppN
9 NpppppN
8 NpppppN
7 SSSSSSS
6 SSSSSSS
5 SSSSSSS
4 SnnnnnS
3 SnnnnnS
2 SnnnnnS
1 SSSSSSS
0 nnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active, S=Substrate fill (P), N=Substrate fill (N)

## Polysilicon
```
  0123456
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
  0123456
4 &+&+&+&
3 +++++++
2 &+
1      O
0      o
9 CC   O
8 Cc   o
7 CCCC C
6 Cc c c
5 CC C C
4 Cc   c
3
2    c
1
0  c c c
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS | VSS2 | VSS3 | VSS4 | L_HI |
| --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   | X | X | X |   |   |
| NMOS2 |   |   |   |   | X | X |
| PMOS1 | X |   |   |   |   | X |
| PMOS2 | X |   |   |   |   |   |
