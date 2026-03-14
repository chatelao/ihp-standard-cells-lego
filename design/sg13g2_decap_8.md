# Design Documentation for sg13g2_decap_8

## Substrate
```
  0123456789012
5 NNNNNNNNNNNNN
4 NNNNNNNNNNNNN
3 NNNNNNNNNNNNN
2 NNNNNNNNNNNNN
1 NNNNNNNNNNNNN
0 NNNNNNNNNNNNN
9 NNNNNNNNNNNNN
8 NNNNNNNNNNNNN
7 SSSSSSSSSSSSS
6 SSSSSSSSSSSSS
5 SSSSSSSSSSSSS
4 SSSSSSSSSSSSS
3 SSSSSSSSSSSSS
2 SSSSSSSSSSSSS
1 SSSSSSSSSSSSS
0 SSSSSSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  0123456789012
5
4  ppppppppppp
3  ppppppppppp
2  ppppppppppp
1
0
9
8
7
6
5  nnnnnnnnnnn
4  nnnnnnnnnnn
3  nnnnnnnnnnn
2  nnnnnnnnnnn
1  nnnnnnnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  0123456789012
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
  0123456789012
5 +++++++++++++
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
0 -------------
```
Legend: +=VDD, -=VSS

## Metal 2
```
  0123456789012
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
