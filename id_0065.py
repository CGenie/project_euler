#!/usr/bin/python2
# #####################################################################
# id_0065.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from fractions import Fraction
from id_0033 import gcd

def e_nth_convergents():
    yield 2
    n = 1
    while True:
        yield 1
        if n > 1:
            yield 1
        yield 2*n
        n += 1

def generate_fraction(lst):
    f = Fraction(lst[-1], 1)
    for i in range(len(lst) - 2, -1, -1):
        n = lst[i]
        f = n + 1/f
        n = f.numerator
        d = f.denominator
        nd = gcd(d, n)
        n = n/nd
        d = d/nd
        f = Fraction(n, d)
    #print f, n, d, nd
    return f

if __name__ == '__main__':
    limit = 100
    n = 1
    f = e_nth_convergents()
    r = Fraction(0, 1)
    lst = []
    while True:
        r = f.next()
        lst.append(r)
        frac = generate_fraction(lst)
        if n >= limit:
            break
        n += 1
    print frac
    print sum([int(x) for x in str(frac.numerator)])
