# Design Documentation for sg13g2_nand2_1

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
3  G   G
2  G   G
1  G   G
0  G   G
9  G   G
8  G   G
7  G   G
6  G   G
5  G   G
4  G   G
3  G   G
2  G   G
1  G   G
0
```
Legend: G=Polysilicon

## Metal 1
```
  0123456
4 +++++++
3
2
1    x
0    O
9    O
8    O
7    O
6  x O x
5  I x I
4    xxx
3      x
2      x
1
0 -------
```
Legend: +=VDD, -=VSS, I=Metal 1 Input, O=Metal 1 Output, x=Connection (upper side)

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
