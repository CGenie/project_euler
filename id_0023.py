#!/usr/bin/python2
# #####################################################################
# id_0023.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
#from id_0008 import mul
from id_0012 import proper_factors
import pickle

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

def is_perfect(a):
    return sum_fact(a) == a

def is_deficient_prefect_abundant(a):
    """Returns:
    -1 if number is deficient
    0 if it's proper
    1 if it's abundant"""
    f = proper_factors(a)
    d = sum(f) - a
    if d  > 0:
        return 1
    if d < 0:
        return -1
    return d

def is_abundant(a):
    return sum_fact(a) > a

def sum_of_two_abundants(n):
    h = n/2 + 1
    for a in range(11, h + 2):
        if is_abundant(a):
            b = n - a
            if is_abundant(b):
                return True
    return False

if __name__ == '__main__':
    f = open("id_0023.pickle", 'r')
    d = pickle.load(f)
    ss = pickle.load(f)
    s = 0
    f.close()
    for x in range(1, 28123):
        if not sum_of_two_abundants(x):
            print "x = " + str(x) + " is NOT a sum of two abundants"
        #if x % 1000 == 0:
        #    print "x = " + str(x)
        if not sum_of_two_abundants(x):
            s += x
    print s
    fwb = open("id_0023.pickle", 'wb')
    pickle.dump(d, fwb)
    pickle.dump(ss, fwb)
    fwb.close()
