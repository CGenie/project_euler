#!/usr/bin/python2
# #####################################################################
# id_0058.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
import pickle
from id_0003 import is_prime

# generator of spiral vertices
def spiral_vertices():
    cnt = 1
    side = 1
    while True:
        jmp = 2*side
        for x in range(4):
            cnt += jmp
            yield cnt
        side += 1

if __name__ == '__main__':
    ratio = 1.
    primes = 0
    n = 1
    side = 1
    f = spiral_vertices()
    while ratio > 0.1:
        for x in range(4):
            ret = f.next()
            if is_prime(ret):
                primes += 1
        n += 4
        side += 2
        ratio = float(primes)/n
        print "Ratio is " + str(ratio) + ", primes = " + str(primes) + ", n = " + str(n)
        if n < 10:
            ratio = 1.
    print side
