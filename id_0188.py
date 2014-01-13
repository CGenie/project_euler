#!/usr/bin/python
# #####################################################################
# id_0188.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize
import sys

@memoize()
def hyperexp(num, pwr):
    if(pwr == 1):
        return num
    return num**hyperexp(num, pwr - 1)

if __name__ == '__main__':
    for p in range(1, 1855):
        n = hyperexp(1777, p)
        print(p)
    M = 10**8
    print(n % M)
