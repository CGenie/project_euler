#!/usr/bin/python2
# #####################################################################
# id_0025.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0002 import fib_iter

def fib_n_digits(n):
    i = 0
    f = fib_iter()
    while True:
        p = f.next()
        if p/(10**(n - 1)) >= 1:
            break
        i += 1
    return i

if __name__ == '__main__':
    print fib_n_digits(1000)
