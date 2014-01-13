#!/usr/bin/python2
# #####################################################################
# id_0041.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0003 import is_prime
from itertools import permutations

def is_n_pandigital(num, n):
    digits = [str(x) for x in range(1, n + 1)]
    s = str(num)
    if len(s) != n:
        return False
    for x in s:
        try:
            digits.remove(x)
        except ValueError:
            return False
    return True

def gen_pandigitals_n(n):
    digits = [str(x) for x in range(1, n + 1)]
    for c in permutations(digits):
        yield int(''.join(c))

if __name__ == '__main__':
    m = 0
    N = 0
    for n in range(1, 9):
        f = gen_pandigitals_n(n)
        while True:
            try:
                ret = f.next()
                if ret > m and is_prime(ret):
                    m = ret
                    N = n
                    print '%d is largest pandigital prime so far' % m
            except StopIteration:
                break
    print m
