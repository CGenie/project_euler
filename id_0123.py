#!/usr/bin/python
# #####################################################################
# id_0123.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize

def gen_primes():
    lst_primes = [2]
    yield 2
    p = 3
    while True:
        prime = True
        for x in lst_primes:
            if p % x == 0:
                prime = False
                break
        if prime:
            lst_primes.append(p)
            yield p
        p += 2

if __name__ == '__main__':
    gp = gen_primes()
    M = 10**10
    n = 0
    while True:
        pn = next(gp)
        n += 1
        if pn**2 >= M:
            ret = ((-1)**n + 1 + ((-1)**(n - 1) + 1)*n*pn) % pn**2
            if (n + 1) % 100 == 0:
                print("pn = " + str(pn) + ", n = " + str(n) + ", ret = " + str(ret))
            if ret > M:
                print("sol = " + str(n))
                break
        
