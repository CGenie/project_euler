#!/usr/bin/python2
# #####################################################################
# id_0049.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from itertools import combinations, permutations
from id_0003 import is_prime
from helper import unique

def contains_arithmetic_sequence(lst, l):
    for c in combinations(lst, l):
        seq = True
        d = c[1] - c[0]
        for i in range(l - 1):
            if c[i + 1] - c[i] != d:
                seq = False
                break
        if seq:
            print "Arithmetic sequence found for " + str(c)
            return True
    return False

def is_unusual(num):
    if is_prime(num):
        l = [x for x in str(num)]
        lst = []
        for p in permutations(l):
            x = int(''.join(p))
            if is_prime(x) and len(str(x)) == 4:
                lst.append(x)
        lst = unique(lst)
        lst.sort()
        if len(lst) >= 3 and contains_arithmetic_sequence(lst, 3):
            #print str(lst) + " is unusual"
            return True
    return False

if __name__ == '__main__':
    digits = range(1, 10)
    for n in xrange(1001, 10000, 2):
        if is_unusual(n):
            print "%d is unusual" % n
