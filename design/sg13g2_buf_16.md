# Design Documentation for sg13g2_buf_16

## Substrate
```
  01234567890123456789012345678901234567890123
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
2 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
1 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
9 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
8 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
7 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
6 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
5 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
4 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
3 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
2 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
1 SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
0 NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
```
Legend: N=N-Well, S=Substrate

## Active
```
  01234567890123456789012345678901234567890123
4 pppppppppppppppppppppppppppppppppppppppppppp
3
2
1  ppppppppppppppppppppppppppppppppppppppppppp
0  ppppppppppppppppppppppppppppppppppppppppppp
9  ppppppppppppppppppppppppppppppppppppppppppp
8  ppppppppppppppppppppppppppppppppppppppppppp
7
6
5
4  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
3  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
2
1
0 nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
```
Legend: n=NMOS Active, p=PMOS Active

## Polysilicon
```
  01234567890123456789012345678901234567890123
4
3
2   G G        G G G G G        G G G G G
1   G G        G G G G G        G G G G G
0   G G        G G G G G        G G G G G
9   G G        G G G G G        G G G G G
8   G G        G G G G G        G G G G G
7   G G        G G G G G        G G G G G
6   GGGGGGGGGGGGGGGGGGGGGGGGGGGGG GGGGGGGGGG
5   G G        G G G G G        G G G G G
4   G G        G G G G G        G G G G G
3   G G        G G G G G        G G G G G
2   G G        G G G G G        G G G G G
1
0
```
Legend: G=Polysilicon

## Metal 1
```
  01234567890123456789012345678901234567890123
4 &+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+
3  +   +      +   +   +   +  +   +   +   +
2  & c & cc c & c & c & c & c+c c+c c+c c+c c
1  + O + O  O + O + O + O +  + O + C + C + C
0  & o & oc o & o & o & o & c+cOc+cCc+cCc+cCc
9  + O   O  O   O   O   O      O   C   C   C
8  c o   oc o   o   o   o   c   cC  c c   c c
7    O   O  O   O   O   O        C
6    O   OOOO   O   O   O cCcCcCcC      iIiI
5    O   O  O   O   O   O        C
4  _ o _ oc o _ o _ o _ oOOOoOOOcCCCcCcCCCcCc
3  - O - O  O - O - O - O -  - O - C - C - C
2  _ c _ cc c _ c _ c _ c _ c-c c-c c-c c-c c
1  -   -      -   -   -   -  -   -   -   -
0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
```
Legend: +/&=VDD, -/_=VSS, I/i=Metal 1 Input, O/o=Metal 1 Output, c/i/o/&/_=Contacted metal (lowercase)

## Connectivity Matrix

| Silicon | VDD | VDD3 | VDD4 | VDD5 | VDD7 | VSS | VSS2 | VSS4 | Input1 | Internal1 | Internal10 | Internal11 | Internal12 | Internal2 | Internal3 | Internal4 | Internal5 | Internal6 | Internal7 | Internal8 | Output1 | Output10 | Output11 | Output12 | Output2 | Output3 | Output4 | Output5 | Output6 | Output8 | Output9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NMOS1 |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| NMOS2 |   |   |   |   |   | X | X | X |   | X |   |   |   |   |   |   |   |   |   |   | X |   |   |   | X | X | X | X |   |   |   |
| PMOS1 | X | X | X | X | X |   |   |   |   |   | X |   |   | X | X | X |   | X |   | X | X |   | X |   | X | X | X | X | X | X | X |
| PMOS2 | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Poly1 |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   | X | X | X |   |   |   | X | X |   |   |
| Poly2 | X |   |   |   |   | X |   |   | X | X |   | X | X | X | X |   | X | X | X | X |   |   |   |   |   |   |   |   |   |   |   |

## Silicon Neighbourhood

| Silicon | Poly1 | Poly2 |
| --- | --- | --- |
| NMOS1 |   |   |
| NMOS2 | O | O |
| PMOS1 | O | O |
| PMOS2 |   |   |
