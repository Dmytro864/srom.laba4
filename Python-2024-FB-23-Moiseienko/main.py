#!/usr/bin/python3 
from Mathe.gf import *
from random import getrandbits
import time 

def main() -> None:
    fld = GF()
    BITS = fld.m 
    A,B,N = getrandbits(BITS),getrandbits(BITS),getrandbits(BITS)
    a,b,n = fld(A),fld(B),fld(N)
    print("A",a)
    print("B",b)
    print("N",n)
    print("A + B",a+b)
    print("A * B",a*b)
    print("A^2",a**2)
    print("A^-1",a.inv())
    print("A^N",a**n)
    print("tr(A)",a.trace())



if __name__ == "__main__":
    main()  
