#!/usr/bin/python
# #####################################################################
# id_0108.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from helper_py3 import memoize

def different_sols(n):
    dd = 0
    for x in range(n + 1, 2*n + 1):
        if n*x % (x - n) == 0:
            dd += 1
    return dd

def factors(n):
    fct = 2

    for x in range(2, n):
        if n % x == 0:
            fct += 1

    return fct

if __name__ == '__main__':
    n = 4
    mm = 0

    while True:
        dd = factors(n)
        mm = max(dd, mm)
        if dd >= 1000:
            print("n_sol = ", n, ", dd = ", dd)
            break
        if n % 1000 == 0:
            print("n = ", n, ", dd = ", dd, ", mm = ", mm)
        n += 1
