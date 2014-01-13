#!/usr/bin/python
# #####################################################################
# id_0307.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize

@memoize()
def omega(k, n):
    if n == 1:
        return 1
    if k == 0:
        return 1
    s = 0
    for kn in range(k):
        s += omega(k - kn, n - 1)
    return s

@memoize()
def a(k, n):
    if n == 1:
        return 1
    if k == 0:
        return 1
    s = 0
    for kn in range(3):
        s += a(k - kn, n - 1)
    return s

if __name__ == '__main__':
    print(float(a(3, 7))/omega(3, 7))
    
