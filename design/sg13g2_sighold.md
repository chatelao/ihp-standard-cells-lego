# Design Documentation for sg13g2_sighold

## Substrate
```
  012345678
4 NNNNNNNNN
3 NNNNNNNNN
2 NNNNNNNNN
1 NNNNNNNNN
0 NNNNNNNNN
9 NNNNNNNNN
8 NNNNNNNNN
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
4
3  ppppppp
2  ppppppp
1  ppppppp
0
9
8
7
6
5  nnnnnnn
4  nnnnnnn
3  nnnnnnn
2  nnnnnnn
1  nnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678
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
  012345678
4 +++++++++
3
2
1
0
9
8  C     C
7  CCCCCCC
6  C     C
5  CCCC  x
4  C     x
3
2
1
0 ---------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, x=Connection (upper side)

## Metal 2
```
  012345678
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
