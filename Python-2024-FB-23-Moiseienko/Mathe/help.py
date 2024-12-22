import random
def gcd(a:int, b:int) -> int:
    if b == 0: 
        return a 
    else: 
        return gcd(b, a%b)

def mod_pow(a:int,b:int,m:int) -> int:
    r = 1
    a = a % m 
    while b > 0:
        if (b & 1) == 1:
            r = (r * a) % m 
        b = b >> 1
        a = (a * a) % m 
    return r

def mr_test(n:int,d:int) -> bool:
    x = random.randint(1, n)
    if gcd(n, x) != 1:
        return False 
    r = mod_pow(x, d, n)
    if r == 1 or r == n - 1:
        return True
    while d != n - 1:
        r = (r * r) % n 
        d *= 2
        if r == 1:
            return False 
        if r == n - 1:
            return True 
    return False

def is_prime(n:int, k:int = 5) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    d = n - 1
    c = 0
    while not d % 2:
        d //= 2
        c += 1
    for i in range(k):
        if not mr_test(n, d):
            return False 
    return True

def check(m:int) -> bool:
    p = 2*m + 1
    if not is_prime(p):
        return False 
    if p % 4 == 3 and pow(2,m,p) == 1:
        return True
    elif pow(2,2*m,p) == 1:
        return True
    return False
    

