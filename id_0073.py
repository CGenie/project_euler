#!/usr/bin/python2
# #####################################################################
# id_0073.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0033 import gcd
from fractions import gcd as frac_gcd

if __name__ == '__main__':
    M = 12000
    d = 2
    d_num = {}
    cnt = 0
    while True:
        if d % 100 == 0:
            print d
        for n in range(d/3 + 1, d/2 + (d % 2)):
            #g = gcd(n, d)
            #g = 1
            #g = frac_gcd(d, n)
            #print "n = %d, d = %d, gcd = %d" % (n, d, g)
            #ng = n/g
            #dg = d/g
            #d_num[(ng, dg)] = 1
            if frac_gcd(d, n) == 1:
                cnt += 1
        if d >= M:
            break
        d += 1
    print cnt
