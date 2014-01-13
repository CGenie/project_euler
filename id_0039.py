#!/usr/bin/python2
# #####################################################################
# id_0039.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from math import sqrt

def num_triangles_with_perimeter(p):
    d = {}
    for a in xrange(1, p - 2):
        for b in xrange(a, p - 1):
            sqr = a**2 + b**2
            c = p - a - b
            if c**2 - sqr == 0:
                l = [a, b, c]
                l.sort()
                d[tuple(l)] = 1
    return len(d.keys())

if __name__ == '__main__':
    m = 0
    for x in range(3, 1001):
        ret = num_triangles_with_perimeter(x)
        if x % 100 == 0:
            print "x = %d, ret = %d" % (x, ret)
        if m < ret:
            m = ret
            print "x = %d, m = %d is new maximum" % (x, ret)
    print m
