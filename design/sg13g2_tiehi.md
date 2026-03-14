# Design Documentation for sg13g2_tiehi

## Substrate
```
  01234567
5 NNNNNNNN
4 NNNNNNNN
3 NNNNNNNN
2 NNNNNNNN
1 NNNNNNNN
0 NNNNNNNN
9 NNNNNNNN
8 NNNNNNNN
7 SSSSSSSS
6 SSSSSSSS
5 SSSSSSSS
4 SSSSSSSS
3 SSSSSSSS
2 SSSSSSSS
1 SSSSSSSS
0 SSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567
5
4  pppppp
3  pppppp
2  pppppp
1
0
9
8
7
6
5  nnnnnn
4  nnnnnn
3  nnnnnn
2  nnnnnn
1  nnnnnn
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567
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
  01234567
5 ++++++++
4
3
2
1      O
0      O
9  C   O
8  C
7  CCC C
6    C C
5  C C C
4  C   C
3
2
1
0 --------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, O=Metal 1 Output

## Metal 2
```
  01234567
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
