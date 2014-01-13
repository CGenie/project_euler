#!/usr/bin/python2
# #####################################################################
# id_0012.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0003 import is_prime
from helper import unique

def proper_factors(n):
    lst = []
    for x in range(1, n/2 + 1):
        if n % x == 0:
            lst.append(x)
    return lst

def factors(n):
    """Return a list of all factors of n"""
    lst = proper_factors(n)
    lst.append(n)
    return lst

def trinum(n):
    return int(0.5*(n + 1)*n)

def trinum_factors(n):
    s = 12000
    while True:
        # include 1 as a factor, that's why we add 1
        t = trinum(s)
        l = len(factors(t)) + 1
        if l > 200 or s % 50 == 0:
            print "s = " + str(s) + ", l = " + str(l)
        if l > n:
            return t
        s += 1

if __name__ == '__main__':
    print trinum_factors(500)
