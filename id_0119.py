#!/usr/bin/python
# #####################################################################
# id_0119.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize

def is_power(n):
    p = 2
    s = sum([int(x) for x in str(n)])
    while True:
        ret = n**(1./p)
        if ret < 2:
            return False
        if abs(ret - s) < 10**(-5):
            return True
        if s - ret > 1:
            break
        p += 1

if __name__ == '__main__':
    # generate all powers of consecutive numbers, check if they have good digits
    ret = []
    for x in range(2, 10**8):
        p = 1
        while True:
            n = x**p
            if n > 10**20:
                break
            s = sum([int(k) for k in str(n)])
            if n >= 10 and s == x:
                ret.append(n)
                print("found: n = " + str(n))
            p += 1
            if len(ret) > 30:
                ret.sort()
                print(ret[29])
    ret.sort()
    print(ret)
