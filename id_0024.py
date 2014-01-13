#!/usr/bin/python2
# #####################################################################
# id_0024.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from itertools import permutations

if __name__ == '__main__':
    perm = []
    alph = [str(x) for x in range(10)]
    for p in permutations(alph):
        perm.append(''.join(p))
    perm.sort()
    print perm[10**6 - 1]
