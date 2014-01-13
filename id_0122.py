#!/usr/bin/python
# #####################################################################
# id_0122.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize

def is_prime(n):
    for x in range(2, n//2 + 1):
        if n % x == 0:
            return False
    return True

#@memoize()
def base_k(n, k):
    # Returns the number n in base k
    if n == 0:
        return []
    ret = base_k(n//k, k)
    ret.append(n % k)
    return ret

@memoize()
def muls_prime(n):
    # Return the minimal number of multiplications if n is prime
    # This is (???) the len of "binary" muls
    n2 = base_k(n, 2)
    return (len(n2) - 1) + (sum(n2) - 1)

@memoize()
def muls(n):
    if n == 0 or n == 1:
        return 0
    if is_prime(n):
        return muls_prime(n)
    # find a prime divisor of n
    #pdn = [k for k in range(2, n//2 + 1) if n % k == 0]
    m = n
    for k in range(2, n//2 + 1):
        nk = base_k(n, k)
        s = 0
        mk = muls(k)
        for x in nk:
            s += muls(x)
            if x != 0:
                s += mk
        s += (len(nk) - 1 - 1)*mk
        m = min(m, s)
    return m

@memoize()
def muls2(n):
    if n == 0 or n == 1:
        return 0
    if is_prime(n):
        return muls_prime(n)
    # find a prime divisor of n
    #pdn = [k for k in range(2, n//2 + 1) if n % k == 0]
    m = n
    for k in [x for x in range(2, n//2 + 2) if n % x == 0]:
        nk = base_k(n, k)
        s = 0
        mk = muls2(k)
        for x in nk:
            s += muls2(x)
            if x != 0:
                s += mk
        s += (len(nk) - 1 - 1)*mk
        m = min(m, s)
    return m

if __name__ == '__main__':
    s = 0
    for x in range(1, 201):
        r1 = muls(x)
        r2 = muls2(x)
        s += r1
        print("x = " + str(x) + ", muls(x) = " + str(r1) + ", muls2(x) = " + str(r2) + ", equal = " + str(r1 == r2))
    print("sol = " + str(s))
