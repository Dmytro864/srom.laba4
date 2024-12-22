#main file for Mathe lib, implemetation of operation in normal basis
from typing import Any
from Mathe.help import *
from math import log2
BASE = 64

def mCheck(i:int,j:int,p:int) -> bool:
    i,j = 2**i,2**j
    if (i+j)%p == 1 or (i-j)%p == 1 or (-i+j)%p == 1 or (-i-j)%p == 1:
        return True 
    else:
        return False 

def getMatrix(m:int):
    p = m*2 + 1 
    res = 0
    for i in range(m):
        for j in range(m):
            if mCheck(i,j,p):
                res ^= 1 << (m*i +  j)
    return GFelement(res,m,0)


class GF:
    def __init__(self, m=419) -> Any:
        # if check(m):
        if True:
            self.m = m
            self.p = 2**m
            self.matrix = getMatrix(m)
        else:
            raise ValueError("Invalid value for creating GF.")
    def __call__(self, n) -> Any:
        tmp = GFelement(n, self.m, self.matrix)      
        return tmp
    
def parse(n:int) -> list:
    res = []
    m = 2**BASE
    while n:
        res += [n % m]
        n = n // m 
    return res


class GFelement:
    def __init__(self, number, m, matrix):
        if isinstance(number, int):
            if number == 0: words = [0]
            elif number == 1: words = [1]
            else: words = parse(number)
            
        elif isinstance(number, list):
            while number[-1] == 0 and len(number) > 3:
                number.pop()
            words = number
        else:
            raise ValueError("Invalid input")
        self.m = m
        self.words = words
        self.l = self.bitLen()
        self.matrix = matrix



    def bitLen(self):
        if set(self.words) == {0}:
            return 0
        c = 0
        while self.words[-1-c] == 0: c += 1
        msb = self.words[-1-c]
        bitsize = 0
        while msb > 0:
            msb >>= 1
            bitsize += 1
        return (len(self.words) - 1 - c)*64 + bitsize

    def lshift(self, bits):
        word = 64
        res = GFelement(self.words,self.m,self.matrix)
        b_words = bits // word 
        b_shift = bits % word
        if b_words != 0:
            res.words = [0]*b_words + res.words
            res.l = res.bitLen()
        if b_shift != 0:
            result = res.words + [0]
            for i in range(len(res.words),0,-1):
                curr = (result[i] << b_shift) & ((1 << (64)) - 1)
                result[i] = curr | (result[i-1] >> (word - b_shift))
            result[0] = (result[0] << b_shift) & ((1 << (word)) - 1)
            if set(result) == {0}: result = [0]
            res.words = result
            res.l = res.bitLen()
        return res 

    def isnull(self):
        if set(self.words) == {0}:
            return True 
        return False

    def getBase(self) -> int:
        res = 0
        for elem in self.words[::-1]:
            res = (res * 2**BASE) + elem
        return res
    def __repr__(self):
        return hex(self.getBase())
    
    def __str__(self):
        return hex(self.getBase())

    def __add__(self, other):
        res_ = []
        for i in range(max(len(self.words), len(other.words))):
            if i >= len(self.words): a = 0
            elif i >= len(other.words): b = 0
            else:
                a,b = self.words[i],other.words[i]
                res_ += [a^b]
        return GFelement(res_,self.m,self.matrix)
    
    def __pow__(self,n):
        if n == 2:
            c = self.words[0] & 1 
            n_ = rShiftBit(self)
            if c:
                n_.words[-1] ^= 1 << (self.m - 1)%64
            return n_

    

    def __mul__(self,other):
        a_ = list(self.words)
        b_ = list(other.words)
        m = self.matrix.getBase()
        m_ = list(self.matrix.words) 
        a_ += [0]*((self.m//BASE + 1) - len(a_))
        # print(m_)
        b_ += [0]*((self.m//BASE + 1) - len(b_))
        res = 0
        # for i in range(self.m-1,-1,-1):
        for i in range(self.m):
        # for i in range(s):
            r = mulStep(a_,b_,m_,self.m)
            # print(f"i = {i},r = {r},totalRes = {res}")
            res ^= r << (self.m - 1 - i) 
            # print("inside mu;")
            # printBin(a_,self.m)
            # printBin(b_,self.m)
            a_ = lShiftCycle(a_,self.m)
            # print("b_",bin(b_[0])[2:])
            b_ = lShiftCycle(b_,self.m)
            # print(bin(a_[0])[2:].zfill(self.m),bin(b_[0])[2:].zfill(self.m))
            
            # print("new b",bin(b_[0])[2:].zfill(self.m))
        return GFelement(res,self.m,self.matrix)
    def trace(self):
        trace = 0
        d = list(self.words)
        for elem in d:
            while elem:
                trace = (trace + elem%2)%2
                elem = elem//2
        return trace
    def inv(self):
        y = GFelement(list(self.words),self.m,self.matrix)
        r = int(log2(self.m - 1)) +1
        s = self.m - 1
        for k in range(r):
            z = getN2powers(y,2**k)
            print(k)
            y = y * z
            print("end of mul in inv")
            print(y,y**2)
        y = y**2
        return y 

def getN2powers(number,n):
    res = GFelement(number.words,number.m,number.matrix)
    for i in range(n):
        res = res**2 
    return res 

def printBin(a,m):
    res = 0
    for elem in a[::-1]:
        res = (res * 2**BASE) + elem
    print(bin(res)[2:].zfill(m))

def lShiftCycle(number:list,m):
    c = int((number[-1] & (1 << (m%64 - 1))) != 0)
    # print(bin(number[-1])[2:])
    # print(bin(1 << (m%64 - 1))[2:])
    # print("C",c)
    n_ = lShiftBit(number,m)
    # print("n_")
    # printBin(n_)
    n_[0] ^= c
    return n_

def lShiftBit(number,m):
    n_ = list(number)
    if len(n_) == 1:
        n_[0] = (n_[0] << 1) & int('1'*(m%64),2)
        # print("n_ ", bin(n_[0])[2:])
        return n_
    n_[-1] = (n_[-1] << 1) & int('1'*(m%64),2) | n_[-2] >> 63
    for i in range(len(n_)-2,0,-1):
        n_[i] = (n_[i] << 1) & int('1'*(64),2) | n_[i-1] >> 63
    n_[0] = (n_[0] << 1) & int('1'*(64),2)
    # print("insode lshiftbit")
    # print(bin(n_[-1])[2:])
    # print(len(bin(n_[-1])[2:]) > m%64)
    return n_

def rShiftBit(number):
    a = list(number.words)
    for i in range(len(a) - 1):
        c = a[i+1] & 1
        a[i] = a[i] >> 1 | c << 63 
    a[-1] >>= 1 
    return GFelement(a,number.m,number.matrix)

def mulStep(a,b,m,size):
    res = 0
    # print("A",bin(a[0])[2:].zfill(size))
    for i in range(size):
        i_ = (size-1-i)*size
        rMA = 0
        for j in range(size):
            j_ = i_ + j
            aj = size - j - 1
            a_tmp = int((a[aj//64] & 1 << (aj % 64)) != 0)
            m_tmp = int((m[j_//64] & 1 << (j_ % 64)) != 0)
            # print(a_tmp,end=" ")
            mul =  (a_tmp * m_tmp)
            # print(i,j,mul)
            rMA += mul
        # print()
        rMA = rMA % 2
        if rMA:
            res ^= rMA << i#(size - 1 - i)
    #print(bin(res)[2:].zfill(size))
    out = 0
    for i in range(size):
        bi = size - i - 1
        b_tmp = int((b[i//64] & 1 << (i % 64)) != 0)
        r_tmp = int((res & 1 << i) != 0)
        out += b_tmp*r_tmp
    out = out % 2
    # print("out",out)
    return out

    

