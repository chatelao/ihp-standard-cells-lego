# Design Documentation for sg13g2_tielo

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
3   x
2   x
1
0  C   C
9  C   C
8  C   C
7    C C
6    C C
5    C
4  CCC x
3      x
2   x xx
1   x
0 -------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, x=Connection (upper side)

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
