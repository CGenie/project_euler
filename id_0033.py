#!/usr/bin/python2
# #####################################################################
# id_0033.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0008 import mul

def fractions_equal((a, b), (c, d)):
    return a*d == b*c

def hd(a):
    return a/10

def ld(a):
    return a % 10

def hdc(a):
    return hd(a) if ld(a) != 0 else 0.1

def ldc(b):
    return ld(b) if ld(b) !=0 else -1

d_gcd = {}

def gcd(a, b):
    n = max(a, b)
    r = min(a, b)
    try:
        return d_gcd[(n, r)]
    except KeyError:
        if r == 0:
            d_gcd[(n, 0)] = n
        else:
            d_gcd[(n, r)] = gcd(r, n - r*(n/r))
        return d_gcd[(n, r)]

def simplify((a, b)):
    d = gcd(a, b)
    return (a/d, b/d)

def is_curious((a, b)):
    possibilities = [(hdc(a), hdc(b)), (hdc(a), ldc(b)), (ldc(a), hdc(b)), (ldc(a), ldc(b))]
    equalities    = [(ldc(a), ldc(b)), (ldc(a), hdc(b)), (hdc(a), ldc(b)), (hdc(a), hdc(b))]
    for i, frac in enumerate(possibilities):
        if equalities[i][0] == equalities[i][1] and fractions_equal((a, b), frac):
            print "%d/%d = %d/%d" % (a, b, frac[0], frac[1])
            return True
    return False

def find_fractions():
    d = {}
    for a in range(10, 100):
        for b in range(a + 1, 100):
            if is_curious((a, b)):
                try:
                    tmp = d[simplify((a, b))]
                except KeyError:
                    d[simplify((a, b))] = 1
    return d

if __name__ == '__main__':
    f = find_fractions()
    print simplify((mul([x for x, y in f.keys()]), mul([y for x, y in f.keys()])))
