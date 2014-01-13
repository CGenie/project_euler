#!/usr/bin/python
# #####################################################################
# id_0104.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from math import sqrt
from math import log

digits = '123456789'

def is_pandigital(n):
    ns = str(n)
    return len(ns) == 9 and all(d in ns for d in digits)

def is_pandigital_s(ns):
    return len(ns) == 9 and all(d in ns for d in digits)

def fib_it():
    f_o = 1
    f_n = 1
    yield f_o
    yield f_n
    while True:
        (f_n, f_o) = (f_n + f_o, f_n)
        yield f_n

if __name__ == '__main__':
    f = fib_it()
    k = 1
    pwr10 = 10**9
    while True:
        n = next(f)
        if n >= pwr10:
            nl = str(n % pwr10)
            if is_pandigital(nl):
                ll = int(log(n, 10)) + 1
                nf = str(int(n/10**(ll - 9)))
                if is_pandigital_s(nf):
                    break
        k += 1
        if k % 5000 == 0:
            print("k = ", k)
    print("ans = ", k)
