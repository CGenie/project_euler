#!/usr/bin/python2
# #####################################################################
# id_0021.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0012 import proper_factors

d = {}
def fact(n):
    try:
        return d[n]
    except KeyError:
        d[n] = proper_factors(n)
        return d[n]

ss = {}
def sum_fact(n):
    try:
        return ss[n]
    except KeyError:
        ss[n] = sum(fact(n))
        return ss[n]

def amicable(a, b):
    sa = sum_fact(a)
    if sa == b:
        sb = sum_fact(b)
        if sb == a:
            return True
    return False

if __name__ == '__main__':
    s = 0
    for a in range(1, 9999):
        if a % 10 == 0:
            print "a = " + str(a)
        for b in range(a + 1, 10000):
            if amicable(a, b):
                print "Amicable: a = " + str(a) + ", b = " + str(b) 
                s += a + b
    print s
