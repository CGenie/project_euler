#!/usr/bin/python
# #####################################################################
# id_0126.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize

def cubes(a, b, c):
    return a*b + a*c + b*c

if __name__ == '__main__':
    d = {}
    for a in range(1, 10):
        print("a = ", a)
        for b in range(a, 10):
            for c in range(b, 10):
                r = cubes(a, b, c)
                d[r] = d.get(r, 0) + 1
    for k, v in enumerate(d):
        if v == 5:
            print("sol = ", k)
    
