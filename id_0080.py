#!/usr/bin/python3.1
# #####################################################################
# id_0080.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from decimal import *
from math import sqrt

d_sqrt = {}

def is_square(num):
    try:
        n = d_sqrt[num]
    except KeyError:
        d_sqrt[num] = int(sqrt(num))
        n = d_sqrt[num]
    return n*n == num


def sum_of_digits(n):
    getcontext().prec = 105
    v = str(Decimal(n).sqrt())
    #print(v)
    ret = 0
    for x in range(0, 101):
        if v[x] != '.':
            ret += int(v[x])
    return ret



if __name__ == '__main__':
    s = 0
    for n in range(1, 101):
        if not is_square(n):
            s += sum_of_digits(n)
    print("s = ", s)
