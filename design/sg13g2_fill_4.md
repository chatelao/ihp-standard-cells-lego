# Design Documentation for sg13g2_fill_4

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
4
3
2  ppppp
1  ppppp
0  ppppp
9  ppppp
8  ppppp
7
6
5
4  nnnnn
3  nnnnn
2  nnnnn
1
0
```
Legend: n=NMOS Active, p=PMOS Active

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
0 -_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, x/o/&/_=Connection (upper side)

## Metal 2
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
Legend: M=Metal 2
