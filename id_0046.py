#!/usr/bin/python2
# #####################################################################
# id_0046.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from id_0003 import is_prime

twice_square = {}

def is_goldbachian(num):
    for n in range(1, num/2):
        try:
            ts = twice_square[n]
        except KeyError:
            twice_square[n] = 2*n**2
            ts = twice_square[n]
        d = num - ts
        if d > 1 and is_prime(d):
            return True
    return False

if __name__ == '__main__':
    n = 4
    while True:
        num = 2*n + 1
        if not is_prime(num) and not is_goldbachian(num):
            print "%d is not goldbachian" % num
            break
        n += 1
