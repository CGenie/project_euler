#!/usr/bin/python
# #####################################################################
# id_0207.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize
import itertools as it
import pickle
import os

def erat3( ):
    D = { 9: 3, 25: 5 }
    yield 2
    yield 3
    yield 5
    MASK= 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
    MODULOS= frozenset( (1, 7, 11, 13, 17, 19, 23, 29) )

    for q in it.compress(
            it.islice(it.count(7), 0, None, 2),
            it.cycle(MASK)):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = q + 2*p
            while x in D or (x%30) not in MODULOS:
                x += 2*p
            D[x] = p

lst_primes = []
set_primes = set()

@memoize()
def divisors(n):
    if n == 1:
        return 1
    if n in set_primes:
        return 2
    for p in lst_primes:
        if n % p == 0:
            break
    k = 0
    while n % p == 0:
        k += 1
        n = n//p
    return divisors(n)*(k + 1)
    
if __name__ == '__main__':
    M = 10**7
    pg = erat3()
    p = next(pg)
    lst_primes = [p]
    if os.path.isfile('id_0207.pickle'):
        with open('id_0207.pickle', 'rb') as f:
            lst_primes = pickle.load(f)
    else:
        while p < M:
            p = next(pg)
            lst_primes.append(p)
        with open('id_0207.pickle', 'wb') as f:
            pickle.dump(lst_primes, f)
    set_primes = set(lst_primes)
    s = 0
    dd = set()
    for n in range(2, M):
        d = divisors(n)
        if d in dd:
            s += 1
        else:
            dd.add(d)
        if n % 10000 == 0:
            print(n)
    print("sol = ", s)
