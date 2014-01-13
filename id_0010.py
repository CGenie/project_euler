#!/usr/bin/python2
# #####################################################################
# id_0010.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0003 import is_prime

def sum_primes_below(n):
    s = 0
    for x in range(2, n):
        if is_prime(x):
            s += x
    return s

if __name__ == '__main__':
    print sum_primes_below(int(2E6))
