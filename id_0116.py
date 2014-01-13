#!/usr/bin/python
# #####################################################################
# id_0116.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize

@memoize()
def tiles(n, k, num):
    if num == 1:
        return n - k + 1
    s = 0
    for x in range(n - 2*k + 1):
        s += tiles(n - k - x, k, num - 1)
    return s

if __name__ == '__main__':
    s = 0
    for x in range(1, 26):
        s += tiles(50, 2, x)
    for x in range(1, 17):
        s += tiles(50, 3, x)
    for x in range(1, 13):
        s += tiles(50, 4, x)
    print("sol = ", s)
