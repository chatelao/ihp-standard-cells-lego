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
4
3  ppppp
2  ppppp
1  ppppp
0
9
8
7
6
5  nnnnn
4  nnnnn
3  nnnnn
2  nnnnn
1  nnnnn
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

## Metal 1
```
  0123456
4 +++++++
3 +
2 +
1
0      O
9 CC   O
8  C   O
7  CCC C
6 C  C C
5 C    C
4 C    C
3
2    x
1    x
0 -------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, O=Metal 1 Output, x=Connection (upper side)

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
