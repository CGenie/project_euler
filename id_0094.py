#!/usr/bin/python
# #####################################################################
# id_0094.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize
from math import sqrt

def is_triangle(a, b, c):
    # check if triangle inequality is satisfied
    return (a + b > c) and (a + c > b) and (b + c > a)

def area(a, b, c):
    P = (a + b + c)*(b + c - a)*(a + b - c)*(a + c - b)
    return sqrt(P/16.)

if __name__ == '__main__':
    M = 10**9
    eps = 10**(-6)
    ret = 0
    n = 0
    for x in range(1, M//3 + 5):
        for p in (-1, 1):
            a = area(x, x, x + p)
            if is_triangle(x, x, x + p) and abs(int(a) - a) < eps:
                if 3*x + p <= M:
                    ret += 3*x + p
                n += 1
                if n % 100 == 0:
                    print("Triangle found: " + str(x) + ", " + str(x) + ", " + str(x + p) + ", area = " + str(a))
    print("sol = " + str(ret))
