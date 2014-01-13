#!/usr/bin/python2
# #####################################################################
# id_0057.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from fractions import Fraction

if __name__ == '__main__':
    cnt = 0
    s = Fraction(1, 1)
    for i in xrange(1000):
        s += 1
        s = 1/s
        s += 1
        n = str(s.numerator)
        d = str(s.denominator)
        if len(n) > len(d):
            print "i = " + str(i) + ", s = " + str(s) + ", numerator has more digits than denominator"
            cnt += 1
    print cnt
