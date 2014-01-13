#!/usr/bin/python2
# #####################################################################
# id_0034.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from math import factorial

def sum_fact(num):
    return sum([factorial(int(x)) for x in str(num)])

def is_curious(num):
    return num == sum_fact(num)

if __name__ == '__main__':
    s = 0
    for x in range(3, 254100):
        if is_curious(x):
            s += x
    print s
