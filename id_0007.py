#!/usr/bin/python2
# #####################################################################
# id_0007.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0003 import is_prime

def find_nth_prime(n):
    s = 0
    p = 2
    while True:
        if is_prime(p):
            s += 1
        if s == n:
            break
        p += 1
    return p

if __name__ == '__main__':
    print find_nth_prime(10001)
