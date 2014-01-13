#!/usr/bin/python2
# #####################################################################
# id_0045.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0042 import is_triangle_num
from id_0044 import is_pentagonal
from math import sqrt

hexagonal = {}

def is_hexagonal(hn):
    try:
        return hexagonal[hn]
    except KeyError:
        s = 1 + 8*hn
        delta = int(sqrt(s))
        ret = ((delta**2 - s) == 0) and ((1 + delta) % 4 == 0)
        hexagonal[hn] = ret
        return ret

if __name__ == '__main__':
    s = 0
    n = 1
    while True:
        Pn = n*(n + 1)/2
        if is_pentagonal(Pn) and is_hexagonal(Pn):
            s += 1
            print "%d is triangular (n = %d), pentagonal and hexagonal" % (Pn, n)
            if s == 3:
                break
        n += 1
