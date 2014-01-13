#!/usr/bin/python
# #####################################################################
# id_0110.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from math import log
from id_0003 import is_prime
from itertools import product

if __name__ == '__main__':
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    M = 8*10**6 - 1
    p = len(primes)
    N = M**(1./p)
    x = []
    for pp in primes:
        N *= (log(pp))**(1./p)
    for pp in primes:
        print "pp = " + str(pp) + ", x_pp = " + str(0.5*N/log(pp) - 0.5)
        x.append(int(0.5*N/log(pp) - 0.5))
    pro = []
    for pp in range(p):
        pro.append([0, 1])
    prod = product(*pro)
    m = 10**20
    ym = []
    for tt in prod:
        y = map(lambda i: x[i] + tt[i], range(p))
        s = 1
        for yy in y:
            s *= (2*yy + 1)
        #print "s = " + str(s)
        if s > M:
            print "success!"
            print y
            n = 1
            for i in range(p):
                n *= (primes[i])**(y[i])
            if m > n:
                m = n
                ym = y
            print n
    print m
    print ym
