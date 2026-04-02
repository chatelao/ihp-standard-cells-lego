# Design Documentation for sg13g2_fill_8

## Substrate
```
  01234567890123
4 SSSSSSSSSSSSSS
3 NNNNNNNNNNNNNN
2 NNNNNNNNNNNNNN
1 NNNNNNNNNNNNNN
0 NNNNNNNNNNNNNN
9 NNNNNNNNNNNNNN
8 NNNNNNNNNNNNNN
7 NNNNNNNNNNNNNN
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 NNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123
4 pppppppppppppp
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
3  nnnnnnnnnnnnn
2  nnnnnnnnnnnnn
1  nnnnnnnnnnnnn
0 nnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123
4
3
2
1
0  GGGGGGGGGGGGG
9  GGGGGGGGGGGGG
8  GGGGGGGGGGGGG
7  GGGGGGGGGGGGG
6  GGGGGGGGGGGGG
5  GGGGGGGGGGGGG
4
3
2
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123
4 &+&+&+&+&+&+&+
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
0 _-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VSS |
| --- | --- | --- |
| NMOS1 |   | X |
| PMOS1 | X |   |
| Poly1 |   |   |
