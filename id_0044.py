#!/usr/bin/python2
# #####################################################################
# id_0044.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from math import sqrt

pent = {}
tol = 10**-6

def is_pentagonal(Pn, cache = True):
    try:
        return pent[Pn]
    except KeyError:
        s = 1 + 24*Pn
        delta = sqrt(s)
        #r = (1 + delta)/6
        #ret = abs(int(r) - r) < tol
        ret = (delta**2 - s == 0) and ((1 + delta) % 6 == 0)
        if cache:
            pent[Pn] = ret
        return ret

if __name__ == '__main__':
    D = 10**8
    n = 2
    #n = 100000
    #D = 233840
    while True:
        Pn = n*(3*n - 1)/2
        if n % 1000 == 0:
            print "n = %d" % n
        for m in xrange(1, n):
            Pm = m*(3*m - 1)/2
            d = Pn - Pm
            if D > d:
                if is_pentagonal(d) and is_pentagonal(Pn + Pm):
                    print "Pentagonal pair found: %d (n = %d) and %d (n = %d)" % (Pn, n, Pm, m)
                    print "Difference: %d" % d
                    D = d
                    print "Also, new minimizing difference"
        n += 1
