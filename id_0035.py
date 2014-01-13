#!/usr/bin/python2
# #####################################################################
# id_0035.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0003 import is_prime

def circulars(num):
    s = str(num)
    l = len(s)
    ss = s*2
    return [int(ss[x:x + l]) for x in range(l)]

def is_circular_prime(num):
    for x in circulars(num):
        if not is_prime(x):
            return False
    return True

if __name__ == '__main__':
    s = 0
    for x in range(2, 10**6):
        if is_circular_prime(x):
            s += 1
    print s
