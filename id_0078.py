#!/usr/bin/python3.1
# #####################################################################
# id_0078.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0076 import Sums
#import cProfile

# generates pentagonal numbers
def pentagonal():
    n = 1
    while True:
        yield int(n*(3*n - 1)/2)
        yield int(n*(1 + 3*n)/2)
        n += 1

# Euler generating function for the partition function P
Pd = {0: 1}
def P(n):
    try:
        return Pd[n]
    except KeyError:
        s = 0
        i = 0
        #print("n = ", n)
        p = pentagonal()
        for x in p:
            sgn = 1
            if x <= n:
                if (i % 4) >= 2:
                    sgn = -1
                #print("n = ", n, ", x = ", x, ", sgn = ", sgn, ", P(n - x) = ", P(n - x), ", i = ", i)
                s += sgn*P(n - x)
            else:
                break
            i += 1
        Pd[n] = s
    return Pd[n]

if __name__ == '__main__':
    n = 1
    ret = 1
    while (ret % 10**6 != 0):
        ret = P(n)
        if (ret % 10 == 0):
            print("n = ", n, ", ret = ", ret)
        n += 1
    
    print("w = ", P(n))
