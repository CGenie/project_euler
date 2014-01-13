#!/usr/bin/python2
# #####################################################################
# id_0027.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0003 import is_prime

def num_consecutive_primes(f):
    n = 0
    while True:
        r = f(n)
        if r < 0 or not is_prime(f(n)):
            break
        n += 1
    return n

if __name__ == '__main__':
    l = 0
    A = 0
    B = 0
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            f = lambda n: n**2 + a*n + b
            r = num_consecutive_primes(f)
            if l < r:
                l = r
                A = a
                B = b
                print "l = %d, A = %d, B = %d" % (l, A, B)
    print A, B
    print A*B
