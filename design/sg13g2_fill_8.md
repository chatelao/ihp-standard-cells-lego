# Design Documentation for sg13g2_fill_8

## Substrate
```
  01234567890123
3 NNNNNNNNNNNNNN
2 NNNNNNNNNNNNNN
1 NNNNNNNNNNNNNN
0 NNNNNNNNNNNNNN
9 NNNNNNNNNNNNNN
8 NNNNNNNNNNNNNN
7 SSSSSSSSSSSSSS
6 SSSSSSSSSSSSSS
5 SSSSSSSSSSSSSS
4 SSSSSSSSSSSSSS
3 SSSSSSSSSSSSSS
2 SSSSSSSSSSSSSS
1 SSSSSSSSSSSSSS
0 SSSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123
3
2  pppppppppppp
1  pppppppppppp
0  pppppppppppp
9
8
7
6
5  nnnnnnnnnnnn
4  nnnnnnnnnnnn
3  nnnnnnnnnnnn
2  nnnnnnnnnnnn
1  nnnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123
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
  01234567890123
3 ++++++++++++++
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
0 --------------
```
Legend: +=VDD, -=VSS

## Metal 2
```
  01234567890123
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
