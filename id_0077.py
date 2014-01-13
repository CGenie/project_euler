#!/usr/bin/python3.1
# #####################################################################
# id_0077.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from itertools import product
from math import sqrt

d_prime = {1: False}

def is_prime(n):
    try:
        return d_prime[n]
    except KeyError:
        for x in range(2, int(sqrt(n)) + 1):
            if is_prime(x) and n % x == 0:
                d_prime[n] = False
                return d_prime[n]
        d_prime[n] = True
        return d_prime[n]

lst_primes = []
for x in range(2, 100):
    if is_prime(x):
        lst_primes.append(x)

def smaller_primes(N):
    ret = []
    i = 0
    lp = lst_primes[i]
    while lp <= N:
        ret.append(lp)
        i += 1
        lp = lst_primes[i]
    return ret

def primes_range(m, M):
    f = lambda x: (x >= m) and (x <= M)
    ret = filter(f, lst_primes)
    return ret

def sums(N):
    ret = 0
    for L in range(1, int(N/2)):
        lst = []
        for x in range(L):
            lst.append(smaller_primes(N))
        pr = product(*lst)
        for d in pr:
            s = sum(d)
            diff = N - s
            if diff > 0 and is_prime(diff):
                z = True
                for x in range(L - 1):
                    if d[x] > d[x + 1]:
                        z = False
                        break
                if z and (d[0] >= diff):
                    ret += 1
                    print(diff, d)
    return ret

Cd = {(4, 1, 2): 1}
def C(N, L, start):
    try:
        return Cd[(N, L, start)]
    except KeyError:
        if L == 1:
            ret = 0
            for p in primes_range(start, int(N/2)):
               d = N - p
               if is_prime(d):
                   ret += 1
            return ret
        else:
            ret = 0
            for p in primes_range(start, int(N/L)):
                ret += C(N - p, L - 1, p)
            return ret

def new_sums(N):
    s = 0
    for L in range(1, int(N/2)):
        s += C(N, L, 2)
    return s

if __name__ == '__main__':
    ret = 0
    N = 4
    while ret < 5000:
        ret = new_sums(N)
        print("N = ", N, ", sums = ", ret)
        N += 1
