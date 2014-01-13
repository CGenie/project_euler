#!/usr/bin/python2
# #####################################################################
# id_0071.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
#from fractions import Fraction
from id_0033 import gcd

if __name__ == '__main__':
    M = 10**6
    d = 2
    # look for proper fractions close and less-than 3/7
    #fr = Fraction(0, 1)
    # tolerance
    tol = 5*10**-5
    best_n = 0
    best_d = 1
    best_num = 0.
    while True:
        for n in range(3*d/7 - 2, 3*d/7 + 1):
            num = float(n)/float(d)
            if num < 3./7 and best_num < num:
                best_n = n
                best_d = d
                best_num = num
                print "New best approximation found: n = %d, d = %d, n/d = %f" % (n, d, num)
        if d == M:
            break
        d += 1
    g = gcd(best_n, best_d)
    print "The fraction: n/d = %d/%d" % (best_n/g, best_d/g)
