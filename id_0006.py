#!/usr/bin/python2
# #####################################################################
# id_0006.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def diff(n):
    s = sum([x**2 for x in range(1, n + 1)])
    ss = sum([x for x in range(1, n + 1)])**2
    return ss - s

if __name__ == '__main__':
    print diff(100)
