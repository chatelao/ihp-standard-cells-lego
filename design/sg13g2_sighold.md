# Design Documentation for sg13g2_sighold

## Substrate
```
012345678
NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
NNNNNNNNN
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
SSSSSSSSS
```
Legend: N=N-Well, S=Substrate

## Active
```
012345678

 pXXXXXp
 ppppppp
 ppppppp

       X


 nnnnnnn
 nnnnnnn
 nnnnnnn
 nnnnnnn
 nXXXXXn

```
Legend: X=Connection (lower side), n=NMOS Active, p=PMOS Active

## Polysilicon
```
012345678

  XXXXX



       X






  XXXXX

```
Legend: X=Connection (lower side)

## Metal 1
```
012345678
+++++++++
  xxxxx



 C     x
 CCCCCCC
 C     C
 CCCC  C
 C     C


  xxxxx
---------
```
Legend: +=VDD, -=VSS, C=Metal 1 Connection, x=Connection (upper side)

## Metal 2
```
012345678














```
