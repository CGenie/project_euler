#!/usr/bin/python
# #####################################################################
# id_0297.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoized

fibarr = []
zeck = {1: 1}

@memoized
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

@memoized
def zeckendorf(n):
    # find largest fibonacci number less than n
    if n == 0:
        return 0
    if n == 1:
        return 1

    k = 1
    curr = fibarr[k]
    prev = fibarr[k - 1]
    while curr <= n:
        prev, curr = fibarr[k - 1], fibarr[k]
        k += 1
    return 1 + zeckendorf(n - prev)

def fibgen():
    n = 1
    while True:
        yield fib(n)
        n += 1

if __name__ == '__main__':
    s = 1
    ret = 0
    fg = fibgen()
    while ret <= 10**6:
        ret = next(fg)
        fibarr.append(ret)
    prev = 1
    print(fibarr)
    for f in fibarr[1:-1]:
        for k in range(prev + 1, f):
            zeck[k] = 1 + zeck[k - prev]
            s += zeck[k]
        prev = f
        zeck[f] = 1
        s += 1
    print(s)
    print(2**(len(fibarr) - 7))
    for k in range(f + 1, 10**6):
        zeck[k] = 1 + zeck[k - f]
        s += zeck[k]
    print(s)
    # the number of Zeckendorf decompositions in the interval [F_n, F_{n + 1}) is equal to F_{n - 1}
    # (see http://pubget.com/paper/pgtmp_10083204)
    
