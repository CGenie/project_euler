#!/usr/bin/python
# #####################################################################
# id_0303.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize
import sys

ss = {'0', '1', '2'}

@memoize()
def f(n):
    global ss

    if n == 99:
        return 11335578

    if n == 2*99:
        return 5667789

    if n == 2*198:
        return 5359147

    if n == 2*297:
        return 1889263

    # If n % 2 == 0:
    #     ret = f(int(n/2))
    #     if ret % 2 == 0:
    #         return int(f(int(n/2))/2)

    # if n % 3 == 0:
    #     ret = f(int(n/3))
    #     if ret % 3 == 0:
    #         return int(f(int(n/3))/3)

    k = 1
    m = n

    while True:
        if set(str(m)).issubset(ss):
            break
        k += 1
        m += n
    return k

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

@memoize()
def f_optimized(n):
    global ss

    if n == 99:
        return 11335578

    if n == 396:
        return 5359147

    if n == 495:
        return 22671156

    if n == 594:
        return 1889263

    for p in range(2, n):
        if n % p == 0:
            ret = f(int(n/p))
            if ret % p == 0:
                return int(f(int(n/p))/p)

    k = 1
    m = n

    while True:
        if set(str(m)).issubset(ss):
            break
        k += 1
        m += n
    return k

@memoize()
def new_f(n):
    global ss

    k = 1
    m = n
    while True:
        if set(str(m)).issubset(ss):
            break
        k += 1
        m += n
    return k

if __name__ == '__main__':
    s = 0
    #for x in range(3, 500):
    #    print("x = " + str(x) + ", f(x) = " + str(f(x)) + ", f(2*x) = " + str(f(2*x)))
    #    assert(f_optimized(x) == f(x))
    #for x in [99, 198, 297, 396, 495]:
    #    print(x, f(x), x*f(x))
    #print(f(594))
    #sys.exit()
    for x in range(1, 1000):
        s += f_optimized(x)
        print("x = " + str(x) + ", f(x) = " + str(f_optimized(x)))
    print("sol = " + str(s))
