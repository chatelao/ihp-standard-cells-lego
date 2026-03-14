# Design Documentation for sg13g2_fill_8

## Substrate
```
  012345678901234
5 NNNNNNNNNNNNNNN
4 NNNNNNNNNNNNNNN
3 NNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNN
7 SSSSSSSSSSSSSSS
6 SSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSS
0 SSSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  012345678901234
5
4  ppppppppppppp
3  ppppppppppppp
2  ppppppppppppp
1
0
9
8
7
6
5  nnnnnnnnnnnnn
4  nnnnnnnnnnnnn
3  nnnnnnnnnnnnn
2  nnnnnnnnnnnnn
1  nnnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  012345678901234
5
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
  012345678901234
5 +++++++++++++++
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
0 ---------------
```
Legend: +=VDD, -=VSS

## Metal 2
```
  012345678901234
5
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
