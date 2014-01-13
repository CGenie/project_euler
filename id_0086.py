#!/usr/bin/python
# #####################################################################
# id_0086.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from collections import defaultdict

M = 1818
MM = 2*M

d_sqr = {1: 1}
d_sqrt = {1: 1}
d_ss = {}

def SS(n, mx):
    try:
        return d_ss[(n, mx)]
    except KeyError:
        if n <= mx:
            d_ss[(n, mx)] = int(n/2)
        else:
            d_ss[(n, mx)] = SS(2*mx - n, mx) + 1
    return d_ss[(n, mx)]

def sqr(n):
    try:
        return d_sqr[n]
    except KeyError:
        d_sqr[n] = n**2
        d_sqrt[n**2] = n
    return d_sqr[n]

if __name__ == '__main__':
    # compute all squares up to 5*M**2
    for x in range(2, 3*M):
        d_sqr[x] = d_sqr[x - 1] + 2*(x - 1) + 1
        d_sqrt[d_sqr[x]] = x
    print("squares computing done")
    # compute all possible sums of squares
    d_sums = defaultdict(list)
    for a in range(1, M + 1):
        for b in range(2, 2*a + 1):
            d_sums[d_sqr[a] + d_sqr[b]].append((a, b))
    s = 0
    for mm in d_sums:
        if mm in d_sqrt:
            #print(mm, d_sums[mm])
            for (a, b) in d_sums[mm]:
                s += SS(b, a)
    print("ans = ", s)
