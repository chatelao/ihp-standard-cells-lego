# Design Documentation for sg13g2_fill_1

## Substrate
```
  01
5 NN
4 NN
3 NN
2 NN
1 NN
0 NN
9 NN
8 NN
7 SS
6 SS
5 SS
4 SS
3 SS
2 SS
1 SS
0 SS
```
Legend: N=N-Well, S=Substrate

## Active
```
  01
5
4 p
3 p
2 p
1
0
9
8
7
6
5 n
4 n
3 n
2 n
1 n
0
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01
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
  01
5 ++
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
0 --
```
Legend: +=VDD, -=VSS

## Metal 2
```
  01
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
