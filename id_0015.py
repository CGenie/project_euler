#!/usr/bin/python2
# #####################################################################
# id_0015.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from math import factorial

def routes(pos_x, pos_y, n):
    s = 0

    # we have reached our destination, increase s
    if pos_x == n and pos_y == n:
        s += 1
    else:
        # we can either go right...
        if pos_x < n:
            s += routes(pos_x + 1, pos_y, n)
        # ...or down
        if pos_y < n:
            s += routes(pos_x, pos_y + 1, n)
    return s

# another, faster way to do it (a little math...)
def binomial(n, k):
    return factorial(n)/(factorial(k)*factorial(n - k))

def routes2(n):
    return binomial(2*n, n)

if __name__ == '__main__':
    print routes2(20)
    
