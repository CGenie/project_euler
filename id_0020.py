#!/usr/bin/python2
# #####################################################################
# id_0020.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
from math import factorial
from id_0016 import sum_digits

if __name__ == '__main__':
    print sum_digits(factorial(100))
