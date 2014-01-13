#!/usr/bin/python
# #####################################################################
# id_0113.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize

@memoize()
def increasing(n, start = 0):
    if n == 1:
        return 10 - start
    ret = 0
    for x in range(start, 10):
        ret += increasing(n - 1, x)
    return ret

@memoize()
def decreasing(n, start = 9):
    if n == 1:
        return start + 1
    ret = 0
    for x in range(start + 1):
        ret += decreasing(n - 1, x)
    return ret

if __name__ == '__main__':
    s = 0
    for n in range(1, 101):
        s += increasing(n, 1)
        s += decreasing(n, 9)
        s -= 10
    print s
