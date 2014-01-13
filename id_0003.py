#!/usr/bin/python2
# #####################################################################
# id_0003.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from math import sqrt
from helper import unique

d_prime = {1: False}

def is_prime(n):
    try:
        return d_prime[n]
    except KeyError:
        for x in xrange(2, int(sqrt(n)) + 1):
            if is_prime(x) and n % x == 0:
                d_prime[n] = False
                return d_prime[n]
        d_prime[n] = True
        return d_prime[n]

d_prime_fact = {}

def prime_factors_non_unique(n):
    try:
        return d_prime_fact[n]
    except KeyError:
        pf = []
        if n == 2:
            return [2]
        for x in xrange(2, n):
            if is_prime(x) and n % x == 0:
                pf += prime_factors_non_unique(n/x) + [x]
        pf.sort()
        return pf

def prime_factors(n):
    return unique(prime_factors_non_unique(n))

if __name__ == '__main__':
    print max(prime_factors(600851475143))
